import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token
from bad_words import words

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

def sender(id,text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text.lower()
                id = event.chat_id

                print("User:",event.user_id,"Message:", msg)

                if msg == 'привет':
                    sender(id, "Здравствуй, кванторианец")

                if msg == 'где находится кванториум?':
                    sender(id, "«Детский технопарк Кванториум Дружба» находится по адресу Россия, Рязань, улица Дзержинского, 6.")

                if msg in words:
                    sender(id, f'@{event.user_id}, вы нарушили правило беседы!')

