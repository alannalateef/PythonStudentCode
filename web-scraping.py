from pylab import *
import urllib2 as url
# for Python 3: import urllib.request as url

f = url.urlopen('http://www.binghamton.edu/')

c = 0

for line in f:
    if 'binghamton' in line.lower():
        c += 1
        print line

f.close()

print c