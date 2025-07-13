import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

channel_name = 'chat_channel'

print('Готов отправлять сообщения. Запустите subscriber.py в другом терминале.')
time.sleep(3)

while True:
	message_to_send = input('Введите ваше сообщение (или exit для выхода):')

	if message_to_send.lower() == 'exit':
		break

	# Публикуем сообщение в наш канал команда (PUBLISH)
	r.publish(channel=channel_name, message=message_to_send)
	print(f'сообщение "{message_to_send}" отправлено!')

print('Издатель завершил работу')