from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/ChemoFighter')
client = MongoClient(host=host)
db = client.get_default_database()
roster = db.roster

app = Flask(__name__)

@app.route('/')
def main_menu():
    """Home Screen"""
    return render_template('chemo_index.html', roster=roster.find())

@app.route('/roster', methods=['POST'])
def roster_submit():
    """submit a new Character"""
    character = {
        'name': request.form.get('name'),
        'health': request.form.get('health'),
        'power': request.form.get('power'),
        'defence': request.form.get('defence')
    }
    roster.insert_one(character)
    return redirect(url_for('main_menu'))

@app.route('/roster/<character_id>', methods=['POST'])
def roster_update(character_id):
    """submit a edited Character"""
    updated_character = {
        'name': request.form.get('name'),
        'health': request.form.get('health'),
        'power': request.form.get('power'),
        'defence': request.form.get('defence')
    }
    roster.update_one(
        {'_id': ObjectId(character_id)},
        {'$set': updated_character})
    return redirect(url_for('roster_show', character_id=character_id))

@app.route('/roster/new')
def roster_new():
    """Create a new character."""
    return render_template('roster_new.html', character = {}, title = 'New Character')

@app.route('/roster/<character_id>/edit')
def roster_edit(character_id):
    """Show the edit form for a character."""
    character = roster.find_one({'_id': ObjectId(character_id)})
    return render_template('roster_edit.html', character=character, title = 'Edit Character')

@app.route('/roster/<character_id>')
def roster_show(character_id):
    """Show a single character."""
    character = roster.find_one({'_id': ObjectId(character_id)})
    return render_template('roster_show.html', character=character)

@app.route('/roster/<character_id>/delete', methods=['POST'])
def roster_delete(character_id):
    """Delete one character."""
    roster.delete_one({'_id': ObjectId(character_id)})
    return redirect(url_for('main_menu'))

@app.route('/team', methods=['POST'])
def team_submit():
    """Submit a team."""
    
    return redirect(url_for('stock_index'))

@app.route('/team/select')
def team_select():
    """Choose team size"""
    return render_template('team_select.html', roster=roster.find())

@app.route('/team/choose')
def team_choose():
    """Choose team characters"""
    return render_template('team_choose.html', roster=roster)

if __name__ == '__main__':
    #app.run(debug=True)
    #If port problem appears
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))