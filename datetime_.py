from datetime import datetime,  date, timedelta, time



dt_now = date.today()
print(f"Сегодня {dt_now}")


delta_d = timedelta(days=1)
delta_m = timedelta(days=30)


dt_yest=dt_now - delta_d
print(f"Вчера {dt_yest}")

dt_month = dt_now-delta_m
print(f"Месяц назад {dt_month}")

mystr = "01/01/17 12:10:03.234567" 
mystr_new = datetime.strptime(mystr, "%d/%m/%y %H:%M:%S.%f")
print(mystr_new)


