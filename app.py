from flask import Flask, jsonify
from py2neo import Graph

from routes.users import users_bp
from routes.comments import posts_bp
from routes.posts import comments_bp

app = Flask(__name__)

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

@app.route('/')
def index():
    return jsonify({
        "message": "Bienvenue sur l'API Neo4j",
        "endpoints": {
            "users": "/users",
            "posts": "/posts",
            "comments": "/comments"
        }
    })

app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(comments_bp)


if __name__ == '__main__':
    app.run(debug=True)
