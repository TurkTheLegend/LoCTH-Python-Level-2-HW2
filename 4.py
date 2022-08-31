def TelNumberCheck(x):
    assert x[0] == "+" ,'Error Code must start with "+"'
    assert "0" <= x[1] <= "9" and "0" <= x[2] <= "9" ,"Error Code must be + and followed by 2 digits"
    assert len(x) == 13 , "The phone number does not match the length specified" #เวเขียนโจทย์ผิด
    assert type(x) == str ,"The phone number must be a String"
    if x[:3] == "+66":
        return "Thailand"
    elif x[:3] == "+34" :
        return "Spain"
    else :
        return "OtherCountry"

TelNumber = str(input())
print(TelNumberCheck(TelNumber))