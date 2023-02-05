def calculate(operation:str, x:float, y:float):
    '''
    Operation - takes the string [add, sub, mul, div]
    x and y - two numbers
    '''

    operations = {'add':lambda x, y: x + y,
                 'sub':lambda x, y: x - y,
                 'mul':lambda x, y: x * y,
                 'div':lambda x, y: x / y} 
    assert operation in operations,  f"{operation} is not in database"

    func = operations[operation]

    return func(x, y)
