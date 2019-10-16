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

@app.route('/stock/<item_id>/delete', methods=['POST'])
def stock_delete(item_id):
    """Delete one item."""
    stock.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('stock_index'))

@app.route('/stock/new')
def stock_new():
    """Create a new item."""
    return render_template('stock_new.html', item = {}, title = 'New Item')

@app.route('/stock/<item_id>/edit')
def stock_edit(item_id):
    """Show the edit form for a item."""
    item = stock.find_one({'_id': ObjectId(item_id)})
    return render_template('stock_edit.html', item=item, title = 'Edit Item')