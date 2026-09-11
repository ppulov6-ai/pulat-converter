#!/usr/bin/env python3
import os, sys, threading, webbrowser
from http.server import ThreadingHTTPServer
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for p in (HERE, ROOT, os.path.join(ROOT, "app")):
    if os.path.isdir(p) and p not in sys.path:
        sys.path.insert(0, p)
from webapp import make_handler
HOST, PORT = "127.0.0.1", 17831
def main():
    httpd = ThreadingHTTPServer((HOST, PORT), make_handler())
    threading.Timer(0.4, lambda: webbrowser.open(f"http://{HOST}:{PORT}/")).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return 0
if __name__ == "__main__":
    sys.exit(main())
