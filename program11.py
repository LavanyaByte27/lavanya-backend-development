from flask import Flask ,request,jsonify
app = Flask(__name__)


orders = []
@app.route('/addorders',methods =['POST'])
def add_order():
    data = request.get_json()
    orders.append(data)
    return jsonify({"message":"order add succesfully","order":data})
@app.route("/show orders",methods=['GET'])
def show_orders():
    return jsonify(orders)
if __name__=="__main__":
    app.run(debug=True)