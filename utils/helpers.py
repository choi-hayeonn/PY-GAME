import random
from characters import Warrior, Mage, Rogue

def choose_character():
    # 캐릭터 선택 함수 
    print("\n◻◻◻ 캐릭터 선택 ◻◻◻")
    print("1. 전사 (Warrior)")
    print("2. 마법사 (Mage)")
    print("3. 도적 (Rogue)")
    
    while True:
        choice = input("캐릭터를 선택하세요 (1, 2, 3): ")
        
        if choice == "1":
            name = input("전사의 이름을 입력하세요: ")
            return Warrior(name)
        elif choice == "2":
            name = input("마법사의 이름을 입력하세요: ")
            return Mage(name)
        elif choice == "3":
            name = input("도적의 이름을 입력하세요: ")
            return Rogue(name)
        else:
            print("1, 2, 3 중에서 선택해주세요!")

def create_random_enemy(exclude_user=None):
    # 랜덤 적 생성 
    warrior_names = ["오크 전사", "고블린 워리어", "스켈레톤 나이트"]
    mage_names = ["다크 위저드", "푸른염화술사", "빙결마법사"]
    rogue_names = ["그림자 암살자", "도둑 두목", "닌자 거북이"]
    
    # 플레이어와 다른 클래스 적 생성
    if exclude_user == Warrior:
        # 플레이어가 전사면 '마법사나 도적' 적 생성
        if random.choice([True, False]):
            enemy_name = random.choice(mage_names)
            return Mage(enemy_name)
        else:
            enemy_name = random.choice(rogue_names)
            return Rogue(enemy_name)
    elif exclude_user == Mage:
        # 플레이어가 마법사면 '전사나 도적' 적 생성
        if random.choice([True, False]):
            enemy_name = random.choice(warrior_names)
            return Warrior(enemy_name)
        else:
            enemy_name = random.choice(rogue_names)
            return Rogue(enemy_name)
    elif exclude_user == Rogue:
        # 플레이어가 도적이면 '전사나 마법사' 적 생성
        if random.choice([True, False]):
            enemy_name = random.choice(warrior_names)
            return Warrior(enemy_name)
        else:
            enemy_name = random.choice(mage_names)
            return Mage(enemy_name)