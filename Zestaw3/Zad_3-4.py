def get_number_and_print_its_third_power():
    while(1):
        userInput = input("Enter number: ")
        if(userInput == "stop"): break
        try:
            userInput = float(userInput)
            print(userInput)
            print(pow(userInput, 3))
        except:
            print("This is not a float number! Try again.")   

if __name__ == "__main__":
    get_number_and_print_its_third_power()