def validate(close,open):
    if close == "}" and open == "{":
        return True
    if close == "]" and open == "[":
        return True
    if close == ")" and open == "(":
        return True
    return False
stack = [0,0]
top = 1
ip = input()
balance = 0
open_is_there_flag = 0
answer = ""
balance_counter = 0
val_flag = 0 
for i in ip:
    if i == "*" and stack[-1] == "*"and stack[-2] == "*":
        continue
    if i in ["{","[","("]:
        stack.append(i)
        top += 1
        open_is_there_flag = 1
        continue
    if i == "*" and open_is_there_flag == 1:
        continue
    if i == "*" and open_is_there_flag == 0:
        val_flag = 1
        continue
    if i in ["}","]",")"] and open_is_there_flag == 0:
        answer ="NO"
        continue    
    if i in ["}","]",")"] and open_is_there_flag == 1:
        if stack[top] == "*" and stack[top-1] == "*" and validate(i,stack[top-2]) == True:
            del stack[top]
            del stack[top - 1]
            del stack[top - 2]
            top = top - 3
            balance_counter += 1
            continue
if len(stack) == 2 and val_flag == 0:
    answer = "YES"
else:
    answer = "NO"
print(answer, balance_counter)
