def getStringFilledWithZeros(listOfNumbers):
    return "".join([str(number).zfill(3) for number in listOfNumbers])

if __name__ == "__main__":
    listOfNumbers = [1, 2, 5, 6, 8, 12, 21, 43, 78, 120, 320, 405, 547, 987]
    print(getStringFilledWithZeros(listOfNumbers))