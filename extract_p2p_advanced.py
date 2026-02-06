import requests
import json

def get_binance_p2p():
    url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    
    # Target 500 USD -> 265,000 VES
    payload = {
        "asset": "USDT",
        "fiat": "VES",
        "merchantCheck": True,
        "page": 1,
        "payTypes": ["Pago Movil"],
        "publisherType": "merchant",
        "rows": 10,
        "tradeType": "BUY", # We want to SELL to them
        "transAmount": "265000"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://p2p.binance.com",
        "Referer": "https://p2p.binance.com/en/trade/sell/USDT?fiat=VES&payment=Pago%20Movil"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json().get('data', [])
            result = []
            for item in data:
                adv = item.get('adv', {})
                advertiser = item.get('advertiser', {})
                result.append({
                    "nickname": advertiser.get('nickName'),
                    "price": adv.get('price'),
                    "min": adv.get('minSingleTransAmount'),
                    "max": adv.get('maxSingleTransAmount'),
                    "completion": advertiser.get('monthFinishRate')
                })
            return result
        else:
            return {"error": f"Status code {response.status_code}", "text": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    sell_side = get_binance_p2p()
    # Also get one value for Buy side for reference
    print(json.dumps(sell_side))
