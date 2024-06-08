# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form action="/send" method="post">
        <label for="secret">Enter Secret:</label>
        <input type="text" id="secret" name="secret" required>
        <button type="submit">Send Secret</button>
    </form>
    '''

@app.route('/send', methods=['POST'])
def send_secret():
    secret = request.form['secret']
    response = requests.post('https://onetimesecret.com/api/v1/share', data={
        'secret': secret,
        'ttl': '3600', # Time to live in seconds
        'passphrase': '', # Optionally you can add a passphrase
    }, auth=('rod.costa8@gmail.com', 'f918864fa74b3e31d1793ff15a485d206540b51c'))
    
    if response.status_code == 200:
        secret_info = response.json()
        return jsonify(secret_info)
    else:
        return 'Error sharing secret', response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

