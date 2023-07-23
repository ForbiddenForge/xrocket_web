from flask import Flask, send_from_directory


def create_webapp():
    app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
    
    @app.route("/")
    def bix():
        return send_from_directory('static', 'index.html')
    
    
    return app