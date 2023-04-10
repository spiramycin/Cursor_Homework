from flask import Flask, abort
from datetime import datetime, timedelta, timezone

app = Flask(__name__)


@app.route('/')
def basic():
    app.logger.info('Reached hello route')
    return '<h1>Good start</h1>'

@app.route('/datetime/')
@app.route('/datetime/<string:tz>')
def get_time(tz=None):
    if tz:
        try:
            tz = timezone(timedelta(hours=int(tz)))
        except ValueError:
            abort(406, 'Please choose correct timezone')
    current_time = datetime.now(tz=tz).strftime('Current date %d-%m-%Y and time %H:%M:%S  %z')
    return current_time


@app.route('/datetime')
def get_documents():
    app.logger.info(f'Show documentation')
    return get_documents.__doc__.replace('\n', '<br>')




if __name__ == '__main__':
    import logging
    app.logger.setLevel(logging.DEBUG)


    app.run(host='127.0.0.1', port=5000, debug=True)