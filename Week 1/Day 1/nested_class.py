class Army:
    def __init__(self):
        self.name="Rahul"
        self.gn=self.Gun()
    
    def show(self):
        print("Name",self.name) 
        
    class Gun:
        def __init__(self):
            self.name = "AK47"
            self.capacity = "75 Rounds"
            self.length = "34.3 m"
            
        def disp(self):
            print("Gun name", self.name) 
            print("Gun Capacity", self.capacity)
            print("Gun Length", self.length)
                              
                              
a = Army()
print(a.name)
print(a.show())
print(a.gn.name)
a.gn.disp()                              