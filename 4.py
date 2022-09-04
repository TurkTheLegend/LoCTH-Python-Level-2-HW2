def TelNumberCheck(x):
    assert x[0] == "+" , 'The phone number must start with "+"'
    assert x[1:] in ["0","1","2","3","4","5","6","7","8","9"] , "The phone number must be digit"
    assert len(x) == 13 , "The phone number does not match the length specified" 
    assert type(x) == str ,"The phone number must be a String"
    if x[:3] == "+66":
        return "Thailand"
    elif x[:3] == "+34" :
        return "Spain"
    else :
        return "OtherCountry"

TelNumber = str(input())
print(TelNumberCheck(TelNumber))