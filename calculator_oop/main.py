import calculator

number1=int(input("Please enter first number: "))
number2=int(input("Please enter second number: "))

calculatorObject=calculator.calculatorclass(number1,number2)
sum=calculatorObject.add()
calculator.calculatorclass.op_count +=1
print (sum)
print (f"TotalOperations = {calculator.calculatorclass.op_count}")
sub=calculatorObject.sub()
calculator.calculatorclass.op_count +=1
print (sub)
print (f"TotalOperations = {calculator.calculatorclass.op_count}")
mul=calculatorObject.mul()
calculator.calculatorclass.op_count +=1
print (mul)
print (f"TotalOperations = {calculator.calculatorclass.op_count}")
div=calculatorObject.div()
calculator.calculatorclass.op_count +=1
print (div)
print (f"TotalOperations = {calculator.calculatorclass.op_count}")
