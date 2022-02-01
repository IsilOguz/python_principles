def code():
    def validate(a):
        if "def" not in code:
            return ("missing def")
            
        if ":" not in code:
            return ("missing :")
            
        if "('')" not in code:
            return ("missing paren")
    
        if "()" not in code:
            return ("missing param")
        
        if "    " not in code:
            return ("missing indent")
            
        if "validate" not in code:
            return ("wrong name")
            
        if "return" not in code:
            return ("missing return")
    print (validate("test"))        
print(code())
        