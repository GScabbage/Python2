class calculatorclass:
    op_count=0
    def add_op(cls):
        cls.op_count += 1

    def __init__(self,num1,num2):
        self.numm1=num1
        self.numm2=num2

    def add(self):
        self.add_op()
        return self.numm1+self.numm2
    def sub(self):
        self.add_op()
        return self.numm1+self.numm2
    def mul(self):
        self.add_op()
        return self.numm1*self.numm2
    def div(self):
        self.add_op()
        try:
            return self.numm1/self.numm2
        except ZeroDivisionError:
            return "Infinity"
