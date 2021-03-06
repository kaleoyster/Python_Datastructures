## Python Program to interchange keys and values
mapNbi= {       '25':'MA',
                '04':'AZ',
                '08':'CO',
                '38':'ND',
                '09':'CT',
                '19':'IA',
                '26':'MI',
                '48':'TX',
                '35':'NM',
                '17':'IL',
                '51':'VA',
                '23':'ME',
                '16':'ID',
                '36':'NY',
                '56':'WY',
                '29':'MO',
                '39':'OH',
                '28':'MS',
                '11':'DC',
                '21':'KY',
                '18':'IN',
                '06':'CA',
                '47':'TN',
                '12':'FL',
                '24':'MD',
                '34':'NJ',
                '46':'SD',
                '13':'GA',
                '55':'WI',
                '30':'MT',
                '54':'WV',
                '15':'HI',
                '32':'NV',
                '37':'NC',
                '10':'DE',
                '33':'NH',
                '44':'RI',
                '50':'VT',
                '42':'PA',
                '05':'AR',
                '20':'KS',
                '45':'SC',
                '22':'LA',
                '40':'OK',
                '72':'PR',
                '41':'OR',
                '27':'MN',
                '53':'WA',
                '01':'AL',
                '31':'NE',
                '02':'AK',
                '49':'UT'
        }

values = []
keys = []
for k,v in mapNbi.items():
    values.append(k)
    keys.append(v)

stateToCode = {k:v for k, v in zip(keys, values)}
print(stateToCode)

