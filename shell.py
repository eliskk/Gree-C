import src.lexer as l

while True:

    consolein = input("$ ")
    result, error = l.run(consolein)

    if error: print(error.stringify)
    else: print(result)
