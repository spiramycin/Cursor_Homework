from flask import Flask, request, Response, abort
from functools import lru_cache
from Flask_intro import methods
from methods import formatters, get_doc
from util import convertation_str_to_bool


app = Flask(__name__)



@app.route('/stats/')
@lru_cache(maxsize=1)  # can use cuz no flask proxies refered
def stats_root():
    """List all methods."""
    ret = {'methods': list(methods)}

    format = request.args.get('format')
    if format:
        func_format = formatters[format][1]
        return func_format(ret)
    format_str = "<h1>{}. {}</h1> <p>{}</p>"
    ret['methods'] = [format_str.format(i, name, get_doc(name)) for i, name in enumerate(ret['methods'], start=1)]
    return Response(ret['methods'])



@app.route('/stats/<string:method>')
def stats(method):
    kwargs = request.args.to_dict()
    kwargs = convertation_str_to_bool(**kwargs)
    print(kwargs)
    try:
        func = methods[method]
    except KeyError:
        abort(404, f'Method {method} not found')

    try:
        # format is set on a statapi module level defaults
        res, mime = func(**kwargs)
    except Exception as exc:
        abort(400)

    # TODO: add error reporting verbosity
    #       e.g. when format is not supported

    return Response(res, mimetype=mime)


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    import logging
    app.logger.setLevel(logging.DEBUG)

    # (!) Never run your app on '0.0.0.0 unless you're deploying
    #     to production, in which case a proper WSGI application
    #     server and a reverse-proxy is needed
    #     0.0.0.0 means "run on all interfaces" -- insecure
    app.run(host='127.0.0.1', port=5000, debug=True)