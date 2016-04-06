import argparse
import requests
import json

__author__ = 'Drew Shoemaker'

'''
Weather Report from the command line
'''

API_KEY = "9f65ee31c79c3b02e06fb4791b030ba2"


def setup_args():
    '''Defines command line arguments '''
    parser = argparse.ArgumentParser(prog='weather-check',
                                     description='Get weather data from city.')
    parser.add_argument('city', metavar='C', nargs='?',
                        help='the city you want to check for the weather' +
                        'Spaces in city names should be excluded (eg NewYorkCity).')
    parser.add_argument('countrycode', metavar='S', nargs='?', default='us',
                        help='country code of the city (defaults to us')
    return parser

def get_args():
    '''Get arguments passed from command line'''
    parser = setup_args()
    args = parser.parse_args()
    city = args.city
    country_code = args.countrycode
    return city, country_code


city, country_code = get_args()

url= "http://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid={2}".format(city, country_code, API_KEY)


response = requests.get(url)

print response.json()

