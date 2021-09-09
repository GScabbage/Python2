import calculator

number1=int(input("Please enter first number: "))
number2=int(input("Please enter second number: "))

calculatorObject=calculator.calculatorclass(number1,number2)
sum=calculatorObject.add()
print (sum)
print(f"Total Operations = {calculatorObject.op_count}")
sub=calculatorObject.sub()
print (sub)
print(f"Total Operations = {calculatorObject.op_count}")
mul=calculatorObject.mul()
print (mul)
print(f"Total Operations = {calculatorObject.op_count}")
div=calculatorObject.div()
print (div)
print(f"Total Operations = {calculatorObject.op_count}")
