# -*- coding: utf-8 -*-

import random
import string

import pandas as pd

from koordinatmaskin import RandomCoordinate

def create_refpoints(bbox, outfile):

    rc = RandomCoordinate(bbox=bbox)

    data = []

    for a in string.ascii_uppercase:
        for b in string.ascii_uppercase:

            # Create refpoint name
            row = {'name': '{}{}'.format(a,b)}

            # Apply random function
            pos_func, row['position_type'] = random.choice([
                (rc.randomMGRS, 'MGRS'), 
                (rc.randomDD, 'DD_LON, DD_LAT'),
                (rc.randomDMS, 'DMS'),
            ])

            # Apply chosen function
            row['position'] = pos_func()

            data.append(row)

    # Create Excel
    df = pd.DataFrame(data)
    df.to_excel(outfile, sheet_name='refpoints', index=False)

if __name__ == '__main__':

    bbox = dict(
        top=61,
        bottom=60,
        right=9,
        left=8,
    )
    
    outfile = 'data/refpoints.xlsx'

    create_refpoints(bbox, outfile)

    
