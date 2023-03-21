from sys import argv as CommandLineArguments
import datetime as CalenderAndClock
import time as Time

if (len(CommandLineArguments) < 2) or (len(CommandLineArguments) > 2):
    print("Error. The Correct Syntax Is <Operation>\n")
    print("You Can Assign The Following Arguments To The <Operation>")
    print("*DateAndTime(Christian Date And System's Time)\n*Data(Christian Date)\n*Time(System's Time)\n*Day(The Day At The Current Week)")

    exit()

Operation = CommandLineArguments[1]

match Operation.lower():
    case "dateandtime":
        print("Christian Date And Now Time Is",
              CalenderAndClock.datetime.now())

        exit()

    case "date":
        print("Christian Date Of To Day Is",
              CalenderAndClock.date.today())

        exit()

    case "time":
        NowTime = Time.localtime(Time.time())
        print(
            f"Now Time Is {NowTime.tm_hour}:{NowTime.tm_min}:{NowTime.tm_sec}")

        exit()

    case "day":
        NowTime = Time.localtime(Time.time())
        NameOfDay = str()

        match NowTime.tm_wday:
            case 0:
                NameOfDay = "Monday"
            case 1:
                NameOfDay = "Tuesday"
            case 2:
                NameOfDay = "Wednesday"
            case 3:
                NameOfDay = "Thursday"
            case 4:
                NameOfDay = "Friday"
            case 5:
                NameOfDay = "Saturday"
            case 5:
                NameOfDay = "Sunday"

        print("This Day's Name At The Current Week Is", NameOfDay)

        exit()

    case _:
        print("Error : Sorry. Your Operation Not Valid")
