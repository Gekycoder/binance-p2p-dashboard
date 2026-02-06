import requests
import json

def get_criptoya_data():
    try:
        # Criptoya Binance P2P endpoint
        # Method: Binance P2P, Asset: USDT, Fiat: VES
        res = requests.get('https://criptoya.com/api/binancep2p/usdt/ves/1')
        data = res.json()
        
        # BCV
        bcv_res = requests.get('https://ve.dolarapi.com/v1/dolares/oficial')
        bcv_rate = bcv_res.json().get('promedio', 378.46)
        
        output = {
            "p2p": data,
            "bcv": bcv_rate
        }
        print(json.dumps(output))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    get_criptoya_data()
