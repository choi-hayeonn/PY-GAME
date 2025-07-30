import random
import time 
from characters import Warrior, Mage, Rogue

class BattleManager:
    # 전투 관리 시스템
     
    def __init__(self):
        # 전투 딜레이
        self.battle_delay = 2

    def start_battle(self, player, enemy):
        # 전투 시작
        print("🗡️  전투가 시작되었습니다! 🗡️")
        print(f"{player.name} VS {enemy.name}")
        
        # 초기 상태 표시
        player.show_status()
        print()
        enemy.show_status()
        print()

        # 선공 결정
        first_attacker, second_attacker = self.decide_first_attacker(player, enemy)
        print(f"🎯 {first_attacker.name}이(가) 선공권을 가져갑니다!")
        
        time.sleep(self.battle_delay)

        # 전투 진행 반복문
        turn = 1
        while player.is_alive() and enemy.is_alive():
            print(f"\n◻◻◻ Turn {turn} ◻◻◻")
            
            # 첫 번째 공격자의 턴
            if not self.run_turn(first_attacker, second_attacker):
                break
            
            time.sleep(self.battle_delay)
            
            # 두 번째 공격자가 살아있으면 반격!!
            if second_attacker.is_alive():
                if not self.run_turn(second_attacker, first_attacker):
                    break
            
            time.sleep(self.battle_delay)
            turn += 1

            # 매 5턴마다 상태 표시해주기~ 
            if turn % 5 == 0:
                print("\n◻◻◻ 현재 상태 ◻◻◻")
                player.show_status()
                print()
                enemy.show_status()
                print()
        
        # 전투 결과 발표
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

        # 70% 기본 공격, 30% 특수 공격
        attack_choice = random.randint(1, 100)
            
        if attack_choice <= 70:
            print(f"\n{attacker.name}의 기본 공격!")
            attacker.attack(target)
        else:
            print(f"\n{attacker.name}의 특수 공격!")
            attacker.special_attack(target)
            
        # 타겟이 죽었는지 확인
        if not target.is_alive():
            return False
                
    
    def announce_winner(self, player, enemy):
        # 승부 결과 발표 
        print("🩸 전투 종료! 🩸")
        
        if player.is_alive():
            print(f"🏆 {player.name} 승리! 🏆")
            print(f"남은 체력: {player.health}/{player.max_health}")
        else:
            print(f"💀 {enemy.name} 승리!")
            print(f"{player.name}이(가) 쓰러졌습니다...")
        