import requests
import json
import math

#this just prints out the api in a nicer format so its easier for us to see


#wetaher class holds all the logic and getters for getting info from the api
class weather_api():
    def __init__(self,city):
        self.__city = city
        self.__mode = None
        self.__response = self.__api_call()
        self.day_or_night_setter()

    def __api_call(self): #private method 
        parameters = {
        "key": "9e7572dd28a24a9fa8125738232909",
        "q": self.__city,
        "days": 2
        }
        response = requests.get("http://api.weatherapi.com/v1/forecast.json", params = parameters)
        return response
    
    def jprint(self):
        #creates a formatted string of the python JSON obj
        text = json.dumps(self.__response.json(), sort_keys=True, indent=4)
        print(text)


    def get_city(self):
        return self.__city
    
    def get_current_temp_f(self):
        temp_f = self.__response.json()["current"]["temp_f"]
        temp_f = math.floor(temp_f)
        temp_f = str(temp_f)
        return temp_f
    
    def get_current_temp_c(self):
        temp_c = self.__response.json()["current"]["temp_c"]
        temp_c = math.floor(temp_c)
        temp_c = str(temp_c)
        return temp_c

    def get_current_condition(self):
        condition = self.__response.json()['current']['condition']['text']
        return condition

    def get_current_max_temp(self):
        max_temp = self.__response.json()['forecast']['forecastday'][0]['day']['maxtemp_f']
        max_temp = math.floor(max_temp)
        return max_temp

    def get_current_low_temp(self):
        low_temp = self.__response.json()['forecast']['forecastday'][0]['day']['mintemp_f']
        low_temp = math.floor(low_temp)
        return low_temp
    
    def get_current_hour(self): #implement logic for checking if past 30 mins to upper it
        current_time = self.__response.json()['current']['last_updated']
        current_time = current_time[-5::] #contains string with current time, make logic that if the last two is greater than 30 dont floor but the other one
        current_time = current_time[:2:]#takes first two of of the hour/ logic would make it higher if hour higher than 30
        current_time = int(current_time)
        return current_time

    def get_currrent_sunset_time(self):
        time_of_sunset = self.__response.json()['forecast']['forecastday'][0]['astro']['sunset']
        if(time_of_sunset.endswith('PM')):#this for some annoying reason needs to be converted to 24 hour format so do logic in there also floor or upper logic
            time_of_sunset = time_of_sunset[:2:]
            time_of_sunset = int(time_of_sunset) + 12
        else:
            time_of_sunset = time_of_sunset[:2:]
            time_of_sunset = int(time_of_sunset)

        return time_of_sunset    

    def day_or_night_setter(self):
        if(self.get_current_hour() > self.get_currrent_sunset_time()): #if its past the sunset time for that city then the mode is night mode
            self.__mode = 'night'
        else:
            self.__mode = 'day'

    def get_hour(self, hour_from_current):#gets hour n hours away from current hour.
        curr = self.get_current_hour() + hour_from_current

        if(curr >= 24):
            curr = curr - 24
            curr = self.__response.json()["forecast"]['forecastday'][1]['hour'][curr]['time']
            curr = curr[10:13:]
            return int(curr)

        curr = self.__response.json()["forecast"]['forecastday'][0]['hour'][curr]['time']
        curr = curr[10:13:]
        return int(curr)
    
    def get_mode(self):
        return self.__mode
    
    def get_hour_condition(self,away_from):
        curr = self.get_current_hour() + away_from
        if(curr >= 24):
            curr = curr - 24
            return self.__response.json()["forecast"]['forecastday'][1]['hour'][curr]['condition']['text']
        
        return self.__response.json()["forecast"]['forecastday'][0]['hour'][curr]['condition']['text']


    def get_hour_temp_f(self,away_from):
        curr = self.get_current_hour() + away_from
        if(curr >= 24):
            curr = curr - 24
            temp = math.floor(self.__response.json()["forecast"]['forecastday'][1]['hour'][curr]['temp_f'])
            return temp
        
        temp = math.floor(self.__response.json()["forecast"]['forecastday'][0]['hour'][curr]['temp_f'])
        return temp





#lets do 

# background colors and icons depending on 1. the time, and 2. the current condition
#if the cities time is after the places sunset, then we use night icons and then decide based on current condition
#otherwise we use day icons

