import datetime

today=datetime.datetime.today()
yesterday=today-datetime.timedelta(1)
tomorrow=today+datetime.timedelta(1)
print(yesterday,today,tomorrow, sep='\n')
