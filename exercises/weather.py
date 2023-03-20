import time

temp = int(input("What is the temperature outside?\n"))
weather = input("What is the weather like? Please choose from one of these options (sunny, cloudy, raining, snowing)\n")

weather = weather.lower()

w_dict = {
    1:"sunny",
    2:"cloudy",
    3:"raining",
    4:"snowing"
}

if temp >= 70:
    if weather == w_dict[1] or weather == w_dict[2]:
        print("Wear a light T shirt")
    elif weather == w_dict[3]:
        print("Take an umbrella.")
    else:
        print("Weird weather, are you sure you typed it in right?")

elif temp < 70 and temp >=55:
    if weather == w_dict[1] or weather == w_dict[2]:
        print("You should take a sweatshirt with you.")
    elif weather == w_dict[3]:
        print("You should wear a rain jacket and some boots.")
    else:
        print("Weird weather, are you sure you typed it in right?")

elif temp < 55 and temp >=30:
    if weather == w_dict[1] or weather == w_dict[2]:
        print("Wear a coat, it's cold out.")
    elif weather == w_dict[3] or weather == w_dict[4]:
        print("Wear a waterproof coat and boots.")
    else:
        print("Weird weather, are you sure you typed it in right?")

elif temp < 30:
    if weather == w_dict[1] or weather == w_dict[4]:
        print("Bundle up, it's cold out!")
    else:
        print("Weird weather, are you sure you typed it in right?")

time.sleep(30)