from flask import Flask
from dotenv import load_dotenv

load_dotenv()

# Create the Flask application object
app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/')
def hello():
    return "Hello World"

import controller.user_controller as user_controller
import controller.product_controller as product_controller