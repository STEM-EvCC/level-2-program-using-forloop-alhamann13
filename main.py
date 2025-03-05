# Data Samples, variables re-named for personal aesthetic reasons.
missionNames = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
missionYears = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
missionSuccess = [True, False, True, True, True, True, False]

numberMissions = 0
successfulMissions = 0
missionsPre2000 = 0

numberMissions = len(missionNames)
print(f"Total number of missions: {numberMissions}")

successfulMissions = sum(missionSuccess)
print(f"The total number of successful missions : {successfulMissions}")

successRate = (successfulMissions / numberMissions) * 100
print(f"Success rate: {successRate:.2f}%")

print("Missions launched before 2000: ")
for name, year in zip(missionNames, missionYears):
    if year < 2000:
        print(" - ", name)

#for mission_info in zip(missionNames, missionYears):
 #   print(mission_info, mission_info[0], mission_info[1])

#print()

#for name, year in zip(missionNames, missionYears):
#    print(name, year)

#print()

#for i in range(0, len(missionNames)):
#    print(i, missionNames[i], missionYears[i])
