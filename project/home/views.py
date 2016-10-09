from flask import render_template, Blueprint, flash, url_for
from markovbot import MarkovBot
import os
import sys


home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/', methods=['GET'])
def home():
    print(sys.argv[0])
    bot = MarkovBot()
    bot.read('./project/home/assets/hank_log.txt')
    string = bot.generate_text(25)
    return render_template('index.html', filler=string)
