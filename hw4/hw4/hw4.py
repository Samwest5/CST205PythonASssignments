# Sam Westigard
# CST 205
# HW 4
# Provides functions and routing for webpages calls home html and picture html

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from random import randint
from imageInfo import info
from PIL import Image


app = Flask(__name__)
bootstrap = Bootstrap(app)


def randomPicture():
    return randint(0,9)


@app.route('/')
def home():
    return render_template('home.html',
                           rand1=randomPicture(),
                           rand2=randomPicture(),
                           rand3=randomPicture(),
                           info=info)


@app.route('/picture/<ID>/<pIndex>')
def picture(pIndex, ID):
    im = Image.open('static/' + ID + '.jpg')
    picFormat = im.format
    picMode = im.mode
    picWidth, picHeight = im.size
    picTitle = info[int(pIndex)]['title']
    picAuthor = info[int(pIndex)]['flickr_user']
    return render_template('picture.html', ID=ID,
                           pFormat=picFormat, pMode=picMode,
                           pWidth=picWidth, pHeight=picHeight,
                           pTitle=picTitle, pAuthor=picAuthor)


if __name__ == '__main__':
    app.run()

