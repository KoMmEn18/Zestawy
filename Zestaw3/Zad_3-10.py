def roman_to_int(roman_number):
    roman_dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    integer_number = 0
    i = 0
    for i in range(len(roman_number)):
        if i > 0 and roman_dictionary.get(roman_number[i]) > roman_dictionary.get(roman_number[i-1]):
            integer_number += roman_dictionary.get(roman_number[i]) - 2 * roman_dictionary.get(roman_number[i-1])
        else:
            integer_number += roman_dictionary.get(roman_number[i])
    
    print(integer_number)

if __name__ == "__main__":
    roman_to_int("XVIII") #18
    roman_to_int("IV") #4
    roman_to_int("CDXLIII") #443
    roman_to_int("MMMCMLXXXVII") #3987
    roman_to_int("XXXVIII") #38
    roman_to_int("CD") #400