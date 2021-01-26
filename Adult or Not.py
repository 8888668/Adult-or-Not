# 2021/01/25 10:24:07 Daniel Chen
# Solve bugs.

# 2021/01/24 10:59:49 Daniel Chen
# Solve some bug and simplified the part of calculating age.

# 2021/01/23 20:22:25 Daniel Chen
# Adult or Not -- Daniel Chen's first python project.

import time
print('what is your birthday?')

date = ['year', 'month', 'day', 'adult']
# Controlling the while is running or not.

greater_month = [1, 3, 5, 7, 8, 10, 12]
# Preparing detect the enter is a day or not.

while 'adult' in date:
    date.append('play')
    # Start the while which is asking you want to play it again or not.

    while 'year' in date:
        birth_year = input('Year:').strip()

        if birth_year.isdigit() == False:
            print("Please enter a suitable number.")
            # Make sure it is a number.

        elif (int(birth_year) > int(time.strftime('%Y')) or
              int(birth_year) <= int(time.strftime('%Y')) - 100):
            print('Please enter a suitable year.')
            # Make sure it is a year.

        else:
            date.remove('year')
            # Stop the while which is asking you birth year.

    while 'month' in date:
        birth_month = input('month:').strip()

        if birth_month.isdigit() == False:
            print('Please enter a suitable number.')
            # Make sure it is a number.

        elif int(birth_month) not in list(range(1, 13)):
            print('Please enter a suitable month.')
            # Make sure it is a month.

        elif int(birth_year) == int(time.strftime('%Y')):
            if int(birth_month) > int(time.strftime('%m')):
                print('You are not born yet.')
            else:
                date.remove('month')
                # If your birth year are this year, make sure it is real.

        else:
            date.remove('month')
            # stop the while which is asking you birth month.

    while 'day' in date:
        birth_day = input('day:').strip()

        if birth_day.isdigit() == False:
            print('Please enter suitable a number.')
            # Make sure it is a number.

        elif int(birth_day) not in list(range(1, 32)):
            print('Please enter a suitable number.')
            # Make sure it is a day.

        elif int(birth_day) == 31 and int(birth_month) not in greater_month:
            print("There's not 31 in your birth month")
            # Make sure you haven't enter 31 with a common month.

        elif int(birth_month) == 2:
            if int(birth_day) == 30:
                print("there's not 30 in your birth month.")
            elif int(birth_day) == 29:
                if (int(birth_year) % 4) == 0:
                    if (int(birth_year) % 100) == 0:
                        if (int(birth_year) % 400) == 0:
                            date.remove('day')
                        else:
                            print("Threre's not 29 in your birth year.")
                    else:
                        date.remove('day')
                else:
                    print("Threre's not 29 in your birth year.")
            else:
                date.remove('day')
                # Solve some problem with february.

        elif int(birth_month) == int(time.strftime('%m')):
            if int(birth_day) > int(time.strftime('%d')):
                print('You are not bron yet.')
            else:
                date.remove('day')
                # Make sure the day is real.

        else:
            date.remove('day')
            # Stop the while which is asking you the 'day'.

    blurry_age = int(time.strftime('%Y')) - int(birth_year)
    if int(birth_month) > int(time.strftime('%m')):
        age = blurry_age - 1
    elif int(birth_month) < int(time.strftime('%m')):
        age = blurry_age
    else:
        if int(birth_day) > int(time.strftime('%d')):
            age = blurry_age - 1
        elif int(birth_day) == int(time.strftime('%d')):
            print('Quoting the Chinese Constitution,' +
                  'you will be adult tomorrow.')
            age = blurry_age - 1
        else:
            age = blurry_age
            # Calculate the age.

    age = str(age)
    if int(age) >= 18:
        print('You are already adult, your age is ' + age + '.\n')
    else:
        print('You are still underage, your age is ' + age + '.\n')
        # Checking you are adult or not.

    while 'play' in date:
        play = input('Do you want to play it again?\n').strip().lower()
        if play == 'yes' or 'no':
            if play == 'yes':
                date.extend(['year', 'month', 'day'])
                date.remove('play')
            elif play == 'no':
                date.remove('adult')
                date.remove('play')
            else:
                print('\nPlease enter as Yes or No.')
                # Asking you want to play it again or not.
