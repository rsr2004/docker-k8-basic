# app.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

EJBCA_API_URL = 'http://ejbca:8080/ejbca/ejbca-rest-api/v1'

@app.route('/')
def home():
    return 'Welcome to the EJBCA Web Interface!'

@app.route('/status')
def status():
    try:
        response = requests.get(f'{EJBCA_API_URL}/ca/{ca_name}/status')
        return jsonify({
            'ejbca_status': response.json()
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })

@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user_dn = data.get('user_dn')

    # Payload to create a new user
    user_payload = {
        "username": username,
        "password": password,
        "subject_dn": user_dn,
        "token_type": "P12"
    }

    try:
        # Create user in EJBCA
        user_response = requests.post(f'{EJBCA_API_URL}/certificate/user', json=user_payload)
        user_response.raise_for_status()
        
        # Generate certificate for the user
        cert_response = requests.post(f'{EJBCA_API_URL}/certificate/{username}', auth=(username, password))
        cert_response.raise_for_status()
        
        return jsonify({
            'user': user_response.json(),
            'certificate': cert_response.json()
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)

