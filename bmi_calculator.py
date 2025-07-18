from datetime import datetime

def bmi_cal():
    try:
        height = float(input('Input the height (cm) or press anything but number to exit: '))
        print('.')
        weight = float(input('Input the weight (kg): '))
        print('.')
    except:
        print('An error occurred')
        print('.')
        print('.')
        print('.')
        return True

    BMI = weight / (height/100)**2
    print('Your BMI is', round(BMI, 2))
    print('.')
        
    if  BMI < 16: 
        print('You are of severe thinness. You do not need to lose weight.')
        print('.')
        print('You can eat more than three meals a day but remember to keep a balanced diet.')
        print('.')
        print('You can also do some exercise to build up your body.')

    elif 16 <= BMI <17:
        print('You are of moderate thinness. You do not need to lose weight.')
        print('.')
        print('You can eat more than three meals a day but remember to keep a balanced diet.')
        print('.')
        print('You can also do some exercises to strengthen your body.')

    elif 17 <= BMI < 18.5:
        print('You are of mild thinness. You do not need to lose weight.')
        print('.')
        print('Remember to eat regularly and take proper exercise to build up your body.')

    elif 18.5 <= BMI < 25:
        print('You are of normal condition, it is good. ')
        print('.')
        print('Just keep it. It would be better if you exercised more.')

    elif 25<= BMI < 30:
        print('You are of overweight. But do not worry too much. You just need to control your diet and exercise properly.')

    elif 30 <= BMI < 35:
        print('You are of Obese Class I. You need to pay attention to your weight.')
        print('.')
        print('You should take more exercise and control your diet, and seek medical help if necessary.')

    elif 35 <= BMI < 40:
        print('You are of Obese Class II. You need to pay attention to your weight. ')
        print('.')
        print('You should take more exercise and control your diet, and seek medical help if necessary.')

    elif 40 <= BMI < 45: 
        print('You are of Obese Class III. You need to pay attention to your weight. You should exercise regularly and control your diet, and seek medical help if necessary.')
        print('.')
        print('You should exercise regularly and control your diet, and seek medical help if necessary.')
        
    else:
        print('You really need to watch your weight. I suggest you seek medical help.')
        
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if "07:30" <= current_time <= "10:30":
        print('.')
        print('You should eat breakfast.')
    elif "11:00" <= current_time <= "14:00":
        print('.')
        print("You should eat lunch.")
    elif "17:00" <= current_time <= "19:30":
        print('.')
        print("You should eat dinner.")
    elif BMI < 18.5:
        print('.')
        print("You can eat again.")

    return bmi_cal() 