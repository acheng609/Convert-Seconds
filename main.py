'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-(hours*3600))//60
    converted_seconds= (seconds-(hours*3600)-(minutes*60))
    return(hours, minutes, converted_seconds) 

hours, minutes, seconds=convert_seconds(5000)
print(hours, minutes, seconds)

