import http.server
import socketserver
import json
import urllib.request
import urllib.error
import random
import os

PORT = int(os.environ.get('PORT', 5001))

class BinanceBridge(http.server.BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _serve_file(self, filename, content_type):
        try:
            filepath = os.path.join(os.path.dirname(__file__), filename)
            with open(filepath, 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(content)
        except Exception as e:
            self._send_json({"error": f"File {filename} not found"}, status=404)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '/dashboard_arbitraje.html':
            self._serve_file('dashboard_arbitraje.html', 'text/html')
        elif self.path == '/manifest.json':
            self._serve_file('manifest.json', 'application/json')
        elif self.path == '/sw.js':
            self._serve_file('sw.js', 'application/javascript')
        elif 'oficial' in self.path:
            try:
                with urllib.request.urlopen("https://criptoya.com/api/bcv") as res:
                    val = json.loads(res.read())
                    self._send_json({"promedio": float(val)})
            except:
                self._send_json({"promedio": 378.45})
        elif 'trm' in self.path:
            try:
                with urllib.request.urlopen("https://criptoya.com/api/dolarapi/trm") as res:
                    self._send_json(json.loads(res.read()))
            except:
                self._send_json({"promedio": 3950.0})
        elif 'usd' in self.path:
            self._send_json({"promedio": 1.0})
        else:
            self._send_json({"status": "P2P Bridge Active", "port": PORT})

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b""
        
        target_url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "lan": "en",
            "Origin": "https://p2p.binance.com",
            "Referer": "https://p2p.binance.com/en/trade/sell/USDT?fiat=VES",
            "X-Requested-With": "XMLHttpRequest",
            "clienttype": "web"
        }

        req = urllib.request.Request(target_url, data=post_data, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req) as response:
                resp_data = response.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.end_headers()
                self.wfile.write(resp_data)
        except urllib.error.HTTPError as e:
            try:
                body = json.loads(post_data.decode())
                fiat = body.get("fiat", "VES")
                trade = "buy" if b"SELL" in post_data else "sell"
                fallback_url = f"https://criptoya.com/api/binancep2p/{trade}/usdt/{fiat.lower()}/1"
                
                with urllib.request.urlopen(fallback_url) as f_res:
                    f_data = json.loads(f_res.read())
                    mock_data = {"data": [{"adv": {"price": f_data.get("p", 540), "minSingleTransAmount": 1000, "maxSingleTransAmount": 500000}, "advertiser": {"nickName": "RESPALDO_CLOUD", "monthOrderCount": 1000, "monthFinishRate": 1.0, "userRole": "MERCHANT"}} for _ in range(5)]}
                    self._send_json(mock_data)
            except:
                self._send_json({"data": []})
        except Exception as e:
            self._send_json({"error": str(e), "data": []}, status=500)

print(f"--- BRIDGE ACTIVO EN PUERTO {PORT} ---")
print("Servidor de archivos y puente API funcionando.")
with socketserver.TCPServer(("0.0.0.0", PORT), BinanceBridge) as httpd:
    httpd.allow_reuse_address = True
    httpd.serve_forever()
