#!/usr/bin/env python3
"""Local live server for the office view (laptop). Stdlib only, localhost only.

  python3 scripts/serve_office.py [--port 8000]
then open  http://localhost:8000/office-view/office.html
The page detects localhost, lists real run logs from /api/runs and plays them live (it polls every 2 s).
Serves the repo root read-only (GET only). Binds to 127.0.0.1 so nothing is exposed to the network.
"""
import argparse, http.server, json, os, socketserver, urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
RUNS = os.path.join(ROOT, "runs")

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path == "/api/runs":
            items = []
            for n in os.listdir(RUNS):
                if n.endswith(".jsonl"):
                    fp = os.path.join(RUNS, n)
                    with open(fp) as f:
                        lines = sum(1 for l in f if l.strip())
                    items.append({"id": n[:-6], "lines": lines, "mtime": os.path.getmtime(fp)})
            items.sort(key=lambda x: -x["mtime"])
            body = json.dumps(items).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()

    def do_POST(self):
        self.send_error(405, "read-only server")

    def log_message(self, fmt, *args):
        pass

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8000)
    a = p.parse_args()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", a.port), H) as srv:
        print(f"Office view: http://localhost:{a.port}/office-view/office.html  (Ctrl+C to stop)")
        srv.serve_forever()

if __name__ == "__main__":
    main()
