class Add:
    def result(Self,a,b):
        print('Addition', a+b)
        
class Multi(Add):
    def result(Self,a,b):
        print('Multiplication',a*b)
        
m=Add()
m.result(10,30)                