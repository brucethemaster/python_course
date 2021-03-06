# Booleans - logical operations
# result is True; AND means that both operands should be True in order to get the expression evaluated as True
(1 == 1) and (2 == 2)

(1 == 1) or (2 == 2)  # result is True; when using OR, it is enough if only one expression is True, in order to have True as the final result

not(1 == 1)  # result is False; using the NOT operator means denying an expression, in this case denying a True expression

not(1 == 2)  # result is True; using the NOT operator means denying an expression, in this case denying a False expression

# these values always evaluate to False
None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary

bool(None)  # returns False; function that evaluates values and expressions

bool(0)  # returns False; function that evaluates values and expressions

bool(2)  # returns True; function that evaluates values and expressions

bool("router")  # returns True; function that evaluates values and expressions


print(bool("Python 3") and not(23 == 23))

result = 0

x = bool(result) or (7 + 2) == (3 ** 2)

print(x)
