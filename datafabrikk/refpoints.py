import pandas as pd
import string
import random
import mgrs

def pos2dd(lon, lat, row):
    row['position'] = '{:.5f}, {:.5f}'.format(lon, lat)
    row['position_type'] = 'DD_LON, DD_LAT'
    return row

def pos2dms(lon, lat, row):
    m = mgrs.MGRS()

    ew = 'E'
    if lon < 0:
        ew = 'W'

    ns = 'N'
    if lat < 0:
        ns = 'S'

    dms_lon = '{:03d}{:02d}{:02d}{}'.format(*[int(c) for c in m.ddtodms(lon)], ew)
    dms_lat = '{:02d}{:02d}{:02d}{}'.format(*[int(c) for c in m.ddtodms(lat)], ns)

    row['position'] = '{} {}'.format(dms_lat, dms_lon)
    row['position_type'] = 'DMS'
    return row

def pos2mgrs(lon, lat, row):
    m = mgrs.MGRS()
    row['position'] = m.toMGRS(lat, lon)
    row['position_type'] = 'MGRS'
    return row


if __name__ == '__main__':

    data = []

    top=61
    bottom=60
    right=9
    left=8

    outfile = 'data/refpoints.xlsx'

    for a in string.ascii_uppercase:
        for b in string.ascii_uppercase:
            row = {'name': '{}{}'.format(a,b)}

            # Calculate a random position
            lat = bottom + (float(top-bottom) * random.random())
            lon = left + (float(right-left) * random.random())

            # Apply random function
            posfunc = random.choice([pos2mgrs, pos2dd, pos2dms])
            row = posfunc(lon, lat, row)

            data.append(row)

    # Create Excel
    df = pd.DataFrame(data)
    df.to_excel(outfile, sheet_name='refpoints', index=False)
