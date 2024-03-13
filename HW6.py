# Predefined Variables
# PreviousSprintsPoints = 0
# TotalPoints = 0
# totalNumOfSprint = 0
# PList = []
# TotalEHL = 0
# TotalEHH = 0


def CSTV(PreviousSprintsPoints):
    print("Calculate Scrum Teams Velocity")
    SVAverage = PreviousSprintsPoints / 6
    return SVAverage


def CSTEHC():
    PList = []
    TotalEHL = 0
    TotalEHH = 0
    LC = True
    print("Calculate Scrum Team's Effort-Hour Capacity")
    while LC:
        PName = input("Please enter the Scrum Members Name\n")
        PDaysAvailable = int(input("Please enter the Scrum Members Days Available\n"))
        PDaysBusy = int(input("Please enter the Scrum Members Days Busy with Scrum Activities\n"))
        PHoursPerDayL = int(input("Please enter the Scrum Members Lowest Hours Per Day\n"))
        PHoursPerDayH = int(input("Please enter the Scrum Members Highest Hours Per Day\n"))
        Person = [PName, PDaysAvailable, PDaysBusy, PHoursPerDayL, PHoursPerDayH]
        PList.append(Person)
        print(PList)
        TC = input("Do you wanna to add another team member? 'Y' if Yes, 'N' if No\n")
        match TC:
            case 'Y':
                continue
            case 'N':
                LC = False
                for item in PList:
                    AEHL = (item[1] - item[2]) * item[3]
                    AEHH = (item[1] - item[2]) * item[4]
                    item.append(AEHL)
                    item.append(AEHH)

                for item in PList:
                    TotalEHL = TotalEHL + item[5]
                    TotalEHH = TotalEHH + item[6]

                for item in PList:
                    print("Name: " + item[0] + "\n"
                          + "Days Available: " + str(item[1]) + "\n"
                          + "Days Busy with Scrum Activities: " + str(item[2]) + "\n"
                          + "Lowest Hours Per Day: " + str(item[3]) + "\n"
                          + "Highest Hours Per Day: " + str(item[4]) + "\n")

                RV = "Teams Total Effort Hours Range: " + str(TotalEHL) + "-" + str(TotalEHH)
                return RV


print("Welcome to the SCRUM DATA ANALYSIS SYSTEM or SDAS for short.")
print("Please decide what you wish to do!")
choice = int(input("Options:\n"
                   + "1: Calculate Scrum Team's Velocity\n"
                   + "2: Calculate Scrum Team's Effort-Hour Capacity\n"))
print(choice)
match choice:
    case 1:
        UI = int(input("Please enter the total sprint points for your team over the past 6 weeks :)\n"))
        theCSTVAverage = CSTV(UI)
        print(theCSTVAverage)
    case 2:
        returnValue = CSTEHC()
        print(returnValue)
    case default:
        print("The proper choice wasn't entered, now exiting")
        exit()


# ['Jorge', 10, 2, 4, 7], ['Betty', 8, 2, 5, 6], ['Rajesh', 8, 2, 4, 6], ['Simon', 9, 2, 2, 3], ['Heidi', 10, 2, 5, 6]