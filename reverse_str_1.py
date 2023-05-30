def txt(_str):
    length = len(_str) -1 
    for i in range(length,-1,-1):
        print(_str[i], end="")
    
    
Text = txt((input("please enter a text : ")))  