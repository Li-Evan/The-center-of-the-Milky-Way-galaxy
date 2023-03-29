
from models import finishScene
from conf import settings
import random

class Enemy:

    def __init__(self, aggressivity, blood, describe, property):
        self.aggressivity = aggressivity  # 攻击力
        self.blood = blood  # 血量
        self.describe = describe  # 描述
        self.property = property  # 击杀后会掉落的资源

def generate_enemy():
    # 根据概率随机初始化敌人对象
    probabilities = [settings.s_probability, settings.a_probability, settings.b_probability, settings.c_probability]
    items = ["s", "a", "b", "c"]
    item = random.choices(items, weights=probabilities)[0]
    if item == "s":
        enemy_describe = random.choice(settings.s_enemy)
        enemy_aggressivity = settings.s_aggressivity
        enemy_blood = settings.s_blood
    elif item == "a":
        enemy_describe = random.choice(settings.a_enemy)
        enemy_aggressivity = settings.a_aggressivity
        enemy_blood = settings.a_blood
    elif item == "b":
        enemy_describe = random.choice(settings.b_enemy)
        enemy_aggressivity = settings.b_aggressivity
        enemy_blood = settings.b_blood
    elif item == "c":
        enemy_describe = random.choice(settings.c_enemy)
        enemy_aggressivity = settings.c_aggressivity
        enemy_blood = settings.c_blood
    enemy = Enemy(enemy_aggressivity, enemy_blood, enemy_describe, {})
    return enemy

def battle(ship, enemy):
    # 遭遇敌人的文字描述
    print("你遭遇了"+enemy.describe)
    # 打死敌人需要的攻击回合数 enemy.blood/ship.aggressivity
    # 自己被打死需要的攻击回合数 ship.blood/enemy.aggressivity
    # 被敌人打死了
    # round = min(enemy.blood / ship.aggressivity - 1,ship.blood / enemy.aggressivity)
    # ship.blood-=round*enemy
    # if ship.blood<0:
    #     print("fail")
    # else:
    #     print("win")
    # print()
    if enemy.blood / ship.aggressivity - 1 > ship.blood / enemy.aggressivity:
        # 展示文字信息
        print("你被敌人击败了")
        # 以finish_way(2)转到游戏结束模块
        # finishScene.finish()
    else:
        # 扣血
        ship.blood -= abs((enemy.blood / ship.aggressivity - 1)*enemy.aggressivity)

        # 加资源
        for key, value in enemy.property:
            num = ship.property.get(key, 0)
            ship.property[key] = num + 1
        # 展示文字信息
        print("你击败了敌人")

