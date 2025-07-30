# 도적(Rogue) 클래스
# 랜덤 모듈을 이용
import random
from .character import Character

# 1. Character 클래스를 상속
class Rouge(Character):
    def __init__(self, name, level):
        # 도적(Rogue) 체력: 90 공격력: 12
        super().__init__(name, level, health = 80, attck_power = 18)
        self.max_health = 90

# 2. 특수 공격: "급습 (ambush)"
    def special_attack(self, target):
        print(f"{self.name}님이 '급습'스킬을 사용합니다!")
#  • 랜덤 모듈을 이용해서 70% 확률로 3배 데미지를 입힘 (랜덤 확률 시스템 활용)
#  • 실패 시 공격하지 않음