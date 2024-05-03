import requests

url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#current_location_green1 = response.json().get('data').get('603')[0].get('location')

#current_location_green2 = response.json().get('data').get('603')[1].get('location')

#current_speed_green1 = response.json().get('data').get('603')[0].get('speed')

#current_speed_green2 = response.json().get('data').get('603')[1].get('speed')

#current_location_red = response.json().get('data').get('603')[2].get('location')

#current_speed_red = response.json().get('data').get('603')[2].get('speed')


#print(f"speed: {current_speed_green1}\n{current_location_green1}\n\n")

#print(f"speed: {current_speed_green2}\n{current_location_green2}\n\n")

#print(f"speed: {current_speed_red}\n{current_location_red}")





#4006422 ON CAMPUS 1


#4006426 REDSTONE EXPRESS
