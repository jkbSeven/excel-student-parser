import json, os
import xlparser as xl
import xlparser.university as uni

class ESP:
    def __init__(self, workbookPath: str):
        self.workbookPath = workbookPath
        self.xlhandler = xl.XlHandler(workbookPath)
        with open(os.path.join(os.path.dirname(self.workbookPath), "subjects.json"), "r") as file:
            self.subjects = json.load(file)
        
    def runDefault(self) -> None:
        self.handleNames()
        self.shortenGroups()
        self.replaceFakeSpaces()
        self.xlhandler.save()

        self.processGroups()    
        with open(os.path.join(os.path.dirname(self.workbookPath), "subjects_out.json"), "w") as file:
            json.dump(self.subjects, file, indent=2)

        self.xlhandler.save()
        self.xlhandler.close()

    def formatDeafult(self) -> None:
        self.formatting = xl.Formatting(self.xlhandler.outputFile)
        self.formatting.clear()
        for header in self.formatting.headers:
            self.formatting.bold(header)
            self.formatting.align(header, "center")
            self.formatting.titleValue(header)

        for nameCells in self.formatting.sheet.iter_rows(min_row=2, max_col=2):
            for cell in nameCells:
                self.formatting.align(cell, "left")
                self.formatting.titleValue(cell)

        for groupCells in self.formatting.sheet.iter_rows(min_row=2, min_col=3):
            for cell in groupCells:
                self.formatting.align(cell, "center")

        self.formatting.save()
        self.formatting.close()

    def handleNames(self) -> None:
        nameCell = self.xlhandler.findValue("Imię i nazwisko", 1)[0]
        nameColumn = nameCell.column

        self.xlhandler.replace(nameCell, "i ", "")
        self.xlhandler.shiftColumns(nameColumn, -(nameColumn - 1))
        self.xlhandler.split(1, " ")

    def shortenGroups(self) -> None:
        for row in self.xlhandler.sheet.iter_rows(min_row=2, min_col=3):
            for cell in row:
                self.xlhandler.replace(cell, "Grupa ", "")
                self.xlhandler.replace(cell, "Nie chodzę", "N")
                self.xlhandler.replace(cell, "Obojętne", "W")

    def replaceFakeSpaces(self) -> None:
        for row in self.xlhandler.sheet.iter_rows():
            for cell in row:
                self.xlhandler.replace(cell, u"\xa0", " ")

    def processGroups(self) -> None:
        headers = [header.value for header in self.xlhandler.headers[2:]]
        for row in self.xlhandler.sheet.iter_rows(min_row=2):
            firstName, lastName = [cell.value for cell in row[:2]]
            studentChoices = zip(headers, [cell.value for cell in row[2:]])
            student = uni.Student(firstName, lastName)

            for index, (subject, groupsOrder) in enumerate(studentChoices, 1):
                groupsOrderList = groupsOrder.split(";")
                currentCell = self.xlhandler.getCell(row[0].row, index + 2)

                assignment = student.assign(self.subjects, subject, groupsOrderList)
                self.xlhandler.setValue(currentCell, assignment)

if __name__ == "__main__":
    esp = ESP("xlparser/data/WORKBOOK_NAME.xlsx")
    esp.runDefault()
    esp.formatDeafult()

