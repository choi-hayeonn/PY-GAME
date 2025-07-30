# characters/character.py
from abc import ABC, abstractmethod

class Character(ABC):
    # 기본 캐릭터 추상 클래스 
    
    def __init__(self, name, level, health, attack_power):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        # 기본 공격 메서드 
        damage = self.attack_power
        print(f"{self.name}이(가) {target.name}을(를) 기본 공격! {damage}의 피해!")
        target.take_damage(damage)
    
    @abstractmethod
    def special_attack(self, target):
        # 특수 공격 (추상 메서드) 
        pass
    
    def take_damage(self, damage):
        # 피해를 입으면 체력이 감소 
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name}이(가) {damage}의 피해를 입었습니다! 남은 체력: {self.health}")
    
    def is_alive(self):
        # 체력이 0 이하이면 False 
        return self.health > 0
    
    def show_status(self):
        # 캐릭터 정보 출력 
        status = "생존 중" if self.is_alive() else "사망"
        print(f"◻◻◻ {self.name}의 상태 ◻◻◻")
        print(f"레벨: {self.level}")
        print(f"체력: {self.health}/{self.max_health}")
        print(f"공격력: {self.attack_power}")
        print(f"상태: {status}")
    
    def reset_health(self):
        # 캐릭터의 체력 초기화 
        self.health = self.max_health
        print(f"{self.name}의 체력이 완전히 회복되었습니다!")
    
    def get_name(self):
        # 캐릭터의 이름 가져오기 
        return self.name

    def level_up(self):
        # 레벨업 시 능력치 상승 
        self.level += 1
        health_increase = 20
        attack_increase = 3    
        self.max_health += health_increase
        self.health = self.max_health
        self.attack_power += attack_increase        
        print(f"🌟 {self.name}이(가) 레벨업! Lv.{self.level}")
        print(f"   체력 +{health_increase}, 공격력 +{attack_increase}")
