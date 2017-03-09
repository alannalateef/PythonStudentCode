# create a list of sin(n * pi)
# for n = 1, 2, ..., 100

from pylab import *

#x = []
#for n in range(1, 101):
 #   x.append(sin(n*pi))

x = [sin(n*pi) for n in range(1, 101) if n % 2 == 0]
     
y = ['john', 'jane', 'jack', 'joe', 'james', 'jill', 'jess']
z = [name for name in y if name[1] == 'a']

w = {x:x+x for x in y}

def f(x):
    y = x**2
    z = x + y
    return z

def greet():
    print 'hello!'

def experiment():
    c = 1
    while random() > 1./6.: c += 1
    return c
data = [experiment() for i in xrange(10000)]
hist(data, bins = 100)
    
