# app to generate ascii progresion bars and color them based on the current date
# if % of completed task is smaller than % of the passed year they will be on red. else: on green

from datetime import date


first_day = date(2020,1,1)
today = date.today()
tasks = {
    'python': 32
    }

dots = 0

def calc_progression_year():
    number_days = today - first_day
    percentage_year = int(number_days.days / 365 * 100)
    return percentage_year


def store_tasks():
    number_days = today - first_day
    percentage_year = number_days.days / 365 * 100
    
    print('\n')
    task = 'a'
    percentage = 'a'
    
    task = input('insert a task: ')
    if task in tasks:
        print(task + ' was alredy there with a ' + str(tasks[task]) + '%')
    elif task == '':
        print_tasks()
        return

    
    percentage = int(input('insert the %: '))
    if percentage == '':
        print_tasks()
        return
    elif percentage < percentage_year:
        tasks[task] = -percentage
    elif percentage >= percentage_year:
        tasks[task] = +percentage

    store_tasks()


def print_tasks():
    biggest_word = 0
    #size of the biggest word
    min_dots = 10
    #minimum number of dots to print
    num_dots = 0
    task_number_prefix = 1
    
    for task in tasks:
        if len(task) > biggest_word:
            biggest_word = len(task)



    for task in tasks:
        num_dots = biggest_word - len(task)
        num_dots_year = biggest_word - len('Year')
    print('\n')
    print('0. Year' + str(min_dots * '.') + str(num_dots_year * '.') + str(calc_progression_year()) + '%')




    for task in tasks:
        num_dots = biggest_word - len(task)
        num_dots_year = biggest_word - len('Year')
        print(str(task_number_prefix) + '. ' + (str(task) + str(min_dots * '.') + str(num_dots * '.') + str(tasks[task])) + '%')
        task_number_prefix = task_number_prefix + 1
    print('\n')


store_tasks()


























