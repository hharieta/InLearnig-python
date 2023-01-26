def hours2military(hour: str) -> str | None:
    if hour.__contains__("AM"): 
        if hour.split(":")[0] == "12":
            return "00:" + hour.split(":")[1]
        return hour.split("AM")[0]
    elif hour.__contains__("PM"):
        if int(hour.split(":")[0]) < 12:
            return str(12 + int(hour.split(":")[0])) + ":" + hour.split(":")[1]
        else:
            return hour.split("PM")[0]
    else: return hour


def main():
   h = hours2military("2:34")
   print(h)


if __name__ == '__main__':
    main()
