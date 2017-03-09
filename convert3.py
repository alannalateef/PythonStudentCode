# convert3.py
# A program to convert Celsius temps to Fahrenheit.
# This version can be imported without execution

def main():
    celsius = eval(input("What is the Celsius temp?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temp is", fahrenheit, "degrees F.")

if __name__ == '__main__':
    main()

