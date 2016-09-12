#   codecademy
#   coding exercise
#   Python course


def shut_down(s):
    """Returns Str variations depending on input"""
    if s == 'yes':
        print'Shutting down'
        f = 'Shutting down'
        exit()
    elif s == 'no':
        print'Shutdown aborted'
        f = 'Shutdown aborted'
    else:
        print'Sorry'
        f = 'Sorry'
    return f
    
    