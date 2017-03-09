import numpy as np
def main():
    a = np.array([[6, 88, 3, 54], [70, 5, -1, 66], [ 1, -9, 4, 2],[5, 0, 5, 99]])
    print(a)
    b=a[1::2,::2]
##    b = a([[1,3,1,3],[0,0,2,3]])
 #   b0 = a[1][0]
  # b2=a[1][2]
   # b3=a[3][2]
    #b=([b0,b2],[b1,b3])
    print(b)
    c = np.transpose(b)
    avg = np.mean(c)
    sd = np.std(c)
    var = np.var(c)
    print(avg,sd,var)
         


main()


