from django.shortcuts import render

def home(request):
	import requests 
	import json
	
	# Grab crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
	price = json.loads(price_request.content)


    # Geab crypto news 
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api' : api, 'price': price})


def prices(request):
	if request.method == 'POST':
		import requests 
		import json 
		aryan = request.POST['aryan']
		aryan = aryan.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ aryan +"&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'aryan':aryan, 'crypto':crypto})

	else:
		return render(request, 'prices.html', {})



