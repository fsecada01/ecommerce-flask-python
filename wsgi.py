from backend import flask_app

if __name__ == '__main__':
    flask_app.app_context()
    flask_app.run(debug=True)
