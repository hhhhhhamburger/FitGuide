def check_exer_burn():
    print('.')
    burn=float(input("(1.run, 2.walk, 3.pull-ups,4.jumping rope,5.sit-ups,6.exit)Please enter the number of the type of exercise you want to calculate: "))
    print('.')
    if burn==1:
        try:
            weight=float(input("Please enter your weight (kg):"))
            time=float(input("How long do you want to do exercise (minutes): "))
        except:
            print('An error occurred')
            print('.')
            print('.')
            print('.')
            return check_exer_burn()
        k=1.036
        burn=weight*time*k
        print("You will burn",burn,"calories")
        return check_exer_burn()

    elif burn==2:
        try:
            walk=int(input("Enter the number of steps taken for the day:"))
        except:
            print('An error occurred')
            print('.')
            print('.')
            print('.')
            return check_exer_burn()
        calories=walk*0.04
        print("You will burn",calories,"calories")
        return check_exer_burn()


    elif burn==3:
        try:
            number=float(input("Please enter the number of pull-ups you do:"))
        except:
            print('An error occurred')
            print('.')
            print('.')
            print('.')
            return check_exer_burn()
        number=number*50.169
        print("You will burn",number,"calories")
        return check_exer_burn()

    elif burn==4:
        try:
            number=float(input("Please enter how many times you jump in a minute:"))
            weight=float(input("Please enter your weight (kg):"))
            time=float(input("How long do you want to do exercise (minutes):"))
        except:
            print('An error occurred')
            print('.')
            print('.')
            print('.')
            return check_exer_burn()
        
        k=0.0
        if 0<number<=100:
            k=8.81
        elif 100<number<=120:
            k=11.8
        elif 120<number<=160:
            k=12.3
        else:
            k=14.3
        
        calories=time*k*weight*3.5*60/200
        print("You will burn",calories,"calories")
        return check_exer_burn()

    elif burn==5:
        try:
            gender=float(input("(man:1,woman:2 )Please enter your gender(1/2): "))
        except:
            print('An error occurred')
            print('.')
            print('.')
            print('.')
            return check_exer_burn()
        if gender==1:
            age=float(input("Please enter your age:"))
            rate=float(input("Please enter your heart rate:"))
            weight=float(input("Please enter your weight (kg):"))
            time=float(input("How long time do you want to do exercise (minutes):"))
            calories=(age*0.2017+weight*0.09036+rate*0.6309)*time/4.184
            print("You will burn",calories,"calories")           
        else:
            age=float(input("Please enter your age:"))
            rate=float(input("Please enter your heart rate:"))
            weight=float(input("Please enter your weight (kg):"))
            time=float(input("How long time do you want to do exercise (minutes):"))
            calories=(age*0.074+weight*0.05741+rate*0.4472)*time/4.184
            print("You will burn",calories,"calories")
        return check_exer_burn()
        
    elif burn==6:
        print('Now exiting...')
        return True 