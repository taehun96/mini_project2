# 전사(Warrior) 클래스
# 1. Character 클래스를 상속
from .charcter import Character

class Warrior(Charcter):
    def __init__(self, name, level):
        # 전사(Warrior) 체력:100 공격력:15특수 공격 시 2배 공격력 (단, 본인 체력 5 감소)
        super().__init__(name, level, health = 100, attck_power = 15)
        self.max_health = 100
    # 2. 특수 공격: "강력한 일격" (power_strike)
    def special_attack(self, target):
        # 2배의 공격력을 가하지만, 본인도 5의 체력을 잃음
        damage = self.attack_power * 2
        print(f"{self.name}님의 '강력한 일격'스킬 발동! [공격력 2배: {damage}, 체력 5소모]")
        