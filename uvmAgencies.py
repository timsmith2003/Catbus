import requests

url = "https://transloc-api-1-2.p.rapidapi.com/agencies.json"




querystring = {"callback":"call","agencies":"603"}

headers = {
	"X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

#response = requests.get(url, headers=headers, params=querystring)

#full_name = response.json().get('data')[0].get('short_name')

#coords = response.json().get('data')[0].get('position')

#print("\n")
#print(full_name)
#print(coords)
#print("\n")

