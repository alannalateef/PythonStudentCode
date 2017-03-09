def main():
    fname = input("Enter filename: ")
    infile = open(fname,"r")
    data = infile.read()

    a = data.split('\n')
    b = data.split('\n')
    d = ' '.join(b)
    e = d.split(' ')
   # print(e)
    
    c = len(data)

    line = len(a)
    word = len(e)

    print(line)
    print(word)
    print(c)
    
main()
