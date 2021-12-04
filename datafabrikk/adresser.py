# -*- coding: utf-8 -*-

from koordinatmaskin import RandomCoordinate

def create_adresser(bbox, outfile, n=10):
    
    rc = RandomCoordinate(bbox=bbox)

    data = []

    # Counters
    c = 0
    _c = 0
    
    while c < n:
        
        try:
            data.append(rc.randomAddress())
            c+=1
        except:
            _c+=1
        
        # Raise error in case of multiple errors
        if _c > 2*n:
            raise Exception('Failed to geocode')

    with open(outfile, 'wb') as f:
        f.write('\n'.join(data).encode('utf-8'))


if __name__ == '__main__':

    bbox = dict(
        top=59.940697,
        bottom=59.906802,
        right=10.811577,
        left=10.695190,
    )
    
    outfile = 'data/adresser.txt'

    create_adresser(bbox, outfile, n=10)


