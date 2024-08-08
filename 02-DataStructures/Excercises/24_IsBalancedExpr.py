def IsBalanceExpression(expression):
    open_Char = []
    for char in expression:
        if char == "(":
            open_Char.append(char)
        if char == ")":
            if not open_Char:
                return False
            closed = open_Char.pop()
            if closed != "(":
                return False
    if (open_Char):
        return False
    else:
        return True


RESULT = IsBalanceExpression("((1+2))")
print("Balanced" if RESULT else "Not balanced")

RESULT = IsBalanceExpression("((1+2)")
print("Balanced" if RESULT else "Not balanced")
