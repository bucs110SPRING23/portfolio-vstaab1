import requests
class Sunset:
    def __init__(self):
        site1 = "https://ipapi.co/"
        word1 = "latitude"
        word2 = "longitude"
        request_1 = site1 + word1
        request_2 = site1 + word2
        latitude = requests.get(request_1)
        longitude = requests.get(request_2)
        lat = str(latitude.json())
        long = str(longitude.json())
        site2 = "https://api.sunrise-sunset.org/json?"
        site2 = site2 + lat + "/" + long
        r = requests.get(site2)
        time = r.json()
        time = time['results']['sunset']
        self.sunset = "Today's sunset at your current location will occur at " + time + " UTC."
    def __getSunset__(self):
        return str(self.sunset)