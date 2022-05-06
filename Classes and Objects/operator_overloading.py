#operator overlaoding bu adding
class Sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return Sample(self.a+other.a,self.b+other.b)
    def __str__(self):
        return "{} and {}".format(self.a,self.b)
sample1=Sample(5,6)
sample2=Sample(12,4)
print(sample1+sample2)


