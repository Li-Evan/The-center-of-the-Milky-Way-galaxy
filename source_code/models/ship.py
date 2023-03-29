# import pygame
# from conf import settings
# from models import bullet

class Ship:

    def __init__(self):

        self.username = "Evan"
        self.aggressivity = 100 # 攻击力
        self.blood = 50 # 防御罩能量
        self.energy = 50 # 飞船能量
        self.science = 1 # 科技值
        self.distance = 200 # 距离地球距离
        self.property = {
            "蓝晶燃料":0,
            "等离子燃料": 0,
            "星能燃料": 0,
            "量子燃料": 0,
                         } # 各类特殊道具

    def get_weapon(self):
        text = "当前攻击力:"+str(self.aggressivity)+ "\n当前武器:"
        if self.aggressivity<150:
            text += '''光子炮(PhotonCannon)：
            高功率能量武器，可以对敌方飞船造成致命打击。（攻击力百分比100 %）'''
        elif self.aggressivity>=150 and self.aggressivity<200:
            text += ''' 质子导弹(ProtonMissile)：
            导弹武器，可以锁定敌人并追踪敌方飞船，可以在远距离造成巨大的破坏。（攻击力百分比120 %）'''
        elif self.aggressivity>=200 and self.aggressivity<250:
            text += '''离子激光(IonLaser)：
            激光武器，可以迅速消耗敌方飞船的护盾，并造成较大伤害。（攻击力百分比150 %）'''
        elif self.aggressivity>=250 and self.aggressivity<300:
            text += '''    电磁脉冲(ElectromagneticPulse)：
            电磁武器，可以瘫痪敌方飞船的电子设备和护盾系统。（攻击力百分比170 %）'''
        elif self.aggressivity>=300 and self.aggressivity<400:
            text += '''中子枪(NeutronGun)：
            中子武器，可以穿透敌方飞船的装甲，造成严重损伤。（攻击力百分比200 %）'''
        elif self.aggressivity>=400:
            text += '''反物质炮(AntimatterCannon)：
            高级能量武器，可以发射反物质能量，对敌人造成毁灭性打击。（攻击力百分比230 %）'''

        return text

    def get_property(self):
        text = ""
        for key,value in self.property.items():
            text+=(key+":"+str(value)+"\n")
        return text
    def display(self):
        print("当前角色名字:"+self.username)
        print(self.get_weapon())
        print("当前飞船能量:"+str(self.energy))
        print("当前防御罩能量:"+str(self.blood))
        print("当前科技值:"+str(self.science))
        print("当前距离地球距离:"+str(self.distance))
        print("当前道具:"+self.get_property())

if __name__ == '__main__':
    ship = Ship()
    ship.display()
