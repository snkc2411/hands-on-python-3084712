RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(f'{message})


def my_function():
    greet = "Hello"
    return greet


print(my_function())
