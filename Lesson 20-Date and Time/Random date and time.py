import random
import time

def getrandomtime(startDate , enddate):
    print("Printing random date between",startDate , "end", enddate)
    randomgenerator=random.random()
    dateformat="%m/%d/%Y"
    starttime=time.mktime(time.strptime(startDate , dateformat))
    endtime=time.mktime(time.strptime(enddate , dateformat))

    randomtime=starttime + randomgenerator +(endtime - starttime)
    randomdate=time.strftime(dateformat , time.localtime(randomtime))
    return randomdate

print("Random Date=",getrandomtime("1/1/2016" , "12/12/2018"))