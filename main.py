import flask
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/')
def index():
    return flask.send_from_directory('static', 'index.html')

@app.route('/barchart')
def barchart():
    return flask.send_from_directory('static', 'barchart.html')

@app.route('/baraxes')
def baraxes():
    return flask.send_from_directory('static', 'baraxes.html')

@app.route('/scatter')
def scatter():
    return flask.send_from_directory('static', 'scatter.html')

@app.route('/scatternxt')
def scatternxt():
    return flask.send_from_directory('static', 'scatternxt.html')

@app.route('/renderearth')
def renderearth():
    return flask.send_from_directory('static', 'renderearth.html')

@app.route('/barcscginteraction')
def barcscginteraction():
    return flask.send_from_directory('static', 'barcscginteraction.html')

@app.route('/nCov')
def nCov():
    return flask.send_from_directory('static', 'nCov.html')

@app.route('/nCovnxt')
def nCovnxt():
    return flask.send_from_directory('static', 'nCovnxt.html')

@app.route('/nCovnxt-province')
def nCovnxtprovince():
    return flask.send_from_directory('static', 'nCovnxt-province.html')

@app.route('/themeriver')
def themeriver():
    return flask.send_from_directory('static', 'themeriver.html')

@app.route('/themeriver-lr')
def themeriverlr():
    return flask.send_from_directory('static', 'themeriver-lr.html')

@app.route('/themeriver-lr-custom')
def themeriverlrcus():
    return flask.send_from_directory('static', 'themeriver-lr-custom.html')

@app.route('/colorgradient')
def colorgradient():
    return flask.send_from_directory('static', 'color-gradient.html')

@app.route('/scatter-animation')
def scatteranimation():
    return flask.send_from_directory('static', 'Scatter-Animation.html')

@app.route('/multi-channel')
def multichannel():
    return flask.send_from_directory('static', 'Multi-Channel.html')

@app.route('/multi-channel-texture')
def multichanneltexture():
    return flask.send_from_directory('static', 'multi-channel-texture.html')

@app.route('/static/<fname>')
def sendfile(fname):
    return flask.send_from_directory('static', fname)

# https://icon-icons.com/icon/heart-love-like-favourite-follow/131237
# https://icon-icons.com/icon/heart-love-favorite-favourite/13187
@app.route('/favicon.ico') 
def favicon(): 
    return flask.send_from_directory('static', 'loveheart.ico', mimetype='image/vnd.microsoft.icon')

app.run(host='0.0.0.0', port=11666, debug=True)
