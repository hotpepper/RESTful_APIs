from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "LJJM3WQMVU50CL4TFCCFEFFL0KX1TAJNFIKERCX22I21FSK3"
foursquare_client_secret = "XUYML4UJGSFCWZCZOCYWXX2PUKR4AUTUEQZXN2KR3MTSMQDI"


def findARestaurant(mealType, location):
    lat, long = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (
    foursquare_client_id, foursquare_client_secret, lat, long, mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    print result

# 1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

# 2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
# HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

# 3. Grab the first restaurant
# 4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
# 5. Grab the first image
# 6. If no image is available, insert default a image url
# 7. Return a dictionary containing the restaurant name, address, and image url
if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")