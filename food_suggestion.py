def food_sug():
    Menu = input('Would you like us to provide you with a recipe?(Yes/No)')
    if Menu == 'Yes' or Menu == 'yes':
        BLD = input('Which one do you want to choose? \n 1.Breakfast 2.Lunch 3. Dinner \nPlease enter the number of your choice.')
        if BLD == '1' :
            Breakfast_staple_food = input('What kind of staple food would you like to eat? \n 1.Purple potato 2.Maize 3.Pumpkin 4.Taro 5.None \nPlease enter the number of your choice.')
            if Breakfast_staple_food == '1':
                print('We have prepared 3 different kinds of vegetables and meats to accompany the purple potatoes for you.')
                print('.')
                print('1.Eggs + Chicken Breast + Spinach')
                print('2.Beef + Broccoli + Shiitake Mushrooms')
                print('3.Eggs + Asparagus + Enoki Mushrooms')
            elif Breakfast_staple_food == '2':
                print('We have prepared 3 different kinds of vegetables and meats to accompany the maize for you.')
                print('.')
                print('1.Eggs + Crab stick + Cucumbers + Tomatoes + Lettuces')
                print('2.Eggs + Starch-free Ham + Cherry Tomatoes + Pakchoi')
                print('3.Bacon + Cherry Tomatoes + Enoki Mushrooms')
            elif Breakfast_staple_food == '3':
                print('We have prepared 3 different kinds of vegetables and meats to accompany the pumpkin for you.')
                print('.')
                print('1.Eggs + Tomatoes + Lettuces')
                print('2.Chicken Breast + Cucumbers + Cherry Tomatoes ')
                print('3.Bacon + Eggs + Cherry Tomatoes')
            elif Breakfast_staple_food == '4':
                print('We have prepared 3 different kinds of vegetables and meats to accompany the taro for you.')
                print('.')
                print('1.Chicken Meatballs + Tomatoes + Asparagus')
                print('2.Bacon + Color Peppers + Enoki Mushrooms ')
                print('3.Eggs + Starch-free Ham + Broccoli ')
            elif Breakfast_staple_food == '5':
                print('We have prepared 3 different kinds of vegetables and meats without staple food for you.')
                print('.')
                print('1.Chicken Breast + Broccoli + Shiitake Mushrooms + Cherry Tomatoes')
                print('2.Eggs + Asparagus + Cucumbers + Enoki Mushrooms +Tomatoes ')
                print('3.Eggs + Starch-free Ham + Spinach + Broccoli')
            print('.')
            print('You can choose the one you like best.')
            print('For drinks you can choose unsweetened milk, unsweetened black coffee, unsweetened soy milk or freshly squeezed juice.')
        elif BLD == '2':
            Lunch_staple_food = input('What kind of staple food would you like to eat? \n 1.Rice 2.Spaghetti 3.Coarse cereals \nPlease enter the number of your choice.')
            if Lunch_staple_food == '1':
                print('We have prepared 4 different kinds of vegetables and meats to accompany the rice for you.')
                print('.')
                print('1.A poached egg + Boiled cabbage and shrimp + A kiwi fruit')
                print('2.Stir-fried chicken breast with cucumber and carrot + Half an apple')
                print('3.Stir-fried lean pork with bitter gourd + Half a dragon fruit')
                print('4.Stir-fried Beef with Dutch Beans + 2 pieces of red grapefruit')
            elif Lunch_staple_food == '2':
                print('We have prepared 4 different kinds of vegetables and meats to accompany the spaghetti for you.')
                print('.')
                print('1.One egg + two slices of low fat ham')
                print('2.Half a chicken breast + portobello mushrooms')
                print('3.Tuna + half an avocado')
                print('4.One tomato + half a pepperoni')
            elif Lunch_staple_food == '3':
                print('We have prepared 4 different kinds of vegetables and meats to accompany the coarse cereals for you.')
                print('.')
                print('1.Steamed Chicken Breast with Shiitake Mushrooms + Stir-fried Lettuce + Half a Dragon Fruit')
                print('2.Stir-fried broccoli with chicken breast + A bowl of tofu and lean pork soup')
                print('3.Boiled asparagus +  Stir Fried cauliflower + A poached egg ')
                print('4.Boiled cabbage with tofu + A piece of steamed fish + Half an apple ')
            print('.')
            print('You can choose the one you like best.')
            print('Regarding drinks, we recommend drinking only water!')
        elif BLD == '3':
            print('For dinner we recommend not consuming any staple food, so we suggest 5 different kinds of dinners for you!')
            print('.')
            print('1.Stir-fried broccoli with mushrooms and onions + Steamed pumpkin + Boiled broccoli')
            print('2.Milk nachos + Boiled broccoli + Egg + Fried chicken breast')
            print('3.Pan-fried tofu + Boiled corn + Egg + Hawthorn')
            print('4.Boiled broccoli + Egg + Fried chicken breast + Seaweed Soup')
            print('5.Stir-fried chicken breast with spinach + Egg + Boiled broccoli + An orange')
            print('.')
            print('You can choose the one you like best.')
            print('Regarding drinks, we recommend drinking water or the light soup.')
        print('.')
        print('.')
        print('Warm Tips: If you choose to add a meal when you are hungry, choose low-sugar fruits such as apples and kiwis. You can also choose cucumbers, tomatoes or low-fat milk. Thanks!')
        return food_sug()
        
    elif Menu == 'No' or Menu == 'no':
        print('Thank you for your support. Have a nice day!')
        return True

    else:
        print('Please enter your chose(Yes/No). ')
        return food_sug() 