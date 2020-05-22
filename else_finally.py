try:
    number = int(input("Enter number "))
except ValueError:
    print("you did'nt Enter Integer ")
except:
    print("unknown Error ")
else:
    print(f"You enter {number}")
finally:
    print("its final  !!")
