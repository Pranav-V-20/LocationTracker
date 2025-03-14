import phonenumbers
from phonenumbers import geocoder
from num import number
import folium

Key = "Use your own API key"

check_number = phonenumbers.parse(number)
number_location  = geocoder.description_for_number(check_number, "en")
print(number_location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(number_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
long = result[0]['geometry']['lng']
print(lat, long)

map_location = folium.Map(location=[lat, long], zoom_start=9)
folium.Marker([lat, long], popup=number_location).add_to(map_location)
map_location.save("Location.html")
