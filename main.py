class Muscle:

    def __init__(self, name, sets=0):
        self.name = name
        self.sets = sets


class Exercise:

    def __init__(self, name, ch=0, bk=0, fd=0, md=0, rd=0, bi=0, tr=0, qa=0, hm=0, gl=0, cv=0):
        self.name = name
        self.chest = ch
        self.back = bk
        self.fdelts = fd
        self.mdelts = md
        self.rdelts = rd
        self.biceps = bi
        self.triceps = tr
        self.quads = qa
        self.hams = hm
        self.glutes = gl
        self.calves = cv


muscleList = []

muscleList.append(Muscle("Chest", 0))
muscleList.append(Muscle("Back", 0))
muscleList.append(Muscle("Front Delts", 0))
muscleList.append(Muscle("Middle Delts", 0))
muscleList.append(Muscle("Rear Delts", 0))
muscleList.append(Muscle("Biceps", 0))
muscleList.append(Muscle("Triceps", 0))
muscleList.append(Muscle("Quads", 0))
muscleList.append(Muscle("Hams", 0))
muscleList.append(Muscle("Glutes", 0))
muscleList.append(Muscle("Calves", 0))

exerciseList = []

exerciseList.append(Exercise("Horizontal Press",1,0,1,0,0,0,1,0,0,0,0))
exerciseList.append(Exercise("Incline Press",1,0,1,1,0,0,1,0,0,0,0))
exerciseList.append(Exercise("Fly",1,0,1,0,0,0,0,0,0,0,0))
exerciseList.append(Exercise("Horizontal Pull",0,1,0,1,1,1,0,0,0,0,0))
exerciseList.append(Exercise("Vertical Pull",0,1,0,0,1,1,0,0,0,0,0))
exerciseList.append(Exercise("Vertical Press",0,0,1,1,0,0,1,0,0,0,0))
exerciseList.append(Exercise("Lateral Raise",0,0,0,1,0,0,0,0,0,0,0))
exerciseList.append(Exercise("Rear Delt Iso",0,0,0,0,1,0,0,0,0,0,0))
exerciseList.append(Exercise("Bicep Iso",0,0,0,0,0,1,0,0,0,0,0))
exerciseList.append(Exercise("Tricep Iso",0,0,0,0,0,0,1,0,0,0,0))
exerciseList.append(Exercise("Squat",0,0,0,0,0,0,0,1,0,1,0))
exerciseList.append(Exercise("Quad Iso",0,0,0,0,0,0,0,1,0,0,0))
exerciseList.append(Exercise("Hip Hinge",0,0,0,0,0,0,0,0,1,1,0))
exerciseList.append(Exercise("Ham Iso",0,0,0,0,0,0,0,0,1,0,0))
exerciseList.append(Exercise("Horizontal Hip Extension",0,0,0,0,0,0,0,0,1,1,0))
exerciseList.append(Exercise("Glute Iso",0,0,0,0,0,0,0,0,0,1,0))
exerciseList.append(Exercise("Pull Over",1,1,0,0,0,0,1,0,0,0,0))
exerciseList.append(Exercise("Calf Iso",0,0,0,0,0,0,0,0,0,0,1))

print("Welcome to Volume Tracker")
print("Inspired by The Muscle and Strength Pyramids")
print("\nCreate a file named program.txt with your workout program")
print("Each line should contain the movement pattern followed by the number of sets")
print("Ex. Horizontal Press 4")
print("\nMovement Patterns:")
print("Squat\nHip Hinge\nVertical Pull\nVertical Push\n"
      "Horizontal Pull\nHorizontal Push\nIncline Push\nHorizontal Hip Extension\n"
      "Pullover\nFly\nBiceps\nTriceps\nSide Delts\nRear Delts\n")


file = open("program.txt", "r")

for line in file:
    the_string = line
    name, sets = the_string.split()

