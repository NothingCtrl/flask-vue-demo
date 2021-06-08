import flask_login
from flask import redirect, request as flask_request
from backend.schema.User import User, users

# login manager
login_manager = flask_login.LoginManager()

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

@login_manager.unauthorized_handler
def unauthorized():
    if '/api' in flask_request.url:
        return dict(error=True, message="Please log in for access."), 403
    if flask_request.method == 'GET':
        return redirect(flask_login.login_url('login', flask_request.url))
    else:
        return dict(error=True, message="Please log in for access."), 403
