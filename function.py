#Simple function
def greet():
    print("Hello Sidra")
    
greet()

#length function
student="sidra"
print(len(student))

#sorted function
num= "87654321"
print(sorted(num))

#Arguments
def greet(lang):
    if lang=="eng":
        print("sidra")
        
    elif lang=="kashmiri":
        print("huh")
    else:
        print("ok")      
greet("eng")




#return
def greet(lang):
    if lang=="eng":
        return("sidra")
        
    elif lang=="kashmiri":
        return("huh")
    else:
        return("ok")      
greet("eng")

#lambda 
square_lambda= lambda n1,n2:n1*n2
print(square_lambda(2,2))

