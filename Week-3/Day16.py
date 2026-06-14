# Web Requests & APIs
# n import requests
# n GET: response = requests.get(url)
# n response.status_code (200 = OK)
# n data = response.json()
# n Practice: wttr.in/London?format=j1
# n Practice: v2.jokeapi.dev/joke/Any
# n APIs = how Jarvis accesses the internet.


import json
import requests
def get_weather(city: str) -> None:
    url = f"http://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        data: dict = response.json()
        # print(data) # Print the entire JSON response for debugging
        print (json.dumps(data, indent=2))  # Print the entire JSON response for debugging with indentation
        current_condition = data['current_condition'][0]
        temp_c = current_condition['temp_C']
        weather_desc = current_condition['weatherDesc'][0]['value']
        print(f"The current temperature in {city} is {temp_c}°C with {weather_desc}.")
    else:
        print(f"Failed to retrieve weather data for {city}. Status code: {response.status_code}")

# v2.jokeapi.dev/joke/Any
def get_joke() -> None:
    joke_url = "https://v2.jokeapi.dev/joke/Any"
    joke_response = requests.get(joke_url)
    if joke_response.status_code == 200:
        joke_data: dict = joke_response.json()
        if joke_data['type'] == 'single':
            print(f"Joke: {joke_data['joke']}")
        elif joke_data['type'] == 'twopart':
            print(f"Setup: {joke_data['setup']}")
            print(f"Delivery: {joke_data['delivery']}") 


if __name__ == "__main__":
    city: str = input("Enter a city name to get the weather: ")
    get_weather(city) 
    print("\nHere's a joke for you:")
    get_joke()
