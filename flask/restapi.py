from flask import Flask, request, jsonify
from flask_cors import CORS
import main, passwordgenerator

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api', methods=['POST'])
def process():
    data = request.json
    string_input1 = data.get('string_input1')
    string_input2 = data.get('string_input2')
    string_input3 = int(data.get('string_input3'))

    password = passwordgenerator.generate_password(14)
    
    if string_input3 == 1:
        main.create_user(string_input1, password, string_input2)
        main.add_user_to_group(string_input1, "porg")
    elif string_input3 == 0:
        main.delete_user(string_input1)
    
    return string_input1

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
