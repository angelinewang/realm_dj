import os

from base.wsgi import application as app 

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     name = os.environ.get("NAME", "World")
#     return "Hello {}!".format(name)

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
if __name__ == "__main__":
    app.run(port=int(os.environ.get("DBPORT", "8000")),
            host=os.environ.get("DBHOST", "35.195.57.236"), debug=False)
