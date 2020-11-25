import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

# def get_keyboard(buts):
# 	global get_but
# 	nb = []
# 	color = ''
# 	for i in range(len(buts)):
# 		nb.append([])
# 		for k in range(len(buts[i])):
# 			nb[i].append(None)
# 	for i in range(len(buts)):
# 		for k in range(len(buts[i])):
# 			text = buts[i][k][0]
# 			if buts[i][k][1] == 'p':
# 				color = 'positive'
# 			elif buts[i][k][1] == 'n':
# 				color = 'negative'
# 			nb[i][k] = {
#                 "action": {
#                     "type": "text",
#                     "payload": "{\"button\": \"" + "1" + "\"}",
#                     "label": f"{text}"
#                 },
#                 "color": f"{color}"
#             }
# 	first_keyboard = {
# 	    'one_time': False,
# 	    'buttons': nb
# 	    }
# 	first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
# 	first_keyboard = str(first_keyboard.decode('utf-8'))
# 	return first_keyboard
#
# keyboard1 = get_keyboard(
# 	[
# 		[ ('Ссылка на канал DimPy', 'p') ],
# 		[ ('Погода', 'p') ],
# 		[ ('Ссылка на автора канала DimPy', 'p') ]
# 	]
# )

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : 0})

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			if event.from_chat:

				msg = event.text.lower()
				id = event.chat_id

				if msg in ['пока', 'привет']:
					sender(id, f'@{event.user_id}, вы нарушили правило беседы!')