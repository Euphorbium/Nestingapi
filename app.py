from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from nest import nest

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "testuser": generate_password_hash("badpassword"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/api/nest/', methods=['POST'])
@auth.login_required
def nest_post():
    return jsonify(nest(request.json, [arg for arg in request.args]))


if __name__ == '__main__':
    app.run()
