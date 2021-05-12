
#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program will generate a random number between 0 and 9
# and then checks if it matches the right number.


import random


def main():
    # this function generates a random number between 0 and 9
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # input
    print('The randomly generated number is: ', random_number)

    # process & output
    if random_number == 5:
        print("Number generated matches the random number !!")
        print("")
        print("Done.")
    else:
        print("Number generated does not matche the random number,")
        print("Number generated that matches the random number is 5 !!")
        print("")
        print("Done.")


if __name__ == "__main__":
    main()

