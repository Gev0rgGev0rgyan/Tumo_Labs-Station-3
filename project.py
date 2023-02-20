import time


def is_time_right_format(time_str):
    if type(time_str) is str and time_str[0].isdigit() and time_str[1].isdigit() \
            and time_str[2] == ":" and (time_str[3].isdigit() and int(time_str[3]) < 7) \
            and time_str[4].isdigit() and time_str[5] == ":" \
            and time_str[6].isdigit() and int(time_str[6]) < 7 and time_str[7].isdigit():
        return True
    return False


def time_converter(time_str):
    h = int(time_str.split(":")[0])
    m = int(time_str.split(":")[1])
    s = int(time_str.split(":")[2])
    seconds = h * 3600 + m * 60 + s
    return seconds


def stop_watch(sec):
    for sec in range(sec, -1, -1):
        m = sec // 60
        s = sec % 60
        h = m // 60
        m = m % 60
        print(h, ":", m, ":", s)
        time.sleep(1)


def main():
    t = input("Enter time like hh:mm:ss ")
    while not is_time_right_format(t):
        t = input("Please enter right time hh:mm:ss ")
    print(t)
    seconds = time_converter(t)
    stop_watch(seconds)


if __name__ == "__main__":
    main()
