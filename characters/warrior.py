# characters/warrior.py
import random
from .character import Character

class Warrior(Character):
    # 전사 클래스 
    
    def __init__(self, name, level=1):
        super().__init__(name, level, health=120, attack_power=18)
        self.rage = 0
    
    def attack(self, target):
        # 기본 공격 시 분노 게이지 증가 
        super().attack(target)
        self.rage = min(100, self.rage + 15)
        print(f"{self.name}의 분노가 상승합니다! 분노 게이지: {self.rage}/100")
    
    def special_attack(self, target):
        # 전사 특수 공격 → 분노의 연속 베기 
        if self.rage < 50:
            print(f"{self.name}의 분노가 부족합니다! (필요: 50, 현재: {self.rage})")
            return
        
        print(f"🔥 {self.name}이(가) '분노의 연속 베기'를 시전합니다!")        
        attack_count = self.rage // 25
        total_damage = 0
        
        for i in range(attack_count):
            damage = self.attack_power + random.randint(5, 15)
            total_damage += damage
            print(f"  💥 {i+1}번째 베기: {damage} 피해!")
            target.take_damage(damage)
            
            if not target.is_alive():
                break
        
        self.rage = 0
        heal_amount = total_damage // 4
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name}이(가) 전투의 쾌감으로 {heal_amount}만큼 체력을 회복했습니다!")
    
    def show_status(self):
        # 전사의 상태 정보 출력 (+ 분노 게이지) 
        super().show_status()
        print(f"분노 게이지: {self.rage}/100")

    def level_up(self):
        # 전사 레벨업 
        super().level_up()
        self.rage = min(100, self.rage + 20)