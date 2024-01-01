x = "global"

def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "local inside inner function"
        print("inner:",x)
    
    def changed_global():
        global x
        x="global : changed!"
        
    print("outer:",x)
    inner()
    print("outer",x)
    changed_global()
    
print(x)

outer()

print(x)            
        
        