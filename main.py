from flask import Flask, json, jsonify, request

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

tasks= [
    {
        "id": 1,
        "title": u"buy groceries",
        "description": u"milk, cheese",
        "done": False
    },
    {
        "id": 2,
        "title": u"learn python",
        "description": u"find a good tutorial",
        "done": False
    }
]

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

@app.route("/add-data", methods= ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide data in the correct format",
        }, 400)

    task= {
        'id': tasks[-1]['id']+1,
        "title": request.json['title'],
        'description': request.json.get('description', ""),
        "done": False
    }
    
    tasks.append(task)
    return jsonify({
        "status": 'success',
        "message": 'task added successfully'
    })

if(__name__=="__main__"):
    app.run(debug=True)