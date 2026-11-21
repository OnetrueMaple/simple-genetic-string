from time import perf_counter, sleep # I need these for random() down below.
# This contains all characters that can show up inside of our strings. Some are missing, but the ones which are missing are honestly pretty annoying to account for.
allchars   = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', ' ', '-', '/', '?', ';', ':', '[', ']', '{', '}', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def collapse(number):                # I want to take an integer and derive a single bit that is representative of the entire number.
    if(not isinstance(number, int)): # If an integer is not passed, throw an error.
        raise ValueError(f"collapse() expects an integer, got \'{type(number)}\'!")

    binary = bin(number)[2:]     # Turn the passed number into a binary number.
    bit = 0                      # The bit I will have returned. Represents the 'sum' of all information inside of 'number'
    for i in range(len(binary)): # For every bit inside number...
        bit ^= int(binary[i])    #    XOR the bits together. Doesn't destroy information, collapses it into a single bit instead.
    return bit                   # Returns the sum of all information!

def conv(num): # Converts a base 2 to base 10
    if(isinstance(num, str)):       # If 'num' is a string, assume it's a binary number and...
        length  = len(num) - 1      # Used to know which power of 2 to add to the next variable.
        decimal = 0                 # Stores the sum of all bits' value.
        for i in range(len(num)):   # For every bit inside 'num'...
            decimal += int(num[i]) * (2 ** length)  # Add the bit's value (0 or 1) multiplied by 2^(place value) to decimal.
            length  -= 1                            # Reduce the place value counter by 1. We start from left to right, so the power of 2 should drop as we move through the string.
        return decimal              # Returns the calculated value.
    else:                           # If 'num' is not a string, return None
        return None

def random(bound):  # Generate a random number between 0 and 'bound'.
    if(bound <= 0): # The below code isn't capable of generating a negative number, so...
        return 0    #    I will bypass that by explicitly making a blanket case skip random number generation entirely if the boundary is negative or 0.
    binbound      = 0   # Highest possible number using the same number of bits as 'bound'
    for i in range(len(bin(bound)[2:])):
        binbound += 2 ** i
    candidate     = ""  # Stores the proposed random number.
    again = True        # Used to reiterate the below loop until a suitable number is found.
    while(again):       # While the candidate number is above the passed 'bound'...
        for i in range(len(bin(binbound)[2:])): # For the number of bits used for 'bound'...
            start      = perf_counter()         # Store the current time stamp...
            sleep(0)                            # OS thing, but this function takes an inconsistent amount of time to complete and run the next line of code.
            candidate += f"{collapse(int((perf_counter() - start) * (10 ** 8)))}" # Take another timestamp, subtract the first, take 8 (or more) bits, collapse it into a single bit, then add that bit to 'candidate'
        if(conv(candidate) < bound): # If the candidate number is below the passed 'bound'...
            again     = False        #    don't reiterate the loop.
        else:                        # Otherwise...
            candidate = ""           #    reset the candidate and generate a new number.
    return conv(candidate)           # Return the "random" number

def convert_data(data): # I want a function that will easily convert between the IDs for each character in allchars and back again.
    if(isinstance(data, int)):          # If the passed value is an int, assume it's an ID and...
        new = allchars[data]            #   pull the char at that index inside allchars to return.
        return new
    elif(isinstance(data, str)):        # If the passed value is a string, assume it's a single character and...
        new = 0                         #   create a counter used to...
        while(allchars[new] != data):   #   iterate through the entirety of allchars until the referenced character matches the passed character.
            new += 1
        return new                      # Return the counter variable since it now matches the correponding ID!