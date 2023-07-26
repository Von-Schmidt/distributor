from flask import Flask, request, jsonify
from flask_cors import CORS
import main, passwordgenerator, namebase

groupid = "distributors"
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api', methods=['POST'])
def process():
    conn = namebase.create_connection()

    data = request.json
    name = data.get('string_input1')
    email = data.get('string_input2')
    username = data.get('string_input3')
    company = data.get('string_input4')

    password = passwordgenerator.generate_password(14)

    main.create_user(username, password, email)
    main.add_user_to_group(username, groupid)
    
    namebase.add_user(name, username, email, company)

    namebase.close_connection(conn)

    return username

@app.route('/api', methods=['GET'])
def get_users():
    users = namebase.get_all_users()
    return jsonify(users)

@app.route('/api/<username>', methods=['DELETE'])
def delete(username):
    namebase.delete_user(username)
    main.delete_user(username)
    return {'result': 'User deleted'}

@app.route('/api/table', methods=['DELETE'])
def delete_table():
    namebase.delete_all_users()
    namebase.delete_table()
    return {'result': 'Table deleted'}

@app.route('/api/table', methods=['POST'])
def create_table():
    namebase.create_table()
    return {'result': 'Table created'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
