from flask import Flask
from routes import *

app = Flask(__name__)

# Register blue prints for all routes
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True, port=5000)