import json

def calc():
    answers = {'Results':[]}
    with open('Results.json', 'w') as f:
        json.dump(answers, f, indent=4)
    rotate = int(input("How many times do you want to run the calculator: "))
    i=0
    while i < rotate:
        try:
            n1=int(input("Please enter first number: "))
            n2=int(input("Please enter second number: "))
            try:
                add= n1+n2
                sub= n1-n2
                mul= n1*n2
                div= n1/n2
                i=i+1
            except ZeroDivisionError:
                print ("Division not possible due to zero division error")
                add= n1+n2
                sub= n1-n2
                mul= n1*n2
                div = "Infinity"
                i=i+1
            except:
                print ("I don't know what you have done but it not right")
            else:
                print("Iteration number",i,"completed",rotate-i, "iterations left" )
            finally:

                res = {'Result from input' : i, 'Input 1' : n1, 'Input 2' : n2, 'Addition' : add, 'Subtraction' : sub, 'Multiplication' : mul, 'Division' : div}
                with open('Results.json','r+') as file:
                    data=json.load(file)
                    data["Results"].append(res)
                    file.seek(0)
                    json.dump(data,file,indent=4)

        except:
            print ("Uh oh, you entered something that is not a number")
    with open('Results.json', 'r') as file:
        ans=json.load(file)
        print (type(ans))

    for key, value in ans.items():
        print (f"{key}= {value}")
calc()
