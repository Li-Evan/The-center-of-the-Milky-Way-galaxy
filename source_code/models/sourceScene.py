import random
from models import battleScene
from models import ship


class Source:
    def __init__(self,ship):
        self.ship = ship
        # 不同场景的概率表
        self.num_scene = 2
        self.possibility = 1/self.num_scene
        self.probability_table = [self.possibility for _ in range(self.num_scene)]
        # 不同场景的函数
        self.source_table = [self.source1,self.source2]


    def generate_source(self):
        func = random.choices(self.source_table, weights=self.probability_table)[0]
        func()

    def source1(self):
        print("你来到了一个看起来非常普通的星球，这里的环境相对较为平静，没有特别明显的资源，但你仍然可以选择在这里停留一段时间。")
        print('''
        选择1描述：仔细探索这个星球的每一个角落。（花费5燃料）
        选择2描述：寻找周围星系中是否有更适合你的资源。
        ''')
        choice = eval(input("请输入你的选择"))
        if choice==1:
            self.ship.energy-=5
            x = random.choice([1,2])
            if x == 1:
                print('''
                你花了很长时间在这个星球上找寻资源，但是没有发现什么特别有价值的东西
                ''')
            else:
                print(
                    '''
                    你进入这个星球的大气层后，遭遇了一场突如其来的暴风雨，你不得不用尽全力才能保证飞船不被摧毁。
                    你成功了，但是你的飞船受损严重，需要花费一定的时间和资源进行修复。
                    你失去了10点防护罩能量。
                    '''
                )
                self.ship.blood -= 10
        elif choice==2:
            print(
                '''
                你乘坐飞船离开了这个星球，花费了一些时间寻找周围的星系，终于发现了一个适合你的资源丰富的星球。
                你获取了10点防御罩能量和1块蓝晶燃料。
                '''
            )
            self.ship.blood+=10
            num = self.ship.property.get("蓝晶燃料",0)
            self.ship.property["蓝晶燃料"] = num+1
        else:
            print("wrong choice")


    def source2(self):
        print("你来到了一片星际云雾区域，你可以选择前往云雾区域内部探索，或者离开此区域前往其他地方。")
        print('''
        选择1描述：前往云雾区域内部探索。
        选择2描述：离开此区域前往其他地方。
        ''')
        choice = eval(input("请输入你的选择"))
        if choice==1:
            print(
                '''
                你发现了一颗能量巨星，可以获得大量能源资源；
                但是，由于云雾区域的电磁干扰，你的飞船遭受了一定的损坏，需要花费一些时间进行修复。
                （获得1个星能燃料，失去10点防护罩能量）
                '''
            )
            num = self.ship.property.get("星能燃料",0)
            self.ship.property["星能燃料"] = num+1
            self.ship.blood -= 10
        elif choice==2:
            print(
                '''
                你离开了星际云雾区域，但是在途中遭遇到一支外星侵略军队，需要进行战斗。
                '''
            )
            # 生成敌人
            enemy = battleScene.generate_enemy()
            # 进入战斗场景
            battleScene.battle(self.ship, enemy)
        else:
            print("wrong choice")

if __name__ == '__main__':
    source = Source(ship.Ship())