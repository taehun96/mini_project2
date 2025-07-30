from characters.character import Character
import random

class DemonSlayer(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack_power = 15)
        self.special_power = 35
        self.max_health = 100

    def special_attack(self, target):
        print(f"{self.name}가 😈악마의 힘😈을 해방합니다!")
        
        damage = self.special_power
        if random.random() < 0.3:
            damage *= 1.5
            print("'😈데몬베인😈'스킬 발동! 피해량 증가!")

        print(f"{target.name}에게 {int(damage)}의 피해를 입힙니다.")
        target.take_damage(int(damage))

        recoil = int(damage * 0.25)  # 반동 피해
        self.health -= recoil
        print(f"{self.name}도 반동 피해로 {recoil}의 🩸피해를 입습니다! (현재 💝체력: {self.health})")

    def reset_health(self):
        self.health = self.max_health