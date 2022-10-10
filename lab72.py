user_in = []

while True:
    inp = input("> ")
    if inp == "":
        break
    user_in.extend(inp.split(" "))

user_in = set(user_in)
print(" ".join(user_in))