import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = 'AIzaSyCEu3RIzQBgWycWCQyn3elsjYPuyV3kA3Y'
    locactionString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (
        locactionString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    # print "response header: %s\n\n" % response['status']
    lat = result['results'][0]['geometry']['location']['lat']
    lng = result['results'][0]['geometry']['location']['lng']
    return (lat, lng)

nyc = getGeocodeLocation("New York, NY")
# nyc['results'][0]['geometry']['location']