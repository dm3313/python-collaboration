#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:53:37 2024

@author: devin
"""
# Creates the to do list
to_do_list = list()

# Marks an item as completed
def completed(input_item, to_do_list):
    # Runs list_to_check function
    in_list = list_to_check(input_item, to_do_list)
    # If the item input is currently in the list, mark as completed
    if in_list:
        to_do_list.remove(input_item)
        to_do_list.append(f"{input_item} --> completed")
    # Else, return that the item is not in the list
    else:
        print("This item is not in your to do list!")
        
# Checks if a given item is in the to do list
def list_to_check(input_item, to_do_list):
    # Initialized as false
    in_list = False
    # Iterate over all items in the list
    for item in to_do_list:
        # Compares all items in the list currently to the current input
        if input_item == item:
            # Set in_list to true
            in_list = True
            # Break - this makes sure we exit the for loop the second we find the item
            # If we didn't, in_list would get set back to false if the item we want is not the last item
            break
        # Else, in_list is false - the item is not in the list
        else:
            in_list = False
    return(in_list)

# Deletes a value from the list
def delete(item, to_do_list):
    # Runs list_to_check to prevent errors
    in_list = list_to_check(item, to_do_list)
    # Removes an item if it finds the input item in the list
    if in_list:
        to_do_list.remove(item)
    # Else, returns a programmed error
    else:
        print("The specified item is not in your to do list.")

# Lets the user view the to do list in its current state
def view(to_do_list):
    # If the to do list is empty
    if len(to_do_list) == 0:
        # Remind the user
        print("The to do list is currently empty. Add a value to view!")
    else:
        # Otherwise, iterate over the items in the to do list and print them line by line
        # Using capitalize for nice, consistent formatting
        print("Here is your current to do list:")
        for item in to_do_list:
            print(item.capitalize())

# Adds a value to the list
def add(item, to_do_list):
    # Runs list_to_check function
    in_list = list_to_check(item, to_do_list)
    # If the item is in the list, do not add it
    if in_list:
        print("This item is already in the to do list!")
    # Otherwise, add the item to the to do list
    else: 
        to_do_list.append(item)

def main():
    # User instructions
    instructions = """Welcome! This program allows you to create a do list. Please refer below to the commands:
        Type "add" to add a new item to the to do list
        Type "delete" to delete a new item to the to do list
        Type "view" to view all items in the dictionary
        Type "done" to mark an item as complete"""
    print(instructions)
    print("")
    # Go on forever until physically stopped
    while True:
        # Allow the user to make a choice
        choice = input("Type your preferred action (add, delete, view, done): ").casefold()
        # If a user selects view, they do not need to input a value
        if choice != "view":
            # Ensures that the input is still one of the correct options
            if choice == "add" or choice == "delete" or choice == "done":
                # Allows the user to input a value to add, delete, or complete
                requested_item = input("Please type out a to do list item: ").casefold()
                # Run correct functon based on user input
                if choice == "add":
                    add(requested_item, to_do_list)
                elif choice == "delete":
                    delete(requested_item, to_do_list)
                elif choice == "done":
                    completed(requested_item, to_do_list)
            # If the user does not input one of the correct options, display that
            else:
                print("Not a valid choice!")
        # If choice IS view, run view function without entering this nested loop
        else:
            view(to_do_list)
        print("")
        
main()