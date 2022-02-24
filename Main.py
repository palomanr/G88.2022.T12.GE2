from UC3M_Care import VACCINE_MANAGER
from UC3M_Care import VACCINEREQUEST
import string

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
shift = 3


def Encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + shift) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def Decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) - shift) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def main():
    mng = VACCINE_MANAGER()
    res = mng.readAccessRequestFromJson("test.json")
    strRes = res.__str__()
    print(strRes)
    EncodeRes = Encode(strRes)
    print("Encoded Res "+ EncodeRes)
    DecodeRes = Decode(EncodeRes)
    print("Decoded Res: " + DecodeRes)


if __name__ == "__main__":
    main()
