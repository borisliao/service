import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # SECRET_KEY is used by Flask and extensions to keep data safe.
    # It’s set to 'dev' to provide a convenient value during development, but it should be overridden with a random value when deploying.
    # DATABASE is the path where the SQLite database file will be saved.
    # It’s under app.instance_path, which is the path that Flask has chosen for the instance folder.

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello', methods=['GET'])
    def hello():
        return 'Hello, World!'

    return app
