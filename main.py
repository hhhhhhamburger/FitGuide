from tdee_calculator import TDEE_cal
from bmi_calculator import bmi_cal
from exercise_calculator import check_exer_burn
from lose_weight import lose_kilo
from food_suggestion import food_sug

print('Thank you for using the KEEP FIT program.')
print('Please notice that this program is designed with the standard of losing 1-2 kilograms per week for safety reasons. Losing weight too fast will cause side effects such as headaches, fatigue, irritability and hair loss.')

while True:
    print('.')
    print('.')
    print('.')
    option = input('Please input the function you want to use.(1.TDEE calculator/2.Bmi calculator/3.Exercise Calculator/4.Daily lose weight/5.Meal Suggestions/6.Exit) ')

    if option == 'TDEE calculator' or option == '1':
        TDEE_cal()
    elif option == 'Bmi calculator' or option == '2':
        bmi_cal()
    elif option == 'Exercise Calculator' or option == '3':
        check_exer_burn()
    elif option == 'Daily lose weight' or option == '4':
        lose_kilo()
    elif option == 'Meal Suggestions' or option == '5':
        food_sug()
    elif option == 'exit' or option == 'Exit' or option == '6':
        print('Now exiting...')
        exit()