def getStringOfNumbers(listOfNumbers):
    return "".join([str(number) for number in listOfNumbers])

if __name__ == "__main__":
    listOfNumbers = list(range(1, 100, 2))
    print(getStringOfNumbers(listOfNumbers))
    