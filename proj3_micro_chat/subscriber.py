import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# создаем специальный объект для подписки
p = r.pubsub()

# Подписываемся на канал с именем 'chat_channel'
p.subscribe('chat_channel')
print('Подключился к "chat_channel". Жду сообщений...')

# Запускаем бесконечный цикл для прослушки сообщений
for message in p.listen():
	# Первое сообщение, которое придет, будет системным (о подтверждении подписки).
	# Нам нужно только сообщения типа 'message'
	if message['type'] == 'message':
		print(f'Новое сообщение в чате: {message['data']}')