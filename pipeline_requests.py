import requests

api_key = "apikey"
base_url = "https://alpha-vantage.p.rapidapi.com/query?"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

parameters = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": "IBM"
}

response = requests.get(base_url, headers=headers, params=parameters)


if response.status_code == 200:
    data = response.json()
    
    weekly_data = data.get("Weekly Time Series", {})  
 
    data_record = []
    if weekly_data:
        print("Weekly Time Series Data for IBM:")
        for date, stats in weekly_data.items():
           data_record.append([date,float(stats["1. open"]), float(stats["2. high"]),float(stats["3. low"]), float(stats["4. close"]),int(stats["5. volume"])])
        print(data_record[0])
    else:
        print("No weekly data found.")
else:
    print("API call failed with status code:", response.status_code)