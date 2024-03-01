from variables import *
status = 1

def echo(splitted):
    global status
    splitted.pop(0)
    argument = splitted
    if argument == []:
        if status == 1:
            print('ECHO is on.')
        else:
            print('ECHO is off.')
    elif [x.lower() for x in argument] == ['off']:
        status = 0
    elif [x.lower() for x in argument] == ['on']:
        status = 1
    elif len(argument)==1 and [argument[0][0],argument[0][-1]] == ['%','%']:
        variable = argument[0][1:-1]
        if variable in globals():
            print(eval(variable))
        else:
            print(*argument)
    else:
        print(*argument)



def run():
    while True:
        line = input('>')
        splitted = line.split()
        command = splitted[0]
        if command == 'echo':
            echo(splitted)
        elif command == 'exit':
            break
        else:
            print(f'{command} is not a built in command')

if __name__ == '__main__':
    run()
