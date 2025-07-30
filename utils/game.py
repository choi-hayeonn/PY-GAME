# utils/game.py
from battle import BattleManager
from .helpers import choose_character, create_random_enemy

class GameManager:
    # 전반적인 게임 관리 
    
    def __init__(self):
        self.battle_manager = BattleManager()
        self.player = None
        self.wins = 0
        self.losses = 0
    
    def start_game(self):
        # 게임 시작 
        print("🎮 RPG 전투 게임에 오신 것을 환영합니다! 🎮")
        
        self.player = choose_character()
        print(f"\n환영합니다, {self.player.name}!")
        
        while True:
            enemy = create_random_enemy(exclude_user=self.player)

            if enemy is None:
                print("❌ 적이 생성되지 않아 기본 전사로 대체됩니다.")
                from characters import Warrior
                enemy = Warrior("기본 전사")
            print(f"\n🎯 새로운 적이 나타났습니다: {enemy.name}")
            print(f"\n{enemy.name}과의 전투에서 승리하세요💪")

            victory = self.battle_manager.start_battle(self.player, enemy)
            
            if victory:
                self.wins += 1
                print(f"\n🏆 현재 승리 횟수: {self.wins}승")
                
                if self.wins % 5 == 0:
                    print(f"\n🌟 축하합니다! {self.wins}승 달성으로 레벨업하였습니다!")
                    self.player.level_up()
                    self.player.show_status()
                    
                    if not self.ask_continue_after_levelup():
                        break
                
                if not self.ask_next_battle():
                    break
                    
                self.player.health = min(self.player.max_health, 
                                       self.player.health + self.player.max_health // 3)
                print(f"\n💊 {self.player.name}이(가) 잠시 휴식을 취해 체력을 회복했습니다!")
                print(f"\n다음 전투의 승리를 빕니다~~🍀")                
            else:
                self.losses += 1
                print(f"\n😨 패배... 현재 패배 횟수: {self.losses}회")
                
                if self.losses >= 5:
                    print("\n💀💀💀 5번의 패배로 게임이 종료됩니다! 💀💀💀")
                    break
                
                if not self.ask_retry():
                    break
                
                self.player.health = self.player.max_health // 2
                print(f"\n🙏 {self.player.name}이(가) 부활했습니다! (체력 50% 회복)")
        
        self._show_final_stats()
    
    def ask_continue_after_levelup(self):
        # 레벨업 후 계속 플레이 여부 확인 
        while True:
            choice = input("\n🎮 계속 게임을 진행하시겠습니까? (y/n): ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("❌ y 또는 n을 입력해주세요!")
    
    def ask_next_battle(self):
        # 다음 전투 여부 확인 
        while True:
            choice = input("\n⚔️ 다음 적과 전투하시겠습니까? (y/n): ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("❌ y 또는 n을 입력해주세요!")
    
    def ask_retry(self):
        # 재도전 여부 확인  
        while True:
            choice = input("\n🔄 다시 도전하시겠습니까? (y/n): ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("❌ y 또는 n을 입력해주세요!")
    
    def _show_final_stats(self):
        # 최종 통계 
        print("\n🎮 게임 종료 🎮")
        print(f"플레이어: {self.player.name} (Lv.{self.player.level})")
        print(f"총 승리: {self.wins}회")
        print(f"총 패배: {self.losses}회")
        
        if self.wins > 0:
            win_rate = (self.wins / (self.wins + self.losses)) * 100
            print(f"승률: {win_rate:.2f}%")
        
        print("\n게임을 플레이해주셔서 감사합니다!🖤")
