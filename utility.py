import datetime

now = datetime.datetime.now()
timestamp_with_dot = str(now)
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")


# input is a datetime object, returns a datetime object
def add_hour(time, n):
    return time + datetime.timedelta(hours=n)


if __name__ == "__main__":
    print(timestamp_with_dot)
    print(timestamp)
    print(current_date)
    print(current_time)
    print(str(add_hour(now, 3.6)))
