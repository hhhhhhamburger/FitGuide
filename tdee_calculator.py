from datetime import datetime

def TDEE_cal():
    print('.')
    print('.')
    print('.')
    try:
        gender = input('What\'s your gender?(M/F)? ')
        height = float(input('What\'s your height(cm)? '))
        weight = float(input('What\'s your weight(kg)? '))
        age = int(input('What\'s your age? '))
        day_exercise = int(input('How many days will you exercise per week? '))
    except:
        print('An error occurred')
        print('.')
        print('.')
        print('.')
        return TDEE_cal()

    if gender.lower().startswith("m") or gender.lower().startswith("b"):
        sex = 88.362
    elif gender.lower().startswith("f") or gender.lower().startswith("w"):
        sex = 447.593
    
    if day_exercise == 0:
        activity = 1.2
    elif day_exercise == 1 or day_exercise == 2:
        activity = 1.375
    elif day_exercise == 3 or day_exercise == 4 or day_exercise == 5:
        activity = 1.55
    elif day_exercise == 6 or day_exercise == 7:
        activity = 1.725
    elif day_exercise > 7:
        activity = 1.9

    if gender.lower().startswith("m") or gender.lower().startswith("b"):
        BMR = sex + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower().startswith("f") or gender.lower().startswith("w"):
        BMR = sex + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    TDEE = BMR * activity

    print("Your TDEE(Total daily energy expenditure) is " ,TDEE, ". Please move to the Daily lose weight procedure.")
    return True 