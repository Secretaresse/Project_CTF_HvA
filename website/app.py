# Backend for PAD Main website
# This file is owned by Team D

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.secret_key = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d59727823bcbf'
   
    from pandactf import Panda
    from cookiesctf import Cookies
    from adminctf import Adminctf
    from login import Login
    from signup import Signup
    from home import Home
    from leaderbord import Leaderbord

    app.register_blueprint(Panda, url_prefix='/')
    app.register_blueprint(Cookies, url_prefix='/')
    app.register_blueprint(Adminctf,url_prefix='/')
    app.register_blueprint(Login, url_prefix='/')
    app.register_blueprint(Signup, url_prefix='/')
    app.register_blueprint(Home, url_prefix='/')
    app.register_blueprint(Leaderbord, url_prefix='/')



    return app
    

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=3000)
