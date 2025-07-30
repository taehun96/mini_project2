import random
from characters.character import Character

# player : Character 이런 식으로 쓰는건 타입 힌트, 주석 힌트로써 사용 가능
class BattleManager:
    def __init__(self, player : Character, enemy: Character):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        self.player.reset_health()
        self.enemy.reset_health()

        print("Start Battle")
        # 랜덤 모듈을 이용해서 전투의 선공(첫 번째 공격자)을 랜덤으로 결정한다.
        first_attack_player, second_attack_player = (self.player, self.enemy) if random.choice([True, False]) else (self.enemy, self.player)
        print(f"{first_attack_player}님이 선공입니다.")

        turn = 1

        # 첫 번째 캐릭터가 공격
        while self.player.live() and self.enemy.live():
            print(f"{turn}턴 : {first_attack_player}님의 공격 턴")
            # 기본 공격 vs특수 공격 선택:
            # 랜덤 모듈을 통해 70% 확률로 기본 공격, 30% 확률로 특수 공격
            if random.random() <= 0.7:
                first_attack_player.attack(second_attack_player)
            else:
                first_attack_player.special_attack(second_attack_player)
            
            # 한 캐릭터의 체력이 0이 되면 전투 종료
            if not second_attack_player.live():
                print(f"""{second_attack_player}님이 죽었습니다.
                    축하합니다. {first_attack_player} 승리!""")
                break

            # 두 번째 캐릭터가 살아있으면 반격
            first_attack_player, second_attack_player = second_attack_player, first_attack_player
            turn += 1
        
        print("End Battle")



# 1. 전투 흐름:
    # 타임 모듈을 이용해서, 전투 진행시 딜레이를 추가하여 더 자연스러운 전투를 연출한다.
# 3. 예외 처리
    # 마나 부족 시 공격 불가