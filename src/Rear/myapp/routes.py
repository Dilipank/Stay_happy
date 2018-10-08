from myapp import app
from myapp.models import User
import json
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# @app.route('/all_list', methods = ['GET', 'POST'])
# def all_list():
#     #content = request.get_json()
#     #print (content)
#     all = User.query.all()
#     res = []
#     for u in all:
#         res.append({'name': u.name, 'location': u.location})
#     jlist = json.dumps(res)
#     return jlist

@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        content = request.get_json()
        filter = User.query.filter_by(location = content['location']).all()
        x = [{'name': hotel.name, 'location': hotel.location} for hotel in filter]
        convert = json.dumps(x)
        return convert
    no_filter = User.query.all()
    x = [{'name': hotel.name, 'location': hotel.location} for hotel in no_filter]
    convert = json.dumps(x)
    return convert