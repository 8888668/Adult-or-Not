# 2021/01/28 11:37:42 Daniel Chen
# Solve bugs.

# 2021/01/25 10:24:07 Daniel Chen
# Solve bugs.

# 2021/01/24 10:59:49 Daniel Chen
# Solve some bugs and simplified the part of calculating age.

# 2021/01/23 20:22:25 Daniel Chen
# Adult or Not -- Daniel Chen's first python project.

import time
print('what is your birthday?')

date = ['year', 'month', 'day', 'adult']
# Controls whether the following code works.

while 'adult' in date:
    date.append('play')
    # Prepare for the following code group.

    while 'year' in date:
        birth_year = input('Year:').strip()

        if birth_year.isdigit() == False:
            print("Please enter a number.")
            # Make sure the enter is a number.

        elif (int(birth_year) > int(time.strftime('%Y')) or
              int(birth_year) <= int(time.strftime('%Y')) - 100):
            if int(birth_year) > int(time.strftime('%Y')):
                print('This year is too big, ',end="")
            elif int(birth_year) <= int(time.strftime('%Y')) - 100:
                print('This year is too small, ',end="")
            print('Please enter a suitable year.')

        else:
            date.remove('year')
            # Stop asking about your birth year.

    while 'month' in date:
        birth_month = input('month:').strip()

        if birth_month.isdigit() == False:
            print('Please enter a number.')
            # Make sure the enter is a number.

        elif int(birth_month) not in list(range(1, 13)):
            print('Please enter a suitable month.')
            # Ensure the enter is a month.

        elif int(birth_year) == int(time.strftime('%Y')):
            if int(birth_month) > int(time.strftime('%m')):
                print('You are not born yet.')
                # Make sure the enter in a real month.

            else:
                date.remove('month')
        else:
            date.remove('month')
            # Stop asking about your birth month.

    while 'day' in date:
        birth_day = input('day:').strip()
        greater_month = [1,3,5,7,8,10,12]

        if birth_day.isdigit() == False:
            print('Please enter a suitable number.')
            # Make sure the enter is a number.

        elif int(birth_day) not in list(range(1, 32)):
            print('Please enter a suitable number.')
            # Make sure the enter is a day.

        elif int(birth_day) == 31 and int(birth_month) not in greater_month:
            print("No 31th in your birth month.")
            # Make sure you haven't enter 31 with a common month.

        elif int(birth_month) == 2:
            if int(birth_day) == 30:
                print("No 30th in your birth month.")
            elif int(birth_day) == 29:
                if (int(birth_year) % 4) == 0:
                    if (int(birth_year) % 100) == 0:
                        if (int(birth_year) % 400) == 0:
                            date.remove('day')
                        else:
                            print("No 2.29 in your birth year.")
                    else:
                        date.remove('day')
                else:
                    print("No 2.29 in your birth year.")
            else:
                date.remove('day')
                # Make sure the enter is an real day which is in february.

        elif int(birth_year) == int(time.strftime('%Y')):
            if int(birth_day) > int(time.strftime('%d')) \
            and int(birth_month) == int(time.strftime('%m')):
                print('You are not bron yet.')
            else:
                date.remove('day')
                # Make sure the enter is an real day.

        else:
            date.remove('day')
            # Stop asking about your birthday.

    blurry_age = int(time.strftime('%Y')) - int(birth_year)
    if int(birth_month) > int(time.strftime('%m')):
        age = blurry_age - 1
    elif int(birth_month) < int(time.strftime('%m')):
        age = blurry_age
    else:
        if int(birth_day) > int(time.strftime('%d')):
            age = blurry_age - 1
        elif int(birth_day) < int(time.strftime('%d')):
            age = blurry_age
        else:
            if blurry_age == 18:
                print('According to the Chinese Constitution, '+
                'you will reach adulthood tomorrow.')
                age = blurry_age - 1
            elif blurry_age == 0:
                age = blurry_age
            else:
                age = blurry_age - 1
                # Calculate your age.

    age = str(age)
    if int(age) >= 18:
        print('You are already adult, your age is ', end='')
    else:
        print('You are still underage, your age is ', end='')
    print(age + '.\n')
    # Check if you are an adult.

    time.sleep(1)
    while 'play' in date:
        play = input('Do you want to play it again?\n').strip().lower()
        if play == 'yes':
            date.extend(['year', 'month', 'day'])
            date.remove('play')
            print('\n')
        elif play == 'no':
            date.remove('adult')
            date.remove('play')
        else:
            print('\nPlease enter as Yes or No.')
            # Asking you want to play it again or not.
