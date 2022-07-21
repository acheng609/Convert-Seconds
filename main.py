def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-(hours*3600))//60
    converted_seconds= (seconds-(hours*3600)-(minutes*60))
    return(hours, minutes, converted_seconds) 

hours, minutes, seconds=convert_seconds(5000)
print(hours, minutes, seconds)

