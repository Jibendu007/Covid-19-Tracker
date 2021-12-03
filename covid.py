import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "7da48e13cdmsh9ea06a20f7c7a8ap1845f7jsn686c08a21397"
    }

response = requests.request("GET", url, headers=headers).json()


def search_city(city1):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['active']) != 0:
            for city in response['state_wise'][each]['district']:
                if city.lower() == city1.lower():
                    return response['state_wise'][each]['district'][city]['active']


flag = 1
while flag != 0:
    city1 = input("Enter the city = ")
    if city1 == "0":
        break
    cases = search_city(city1)
    print("Total Active Cases in " +city1+"is : ",cases)