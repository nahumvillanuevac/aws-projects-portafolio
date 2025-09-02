import random

minimum = 1
attempts = 0
points = 100
difficult = input(("Choose the difficult (Easy(E), Medium(M), Hard(H)): "))
if difficult == "E":
    maximum = 10
elif difficult == "M":
    maximum = 50
elif difficult == "H":
    maximum = 100
elif difficult not in "HEM":
    print("Error, wrong difficult(E,M,D).")
    print("Difficult: default(Easy)")
    maximum = 10

random_num = random.randint(minimum, maximum)
#Loop, repeat when number is wrong, finish when is correct.
#When user fail, attempts increase
while True:
        try:
            user_try = int(input(f"Guess the random number [{minimum}-{maximum}]: "))
            if  user_try > random_num:
                print("Wrong!, your number is too high")
                attempts += 1
            elif user_try < random_num:
                print("Wrong! your number is too low")
                attempts += 1
            else:
                break
        except:
            print("Wrong value!")
total_points = points/attempts
if attempts == 0:
    total_points = 0

print("********************************")
print("|           Correct!           |","\n|           Answer is:", random_num, "      |")
print("|           STATS:             |", "\n|           Attempts:", attempts,"       |")

if difficult not in "HEM":
    print("|           Difficult: E       |")
else:
     print("|           Difficult:",difficult,"      |")
print("           Total points:", total_points)
