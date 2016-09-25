"""
Author: Winston Xing
Date: July 31, 2016
CISC 121
For: Professor Wendy Powley

This program reads a file of tasks given details such as the time and day, and creates a ToDo list 
using linked list implementation. 
It then reads a file of commands that adds and executes additional tasks, where executed tasks are
removed from the ToDo list and added to a DidIt linked list. 
These lists are printed as checkpoints throughout the code and the user is notified of all
errors regarding invalid input.
"""

import urllib.request


"""
This function passes in either the ToDo list or DidIt list as a parameter and
prints the list head.
"""
def printLinkList(head):
    print(head)


"""
This function takes in a read string from the online files as a parameter which
represents a task to add to the ToDo list, and returns a populated node as a dictionary.
"""
def populateNodeWithTask(string):
    node = {} # Empty
    indexOfFirstComma = string.index(',') # Separates the task title and time
    indexOfSecondComma = string.index(',', indexOfFirstComma+1) # Separates the task time and day

    # Provide the keys and values for the node
    node['task'] = string[:indexOfFirstComma]
    node['time'] = int(string[indexOfFirstComma+2:indexOfSecondComma]) # Convert time to an int for comparisons
    node['day'] = string[indexOfSecondComma+2:]
    node['next'] = None
    return node


"""
This function passes in the input from the tasks file and creates and returns the ToDo list.
"""
def createToDo(data):
    toDoList = None
    for string in data:
        toDoList = addTask(toDoList, populateNodeWithTask(string))
    return toDoList


"""
This function passes in a node to add to the ToDo list as a parameter, as well as the list itself.
Nodes are added to the linked list in order of time from the shortest to longest task, using linked list
implementation through pointer references. 
If two tasks require the same amount of time, they are ordered alphabetically by title.
"""
def addTask(toDoList, node):
    print("Adding " + node['task'] + " to the ToDo list.") # Commentary to keep track

    # Handles the initial case for an empty ToDo list
    if toDoList == None:
        return node

    curr, prev = toDoList, toDoList # Initialize the pointer variables

    # Insert node at the front of list and return the node
    if (node['time'] < curr['time']
        or (curr['time'] == node['time'] and node['task'] < curr['task'])):
        node['next'] = curr
        return node

    # Go to where the time of our node is equal to or greater than the current node
    while curr['next'] != None and node['time'] > curr['next']['time']: # None condition is checked first
        prev = curr
        curr = curr['next']

    # Insert at front of time group when times to complete are equal and return the list
    if node['time'] == curr['time'] and node['task'] < curr['task']:
        prev['next'] = node
        node['next'] = curr
        return toDoList

    # Insert somewhere in the middle of time group when times to complete are equal
    # Go to where our task comes after the current task alphabetically
    while curr['next'] != None and node['time'] >= curr['next']['time'] and node['task'] > curr['next']['task']:
        curr = curr['next']

    # Insert the node in the middle of the linked list
    temp = curr['next']
    curr['next'] = node
    node['next'] = temp
    
    return toDoList


"""
This function passes in the ToDo and DidIt linked lists, the task being completed, and the person who completed it.
It then completes the task, removes it from the ToDo list, and adds the same node to the DidIt list as well as the 
person who completed it. 
All exceptions are identified to the user. 
A tuple of the ToDo and DidIt lists is returned.
"""
def executeTask(toDoList, didItList, task, person):
    print("Executing " + task + ".") # Commentary

    curr, deletedNode = toDoList, None

    # Initially checks if the first task in the ToDo list is the task being removed
    if curr['task'] == task:
        deletedNode = toDoList
        toDoList = toDoList['next']
    else:
        while curr['next'] != None:
            if curr['next']['task'] == task:
                deletedNode = curr['next']
                curr['next'] = curr['next']['next'] # Never refers a node to None due to the while loop condition
                break
            curr = curr['next']

    deletedNode['person'] = person # Add person to node
    deletedNode['next'] = didItList # Points same, deleted node to the didItList
    didItList = deletedNode # Point to proper list head

    # If the task being executed was not originally in our ToDo list
    if deletedNode == None:
        print("Invalid task!")

    return (toDoList, didItList)


"""
The main function reads the input files and initializes the ToDo and DidIt lists. It also acts as the driver to run the
inputted commands and handles errors.
"""
def main():
    # Read tasks file and initialize ToDo list
    toDoResponse = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/todo.txt")
    toDoHtml = toDoResponse.read()
    toDoData = toDoHtml.decode('utf-8').splitlines()
    toDoList = createToDo(toDoData)

    # Read commands file and initialize DidIt list to None
    executeResponse = urllib.request.urlopen('http://research.cs.queensu.ca/home/cords2/driver.txt')
    executeHtml = executeResponse.read()
    executeData = executeHtml.decode('utf-8').splitlines()
    didItList = None

    # Series of driver options with commentary
    for command in executeData:
        if command == 'PrintToDo':
            print("The ToDo list: ")
            printLinkList(toDoList)
        elif command == 'PrintDidIt':
            print("The DidIt list: ")
            printLinkList(didItList)
        elif command[:7] == 'AddTask': # Uses indexes known by the length of the string AddTask
            toDoList = addTask(toDoList, populateNodeWithTask(command[9:]))
        elif command[:11] == 'ExecuteTask': # Uses indexes known by the length of the string ExecuteTask
            # Separates the task and person parameters from the read file string
            indexOfComma = command.index(',', 13)
            task = command[13:indexOfComma]
            person = command[indexOfComma+2:]
            
            tup = executeTask(toDoList, didItList, task, person) # Returns a tuple including the ToDo and DidIt lists
            toDoList = tup[0]
            didItList = tup[1]
        else:
            print("Invalid command!")
     

main() 
