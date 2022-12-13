from flask import Flask , jsonify , request
app = Flask(__name__)

todos = [
    { "label": "My first task", 
    "done": False 
    },

    { "label": "My second task",
     "done": False 
     }
]

@app.route('/todos' , methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text #because json_text is the same as 'todos'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request.json)
    return jsonify(todos) 
#fetch from url
#method: POST 
#test sample todo
#catch and error (if it works, do this, if it fails, do that)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) #deletes item in position of todo list
    return jsonify(todos)
#fetch from url
#method: DELETE
#specify which number in the list to delete
#catch and error (if it works, do this, if it fails, do that)






# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)


