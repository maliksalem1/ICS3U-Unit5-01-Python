#!/usr/bin/env python3
# Created by: maliksalem1
# Created on: Nov 2022
# This program uses functions


def celsius_to_fahrenheit():
    tc_string = input("Enter a temperature(°C): ")
    try:
        tc = float(tc_string)
        tf = (9 / 5) * tc + 32
        print("{0}°C is equal to {1}°F.".format(tc, tf))
    except:
        print("Invalid Input")


def main():
    # this function calls other functions

    celsius_to_fahrenheit()

    print("\nDone.")


if __name__ == "__main__":
    main()
