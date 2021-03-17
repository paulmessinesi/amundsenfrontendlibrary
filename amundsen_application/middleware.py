from collections import Callable

from werkzeug.wsgi import ClosingIterator


class PrefixMiddleware:

    def __init__(self, app: Callable, prefix: str = ''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ: dict, start_response: Callable) -> ClosingIterator:
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)

        return self.app(environ, start_response)