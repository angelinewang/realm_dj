from flask import Flask
import os

app = Flask(__name__)

app.run(port=int(os.environ.get("PORT", 3000)), host='0.0.0.0', debug=True)

# @app.route("/")
# def hello_world():
#     name = os.environ.get("NAME", "World")
#     return "Hello {}!".format(name)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
