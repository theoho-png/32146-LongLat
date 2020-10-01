import csv
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = 'https://nominatim.openstreetmap.org/')

def location(city):

    location = geolocator.geocode(str(city) + " Airport")
    return((location.latitude, location.longitude))

#with open('flight.csv', encoding='utf8') as csv_file:
with open('flights.csv', mode='r+', encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('flightCoor.csv', mode='w', newline="") as new_csv_file:
        fieldNames = ["From City", "latitude", "longitude", "To City", "latitude", "longitude"]
        writer = csv.DictWriter(new_csv_file, fieldnames=fieldNames)
        writer.writeheader()
        writer = csv.writer(new_csv_file)

        for i in csv_reader:
        
            fromPlace = i[' From_City ']
            fromLatitude, fromLongitude = location(i[' From_City '])
            print(fromPlace,fromLatitude, fromLongitude)

            toPlace = i[' To_City ']
            toLatitude, toLongitude = location(i[' To_City '])

            row = (fromPlace, fromLatitude, fromLongitude, toPlace, toLatitude, toLongitude,)
            writer.writerow(row)

csv_file.close()
new_csv_file.close()


