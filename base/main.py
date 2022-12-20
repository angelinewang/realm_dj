from flask import Flask
import os

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("DB_PORT", "5432")),
            host="35.195.57.236", debug=False)

# @app.route("/")
# def hello_world():
#     name = os.environ.get("NAME", "World")
#     return "Hello {}!".format(name)

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    # app.run(port=int(os.environ.get("DB_PORT", "8000")),
    #         host=os.environ.get("DB_HOST", "localhost"), debug=False)
