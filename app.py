import os

from flask import Flask
import sqlalchemy
from connect_tcp import connect_tcp_socket

app = Flask(__name__)


def init_connection_pool() -> sqlalchemy.engine.base.Engine:
    # use a TCP socket when INSTANCE_HOST (e.g. 127.0.0.1) is defined
    if os.environ.get("INSTANCE_HOST"):
        return connect_tcp_socket()

    raise ValueError(
        "Missing database connection type. Please define one of INSTANCE_HOST, INSTANCE_UNIX_SOCKET, or INSTANCE_CONNECTION_NAME"
    )


if __name__ == '__main__':
    # main()
    app.run(host="127.0.0.1", port=8080, debug=False)
