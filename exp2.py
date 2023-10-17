def match(string):
    state = 0
    for char in string:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
    return state == 2

# Example usage
print(match("hello world"))  # False
print(match("ab"))  # True
print(match("aab"))  # False
print(match("abab"))  # True
