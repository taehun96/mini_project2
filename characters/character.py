# 1.인스턴스 변수:
from abc import ABC, abstractmethod
class Character(ABC):
    def __init__(self, name, health, attack_power):
    #  name: 캐릭터 이름
        self.name = name
    # health: 체력
        self.health = health
    # attack_power: 공격력
        self.attack_power = attack_power

    # 2. 인스턴스 메서드:
    # attack(self, target): 기본 공격 (추상 메서드)
    def attack(self, target):
        print(f"{self.name}님이 {target.name}을 공격합니다.")
        target.take_damage(self.attack_power)
    # special_attack(self, target): 특수 공격 (추상 메서드)
    @abstractmethod
    def special_attack(self, target):
        pass
    # take_damage(self, damage): 피해를 입으면 체력이 감소
    def take_damage(self, damage):
        self.health -= damage
    # Is_alive(self): 체력이 0 이하이면 false 반환
    def live(self):
        return self.health > 0
    # reset_health(self): 캐릭터의 체력을 초기화
    def reset_health(self):
        pass
    # show_status(self): 캐릭터 정보를 출력
    def show_status(self):
        print(f"[{self.name}] 레벨: {self.level} | 체력: {self.health} | 공격력: {self.attack_power}")
    # get_name(self): 캐릭터의 이름을 가져옴
    def get_name(self):
        return self.name