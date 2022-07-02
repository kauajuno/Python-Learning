def noarg():
    print('Hello')
    print('This is a functions with no inputs')


def onearg(arg):
    print(f'This one gets one input tho, you have chosen {arg}')


def multarg(arg1, arg2, arg3):
    print(f'This one gets multiple inputs, you gave me {arg1}, {arg2} and {arg3}')


noarg()
onearg('SOLCA')
multarg(1, 2, 3)
multarg(arg3=1, arg1=7, arg2=5)
