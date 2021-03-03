#!/usr/bin/env python3

import requests
import json
import datetime

# Example access to Helsedirektoratet API
# Read more and register at https://utvikler.helsedirektoratet.no/
# Joakim Skjefstad, 3. March 2021

subscription_key = 'put-your-subsription-key-here'

def main():
    print("helsedirektoratet API")
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    https_base = "https://api.helsedirektoratet.no"
    final_url = https_base + "/ProduktCovid19/Covid19statistikk/helseforetak"

    print(final_url)

    response = requests.get(final_url, headers=headers)

    if response.status_code == 200:
        print('HTTP 200 - OK')
    else:
        print('HTTP', response.status_code)
        print('Not able to access API, exiting program. Make sure you enter your subscription_key.')
        exit()

    response_json = response.json()

    for item in response_json:
        print(item['region'], item['id'])
        for registreringer in item['covidRegistreringer']:
            reg_datetime = datetime.datetime.strptime(registreringer['dato'], '%Y-%m-%dT%H:%M:%S') # datetime format is 2020-03-08T00:00:00
            print('-', reg_datetime.strftime('%d-%m-%Y'), registreringer['antInnlagte'])

if __name__ == "__main__":
    main()