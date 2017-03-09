def main():
    print('A program to check is it a leap year or not.')
    
    year = eval(input('Please enter any year: '))
         
      
    if year%400==0:
            print('It is a leap year.')
         
       
    elif year%100==0:
            print('It is a not leap year.')
         
      
    elif year%4==0:
            print('It is a leap year.')
         
    else:
            print('It is a not leap year.')
main()
