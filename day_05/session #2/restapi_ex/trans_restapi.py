(base) C:\Users\Purushotham\Desktop\oracle\day_05\session #2\flask_ex>python
>>> import requests
>>> # pip install requests
...
>>> url = r"https://apex.oracle.com/pls/apex/oraclejet/lp/activities/"
>>> data = requests.get(url)
>>> type(data)
<class 'requests.models.Response'>
>>> print(data)
<Response [200]>
>>> data.json()
{'items': [{'id': 1, 'name': 'Baseball', 'short_desc': 'Equipment we carry for baseball players.', 'image': 'css/images/product_images/baseball.jpg'}, {'id': 2, 'name': 'Bicycling', 'short_desc': 'Equipment we carry for biking enthusiasts.', 'image': 'css/images/product_images/gpbike.jpg'}, {'id': 3, 'name': 'Skiing', 'short_desc': 'Equipment we carry for skiing enthusiasts.', 'image': 'css/images/product_images/aceboot.jpg'}, {'id': 4, 'name': 'Soccer', 'short_desc': 'Equipment we carry for soccer players.', 'image': 'css/images/product_images/jrsoccerball.jpg'}], 'hasMore': False, 'limit': 25, 'offset': 0, 'count': 4, 'links': [{'rel': 'self', 'href': 'https://apex.oracle.com/pls/apex/oraclejet/lp/activities/'}, {'rel': 'describedby', 'href': 'https://apex.oracle.com/pls/apex/oraclejet/metadata-catalog/lp/activities/'}, {'rel': 'first', 'href': 'https://apex.oracle.com/pls/apex/oraclejet/lp/activities/'}]}
>>> d = data.json()
>>> d.keys()
dict_keys(['items', 'hasMore', 'limit', 'offset', 'count', 'links'])
>>> d['items']
[{'id': 1, 'name': 'Baseball', 'short_desc': 'Equipment we carry for baseball players.', 'image': 'css/images/product_images/baseball.jpg'}, {'id': 2, 'name': 'Bicycling', 'short_desc': 'Equipment we carry for biking enthusiasts.', 'image': 'css/r players.', 'image': 'css/images/product_images/jrsoccerball.jpg'}]