import datetime as dt

def create_dates():
    current_year = dt.datetime.now().date().strftime("%Y") 
    prev_year = str(int(current_year)-1)
    date = dt.datetime.now().date().strftime(r"%m-%d")
    current_date = current_year+"-"+date 
    prev_date = prev_year+"-"+date 

    print(current_date, prev_date)

create_dates()