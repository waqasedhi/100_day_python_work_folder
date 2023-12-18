def greeting(name: str) -> str:
    return 'Hello ' + name


print(b'alice')
# greeting(123)
# greeting(b'Alice')


def greeting1(name: str) -> str:
    return 'Hello ' + name


# greeting(3)         # Argument 1 to "greeting" has incompatible type "int"; expected "str"
# greeting(b'Alice')  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
# greeting("World!")  # No error


def bad_greeting(name: str) -> str:
    return 'Hello ' * name  # Unsupported operand types for * ("str" and "str")


name: str = 700

print(name)
