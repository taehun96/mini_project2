from .character import Character
import random

# 1. Character 클래스를 상속
class Archer(Character):
    def __init__(self, name):
        # 궁수(Archer) 체력: 85 공격력: 14
        super().__init__(name, health = 85, attack_power = 14)
        self.max_health = 85

    # 2. 특수 공격: "치명타 사격(Fatal Shot)"
    def special_attack(self, target):
        print(f"{self.name}님이 '치명타 사격(Fatal Shot)'스킬을 사용합니다!")
        # random() : 0이상 1미만의 float 난수 반환
        Fatal_Shot = random.random()
        
        # 랜덤 모듈을 이용해서 50% 확률로 2.5배 데미지 상승
        if Fatal_Shot <= 0.5:
            damage = self.attack_power * 2.5
            print(f"기본 공격에 치명타 확률을 올립니다. [현재 공격력 : {damage}]")
            target.take_damage(damage)
        
        # 실패 시 기본 공격 적용
        else:
            print(f"치명타 스킬이 발동하지 않습니다.")
            self.attack(target)

    def reset_health(self):
        self.health = self.max_health