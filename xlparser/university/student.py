class Student:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.groups = []
        
    def assign(self, subjects: dict, subject: str, groupsOrderList: list[str]) -> str:
        for group in groupsOrderList:
            if group == "N":
                if group != groupsOrderList[0]:
                    return "ASSIGNMENT ERROR"
                return "N"

            if group == "W":
                return "W"

            if self.collides(subjects, subject, group):
                continue

            groupData = subjects[subject]["groups"][int(group) - 1]
            groupLimit = groupData["limit"]
            alreadyAssigned = groupData["assigned"]
            if alreadyAssigned < groupLimit:
                groupData["assigned"] += 1
                self.groups.append(f"{subject}:{group}")
                return group

        return "UNDEFINED"

    def collides(self, subjects: dict, subject: str, group: str) -> bool:
        for group in self.groups:
            groupSubject, groupNumber = group.split(":")
            if f"{subject}:{group}" in subjects[groupSubject]["groups"][int(groupNumber) - 1]["collisions"]:
                return True

        return False
