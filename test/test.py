import requests 

# https://pitorch-flask.herokuapp.com/predict
# http://localhost:5000/predict
resp = requests.post("http://localhost:5000/predict", data={'que': 'hi'})

print(resp.text)