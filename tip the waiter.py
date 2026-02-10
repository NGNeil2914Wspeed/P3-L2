def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

def calculate_percentage(part, whole):
  percentage = (part / whole) * 100
  return percentage

def tip(whole, part):
    tip = calculate_percentage(part, whole)
    print (f"Total: {whole}, Tip: {tip}")

tip(6767, 21)