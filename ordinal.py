""" 
Problem 72: SUFFIX 

"""
import sys


if __name__ =="__main__":
    # read in the first argument when we run the program through the terminal line. Line 10 showcases how this file should be executed in a terminal line and code quest ideally.
    #  python    ordinal.py        input.txt
    #            | ^^ 0th argument  | ^^  1st argument

    # variables for reading in test input
    first_argument = 1
    test_input_file = sys.argv[first_argument]

    with open(test_input_file) as my_input_file:
        num_inputs = my_input_file.readline()  # don't care about the first line
        tests = []
        for num_string in my_input_file.readlines():
            # make sure we remove white spaces or the endswith will not work, Spaces are considered characters!
            num_string = num_string.strip()
            tests.append(num_string)


    #1. parse through the input to grab the one's digit
    #2. check if endswith 1, 2, or 3
    #3. There are specific edge test cases which fail like 11-13 on a case by case basis.
            # These are one off cases so we can just do a simple check for them.
    #4. Anything else, it should pass.


    for test_value in tests:
        if (test_value.endswith("th")):

            if(test_value.endswith("3th")):

                if ( test_value == "13th"):
                    print(test_value)
                else:
                    test_value = test_value.replace("3th","3rd")
                    print(test_value)

            elif(test_value.endswith("2th")):
                
                if ( test_value == "12th"):
                    print(test_value)
                else:
                    test_value = test_value.replace("2th","2nd")
                    print(test_value)

            elif(test_value.endswith("1th")):

                if ( test_value == "11th"):
                    print(test_value)
                else:
                    test_value = test_value.replace("1th","1st")
                    print(test_value)
            else:
                print(test_value)
        else:
            print(test_value)

