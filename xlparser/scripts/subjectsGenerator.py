import json, itertools, os

def main() -> dir:
    data = {"subjects": {}}

    while True:
        subject = input(f"\n{'':-^30}\nEnter a subject: ")
        if subject == "":
            print("\033[2A\033[0J", end="")
            print("\033[92mFinished generating subjects\033[0m")
            break
        else:
            data["subjects"][subject] = {"groups": []}

        for index in itertools.count(1):
            print(f"\nCreating a group #{index}")
            
            limit = input("Students limit: ")
            if limit == "":
                print("\033[2A\033[0J", end="")
                print("\033[92mSubject creation finished\033[0m", end="")
                break
        
            day = input("Day: ")
            timeStart = input("Time start: ")
            timeEnd = input("Time end: ")
            frequency = input("Frequency: ")
            collisions = input("Collisions: ")

            data["subjects"][subject]["groups"].append({
                "limit": int(limit),
                "day": day,
                "timeStart": timeStart,
                "timeEnd": timeEnd,
                "frequency": int(frequency),
                "collisions": list(map(str.strip, collisions.split(" "))) if collisions != "" else []
            })
    return data

if __name__ == "__main__":
    data = main()
    outputPath = os.path.join(os.path.dirname(__file__), "..", "data/subjects2.json")
    with open(outputPath, "w") as file:
        json.dump(data, file, indent=2)
