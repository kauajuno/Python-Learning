def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}

stop = False

while not stop:
    number_1 = int(input('First number\n'))
    for symbol in operations:
        print(symbol)
    operator = input('Which operation should be done?\n')
    number_2 = int(input('Second number\n'))

    operator = operations[operator]
    result = operator(number_1, number_2)
    print(f'The result is {result}')
    if input('Continue calculating? y/n\n') == 'n':
        stop = True
