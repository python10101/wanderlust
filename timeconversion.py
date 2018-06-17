#Time conversion

sec_per_min=60
sec_per_hour=3600
seconds=eval(input("Enter time in seconds:  "))

hours=seconds/sec_per_hour
seconds=seconds%sec_per_hour

minutes=seconds/sec_per_min
seconds=seconds%sec_per_min

print("The time is: ","%02d:%02d:%02d"%(hours,minutes,seconds))


