import argparse
import csv
from collections import defaultdict

parser = argparse.ArgumentParser(description='Process WDI datafile')
parser.add_argument('-c', '--codes', nargs='+', default=[],
    help='The data codes for the variables that should be written to file')
parser.add_argument('-k', '--keywords', nargs='+', default=[],
    help='Keywords used to filter the list of datacodes and their full description')
parser.add_argument('-s', '--show-countries', action='store_true', default=False,
    help='Show the list of country codes and the corresponding full name')
args = parser.parse_args()


countries = {}
datacodes = {}
data = defaultdict(dict)

with open('WDI_Data.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    xvalues = [int(x) for x in reader.next()[4:]]
    
    for line in reader:
        countries[line[1]] = line[0]
        datacodes[line[3]] = line[2]
        data[line[3]][line[1]] = [0 if x == '' else float(x) for x in line[4:]]

if args.show_countries:
    for c in sorted(countries.keys()):
        print c, '\t', countries[c]
    print ''

if args.keywords != []:
    args.keywords = [w.lower() for w in args.keywords]
    for c in sorted(datacodes.keys()):
        desc = datacodes[c].lower()
        for w in args.keywords:
            if w in desc:
                print c, '\t', datacodes[c]
                break
    print ''

for code in args.codes:
    if code in datacodes:
        with open(code+'.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Country'] + xvalues)
            for country in sorted(data[code].keys()):
                writer.writerow([country] + data[code][country])
        print 'Created data file for ', code
        print datacodes[code], '\n'
    else:
        print 'Could not find data for code', code
        print ''

