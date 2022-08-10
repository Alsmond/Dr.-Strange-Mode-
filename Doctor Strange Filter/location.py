



import requests


def location ():
    try:
        ipADD=requests.get('https://www.ipify.org/').text
        print(ipADD)
        url='https://www.geojs.io/'+ipADD+'.json'
        geo_request=requests.get(url)
        geo_data=geo_request.json()
        city=geo_data['city']
        country=geo_data['country']
        print(f"sir am not sure,but i think we are in {city} city of {country} country")
    except  Exception as e:
        print("sorry sir,Due to network error i a not able to find where we are.")
        pass