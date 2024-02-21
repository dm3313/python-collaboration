#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:53:37 2024

@author: devin
"""

to_do_list = set()

def view(to_do_list):
    if len(to_do_list) == 0:
        print("The to do list is currently empty. Add a value to view!")
    else:
        print("Here is your current to do list:")
        for item in to_do_list:
            print(item)

def add(item, to_do_list):
    if item in to_do_list:
        print("This item is already in the to do list!")
    else: 
        to_do_list.add(item)

def main():
    instructions = """Welcome! This program allows you to create a do list. Please refer below to the commands:
        Type "add" to add a new item to the to do list
        Type "delete" to delete a new item to the to do list
        Type "view" to view all items in the dictionary
        Type "done" to mark an item as complete"""
    print(instructions)
    while True:
        choice = input("Type your preferred action (add, delete, view, done): ").casefold()
        if choice != "view":
            requested_item = input("Please type out a to do list item: ")
            if choice == "add":
                add(requested_item, to_do_list)
        else:
            view(to_do_list)
main()