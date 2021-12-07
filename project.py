from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Study',
        'description': u'L - 1, 3, 5', 
        'done': False
    }

]

@app.route("/adding-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data."
        }, 400)
    contact = {
        'id':tasks[-1]['id'] + 1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message":"Task added successfully!"
    })

@app.route("/getting-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if __name__ == "__main__":
    app.run(debug = True) 