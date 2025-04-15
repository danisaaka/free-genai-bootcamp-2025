from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///language_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models


class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    spanish_word = db.Column(db.String(100), nullable=False)
    english = db.Column(db.String(100), nullable=False)
    parts = db.Column(db.JSON)


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    words = db.relationship('Word', secondary='word_groups', backref='groups')


class WordGroup(db.Model):
    __tablename__ = 'word_groups'
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))


class StudySession(db.Model):
    __tablename__ = 'study_sessions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))


class StudyActivity(db.Model):
    __tablename__ = 'study_activities'
    id = db.Column(db.Integer, primary_key=True)
    study_session_id = db.Column(
        db.Integer, db.ForeignKey('study_sessions.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class WordReviewItem(db.Model):
    __tablename__ = 'word_review_items'
    id = db.Column(db.Integer, primary_key=True)
    study_session_id = db.Column(
        db.Integer, db.ForeignKey('study_sessions.id'))
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    correct = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes


@app.route('/words', methods=['GET'])
def get_words():
    words = Word.query.all()
    return jsonify([{
        'id': word.id,
        'spanish_word': word.spanish_word,
        'english': word.english,
        'parts': word.parts
    } for word in words])


@app.route('/words/<int:id>', methods=['GET'])
def get_word(id):
    word = Word.query.get_or_404(id)
    return jsonify({
        'id': word.id,
        'spanish_word': word.spanish_word,
        'english': word.english,
        'parts': word.parts
    })


@app.route('/groups', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    return jsonify([{
        'id': group.id,
        'name': group.name
    } for group in groups])


@app.route('/groups/<int:id>', methods=['GET'])
def get_group(id):
    group = Group.query.get_or_404(id)
    return jsonify({
        'id': group.id,
        'name': group.name
    })


@app.route('/groups/<int:id>/words', methods=['GET'])
def get_group_words(id):
    group = Group.query.get_or_404(id)
    words = group.words
    return jsonify([{
        'id': word.id,
        'spanish_word': word.spanish_word,
        'english': word.english,
        'parts': word.parts
    } for word in words])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
