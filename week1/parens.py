# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(next_char)

        if next_char in ")]}":
            if len(opening_brackets_stack) > 0 and are_matching(opening_brackets_stack[-1], next_char):
                opening_brackets_stack.pop()
            else:
                return i + 1
    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
