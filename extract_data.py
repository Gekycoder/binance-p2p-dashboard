import requests
import json
import sys

def get_data():
    # 1. Fetch BCV
    try:
        bcv_res = requests.get('https://ve.dolarapi.com/v1/dolares/oficial')
        bcv_data = bcv_res.json()
        bcv_rate = bcv_data.get('promedio', 378.46)
    except:
        bcv_rate = 378.46

    # 2. Fetch Binance P2P (Sell mode - looking for Buyers)
    # Target: 500 USD ~ 265,000 VES (rough estimate for filtering)
    search_amount = 265000 
    
    payload = {
        "asset": "USDT",
        "fiat": "VES",
        "merchantCheck": True,
        "page": 1,
        "payTypes": ["Pago Movil"],
        "publisherType": "merchant",
        "rows": 10,
        "tradeType": "BUY", # We want to SELL, so we find BUYERS
        "transAmount": str(search_amount)
    }

    try:
        p2p_res = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', json=payload)
        p2p_data = p2p_res.json().get('data', [])
    except Exception as e:
        print(f"Error P2P: {e}")
        p2p_data = []

    # 3. Fetch Binance P2P (Buy mode - looking for Sellers)
    payload["tradeType"] = "SELL"
    try:
        p2p_res_buy = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', json=payload)
        p2p_data_buy = p2p_res_buy.json().get('data', [])
    except:
        p2p_data_buy = []

    output = {
        "bcv": bcv_rate,
        "sell_orders": p2p_data,
        "buy_orders": p2p_data_buy
    }
    
    print(json.dumps(output))

if __name__ == "__main__":
    get_data()
