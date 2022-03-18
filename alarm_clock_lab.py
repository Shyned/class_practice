#Alarm clock



class Alarm_Clock():
    def __init__(self):
        self.alarm_on = False
        self.current_set_time =''
        self.alarm_set_time =""

    #to toggle the alarm on or off.
    def alarm_button(self):
        if self.alarm_on == False:
            push_button = input("Would you like to turn on the alarm clock:(y/n) ")
            if push_button == "y":
                self.alarm_on =True
                print("The alarm is now on.")
                

            else:
                pass
        else:
            pass
    # method to set (or change) the current time and
    # print to the console the current time.
    def current_time (self):
        if self.alarm_on == True:
            self.current_set_time = input("Please enter desired time time set current to (Hr:min): ")
            print(f"Your current time is {self.current_set_time}.")
        else:
            Alarm_Clock.alarm_button(self)

    # to set the current alarm time and print to
    # the console the current alarm time.
    def alarm_time(self):
        if self.alarm_on == True:
            self.alarm_set_time = input("Please enter desired alarm time (Hr:min): ")
            print(f"Your alarm time is {self.alarm_set_time}.")

        
        else:
            Alarm_Clock.alarm_button(self)

    