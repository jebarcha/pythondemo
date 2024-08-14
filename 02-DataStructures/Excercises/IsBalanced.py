def is_balanced(expression: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to match closing brackets with opening ones
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    # Iterate through each character in the expression
    for char in expression:
        if char in matching_bracket.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_bracket.keys():
            # If it's a closing bracket, check if it matches the last opening bracket
            if stack == [] or matching_bracket[char] != stack.pop():
                return False

    # If the stack is empty, all brackets were matched correctly
    return stack == []


# Example usage:
expression = "{[()()]}"
print(is_balanced(expression))  # Output: True

expression = "{[(])}"
print(is_balanced(expression))  # Output: False
