# battle/battle_manager.py
import random
import time
from characters import Warrior, Mage, Rogue

class BattleManager:
    # 전투 관리  
     
    def __init__(self):
        self.battle_delay = 1.5

    def start_battle(self, player, enemy):
        # 전투 시작 
        print("🗡️  전투가 시작되었습니다! 🗡️")
        print(f"{player.name} VS {enemy.name}")
    
        # 적 체력 및 공격력 조정
        enemy.health = int(enemy.health * 1.05)
        enemy.max_health = enemy.health
        enemy.attack_power = int(enemy.attack_power * 0.75)

        player.show_status()
        print()
        enemy.show_status()
        print()

        first_attacker, second_attacker = self.decide_first_attacker(player, enemy)
        print(f"🎯 {first_attacker.name}이(가) 선공권을 가져갑니다!")
    
        time.sleep(self.battle_delay)

        turn = 1
        minimum_turns = 6
        # 적어도 turn6까지 게임을 진행하기 위해
        while turn <= minimum_turns or (player.is_alive() and enemy.is_alive()):
            print(f"\n◻◻◻ Turn {turn} ◻◻◻")

            if player.is_alive() and enemy.is_alive():
                if not self.run_turn(first_attacker, second_attacker):
                    if turn < minimum_turns:
                        print("\n⚠️ 빠른 종료 방지! 체력 25로 부활하여 전투 지속!")
                        first_attacker.health = max(25, first_attacker.health)
                        second_attacker.health = max(25, second_attacker.health)
                    else:
                        break

            time.sleep(self.battle_delay)

            if player.is_alive() and enemy.is_alive():
                if not self.run_turn(second_attacker, first_attacker):
                    if turn < minimum_turns:
                        print("\n⚠️ 빠른 종료 방지! 체력 15로 부활하여 전투 지속!")
                        first_attacker.health = max(15, first_attacker.health)
                        second_attacker.health = max(15, second_attacker.health)
                    else:
                        break

            time.sleep(self.battle_delay)
            turn += 1

            if turn % 6 == 0:
                print("\n◻◻◻ 현재 상태 ◻◻◻")
                player.show_status()
                print()
                enemy.show_status()
                print()

        self.announce_winner(player, enemy)
        return player.is_alive()
    
    def decide_first_attacker(self, player, enemy):
        # 선공권 결정 
        if random.choice([True, False]):
            return player, enemy
        else:
            return enemy, player
    
    def run_turn(self, attacker, target):
        # 턴 실행 
        attack_choice = random.randint(1, 100)
            
        if attack_choice <= 80:
            print(f"\n{attacker.name}의 기본 공격!")
            attacker.attack(target)
        else:
            print(f"\n{attacker.name}의 특수 공격!")
            attacker.special_attack(target)
            
        if not target.is_alive():
            return False
        return True
    
    def announce_winner(self, player, enemy):
        # 결과 발표 
        print("🩸 전투 종료! 🩸")
        
        if player.is_alive():
            print(f"🏆 {player.name} 승리! 🏆")
            print(f"남은 체력: {player.health}/{player.max_health}")
        else:
            print(f"💀 {enemy.name} 승리!")
            print(f"{player.name}이(가) 쓰러졌습니다...")
