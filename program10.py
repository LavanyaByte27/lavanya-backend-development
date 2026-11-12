from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return"server is running.send post request to/n8n-webhook"
@app.route('/n8n -webhook',methods =['Post'])
def n8n_webhook():
    data = request.get_json()
    print("recived from n8n :",data)
    return jsonify({"status":"recived","data":data})
if __name__=="__main__":
    app.run(debug=True)