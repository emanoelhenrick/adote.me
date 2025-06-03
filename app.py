from flask import Flask, send_from_directory
from api.routes import api
from flask_cors import CORS
import os

print(os.path.join(os.path.dirname(__file__), "src/db"))

PORT = 5000

app = Flask(__name__, static_folder="dist", static_url_path="/dist")

CORS(app)

app.json.ensure_ascii = False

app.register_blueprint(api)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join(app.static_folder, "assets"), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.static_folder, "images"), filename)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(port=PORT)
