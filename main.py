import vk

from config import my_token

__author__ = 'i@ayugov.ru'


session = vk.Session(
    access_token=my_token)
api = vk.API(session)


if __name__ == '__main__':
    from statuser import get_info
    from remessenger import get_vk_message

    get_vk_message()
    get_info(uid=None)
