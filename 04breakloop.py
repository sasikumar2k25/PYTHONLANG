# break loop it exit from the loop 

candies = 10

for i in range(candies):
    print("Give one candy to friend")

    if candies - i == 5:
        print("only 5 candies left stop distribution")
        break