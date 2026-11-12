from flask import Flask,request,jsonify
import re
app = Flask(__name__)
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._% +-]+@[a-zA-Z0-9.-]+/.[a-zA-Z]{2,}$'
    re.match(pattern,email)is not None
    @app.route('/register',methods=['POST'])
    def register():
        data = request.get_json()
        name = data.get('name','')
        email = data.grt('email','')
        if not name or not email:
            return jsonify({
        "success":False,"status_code":400,
        "message":"validation error",
        "errors":{
                    "name":"name is required"if not name else None,
                    "email":"email is required"if not email else None
                }
            }),400
        if not is_valid_email(email):
            return jsonify({
                
            })
