# 도적(Rogue) 클래스
# 랜덤 모듈을 이용
from .character import Character
import random

# 1. Character 클래스를 상속
class Rogue(Character):
    def __init__(self, name):
        # 도적(Rogue) 체력: 90 공격력: 12
        super().__init__(name, health = 80, attack_power = 12)
        self.max_health = 90

# 2. 특수 공격: "급습 (ambush)"
    def special_attack(self, target: Character):
        print(f"{self.name}님이 '🥷급습(Ambush)🥷'스킬을 사용합니다!")
        # random() : 0이상 1미만의 float 난수 반환
        ambush = random.random()
        
        # 랜덤 모듈을 이용해서 70% 확률로 3배 데미지를 입힘 (랜덤 확률 시스템 활용)
        if ambush <= 0.7:
            damage = self.attack_power * 3
            print(f"급습 성공 [현재 ⚔️공격력⚔️ : {damage}]")
            target.take_damage(damage)
        
        # 실패 시 공격하지 않음
        else:
            print("급습을 시도했지만 중심을 잃고 본인에게 데미지를 입혔습니다.")
            self.take_damage(10)
        
    def reset_health(self):
        self.health = self.max_health