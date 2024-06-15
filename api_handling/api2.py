import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    # success is key like , dictionary think like that
    # data object mein "data" hai kya
    
    if data["success"] and "data" in data:
        stock_data = data["data"]
        # in js we do lthis , username = user_data.login.username
        name = stock_data["Name"]
        symbol = stock_data["Symbol"]
        return name, symbol
    else:
        # raise will raise the error
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        name , symbol= fectch_random_user_freeapi()
        print(f"name: {name} \nSymbol: {symbol}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()