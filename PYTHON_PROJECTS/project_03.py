# count down time
import time

my_time= int(input("Enter the time in seconds: "))

# code for countdown timer


for x in range(my_time,0,-1):
    seconde=x %60
    # print(x)
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02} :{seconde:02}")
    time.sleep(0.5)


print("Times up")

