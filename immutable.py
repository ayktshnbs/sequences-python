result = True
new_result = result

print(id(result))
print(id(new_result))

result = False
print(id(result))
print(id(new_result))

result ="Correct"
new_result = result
print(id(result))
print(id(new_result))

result += "ish"
print(id(result))
