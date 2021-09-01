from datetime import datetime

def get_info():
    print('Hello!')
    name = input('What is your name? - ')
    month = input('What month were you born in? - ').lower()
    return name, month

def display_message(name, month):
    print(f'Hello, {name}!')
    present_time = datetime.now()
    present_month_name = present_time.strftime('%B').lower()
    if month == present_month_name:
        print('Happy Birthday Month!')
    print('Your name has ' + str(len(name)) + ' letters in it.')

name, month = get_info()

display_message(name, month)

#Extra comment for a github test