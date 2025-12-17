from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# ======================
# Database Model
# ======================
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, body):
        self.title = title
        self.body = body

# ======================
# Schema
# ======================
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "body", "date")

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# ======================
# Routes
# ======================

@app.route('/get', methods=['GET'])
def get_articles():
    articles = Articles.query.all()
    return jsonify(articles_schema.dump(articles))


@app.route('/add', methods=['POST'])
def add_article():
    data = request.get_json()

    # Validation
    if not data or not data.get('title') or not data.get('body'):
        return jsonify({"error": "Title and Body are required"}), 400

    article = Articles(
        title=data['title'],
        body=data['body']
    )

    db.session.add(article)
    db.session.commit()

    return article_schema.jsonify(article), 201


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = Articles.query.get_or_404(id)

    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)


# ======================
# Run App
# ======================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
