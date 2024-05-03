import requests

url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"

querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

route_name = response.json().get('data').get('603')[1].get('long_name')

print(route_name)