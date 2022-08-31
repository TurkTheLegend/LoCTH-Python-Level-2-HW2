import string


def TelNumberCheck(x):
    if x[0] != "+" :
        raise LookupError("Error Code must start with +")
    elif not ("0" <= x[1] <= "9" and "0" <= x[2] <= "9"):
        raise ValueError("Error Code must be + and followed by 2 digits")
    elif len(x) != 13 :
       raise IndexError("The phone number does not match the length specified") #เวเขียนโจทย์ผิด
    elif type(x) != string :
        raise TypeError("The phone number must be a String")
    if x[:3] == "+66":
        return "Thailand"
    elif x[:3] == "+34" :
        return "Spain"
    else :
        return "OtherCountry"

TelNumber = str(input())
print(TelNumberCheck(TelNumber))