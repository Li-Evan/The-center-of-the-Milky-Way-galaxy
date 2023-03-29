from conf import settings
from models import battleScene
from models import ship
from models import civilizationScene
from models import initScene
from models import finishScene
from models import sourceScene
import random

class Galaxy:
    '''
    管理游戏资源和行为的类
    '''

    def __init__(self):
        self.ship = ship.Ship()

    # 进入战斗场景
    def battle(self):
        # 生成敌人
        enemy = battleScene.generate_enemy()
        # 进入战斗场景
        battleScene.battle(self.ship,enemy)

    # 进入资源场景
    def source(self):
        sourceScene.Source(self.ship).generate_source()

    # 改变速度
    def change_speed(self):
        print("请选择你的飞行速度（越快的飞行速度能够增加每单位能量形式的光年数，但是会降低开启各类场景的概率）")
        print("1. 低速 2. 中速 3. 高速")
        speed = eval(input())
        if speed == 1:
            settings.speed = "low"
        elif speed == 2:
            settings.speed = "middle"
        elif speed == 3:
            settings.speed = "high"

    # 每行驶 10 光年以概率生成场景
    def generate_scene(self):
        # 减少距离
        self.ship.distance -= 10
        open_scene_possibility = [0,1]
        # 减少燃料并以概率生成场景
        if settings.speed=="low":
            self.ship.energy -= 10/settings.low_speed_distance
            open_scene_possibility = [settings.low_speed_scene, 1 - settings.low_speed_scene]
        elif settings.speed=="middle":
            self.ship.energy -= 10/settings.middle_speed_distance
            open_scene_possibility = [settings.middle_speed_scene, 1 - settings.middle_speed_scene]
        elif settings.speed=="high":
            self.ship.energy -= 10/settings.high_speed_distance
            open_scene_possibility = [settings.high_speed_scene, 1 - settings.high_speed_scene]
        open_scene = [1, 0]
        open_flag = random.choices(open_scene, weights=open_scene_possibility)[0]
        # print(open_scene_possibility)
        # print(open_flag)
        if open_flag == 1:
            func = random.choices([self.battle, self.source])[0]
            func()


    # 主循环选择界面
    def display_choice(self):
        print(
            '''
            1. 展示角色信息
            2. 以当前速度继续行驶10光年
            3. 更改速度
            '''
        )
        choice = eval(input("请输入你的选择"))
        if choice==1:
            self.ship.display()
        elif choice==2:
            self.generate_scene()
        elif choice==3:
            self.change_speed()

    def run(self):
        initScene.init()
        while True:
            # 展示选项并根据选项运行场景
            self.display_choice()

            # 查看是否达到结束游戏的条件
            finishScene.finish_check(self.ship)
            if settings.finish_flag==1:
                break


if __name__ == '__main__':
    galaxy = Galaxy()
    galaxy.run()