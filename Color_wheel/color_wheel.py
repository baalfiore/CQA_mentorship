# Recommended imports for all problems
# Some problems may require more
import sys 
import math
import string

if __name__ =="__main__":

    cases = int(sys.stdin.readline().rstrip())

    tests = []

    for caseNum in range(cases):
        caseNum = sys.stdin.readline().rstrip()
        tests.append(caseNum)


    ############################## ACTUAL LOGIC ########################################################

    #4. add in for loop
    for test_string in tests:
        # 1. do first test case for violet
        if test_string == "violet":
            output_string = "In order to make violet, blue and red must be mixed."
        elif test_string == "blue-violet":
            output_string = "In order to make violet, blue and red must be mixed."
        elif test_string == "red-violet":
            output_string = "In order to make violet, blue and red must be mixed."
        # 2. do first test case for orange but we're adding some efficiency
        elif "orange" in test_string:
            output_string = "In order to make orange, red and yellow must be mixed.".replace("orange", test_string)
        # 3. add the last case for green
        elif "green" in test_string:
            output_string = "In order to make REPLACE_ME, blue and yellow must be mixed.".replace("REPLACE_ME", test_string)
        else:
            output_string = "Error! could not find color: " + test_string

        print(output_string)





