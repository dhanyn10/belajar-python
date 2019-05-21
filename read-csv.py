import csv
import urllib2

url         = "https://raw.githubusercontent.com/dhanyn10/sample-data/master/ae95c6a6-f607-4ddf-922e-c74d235b182b.csv"
response    = urllib2.urlopen(url)
rcsv        = csv.reader(response)

for row in rcsv:
    print row