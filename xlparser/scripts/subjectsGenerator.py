import json, itertools, os, math

def getData() -> dir:
    data = {}
    try:
        while True:
            subject = input(f"\n{'':-^30}\nEnter a subject name: ")
            if subject == "":
                print("\033[2A" + "\033[0J", end="")
                print("\033[92m" + "Finished generating subjects" + "\033[0m")
                break
            else:
                data[subject] = {"groups": []}
                attending = input("Attending students: ")
                data[subject]["attending"] = int(attending)

            for index in itertools.count(1):
                print(f"\nCreating a group #{index}")
                
                limit = input("Students limit: ")
                if limit == "":
                    print("\033[3A" + "\033[0J", end="")
                    print("\033[92m" + "Subject creation finished" + "\033[0m", end="\n")
                    break
            
                while not isinstance(limit, int):
                    try:
                        limit = int(limit)
                    except ValueError:
                        print("\033[1A" + "\033[0J", end="")
                        limit = input("Limit must be an integer, limit: ")

                collisionsInput = input("Collisions: ")

                if collisionsInput == "":
                    collisions = []

                else:
                    collisions = []
                    collisionsSplit = [collision.strip() for collision in collisionsInput.split(";")]
                    if "," not in collisionsInput:
                        collisions = collisionsSplit
                    else:
                        for collision in collisionsSplit:
                            collidingSubject, collidingGroups = collision.split(":")
                            collidingGroups = collidingGroups.split(",")
                            for collidingGroup in collidingGroups:
                                collisions.append(f"{collidingSubject}:{collidingGroup}")

                data[subject]["groups"].append({
                    "limit": limit,
                    "assigned": 0,
                    "collisions": collisions if collisions != "" else []
                })
    except:
        print("\033[91m" + "An error occurred while generating subjects, please try again" + "\033[0m")
    return data

def verifyLimits(data: dir):
    for subject in data:
        attending = data[subject]["attending"]
        limits = 0
        groupsLimited = 0

        for group in data[subject]["groups"]:
            if group["limit"] != 0:
                groupsLimited += 1
                limits += group["limit"]

        totalGroups = len(data[subject]["groups"])
        leftover = attending - limits

        if leftover < 0 or totalGroups == groupsLimited:
            evenSplit = math.ceil(attending / totalGroups)
            for group in data[subject]["groups"]:
                group["limit"] = evenSplit
        else:
            evenSplit = math.ceil(leftover / (totalGroups - groupsLimited))
            for group in data[subject]["groups"]:
                if group["limit"] == 0:
                    group["limit"] = evenSplit
            
def main():
    data = getData()
    try:
        verifyLimits(data)
    except:
        print("\033[91m" + "An error occurred while verifying limits, please try again" + "\033[0m")

    outputPath = "xlparser/data/subjects.json"
    with open(outputPath, "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    main()
