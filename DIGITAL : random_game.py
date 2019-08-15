import random

rand_num = random.randrange(1, 100)
chance = 8
while (chance >= 1):
    user_prediction = int(input())
    chance -= 1
    if (user_prediction == rand_num):
        print("Yahhh!! You made it. The Number is %d (unused attemps : %d)" % (rand_num, chance))
        break
    elif (user_prediction < rand_num and chance != 0):
        print("Nah!! The number is Greater than %d (%d chance left)" % (user_prediction, chance))
    elif (user_prediction > rand_num and chance != 0):
        print("Nah!! The number is Lesser than %d (%d chance left)" % (user_prediction, chance))
else:
    print("(chance left %d) You Loss!!" %chance)

