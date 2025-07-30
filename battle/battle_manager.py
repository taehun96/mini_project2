import random
import time
from characters.character import Character

class BattleManager:
    def __init__(self, player: Character, enemy: Character):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        self.player.reset_health()
        self.enemy.reset_health()

        print("Start Battle")
        first_attack_player, second_attack_player = (self.player, self.enemy) if random.choice([True, False]) else (self.enemy, self.player)
        print(f"{first_attack_player.get_name()}님이 선공입니다.")

        turn = 1
        while self.player.live() and self.enemy.live():
            print(f"{turn}턴 : {first_attack_player.get_name()}님의 공격 턴")
            time.sleep(1)

            if random.random() <= 0.7:
                first_attack_player.attack(second_attack_player)
            else:
                first_attack_player.special_attack(second_attack_player)

            time.sleep(1.3)

            if not second_attack_player.live():
                print(f"{second_attack_player.get_name()}님이 죽었습니다. 축하합니다. {first_attack_player.get_name()} 승리!")
                break

            first_attack_player, second_attack_player = second_attack_player, first_attack_player
            turn += 1

        time.sleep(1)
        print("End Battle")