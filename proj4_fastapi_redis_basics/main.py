import time
import redis 
from fastapi import FastAPI

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_super_slow_data_from_db(item_id: str):
	"""
	Эта функция имитирует очень медленный запрос к БД/
	Func that imitates super slow DB data
	"""
	print(f'Иду в БД за {item_id}.. займет 2 секунды')
	time.sleep(2)
	return f'Это ОЧЕНЬ медленные данные для товара {item_id}'

@app.get('/items/{item_id}')
def get_item(item_id: str):
	cache_key = f'item:{item_id}'
	cache_data = redis_client.get(cache_key)

	if cache_data:
		print('Ура данный найдеры в кэше Redis!')
		return {'source': 'cache', 'data': cache_data}
	
	print('Эх.. в кэше пусто')
	real_data = get_super_slow_data_from_db(item_id)
	
	redis_client.set(cache_key, real_data, ex=30)
	return {'source': 'cache', 'data': real_data}