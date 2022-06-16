
print("\n---WEATHER EVALUATOR---\n")
temp = int(input("What's the temperature? (in celsius):  "))
if temp>25:
    print("\n-- I hope your A/C's working!\n")
if temp<15:
    print("\n-- I hope your heater's working!\n")
else:
    print("\n-- Nice and mild!\n")

raining = input("Is it raining?  ")
is_raining = raining==("Yes" or "yes")

print("\n---RESULTS---\n")

if is_raining and (temp<15):
    print("It's wet and cold")
elif (is_raining==False) and (temp<15):
    print("It's not raining but cold")
elif (is_raining==False) and (temp>=15):
    print("It's warm but not raining")
else:
    print("It's warm and raining")
print("\n---DONE---\n")
