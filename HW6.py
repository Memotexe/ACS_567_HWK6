LC = True
PreviousSprintsPoints = 0
TotalPoints = 0
totalNumOfSprint = 0
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
                
            else:
                TotalPoints = TotalPoints + PreviousSprintsPoints
                totalNumOfSprint = totalNumOfSprint + 1

    case 2:
        print("Calculate Scrum Team's Effort-Hour Capacity")
    case default:
        print("The proper choice wasn't entered, now exiting")
        exit()
