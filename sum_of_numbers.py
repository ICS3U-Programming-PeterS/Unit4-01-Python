#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 28, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.
import math


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_string = input("Enter a positive integer: ")
    print("")

    try:
        user_num = int(user_number_string)
        if user_num < 0:
            print("\n" + user_num + " is not a positive integer.")
        elif user_num == 0:
            print("0 is not a positive integer.")
        else:
            # calculate the sum of all numbers from 0 to user number
            while loop_counter <= user_num:
                sum = sum + loop_counter
                print("Tracking {} times through loop.".format(loop_counter))
                loop_counter = loop_counter + 1

            print("\nThe sum of the numbers from 0 to {} is: {}.".format(user_num, sum))
    except:
        print(user_number_string + " is not a positive integer.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
