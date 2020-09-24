# Starter code

def italic(func):
    def wrapper(instr):
        return func('<i>' + instr + '</i>')
    return wrapper

def bold(func):
    def wrapper(instr):
        return func('<b>' + instr + '</b>')
    return wrapper

@bold
@italic
def message(s):
    return str(s)

print(message('Hello Oracle!'))

