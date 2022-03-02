print(1, 2, 3, sep='<')


def great(who='Mendes'):
    print('Hellow,', who) 
    
      
great()
great(who='Tomas')
great('Carine')
print('==========================')


def mult_by_five(x):
    return 5*x


def call(srt, fun, arg):
    return fun(arg)


def squared_call(str, fun, arg):
    
    return fun(fun(arg))


print(
    
    call('Calling the first function: ', mult_by_five, 1),
    squared_call('Calling the second function: ', mult_by_five, 1),
    sep=' \n')
print('===========================')


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'which nunmber is biggest?',
    max(100, 52, 14),
    'which number is biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n'
)

print('==========================')


def ruound_to_two_places(x):
    return round(x, 2)


print(ruound_to_two_places(9.9999))
print('===============================')
"""show the smallest absolute vl"""
x = -10
y = 5
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)