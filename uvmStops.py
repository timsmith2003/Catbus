import requests

url = "https://transloc-api-1-2.p.rapidapi.com/stops.json"

querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}


#response = requests.get(url, headers=headers, params=querystring)

#stop = response.json().get('data')[3].get('name')

#print(response.json())

#print("\n")

#print(stop)