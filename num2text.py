# num2text.py
def main():
    print("This prog converts encoded numbers into texts.")
    inString = input("Enter the encoded message: ")
    message = ""
    for numStr in inString.split():
        # convert the (sub)string to a number
        codeNum = eval(numStr)
        # append character to message
        message = message + chr(codeNum) 
    print("The decoded message is:", message)

main()
