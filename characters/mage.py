import random
from .character import Character

class Mage(Character):
    # 마법사 클래스
    
    def __init__(self, name, level=1):
        Character.__init__(self, name, level, health=85, attack_power=12)
        self.mana = 120
        self.max_mana = 120
        self.spell_combo = 0  # 연속 콤보
    
    def attack(self, target):
        # 기본 공격하면 마나 회복 및 콤보 증가
        Character.attack(self, target)
        self.mana = min(self.max_mana, self.mana + 8)
        self.spell_combo += 1
        print(f"마나 회복! 현재 마나: {self.mana}/{self.max_mana}, 콤보: {self.spell_combo}")
    
    def special_attack(self, target):
        # 원소 폭발 : 연속된 원소 마법으로 강력한 콤보 공격 
        mana_cost = 35
        if self.mana < mana_cost:
            print(f"{self.name}의 마나가 부족합니다! (필요: {mana_cost}, 현재: {self.mana})")
            return
        
        print(f"✨ {self.name}이(가) '원소 폭발'을 시전합니다!")
        self.mana -= mana_cost
        
        # 콤보에 따라 원소 마법의 종류와 위력이 달라
        elements = ["🔥 화염", "❄️ 얼음", "⚡ 번개", "🌪️ 바람"]
        
        combo_multiplier = 1 + (self.spell_combo * 0.1)  # 콤보마다 10% 데미지 증가
        total_damage = 0
        
        # 3연속 원소 마법
        for _ in range(3):
            element = random.choice(elements)
            base_damage = self.attack_power + random.randint(8, 20)
            damage = int(base_damage * combo_multiplier)
            total_damage += damage            
            print(f"  {element} 마법: {damage} 피해! (콤보 보너스: x{combo_multiplier:.1f})")
            target.take_damage(damage)            
            if not target.is_alive():
                break
        
        # 강력한 콤보일 경우 추가 효과
        if self.spell_combo >= 5:
            bonus_damage = int(total_damage * 0.3)
            print(f"  🌟 콤보 피니쉬! 추가 {bonus_damage} 마법 피해!")
            target.take_damage(bonus_damage)
        
        self.spell_combo = 0  # 콤보 초기화
        print(f"남은 마나: {self.mana}/{self.max_mana}")
    
    def show_status(self):
        # 마법사의 상태 정보 출력 (+ 마나, 콤보) 
        Character.show_status(self)
        print(f"마나: {self.mana}/{self.max_mana}")
        print(f"콤보: {self.spell_combo}")

    def level_up(self):
        # 마법사 레벨업
        Character.level_up(self)
        mana_increase = 30
        self.max_mana += mana_increase
        self.mana = self.max_mana  # 레벨업 시 마나 완전 회복
        print(f"   마나 +{mana_increase}")