def print_name(first, last='the Clown'):
    print('Your name is %s %s' % (first, last))
    return

def print_name_age(first, last, age):
    print_name(first, last)
    print('Your age is %d' % (age))
    print('Your age is ' + str(age))
    if age > 35:
        print('You are really old.')
    return
