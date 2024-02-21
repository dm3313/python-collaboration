#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:53:37 2024

@author: devin
"""

to_do_list = set()

def add(item, to_do_list):
    if item in to_do_list:
        print("This item is already in the dictionary")
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
        requested_item = input("Please type out a to do list item: ")
        choice = input("Type your preferred action (add, delete, view, done): ").casefold()
        if choice == "add":
            add(requested_item, to_do_list)
main()