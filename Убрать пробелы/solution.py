string = "some    string  "
result = ""
space = False
for item in string:
    if item != " ":
        result += item
        space = False
    else:
        if not space:
            space = True
            result += item