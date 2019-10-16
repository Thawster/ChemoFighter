from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import objectId
import os
from character import Character, Ability, Armor
from arena import Team, Arena

host = os.environment.get('MONGODB_URI', 'mongodb://localhost:27017/ChemoFighter')
client = MongoClient(host=host)
db = client.get_default_database()
roster = db.roster

app = Flask(__name__)

@app.route('/')
def main_menu():
    """Home Screen"""
    return render_template('chemo_index.html' roster=roster)

@app.route('/roster', methods=['POST'])
def roster_submit():
    """submit a new Character"""
    character = {
        'name': request.form.get('name'),
        'starting health': request.form.get('starting health')
    }
    roster.insert_one(character)
    return redirect(url_for('chemo_index'))

@app.route('/roster/<character_id>', methods=['POST'])
def roster_update():
    """submit a edited Character"""
    updated_character = {
        'name': request.form.get('name'),
        'starting health': request.form.get('starting health')
    }
    roster.update_one(
        {'_id': ObjectId(character_id)},
        {'$set': updated_item})
    return redirect(url_for('roster_show', item_id=item_id))
    )