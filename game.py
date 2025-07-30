import random
from characters.Warrior import Warrior
from characters.Mage import Mage
from characters.Rogue import Rogue
from characters.Archer import Archer
from characters.DemonSlayer import DemonSlayer
from battle.battle_manager import BattleManager

character_classes = {
    "1": Warrior,
    "2": Mage,
    "3": Rogue,
    "4": Archer,
    "5": DemonSlayer
}

character_names = {
    Warrior: "전사",
    Mage: "마법사",
    Rogue: "도적",
    Archer: "궁수",
    DemonSlayer: "데몬슬레이어"
}

def choose_character(prompt):
    while True:
        print(f"{prompt} 🤔 직업을 선택하세요:")
        print("1. 🪖 전사 | 2. 🧙‍♂️ 마법사 | 3. 🥷 도적 | 4.🏹 궁수 | 5. 😈 데몬슬레이어")
        choice = input("🤔 직업 선택 (숫자 입력 OR 엔터 시 랜덤 선택): ").strip()

        if choice == "":
            choice = random.choice(list(character_classes.keys()))
            print(f"랜덤으로 선택된 직업: {character_names[character_classes[choice]]}")

        if choice in character_classes:
            cls = character_classes[choice]
            name = character_names[cls]  # 직업명으로 이름 설정
            character = cls(name)
            character.display_name = name + "님"
            return cls(name)
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

def main():
    print("=== 🎮 텍스트 RPG 전투 게임 🎮 ===")
    player = choose_character("플레이어")
    enemy = choose_character("적")

    while True:
        manager = BattleManager(player, enemy)
        result = manager.start_battle()

        if result == "패배":
            print("☠️게임 오버☠️ 수고하셨습니다.")
            break

        retry = input("새로운 적과 다시 👊 전투하시겠습니까? (y/n): ").strip().lower()
        print()
        if retry == "y":
            enemy = choose_character("새로운 적 😈")
        else:
            print("🔚게임을 종료합니다🔚")
            break

if __name__ == "__main__":
    main()