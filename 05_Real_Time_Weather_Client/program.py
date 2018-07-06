#!/usr/bin/env python3
import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    user_zip = False
    banner()
    user_zip = get_zipcode()
    html = get_html_from_web(user_zip)
    report = get_weather_from_html(html)
    print_weather_report(report)


def banner():
    print('----------------------------------------')
    print('        WEATHER CLINT APP               ')
    print('----------------------------------------')
    print()


def get_zipcode():
    zipcode = input('What is your zipcode (e.g. 78660): ')
    return zipcode


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()


    loc = clean_up_text(loc)
    condition = clean_up_text(condition)
    temp = clean_up_text(temp)
    scale = clean_up_text(scale)

    print(condition, temp, scale, loc)

    report = WeatherReport(cond=condition,temp=temp,scale=scale,loc=loc)
    return report


def clean_up_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text

def print_weather_report(report):
    print('The weather in {} is {} {} and {}'.format(report.loc,report.temp,report.scale,report.cond))


if __name__ == '__main__':
    main()