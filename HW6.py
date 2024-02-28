LC = True
PreviousSprintsPoints = 0
TotalPoints = 0
totalNumOfSprint = 0
PList = []
TotalEHL = 0
TotalEHH = 0
print("Welcome to the SCRUM DATA ANALYSIS SYSTEM or SDAS for short.")
print("Please decide what you wish to do!")
choice = int(input("Options:\n"
      + "1: Calculate Scrum Team's Velocity\n"
      + "2: Calculate Scrum Team's Effort-Hour Capacity\n"))
print(choice)
match choice:
    case 1:
        print("Calculate Scrum Teams Velocity")
        while LC:
            PreviousSprintsPoints = int(input("Please enter the Scrum Team's Total Points from Previous Scrums, "
                                              "When you are done please enter 0 to quit"))
            if PreviousSprintsPoints == 0:
                LC = False
                SVAverage = TotalPoints/totalNumOfSprint
                print("Your Scrum Team's Average Velocity is: " + str(SVAverage))
            else:
                TotalPoints = TotalPoints + PreviousSprintsPoints
                totalNumOfSprint = totalNumOfSprint + 1

    case 2:
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

                    print("Teams Total Effort Hours Range: " + str(TotalEHL) + "-" + str(TotalEHH))

    case default:
        print("The proper choice wasn't entered, now exiting")
        exit()
