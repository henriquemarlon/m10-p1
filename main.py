from flask import Flask, request, jsonify
import sqlite3
import jwt
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'To-Do API'
    }
)

app = Flask(__name__)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route('/addTask', methods=['POST'])
def addTask():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    data = request.get_json()
    title = data['title']
    content = data['content']
    cur.execute("INSERT INTO tasks (title, content) VALUES (?, ?)", (title, content))
    con.commit()
    return jsonify({"status": "success"})

@app.route('/getTasks', methods=['GET'])
def getTasks():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return jsonify({"tasks": tasks})

@app.route('/deleteTask', methods=['DELETE'])
def deleteTask():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    title = request.args.get('title')
    cur.execute("DELETE FROM tasks WHERE title = ?", (title,))
    con.commit()
    return jsonify({"status": "success"})

@app.route('/updateTask', methods=['PUT'])
def updateTask():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    data = request.get_json()
    title = data['title']
    content = data['content']
    cur.execute("UPDATE tasks SET content = ? WHERE title = ?", (content, title))
    con.commit()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
