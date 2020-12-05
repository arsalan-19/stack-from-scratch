# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 18:07:16 2020

@author: Arsalan Dawalatabad
"""

capacity = 3
stack = []

def push_to_stack(number_to_push):
    stack.append(number_to_push)
    print(f"Number added in Stack: {number_to_push}\nStack: {stack}")

def pop_from_stack():
    if len(stack) == 0:
        print("Empty Stack can\'t POP")
    else:
        print(f"Element POPPED: {stack[-1]}")
        stack.remove(stack[-1])
        print(f"Stack: {stack}")

def peek_stack():
    if len(stack) == 0:
        print("Stack Empty")
    else:
        print(f"PEEKING element: {stack[-1]}\nStack: {stack}")

if __name__ == "__main__":  
    
    print(f"Stack with Capacity: {capacity}")
    
    while True:
        try:
            print("\nEnter your choice-\n1. Push\n2. Pop\n3. Peek\n4. Exit",end="\t")
            choice = input("Choice: ")
            if int(choice) == 1:
                if len(stack) >= capacity:
                    print(f"\nStack overflow can\'t PUSH\n{stack}\n")
                    continue
                else:                    
                    number_to_push = input("Enter the element to PUSH: ")
                    push_to_stack(number_to_push)
                    continue
            elif int(choice) == 2:
                pop_from_stack()
                continue
            elif int(choice) == 3:
                peek_stack()
                continue
            elif int(choice) == 4:
                print("Exiting")
                break
            else:
                print("Invalid Choice")
                continue
        except:
            print("\nInvalid Input")
            continue