
from flask import Flask, request,jsonify
app = Flask(__name__)
students = []
@app.route('/students',methods=['GET'])
def get_students():
    return jsonify(students)
app.route('/students',methods=['POST'])
def add_students():
    data = request.get_json()
    students.append(data)
    return jsonify({
        "message":"students added successfully","student":data
    }),201
if __name__=="__main__":
    app.run(debug = True)