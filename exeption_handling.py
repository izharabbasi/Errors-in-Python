while True:
    try:
        age = int(input("Enter your age "))
        break
    except ValueError:
        print("invalid value.. Please try again")

if age < 18:
    print("you can not play this game ")
else:
    print("you can play ")
