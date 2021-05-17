#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program adds positive numbers

def main():
    # this function adds positive numbers
    sum_of_numbers = 0

    # input
    integer_as_string = input("How many numbers are you going to add: ")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number > 0:
            
            for positive_number in range(integer_as_number):
                new_number = int(input("Enter a number: "))
                if new_number < 0:
                    continue
                sum_of_numbers = sum_of_numbers + new_number
                
            print("Sum of the positive numbers is = {0}".
            format(sum_of_numbers))
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
