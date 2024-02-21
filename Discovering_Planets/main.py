# Recommended imports for all problems
# Some problems may require more
import sys 
import math
import string

if __name__ =="__main__":

    cases = int(sys.stdin.readline().rstrip())

    tests = []

    for case in range(cases):
        case = sys.stdin.readline().rstrip()
        tests.append(case)






    ############################## ACTUAL LOGIC ########################################################

    for test_string in tests:
        x = test_string.split(' ')
        temperature = float(x[0])
        hasWater = x[1]
        hasMagField = x[2]
        eccentricty = float(x[3])

        isHabitable = True

        #print(f"temp: {temperature}, waterLevel: {hasWater}, MagField: {hasMagField}, eccentricity: {eccentricty}")

        # if the planet is above 100 degrees celsius, its too hot
        if temperature > 100.0:
            print("The planet is too hot.")
            isHabitable = False
        elif temperature < 0.0:
            print("The planet is too cold.")
            isHabitable = False
        elif hasWater == "false":
            print("The planet has no water.")
            isHabitable = False
        elif hasMagField == "true":
            print("The planet has no magnetic field.")
            isHabitable = False
        elif eccentricty > .6:
            print("The planet's orbit is not ideal.")
            isHabitable = False

        if isHabitable:
            print("The planet is habitable.")


        # else if the temp is below 0 degrees celsius, the planet is too cold

        #if the planet does not contain water, the planet has no water
        # if no magnetic field, the planet has no magnetic field
        # if the planet has an eccentricity greater than .6, print the planet's orbit is not ideal
        # otherwise the planet is habitable

 




