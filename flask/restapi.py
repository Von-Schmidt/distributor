from flask import Flask, request, jsonify
from flask_cors import CORS
import main, passwordgenerator, namebase

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
    main.add_user_to_group(username, "porg")
    
    namebase.add_user(name, username, email, company)

    namebase.close_connection(conn)

    return username

@app.route('/api', methods=['GET'])
def get_users():
    users = namebase.get_all_users()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
