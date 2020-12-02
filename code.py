import vk_api, json
from telebot.apihelper import send_message
from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token
from bad_words import words
from vk_api import keyboard

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

keyboard = {
    "one_time": None,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{}",
                 "label": "Вопросы 🤷"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{}",
                "label": "Пригласть 🖐"
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{}",
                "label": "Развлечения 🎉"
            },
            "color": "default"
            }


        ]
    ]
}


keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def sender(id,text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text.lower()
                id = event.chat_id

                print("User:",event.user_id,"Message:", msg)

                if msg == 'привет':
                    sender(id, "Здравствуй, кванторианец")


                elif msg in words:
                    sender(id, f'@{event.user_id}, вы нарушили правило беседы!')

