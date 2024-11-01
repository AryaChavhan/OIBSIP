import requests

def get_weather(city):
    api_key = "_____________" # API from openweathermap is supposed to go here not sharing mine tho
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

       
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print(f"City: {city.capitalize()}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description.capitalize()}")
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print("Error fetching data. Check your internet connection.")
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)