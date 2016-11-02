# File: hw6.py
# Author: Uzoma Uwanamodo
# Date: 10/21/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A simple math helper program
# Collaboration:
# I did not collaborate with anyone on this assignment


# The user's menu options
import sys

MENU_OPTIONS = ["Create a list","Check if list is all same","Check if list is all different","Check if list is sorted","Exit the program"]


    

# createIntList() Create a list of integer from user input
# Input: an integer, the sentinel
# Output: a list, a list of integers created with the users input
def createIntList(SENTINEL):

    # List of integers
    intList = []

    # Prompt user for integers
    promptInt = int(input("Please enter a number, %s to stop: " % SENTINEL))

    # Continue to prompt user for integers until they input SENTINEL value
    while promptInt != SENTINEL:
        intList.append(promptInt)
        promptInt = int(input("Please enter a number, %s to stop: " % SENTINEL))

    # return the created list
    return intList




# getValidInt() takes in a minn and maxx, and gets a number from the
#               user between those two numbers (inclusive)
# Input:      minn and maxx, two integers
# Output:     an integer, between minn and maxx inclusive
def getValidInt(minn, maxx):
    message = "Please enter a number between " + str(minn) + " and " + \
        str(maxx) + " (inclusive): "

    newInt = int(input(message))
    #######################################
    # your code that loops until the user # 
    # enters a valid number goes here     #
    #######################################
    while newInt not in range (minn, maxx+1):
        newInt = int(input(message))

    # while loop exited, return the user's choice
    return newInt




# printMenu() print numbered menu choices for the user
# Input:    None
# Output:   None
def printMenu():
    
    # Print menu request
    print("Please make a choice from the menu: ")
    
    #Print each of the menu options
    for i in range(len(MENU_OPTIONS)):
        print(i+1,"-",MENU_OPTIONS[i])








        
# allTheSame() determine if all the elements in the list are the same
# Input: intList, an integer list
# Output: a boolean indicating whether or not the list is comprised of the same elements
def allTheSame(intList):
    # if the first element is in the rest of the list, return false, otherwise return true
    return [intList[0]]*len(intList) == intList if len(intList) else True




# allTheSame() determine if all the elements in the list are the same
# Input: intList, an integer list
# Output: a boolean indicating whether or not the list is comprised of the same elements
def allDifferent(intList):
    
    # For each integer in the list (except the last one)
    for i in range(len(intList)-1):
        
        # If the current integer appears anywhere else in the list, return False
        if intList[i] in intList[:i] + intList[i+1:]:
            return False
    
    # Otherwise, return True
    return True
    




# sorted() determine whether or not the list is sorted
# Input: intList, an integer list
# Output: sorted, a boolean indicating True if the list is sorted an False if it's not
def sorted(intList):
    for i in range(len(intList)-1):
        if intList[i] > intList[i+1]:
            return False
    return True
    
    
def main():
    
    
    
    # Print the menu choices
    printMenu()
    
    #Define the list the user will be using
    userList = []


    # What action to take based on the chosen option
    CORRESPONDING_ACTION = ["","","allTheSame","allDifferent","sorted"]

    # The part of the text that corresponds to the menu item selected
    CORRESPONDING_TEXT=["","","all the same element", "all unique elements", "sorted","in order"]
    
    # Ask the user for their choice
    menuChoice = getValidInt(1, len(MENU_OPTIONS))
    
    # If they don't ask to exit the program
    while menuChoice != len(MENU_OPTIONS):
        
        # If they select option 1, create a list
        if menuChoice == 1:
            sentinel = int(input("What do you want the sentinel to be? "))
            userList = createIntList(sentinel)
        
        # Otherwise, run the request test on the current list
        # Print out the result of the test
        else:
            print("The list", userList, "is%s %s" % ("" if globals()[CORRESPONDING_ACTION[menuChoice]](userList)  else " not", CORRESPONDING_TEXT[menuChoice if menuChoice != 4 else menuChoice + ~~(not(globals()[CORRESPONDING_ACTION[4]](userList)))]))
        
        # Print line separator
        print("----- ----- ----- ----- ----- -----\n")
        
        # Prompt the user again
        printMenu()
        menuChoice = getValidInt(1, len(MENU_OPTIONS))
    # Thank the user    
    print("Thank you for using the List Info Checker")
main()
    