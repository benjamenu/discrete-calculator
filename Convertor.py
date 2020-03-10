"""
Author: Benjamen Underwood
Date: 05/12/2019
Version: 1
"""
import math

selector = "1"

while selector != "0":
    print("0: Select 0 to exit")
    print("1: Hexadecimal to decimal")
    print("2: Base 10 to Any other Base 1 - 16")
    print("3: Binary to Base 10")
    selector = input("Which conversion would you like? ")

    if selector == "1":

        power = 0
        total = 0

        binary_rep = input("What Hexadecimal number would you like to convert? 0X")
        
        def map_value(value):
            if value == "0":
                return 0
            elif value == "1":
                return 1
            elif value == "2":
                return 2
            elif value == "3":
                return 3
            elif value == "4":
                return 4
            elif value == "5":
                return 5
            elif value == "6":
                return 6
            elif value == "7":
                return 7
            elif value == "8":
                return 8
            elif value == "9":
                return 9
            elif value == "A" or value == "a":
                return 10
            elif value == "B" or value == "b":
                return 11
            elif value == "C" or value == "c":
                return 12
            elif value == "D" or value == "d":
                return 13
            elif value == "E" or value == "e":
                return 14
            elif value == "F" or value == "f":
                return 15
            else:
                return ERROR
            
        position = len(binary_rep) - 1
        while position >= 0:
            if binary_rep[position] != "0":
                multiplier = math.pow(16, power)
                value = map_value(binary_rep[position])
                value *= multiplier
                total += value
                power += 1
                position -= 1
            else:
                power += 1
                position -= 1
                
        print(total)
        print("_____________________________")

    elif selector == "2":

        binaryArr = []
        nextNum = 1
        i = 0
        j = 0
        binary_rep = ""


        def map_value(value):
            if value == 0:
                return 0
            elif value == 1:
                return 1
            elif value == 2:
                return 2
            elif value == 3:
                return 3
            elif value == 4:
                return 4
            elif value == 5:
                return 5
            elif value == 6:
                return 6
            elif value == 7:
                return 7
            elif value == 8:
                return 8
            elif value == 9:
                return 9
            elif value == 10:
                return "A"
            elif value == 11:
                return "B"
            elif value == 12:
                return "C"
            elif value == 13:
                return "D"
            elif value == 14:
                return "E"
            elif value == 15:
                return "F"
            else:
                return ERROR

        base = int(input("What base are you converting to? "))
        num = int(input("What number do you want to convert? "))
        while not nextNum == 0: 
            nextNum = num // base
            remainder = num % base
            binaryArr.append(map_value(remainder))
            i += 1
            
            if nextNum == 0:
                break
            else:
                num = nextNum

        while j != i:
            binary_rep += str(binaryArr[(len(binaryArr) - j - 1)])
            j += 1
            
        print("0x" + binary_rep)
        print("_____________________________")

    elif selector == "3":
        power = 0
        total = 0

        binary_rep = input("What Binary number would you like to convert? ")
        position = len(binary_rep) - 1

        while position >= 0:
            if binary_rep[position] != "0":
                value = math.pow(2, power)
                total += value
                power += 1
                position -= 1
            else:
                power += 1
                position -= 1
            
        print(total)
        print("_____________________________")

    elif selector == "0":
        break
        
    else:
        print("Error Selection not recognized, Please select 1 - 3")
