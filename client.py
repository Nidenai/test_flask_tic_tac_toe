import requests
import json

res_get = requests.get('http://127.0.0.1:5000/api/games')
print(res_get)
res = requests.post('http://127.0.0.1:5000/api/games/newgame', data={'gamename': 'one', 'rows': 3})
print(res)
