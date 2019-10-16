from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import objectId
import os

app = Flask(__name__)

@app.route('/')
def main_menu():
    """Home Screen"""
    return render_template('chemo_index.html')