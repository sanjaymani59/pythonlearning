# Alaram clock  

import time
import datetime
import  pygame

def set_alarm(alaram_time):
    print(f"Alarm set for {alaram_time}")
    sound_file="PYTHON_PROJECTS/audio.mp3"

    is_running=True

    while is_running :
        current_time= datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if(current_time==alaram_time):
            print("Wake up !!!!!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False

        time.sleep(1)




if __name__ == "__main__":
    timee= input("Enter the time (HH:MM:SS):")

    set_alarm(timee)
    