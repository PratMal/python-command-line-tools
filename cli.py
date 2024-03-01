from commands import *
prompt = '>'

while True:
    if echo.status == 0:
        prompt = ''
    else:
        prompt = '>'
    line = input(prompt)
    splitted = line.split()
    try:
        command = splitted[0].lower()
    except IndexError:
        continue
    if command == 'echo':
        echo.echo(splitted)
    elif command == 'exit':
        break
    else:
        print(f'{command} is not a built in command ~yet :)~')