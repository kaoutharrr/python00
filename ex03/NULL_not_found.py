def NULL_not_found(object: any) -> int:
    
    if object is  None :
        print("Nothing: None <class 'NoneType'>")
    elif (isinstance(object, float) and object != object) :
        print("Cheese: nan <class 'float'>")
    elif object is False:
        print("Fake: False <class 'bool'>")
    elif object == 0:
        print("Zero: 0 <class 'int'>")
    elif object == "":
        print("Empty: <class 'str'>")
    else :
        print("Type not Found")
    return 1
