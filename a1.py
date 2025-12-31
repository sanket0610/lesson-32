class ov:
    def __init__(self,var):
        self.var=var

    def __lt__(self,other):
        if(self.var < other.var):
            return "o1 is less than o2"
        else:
            return "o1 is greater than o2"
    def __add__(self,other):
        return self.var + other.var

o1=ov(20)
o2=ov(30)
print("COMPARE:", o1 < o2)
print("ADD:", o1 + o2)