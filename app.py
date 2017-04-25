# dependencies
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/python-songs'
db = SQLAlchemy(app)

import models

# routes
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    return jsonify({
        'message': 'Hey what\'s up hello'
    })

@app.route('/api/v1/songs', methods=['GET'])
def songs():
    # add data to db √
    # get all songs from db
    # return all songs
    # songs = models.Songs.query.all()
    # print(songs)
    # return jsonify(songs=songs)
    # return jsonify(json_list = models.Songs.query.all())
    return jsonify(data=[i.serialize for i in models.Songs.query.all()])


# main
if __name__ == '__main__':
    app.debug = True
    app.run()
