class calculatorclass:
    op_count=0

    def __init__(self,num1,num2):
        self.numm1=num1
        self.numm2=num2

    def add(self):
        return self.numm1+self.numm2
    def sub(self):
        return self.numm1+self.numm2
    def mul(self):
        return self.numm1*self.numm2
    def div(self):
        try:
            return self.numm1/self.numm2
        except ZeroDivisionError:
            return "Infinity"
