# convert2.py
# A program to convert Celsius temps to Fahrenheit.
# This version issues heat and cold warnings.

def main():
    celsius = eval(input("What is the Celsius temp?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees F.")

    # Print warnings for extreme temps
    if fahrenheit >= 90:
        print("It's really hot out there. Be careful!")
    elif fahrenheit <= 30:
        print("Brrrrr. Be sure to dress warmly!")
    else: 
        print ("I don't know what you should wear")

main()
