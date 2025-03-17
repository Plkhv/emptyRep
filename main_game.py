def greetings():
    print('\nWelcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!\nFind the smallest common multiple of given numbers.')
    return name

def outro(name):
    print(f"Congratulations, {name}!")
