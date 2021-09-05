from flask import Flask, abort, redirect, url_for, request, render_template, make_response, session
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
        <form method="post">
            <p><input type=text name=username></p>
            <p><input type=submit value=Login></p>
        </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f'/var/www/uploads/{secure_filename(file.filename)}')
    ...


with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'
