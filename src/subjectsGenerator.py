import json, itertools

data = {"subjects": {}}

while True:
    subject = input(f"\n{'':-^30}\nEnter a subject: ")
    if subject == "":
        print("Finished generating subjects")
        break
    else:
        data["subjects"][subject] = {"groups": []}

    for index in itertools.count():
        print(f"\nCreating a group #{index + 1}")
        
        limit = input("Students limit: ")
        if limit == "":
            print("Subject creation finished")
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
            "collisions": list(map(str.strip, collisions.split(","))) if collisions != "" else []
        })

with open("subjects.json", "w") as file:
    json.dump(data, file, indent=2)
