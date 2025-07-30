# 마법사(Mage) 클래스
# 1. Character 클래스를 상속
from .character import Character

class Mage(Character):
    def __init__(self, name):
        # 마법사(Mage) 체력: 80 공격력: 18 마나: 100 
        super().__init__(name, health = 80, attack_power = 18)
        self.mana = 100
        self.max_health = 80
        self.max_mana = 100

    # 2. 추가 인스턴스 변수: mana(마나, 기본값 100)
    def special_attack(self, target):
        # 마나 부족 시 예외 발생
        if self.mana < 20:
            print(f"{self.name}님의 마나가 부족하여 특수 공격 사용 불가 (현재 마나: {self.mana})")
            self.attack(target) # 마나 부족시 일반 공격으로 대체
            return
        
        # 3. 특수 공격: “파이어볼 fireball"
        # 마나 20을 소모하여 1.5배의 공격력으로 공격
        damage = int(self.attack_power * 1.5)
        self.mana -= 20
        print(f"{self.name}의 특수 공격 '파이어볼' [공격력 1.5배: {damage}, 마나 20 소모]")
        target.take_damage(damage)
        print(f"{self.name}의 마나가 20 감소했습니다. (남은 마나: {self.mana})")

    def reset_health(self):
        self.health = self.max_health
        self.mana = self.max_mana