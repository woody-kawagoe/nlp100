#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import (
    route,
    run,
    template,
    request,
    static_file,
    url,
    get,
    post,
    response,
    view,
    error
)
from pymongo import MongoClient
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

@route("/")
def index(name="hoge"):
    get_val = {
        'name':request.query.name,
        'aliases_name':request.query.aliases_name,
        'tags_value':request.query.tags_value
    }
    get_val['result'] = search(get_key(get_val))
    return template('index', get_val)
def search(key):
    if key:
        client = MongoClient('localhost', 27017)
        artists = client.nlp_artists.artists
        return [x for x in artists.find(key)][:10]
    else:
        return []
def get_key(get_val):
    key = {}
    if get_val['name']: key['name'] = get_val['name']
    if get_val['aliases_name']: key['aliases.name'] = get_val['aliases_name']
    if get_val['tags_value']: key['tags.value'] = get_val['tags_value']
    return key

run(host="localhost", port=8000, debug=True, reloader=True)
