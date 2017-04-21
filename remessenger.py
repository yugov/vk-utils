from main import api

__author__ = 'i@ayugov.ru'


def get_vk_message():
    messages = api.messages.get()
    for message in messages[1:]:
        if message['read_state'] == 0:
            print('Сообщение из VK:\n{name} {surname} пишет:\n{body}'.format(
                surname=api.users.get(user_id=message['uid'])[0]['last_name'],
                name=api.users.get(user_id=message['uid'])[0]['first_name'],
                body=message['body']))


if __name__ == '__main__':
    get_vk_message()
