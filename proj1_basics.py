import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

print(f'Подключились к Redis? Ответ сервера: {r.ping()}')

# Команда set сохраняет данные
# как словарь: my_dict['name'] = 'Vasya'
# Ключ: 'name', значение 'Vasya'
r.set('name', 'Vasya')
r.set('city', 'Moscow')

print('Сохранили в Redis два ключа: "name" и "city"')

# Команда get получает данные
# Как в словаре: user_name = my_dict['name']
user_name = r.get('name')
user_city = r.get('city')

print(f'Получили из Redis: {user_name} из города {user_city}')


# Если ключа нет?
# Пробуем получить ключ, которого нету
non_existent_value = r.get('job')
print(f'Значение для несуществующего ключа "job": {non_existent_value} (тип: {type(non_existent_value)})')