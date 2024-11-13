def add_everything_up(a, b):
    try:
        if type(a) is float or type(b) is float:
            return round(a + b, 3)
        return a + b
    except TypeError as exc:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(5, 2))
