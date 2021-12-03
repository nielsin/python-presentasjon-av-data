# -*- coding: utf-8 -*-

import pandas as pd
import random
import datetime
import mgrs
from zipfile import ZipFile

words = {
    'rank_from': [
        'SJT.',
        'MENIG',
        'KORP.',
        'LT.',
        'KAPT.',
        'RITTMESTER',
        'MAJ.',
    ],
    'name_from': list(pd.read_html('https://no.wikipedia.org/wiki/Liste_over_norske_etternavn')[0].Navn),
    'number': [i+1 for i in range(5)],
    'who': [
        'BV206',
        'CV90',
        'Dingo 2'.upper(),
        'IVECO LMV',
        'M113',
        'MB Feltvogn'.upper(),
        'K9 Vidar'.upper(),
        'Leopard 2A4NO'.upper(),
    ],
    'what': [
        'GÅTT I STILLING',
        'TATT EN TEKNISK HVIL',
        'KJØRT SEG FAST',
        'TATT FYR',
        'GÅTT I BIUVAKK',
    ],
    'dir1': [
        'NORD',
        'NORD-ØST',
        'ØST',
        'SØR-ØST',
        'SØR',
        'SØR-VEST',
        'VEST',
        'NORD-VEST',
    ]
}

words['name_to'] = words['name_from']
words['rank_to'] = words['rank_from']
words['dir2'] = words['dir1']

msg = """DTG {dtg_msg}
FRA: {rank_from} {name_from}
TIL: {rank_to} {name_to}

{number} {who} har {what} i posisjon {mgrs} DTG {dtg}.
Ankom fra {dir2}. Front mot {dir1}.

---{name_from}---
"""

def dt2dtg(dt):
    # DTG 271913Anov08
    return dt.strftime('%d%H%MZ%b%y').upper()

def stridsmelding(top=61, bottom=60, right=9, left=8, dt_from=None, dt_length=None):

    # Message data
    msg_data = {}

    if dt_from is None:
        dt_from = datetime.datetime.now(tz=datetime.timezone.utc)

    if dt_length is None:
        dt_length = datetime.timedelta(days=1)

    # Calculate random datetimes for message
    dt_length_seconds = int(dt_length.total_seconds())
    dt_sec = random.randint(0,dt_length_seconds)
    dt_msg_sec = random.randint(dt_sec, dt_length_seconds)

    # Convert to datetime
    msg_data['dtg'] = dt2dtg(dt_from + datetime.timedelta(seconds=dt_sec))
    msg_data['dtg_msg'] = dt2dtg(dt_from + datetime.timedelta(seconds=dt_msg_sec))

    # Chose random data
    for w in words.keys():
        msg_data[w] = random.choice(words[w])

    # Calculate a random position
    lat = bottom + (float(top-bottom) * random.random())
    lon = left + (float(right-left) * random.random())

    # Convert to mgrs
    m = mgrs.MGRS()
    msg_data['mgrs'] = m.toMGRS(lat, lon)

    # Generate message
    gen_msg = msg.format(**msg_data)

    # Create a filename
    fname = '{dtg_msg}_{name_from}.txt'.format(**msg_data).upper()

    return gen_msg, fname

if __name__ == '__main__':

    outfile = 'data/stridsmelding.zip'
    n = 100

    with ZipFile(outfile, 'w') as myzip:
        
        for i in range(n):
            gen_msg, fname = stridsmelding()

            with myzip.open(fname, mode='w') as myfile:
                myfile.write(gen_msg.encode('utf-8'))