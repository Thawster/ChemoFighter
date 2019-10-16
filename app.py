from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import objectId
import os
from character import Character, Ability, Armor

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
