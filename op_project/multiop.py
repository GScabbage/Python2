n1=int(input("Please enter your first number: "))
n2=int(input("Please enter your second number: "))
add= n1+n2
sub= n1-n2
mul= n1*n2
if (n2 == 0):
    print ("Division not possible due to zero division error")
    div = "Infinity"
else:
    div= n1/n2

answers = [add, sub, mul, div]
with open('Results.txt', 'w') as f:
    for answer in answers:
        f.write(str(answer))
        f.write('\n')
