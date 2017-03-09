from pylab import *

f = open('thegiver.txt','r')

tally = {} # not list, class dictionary (dict)

for line in f: #label statement: control flow of execution #simple loop range of variables, so going to move from first variable to last variable
    #print (line) #line is a variable: prints entire txt file
    for c in line:
        if c in tally:
            tally[c]                       # += 1
        else:
            tally[c] = 1
    

f.close()

matplotlib.rcParams.update({'font.size': 30})
xs = rand(100)
ys = rand(100)
plot(xs,ys,'bo')
title('$\log_2 \sin(\pi x)$')
xlabel('$x$')
ylabel('$y$')
#for (i = 0; i <= 100; i ++) {
#   fprintf(i);
#}


#for i in [' john',' jane',' jess']:
#range(1, 101):
 #   print ('Hello'+ str(i) ,'!')

