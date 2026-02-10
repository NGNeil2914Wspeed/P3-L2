def main(num):
    if (num%3 == 0):
        return num**3
    else:
        return False

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")


naaa = getint("Please enter the number")
print (f"The number after being cubed is divisible by three is (If it is the number will return as the number squared otherwise it will be false): {main(naaa)}")