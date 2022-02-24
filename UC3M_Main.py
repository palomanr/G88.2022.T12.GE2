"""MAIN FUNCTION WHERE WE DEVELOP MOST OF THE ALGORITHMS"""

import string
from UC3M_Care.UC3M_VaccineManager import VACCINEMANAGER

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
ShiftVariable = 3


def enCode(word):
    """FUNCTION TO ENCODE THE GIVEN WORD BY THE USER INSIDE THE SYSTEM"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x_variable = (LETTERS.index(letter) + ShiftVariable) % len(LETTERS)
            encoded = encoded + LETTERS[x_variable]
    return encoded

def deCode(word):
    """FUNCTION USED TO DECODE THE ENCODE WORD FROM THE ENCODE FUNCTION"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x_variable = (LETTERS.index(letter) - ShiftVariable) % len(LETTERS)
            encoded = encoded + LETTERS[x_variable]
    return encoded

def main():
    """INSIDE MAIN FUNCTION WE STORE THE OBJECTS AND PRINT THE CORRESPONDING OUTPUTS TO THE USER"""
    mng = VACCINEMANAGER()
    res = mng.readAccessRequestFromJson("test.json")
    str_res = res.__str__()
    print(str_res)
    encode_res = enCode(str_res)
    print("Encoded Res "+ encode_res)
    decode_res = deCode(encode_res)
    print("Decoded Res: " + decode_res)


if __name__ == "__main__":
    main()
