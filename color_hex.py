
# Exercise 02 - Color Hex

def main ():

    COLOR_CODES = dict(DeepSkyBlue1="#00bfff", DeepSkyBlue2="#00b2ee", DeepSkyBlue3="#009acd",
                       DeepSkyBlue4="#00688b", DimGray="#696969", DodgerBlue1="#1e90ff",
                       DodgerBlue2="#1c86ee", DodgerBlue3="#1874cd", DodgerBlue4="3104e8b",
                       firebrick="#b22222")

    user_color = input("Enter a color: ")
    while user_color != "":
        if user_color in COLOR_CODES:

            print("{} color code is {}".format(user_color, COLOR_CODES[user_color]))

        else:
            print("Sorry! Invalid Color Code. Please Try Again!")
        user_color = input("Enter a color: ")

main()