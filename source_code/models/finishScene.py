from conf import settings



def finish_check(ship):
    '''
    1 燃料耗尽
    2 防护罩能量耗尽
    3 成功
    '''
    if ship.energy<=0:
        print(settings.energy_depletion)
        settings.finish_flag = 1
    elif ship.blood<=0:
        print(settings.blood_depletion)
        settings.finish_flag = 1
    elif ship.distance<=0:
        print(settings.success)
        settings.finish_flag = 1
    else:
        pass
