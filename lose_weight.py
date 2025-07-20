def lose_kilo():
    print('.')
    print('.')
    print('.')
    try:
        TDEE = float(input('Please input your TDEE or press anything but number to exit. '))
        day_abs_cal = float(input('How many calories did you absorb today? '))
        day_burn_cal = float(input('How many calories did you burn through exercise today? '))
    except:
        print('An error occurred')
        print('.')
        print('.')
        print('.')
        return True

    day_cal = day_abs_cal - day_burn_cal

    if TDEE > day_cal:
        abs_goal = TDEE - 500 - day_cal
        print('You still need to absorb '+str(abs_goal)+' calories today.')
    elif TDEE < day_cal:
        burn_goal = day_cal - TDEE + 500
        print('You still need to burn '+str(burn_goal)+' calories today.')
    else:
        print('Congregations! You reach today goal!')
    return lose_kilo() 