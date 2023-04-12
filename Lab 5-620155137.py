#!/bin/python3

import math
import os
import random
import re
import sys

def makeTree(root,trl,trr):
    return ['btree', root,trl,trr]

def make_empty_tree():
    return ['btree']

def is_btree(tree):
    if tree[0] == "btree":
        return True
    else:
        return False
    
def root(tree):
    return tree[1]

def left_subtree(tree):
    return tree[2]

def right_subtree(tree):
    return tree[3]

def is_empty_tree(tree):
    if tree == ['btree']:
        return True
    return False

def is_leaf_tree(tree):
    return is_empty_tree(left_subtree(tree)) and is_empty_tree(right_subtree(tree))

def preorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return [root(tree)]+preorder(left_subtree(tree))+preorder(right_subtree(tree))

def inorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return inorder(left_subtree(tree))+[root(tree)]+inorder(right_subtree(tree))

#
# Include the 'postorder' function (from PROBLEM 1) below.
#

def postorder(tree):
    # Write your code here
    if is_empty_tree(tree):
        return []
    else:
        return postorder(left_subtree(tree)) + postorder(right_subtree(tree)) + [root(tree)]


    
#
# Include the functions for the STACK ADT (from PROBLEM 2) below.
#

def stack():
    # Write your code here
    return ('stack', [])

def contents(stk):
    # Write your code here
    return stk[1] 
    

def top(stk):
    # Write your code here
    return contents(stk)[-1]

def is_stack(obj):
    # Write your code here
    return type(obj) == tuple and obj[0] == 'stack' and type(contents(obj)) == list

def stack_empty(stk):
    # Write your code here
    return contents(stk) == []

def push(stk, el):
    # Write your code here
    contents(stk).append(el)

def pop(stk):
    # Write your code here
    contents(stk).pop()



#
# Complete the 'is_operator' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts an Object.
#
def is_operator(obj):
    # Write your code here
    if obj=="+" or obj=="-" or obj=="*" or obj=="/" :
        return True
    else:
        False
    


def apply_operator(operator, operand2, operand1):#operator #2ndpop element#first popped element
    # Write your code here
    if is_operator(operator):
        if operator=="+":
            return operand2 + operand1
        elif operator=="-":
            return operand2 - operand1
        elif operator=="*":
            return operand2 * operand1
        elif operator=="/":
            return operand2 / operand1
 #returns the rresult of applying the operator

def evalPostfix(tree):
    # Write your code here
    lst= postorder(tree)#applies the postorder function on the given tree and converts the result to a lst
    st1=stack()#creates and stores the stack
    op1=0
    op2=0
    for i in lst: #for each member of the list of operations and operands
        if not is_operator(i):#not an operator
            push(st1,i)#add to stack
        else:
            op1= top(st1)
            pop(st1)
            op2=top(st1)
            pop(st1)
            push(st1,apply_operator(i,op2,op1))#calls the function operator
    return top(st1)#the value which is pushed on the top of the stack which gives the result
