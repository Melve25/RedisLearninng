import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Зададим ключ для нашего пользователя
# Хорошая практика - использовать префиксы (user:, order:) для группировки ключей.
user_key = 'user:101'

initial_data = {
	'name': 'Max',
	'email': 'max@gmail.com',
	'visits': '12',
	'status': 'active'
}

r.hset(user_key, mapping=initial_data)
print(f'Создали профиль для ключа "{user_key}"')

# читаем данные HGETALL и HGET

# HGETALL получает все поля и значения из хэша в виде словаря.
full_profile = r.hgetall(user_key)
print('\nПолный профиль пользователя (hgetall):')
print(full_profile)

# HGET
user_email = r.hget(user_key, 'email')
print(f'\nТолько email пользователя (hget): {user_email}')

# Обновляем и увеличиваем значения

# Обновляем email. Меняем только ОДНО поле
r.hset(user_key, 'email', 'new.max.email@gmail.com')
print('\nОбновили email...')

# Атомарно увеличим счетчик посещений на 1 (команда HINCRBY)
# "Атомарно" значит операция выполнится целиком 
# даже если 1000 программ одновременно пытаются это сделать. результат будет верным.
r.hincrby(user_key, 'visits', 1)
print('Увеличили счетчик посещений...')

# Проверяем результат
update_profile = r.hgetall(user_key)
print('\nИтоговый профиль после всех изменений:')
print(update_profile)