# sumdiff.py

def sumDiff(x, y):
    sum = x + y
    diff = x - y
    return sum, diff

def main():
    num1, num2 = eval(input("Enter two numbers: "))
    s, d = sumDiff(num1, num2)
    print("The sum is", s, "and the difference is", d)

main()
    
