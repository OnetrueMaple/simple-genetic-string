from util import *
ideal      = "The best surprise is no surprise!" # The string my algorithm aims to create through random brute force
generation = {0: 'a'}       # List of all strings created by my genetic algorithm
max_score  = len(ideal)     # Max expected score from an arbitrary string
highest_score = 0           # ID indicating which entry has the highest score

def score(char_list): # Selection bias is necessary, so I have to measure how "close" a string is to our target string, 'ideal'. There's many ways to check, but I want something simple and easy to follow.
    global ideal      # use the global 'ideal' variable inside this function
    points = 0        # used for keeping track of how many points a string gets. Closer to target string -> higher score

    if(len(char_list) <= len(ideal)):       # If the passed string has less characters than the target string, the total number of correct characters leads to higher scores.
        for i in range(len(char_list)):     # Go through each character in the string and check if it matches the target string
            if(char_list[i] == ideal[i]):   # If the character at an index matches the target string...
                points += 1                 #   add points...
        points = points - (len(ideal) - len(char_list)) # and take away points for missing characters, so the string fills up to the correct length before changing characters around.
    elif(len(ideal) < len(char_list)):      # If the passed string has more characters than the target string, the same process as before applies.
        for i in range(len(ideal)):         # Once again checking every character in our string against the target string...
            if(char_list[i] == ideal[i]):   # If the characters at each index of our string and the target string match...
                points += 1                 #   add points...
        points = points - (len(char_list) - len(ideal)) # and take away points for each extra character more than what the target string has to keep the two strings equal length.

    return points     # Return the final points value as the score for the passed string.

def scoreall(fitness=score): # I don't want to write out the code to score all strings per generation, so I'll write a function to simplify the readability of my code.
    global generation        # Use the global generation variable inside this function.
    global highest_score     # Use the global highest_score variable inside this function.

    best = -99999999                    # I need to locally store the best score found so I know which one the best is inside the generation. This is cheaper than access or duplicating the generation.
    highest_score = 0                   # Reset the global variable 'highest_score'. If I'm running scoreall(), I've probably created a new generation and the old value is wrong anyway.
    for key in generation:              # Go through each string, storing the ID into 'key'...
        score = fitness(generation[key])#   locally store the score for each string...
        if(score >= best):              #   if the current string has a higher score than the current best...
            highest_score = key         #       set the global variable to the corresponding ID and...
            best = score                #       update the local best variable for reference later
    # I don't actually need to return a value for this function, all the necessary data is stored in global variables anyway.

def mutate(num_permutations):       # I need a function to change the state of the string, one character at a time. Smallest unit change eventually creates what you want...
    global generation               # Use the global 'generation' variable inside this function.

    base = generation[highest_score]# Grab the best scoring string from current generation before modifying it.
    max_index = len(base)           # Store the highest index inside the string that I can modify without adding characters on accident.
    generation = {0: base}          # Reset the current generation variable to contain only the best scoring string.
    while(len(generation) < num_permutations):  # While there are less than 'num_permutations' strings inside the generation variable...
        function = random(15)                   # Decide whether to swap a character in the string OR add/remove a character from the string.
        if((function % 2) == 0):        # Change a character in the base case...
            index  = random(max_index)  # Randomly choose a character to change
            newchr = random(83)         # Randomly choose to move character up or down
            newlist = f"{base[:index]}{convert_data(newchr)}{base[(index + 1):]}" # Reform the string with the change.
            generation[len(generation)] = newlist   # and add the new string into the new generation!
        else:           # Add or remove a character from the base case
            remove = random(15)     # Randomly decide whether or add or remove a character.
            if((remove % 2) == 0):  # Remove a character from the base string
                index = random(max_index)                       # Randomly choose which character to remove
                newlist = f"{base[:index]}{base[(index + 1):]}" # Reform the string without the selected character
                generation[len(generation)] = newlist           # and add it into the new generation!
            else:       # Add a new character into the string.
                index = random(max_index)                   # Randomly choose where to add the new character.
                newchr = random(83)                         # Randomly decide which character to add into the selected index.
                newlist = f"{base[:index]}{convert_data(newchr)}{base[(index):]}" # Reform the string around the new character.
                generation[len(generation)] = newlist       # and add it into the new generation!

if __name__ == "__main__":
    # Allow the user to choose a string upon running the program.
    valid = False  # Helps me check whether a candidate 'ideal' string is findable
    while(not valid): # While I do not have a findable string...
        print("What string should the program find?")
        ideal = input()         # Allow the user to choose a string upon running the program.
        valid = True            # Resetting to True up here since it would be easier to logically check for invalid strings by...
        for character in ideal:
            if character not in allchars:
                valid = False   # Flags an invalid string as invalid after finding at least one character missing from the 'allchars' array in 'helperfunctions.py'
                print(f"The character '{character}' isn't allowed! Please don't use this character!") # Let the user know the character is disallowed so they can quickly decide not to use it.

    scoreall()                  # Start by scoring the initial generation. The while loop won't have a 'highest_score' value to compare against otherwise.
    generation_count = 0        # Counting variable so I know how long it took my algorithm to generate the target string.
    while(generation[highest_score] != ideal): # While the target string doesn't exist in our generation...
        generation_count += 1   # Increment counting variable for a new generation...
        mutate(25)              # Create 25 new strings from the highest scoring string currently in generation...
        scoreall()              # Rescore the new generation
        print(f"Closest string: '{generation[highest_score]}' for Generation {generation_count}")
    print(f"Generation \'{generation_count}\': {generation}")
print(f"Found the target string: '{generation[highest_score]}' in {generation_count} Generations!")