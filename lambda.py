
from urllib.request import Request, urlopen
import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_weather_update(city):


    api_key = 'db2e46287558f6539b3f915fd3a870e7'
    request = Request("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city,api_key))
    response = json.loads(urlopen(request).read())
    print(response)
    return response


def lambda_handler(event, context):

    logger.debug(event)
    city = event["currentIntent"]["slots"]["location"]

    weather = get_weather_update(city)
    weather_description = weather['weather'][0]['description']
    temp_current = weather['main']['feels_like']
    temp_high = weather['main']['temp_max']
    temp_low = weather['main']['temp_min']
    cloud = weather['clouds']['all']


    return {
      "sessionAttributes": event["sessionAttributes"],
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText",
          "content":"The current temperature in {} is {} degrees with a high  and low of {} & {} degrees respectively with a cloudiness perecentage of {}.".format(city,temp_current,temp_high,temp_low,cloud)
          },
        }
    }
