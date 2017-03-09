from pylab import *
f = open('text.txt', 'r')
data = f.read().decode('utf-8', errors = 'ignore')
f.close()

t = {}
p = data[0]
for i in xrange(1, len(data)):
    c = data[i]
    if p in t:
        t[p].append(c)
    else:
        t[p] = [c]
    p = c

c = 'H'
gibberish = c
for i in xrange(5000):
    c = choice(t[c])
    gibberish += c