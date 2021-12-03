from geopy.geocoders import Nominatim
import random

if __name__ == '__main__':

    data = []

    n = 10

    top=59.940697
    bottom=59.906802
    right=10.811577
    left=10.695190

    outfile = 'data/adresser.txt'

    geolocator = Nominatim(user_agent="geocode_task")

    c = 0
    while c < n:
        # Calculate a random position
        lat = bottom + (float(top-bottom) * random.random())
        lon = left + (float(right-left) * random.random())

        location = geolocator.reverse((lat, lon), language='NO', addressdetails=True)

        try:
            data.append('{road} {house_number}, {postcode} {city}, {country}'.format(**location.raw['address']))
            c+=1
        except:
            pass

    with open(outfile, 'wb') as f:
        f.write('\n'.join(data).encode('utf-8'))


