from flask import Flask,request,jsonify;
app = Flask(__name__)
valid_username="admin"
valid_password="password123"
@app.route('/login',methods = ['POST'])
def login():
    data =request.get_json()
    username = data.get('username','')
    password = data.get('password','')
    if username == valid_username and password==valid_password:
        return jsonify({"success":True,"message":"login succesfully"})
    else:
        return jsonify({"success":False,"message":"inva;id username or password"}),201
if __name__=='__main__':
    app.run(debug=True)
