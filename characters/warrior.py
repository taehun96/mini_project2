# 전사(Warrior) 클래스
# 1. Character 클래스를 상속
from .character import Character

class Warrior(Character):
    def __init__(self, name):
        # 전사(Warrior) 체력:100 공격력:15특수 공격 시 2배 공격력 (단, 본인 체력 5 감소)
        super().__init__(name, health = 100, attack_power = 15)
        self.max_health = 100
    # 2. 특수 공격: "강력한 일격" (power_strike)
    def special_attack(self, target):
        # 2배의 공격력을 가하지만, 본인도 5의 체력을 잃음
        damage = self.attack_power * 2
        print(f"{self.name}님의 '⚔️ 강력한 일격 ⚔️'스킬 발동! [공격력 2배: {damage}, 💝 체력 5소모]")
        target.take_damage(damage)
        self.health -= 5
        print(f"{self.name}님의 체력이 5 감소 (💝 남은 체력:{self.health})")

    # 전투 전 체력 원상 복귀
    def reset_health(self):
        self.health = self.max_health