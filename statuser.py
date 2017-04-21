import datetime
from time import sleep

from main import api

__author__ = 'i@ayugov.ru'


def platform_detecter(plat):
    if plat == 1:
        return 'Мобильная версия сайта'
    elif plat == 2:
        return 'Iphone'
    elif plat == 3:
        return 'Ipad'
    elif plat == 4:
        return 'Android'
    elif plat == 5:
        return 'Windows Phone'
    elif plat == 6:
        return 'Winindows 10'
    elif plat == 7:
        return 'Полная версия сайта'
    else:
        return 'Invalid client'


def get_info(uid=None):
    for friend_id in api.friends.get(user_id=uid):
        profile = api.users.get(user_id=friend_id, fields='last_seen')
        for p in profile:
            if 'last_seen' in p:
                # print(p)
                print(p['last_name'] + ' ' + p['first_name'] + ' был в сети: ' + datetime.datetime.fromtimestamp(
                        int(p['last_seen']['time'])
                    ).strftime('%H:%M:%S %d-%m-%Y') + ' с устройства: ' + platform_detecter(p['last_seen']['platform'])
                )
        sleep(0.4)

if __name__ == '__main__':
    get_info(uid=None)
