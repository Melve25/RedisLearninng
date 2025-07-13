import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# тот же set но появился доп параметр 'ex' (expire)
# 'ex'=5 означает "удалить этот ключ через 5 секунд"
key = 'secret_message'
r.set(key, 'This message will self_destruct', ex=5)

print (f'Сохраняем временный ключ "{key}" на 5 секунд')

# проверяем сразу
value_now = r.get(key)
print(f'Значение сейчас: {value_now}')

# Ждем 6 секунд

print('Ждем 6 секунд...')
time.sleep(6)

# Проверяем значение
value_later = r.get(key)
print(f'Значение через 6 секунд: {value_later}')