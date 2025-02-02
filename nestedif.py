#Nestedif condition

weather = "sunny"
time_of_day = "night"


if weather =="sunny":
    if time_of_day == "day":
        print("you paly with your toy")
    else:
        print("It's night.Time to sleep")
elif weather =="rainy":
    print("You play with your")
elif weather =="snowy":
    if time_of_day =="night":
        print("You play with your tedy bear toy")
    else:
        print("you play with your snown toy")
else:
    print("You stay inside and read the story book")