import random
from .character import Character

class Rogue(Character):
    # 도적 클래스 
    
    def __init__(self, name, level=1):
        Character.__init__(self, name, level, health=95, attack_power=14)
        self.stealth_stack = 0  # 은신 스택 (최대 5)
        self.critical_chance = 20  # 기본 치명타 확률 20%
    
    def attack(self, target):
        # 기본 공격 시 은신 스택 증가 및 치명타 판정 
        crit_roll = random.randint(1, 100)
        damage = self.attack_power
        
        if crit_roll <= self.critical_chance:
            damage = int(damage * 1.5)
            print(f"💀 치명타! {self.name}이(가) {target.name}을(를) 기본 공격! {damage}의 피해!")
        else:
            print(f"{self.name}이(가) {target.name}을(를) 기본 공격! {damage}의 피해!")
        
        target.take_damage(damage)
        
        # 은신 스택 증가
        if self.stealth_stack < 5:
            self.stealth_stack += 1
            self.critical_chance += 5  # 은신 중첩마다 치명타 확률 5% 증가
            print(f"그림자 속으로 은신 스택: {self.stealth_stack}/5")
    
    def special_attack(self, target):
        # 그림자 분신술 - 은신 스택을 활용한 분신 연속 공격 
        if self.stealth_stack < 2:
            print(f"{self.name}의 그림자가 부족합니다! (필요 은신 스택: 2, 현재: {self.stealth_stack})")
            return
        print(f"🌙 {self.name}이(가) '그림자 분신술'을 시전합니다!")
        
        # 은신 스택에 따라 분신 개수 결정 (최대 5개)
        shadow_clones = self.stealth_stack
        success_rate = 60 + (self.stealth_stack * 8)  # 은신 스택마다 성공률 8% 증가
        
        print(f"  {shadow_clones}명의 그림자 분신이 나타납니다!")
        
        successful_attacks = 0
        total_damage = 0
        
        for i in range(shadow_clones):
            attack_roll = random.randint(1, 100)
            
            if attack_roll <= success_rate:
                # 성공 시 강력한 데미지
                damage = self.attack_power + random.randint(10, 25)
                
                # 치명타 판정 (은신 스택으로 인한 높은 치명타율)
                crit_roll = random.randint(1, 100)
                if crit_roll <= (self.critical_chance + 20):  # 특수공격 시 치명타율 +20%
                    damage = int(damage * 2)
                    print(f"  💀 분신 #{i+1} 치명타 습격: {damage} 피해!")
                else:
                    print(f"  🗡️ 분신 #{i+1} 습격 성공: {damage} 피해!")
                
                target.take_damage(damage)
                total_damage += damage
                successful_attacks += 1
                
                if not target.is_alive():
                    break
            else:
                print(f"  👻 분신 #{i+1} 실패ㅠㅠ 상대가 눈치챘습니다!")
        
        # 성공한 공격이 많을수록 보너스 효과
        if successful_attacks >= 3:
            print(f"  🎯 완벽한 습격! {self.name}이(가) 다음 턴까지 회피율 상승!")
        
        # 은신 스택 및 치명타 확률 초기화
        self.stealth_stack = 0
        self.critical_chance = 20
        
        print(f"그림자가 흩어집니다. 총 {successful_attacks}/{shadow_clones} 공격 성공!")
    
    def show_status(self):
        # 도적의 상태 정보 출력 (+ 은신 스택, 치명타 확률) 
        Character.show_status(self)
        print(f"은신 스택: {self.stealth_stack}/5")
        print(f"치명타 확률: {self.critical_chance}%")

    def level_up(self):
        # 도적 레벨업 
        Character.level_up(self)
        self.critical_chance += 5  # 레벨업 시 기본 치명타 확률 증가
        print(f"   치명타 확률 +5% (현재: {self.critical_chance}%)")