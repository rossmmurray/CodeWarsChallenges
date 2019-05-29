def zero(arg=''): return eval(f'0 {arg}')
def one(arg=''): return eval(f'1 {arg}')
def two(arg=''): return eval(f'2 {arg}')
def three(arg=''): return eval(f'3 {arg}')
def four(arg=''): return eval(f'4 {arg}')
def five(arg=''): return eval(f'5 {arg}')
def six(arg=''): return eval(f'6 {arg}')
def seven(arg=''): return eval(f'7 {arg}')
def eight(arg=''): return eval(f'8 {arg}')
def nine(arg=''): return eval(f'9 {arg}')

def plus(val): return f'+ {val}'
def minus(val): return f'- {val}'
def times(val): return f'* {val}'
def divided_by(val): return f'/ {val}'


print(seven(times(five())))