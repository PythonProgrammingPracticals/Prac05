
# Exercise 01 - states_name

def main ():

    STATE_NAMES = dict(QLD = "Queensland", NSW = "New South Wales",
                   NT = "Northern Territory", WA = "Western Australia",
                   ACT = "Australian Capital Territory", VIC = "Victoria",
                   TAS = "Tasmania")
# print(STATE_NAMES)

    state = input("Enter short state: ")
    while state != "":
        if state in STATE_NAMES:

            print(state, "is", STATE_NAMES[state])
        else:
            print("Invalid short state")
        state = input("Enter short state: ")
        state = state.upper()

main()