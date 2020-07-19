# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            # Process opening bracket, write your code here
            bracket = Bracket(next_char, i)
            opening_brackets_stack.append(bracket)
        if next_char in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next_char):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
