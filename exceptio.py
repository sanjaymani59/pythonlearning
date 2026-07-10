try:
    num=int(input("Enter Number :"))
    print(10/num)
except ZeroDivisionError:
    print("cannt divide by zero")
except ValueError:
    print("Invalide error")
finally:
    print("program ends")