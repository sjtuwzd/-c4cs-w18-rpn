#!/usr/bin/env python3

import operator
import getopt, sys

fullCmdArguments = sys.argv

argumentList = fullCmdArguments[1:]

unixOptions = "d"
gnuOptions = ["debug"]

arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)

debug_flag = 0
for currentArgument, currentValue in arguments:
    if currentArgument in ("-d", "--debug"):
        debug_flag = 1

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        if(debug_flag == 1):
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
