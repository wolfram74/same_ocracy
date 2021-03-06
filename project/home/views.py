from flask import render_template, Blueprint, flash, url_for, redirect
from markovbot import MarkovBot
from project import db
from project.home.models import Figure
import os
import sys
import random

home_blueprint = Blueprint('home', __name__, template_folder='templates')
ARCHIVES = './project/assets/%s_tweets.txt'

@home_blueprint.route('/', methods=['GET'])
def home():
    '''
    choices object should have left and right, which should in turn have handle and correct
    '''
    fork = random.randint(0,2)
    splitter = '*)^@'
    choices = {}
    if fork==0:
        #identify real tweeter
        subject_model = random_figure()
        source = open(ARCHIVES % subject_model.handle, 'r')
        string = random.sample(source.readline().decode('utf-8').split(splitter), 1)[0]
        source.close()
        left_handle = '@%s' % subject_model.handle
        right_handle = left_handle + ' twitter bot'
        left_subject = {'handle': left_handle, 'correct': 'correct'}
        right_subject = {'handle': right_handle, 'correct': ''}
    elif fork ==1:
        # identify fake tweet
        subject_model = random_figure()
        string = generate_fake_tweet(subject_model.handle)
        left_handle = '@%s' % subject_model.handle
        right_handle = left_handle + ' twitter bot'
        left_subject = {'handle': left_handle, 'correct': ''}
        right_subject = {'handle': right_handle, 'correct': 'correct'}
    elif fork==2:
        # compare two twitter bots
        fig1 = random_figure()
        fig2 = random_figure()
        string = generate_fake_tweet(fig1.handle)

        if random.randint(0,1)==1:
            left_handle = '@%s twitter bot' % fig1.handle
            right_handle = '@%s twitter bot' % fig2.handle
            left_subject = {'handle': left_handle, 'correct': 'correct'}
            right_subject = {'handle': right_handle, 'correct': ''}
        else:
            left_handle = '@%s twitter bot' % fig2.handle
            right_handle = '@%s twitter bot' % fig1.handle
            left_subject = {'handle': left_handle, 'correct': ''}
            right_subject = {'handle': right_handle, 'correct': 'correct'}


    # return render_template('index.html', tweet=string, left=left_subject, right=right_subject)
    choices['left'] = left_subject
    choices['right'] = right_subject
    choices['correct'] = 'correct'
    return render_template('index.html', tweet=string, choices=choices)

@home_blueprint.route('/next', methods=['GET'])
def next():
    #tracking of user responses will go here in imminent future
    return redirect(url_for('home.home'))


def generate_fake_tweet(subject_handle):
    trying = True
    bot = MarkovBot()
    bot.read('./project/assets/%s_tweets.txt' % subject_handle)
    while trying:
        try:
            string = bot.generate_text(25)
            trying = False
        except:
            print('panicked at the disco')
            continue
    return string

def random_figure():
    figures = db.session.query(Figure).all()
    return random.sample(figures, 1)[0]
