import json, itertools, os, math

def main() -> dir:
    data = {}

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
                print("\033[2A" + "\033[0J", end="")
                print("\033[92m" + "Subject creation finished" + "\033[0m", end="")
                break
        
            limit = int(limit)
            day = input("Day: ")
            timeStart = input("Time start: ")
            timeEnd = input("Time end: ")
            collisions = input("Collisions: ")

            data[subject]["groups"].append({
                "limit": limit,
                "assigned": 0,
                "day": day,
                "timeStart": timeStart,
                "timeEnd": timeEnd,
                "collisions": [collision.strip() for collision in collisions.split(" ")] if collisions != "" else []
            })

    for subject in data:
        attending = data[subject]["attending"]
        limits = 0
        groupsLimited = 0

        for group in data[subject]["groups"]:
            if group["limit"] != 0:
                groupsLimited += 1
                limits += group["limit"]

        if attending != limits:
            leftover = attending - limits
            totalGroups = len(data[subject]["groups"])
            evenSplit = math.ceil(leftover / (totalGroups - groupsLimited))

            for group in data[subject]["groups"]:
                if group["limit"] == 0:
                    group["limit"] = evenSplit
            
    return data

if __name__ == "__main__":
    data = main()
    outputPath = os.path.join(os.path.dirname(__file__), "..", "data/subjects.json")
    with open(outputPath, "w") as file:
        json.dump(data, file, indent=2)
