
# coding: utf-8

# In[52]:

import datetime
class TodaysTimeAndDate(object):
    def __init__(self):
        self.currentDT = datetime.datetime.now()
      #  print(self.currentDT)
        
class Year(TodaysTimeAndDate):
    def __init__(self):  
        super(Year,self).__init__()
        self.todaysYear=self.currentDT.strftime("%Y")
     #   print(self.todaysYear)

class Month (TodaysTimeAndDate):
    def __init__(self):  
        super(Month,self).__init__()
        self.todaysMonth=self.currentDT.strftime("%B")
      #  print(self.todaysMonth)
        
class Date (TodaysTimeAndDate):
     def __init__(self):  
        super(Date,self).__init__()
        self.todaysDate=self.currentDT.strftime("%d")
      #  print(self.todaysDate)
        
class Day (TodaysTimeAndDate):
     def __init__(self):  
        super(Day,self).__init__()
        self.todaysDay=self.currentDT.strftime("%A")
      #  print(self.todaysDay)

class Time (TodaysTimeAndDate):
    def __init__(self):  
        super(Time,self).__init__()
        self.todaysTime=self.currentDT.strftime("%I:%M %p")
       # print(self.todaysTime)
    
        
        
class Everything (Year, Month, Date, Day, Time):
    def  __init__(self):
        super(Everything,self).__init__()
        print("Today is {} {} {}, {} and the time is {}".format(self.todaysDay, self.todaysMonth, self.todaysDate, self.todaysYear, self.todaysTime))
        
Today= Everything()
        
        
        
        
        
        


# In[ ]:



