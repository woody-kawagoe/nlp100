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
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
 
@route("/")
def index(name="hoge"):
    name = request.forms.get("name")
    aliases_name = request.forms.get("aliases-name")
    tag = request.forms.get("tag")
    return template('index', name=name)
 
run(host="localhost", port=8000, debug=True, reloader=True)
