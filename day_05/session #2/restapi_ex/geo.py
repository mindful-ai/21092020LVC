>>> import requests
>>> url = r"http://maps.googleapis.com/maps/api/geocode/json"
>>> rep = requests.get(url, params={'address':'bangalore'})
>>> res
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'res' is not defined
>>> rep
<Response [200]>
>>> rep.json()
{'error_message': 'You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account', 'results': [], 'status': 'REQUEST_DENIED'}