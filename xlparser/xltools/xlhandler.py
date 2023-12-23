import openpyxl as xl

class XlHandler:
    def __init__(self, inputFile: str, inplace: bool = False):
        self.inputFile = inputFile
        if inplace:
            self.outputFile = inputFile
        else:
            self.outputFile = inputFile.rstrip('.xlsx') + '_out.xlsx'
        self.wb = xl.load_workbook(inputFile)
        self.sheet = self.wb.active

    def setSheet(self, sheetName: str) -> None:
        self.sheet = self.wb[sheetName]

    def getCell(self, rowIndex: int, columnIndex: int) -> xl.cell.cell.Cell:
        return self.sheet.cell(row=rowIndex, column=columnIndex)

    def getFirstFromColumn(self, columnIndex: int) -> tuple[int, str] | None:
        for rowIndex in range(1, self.sheet.max_row + 1):
            if (value:=self.sheet.cell(row=rowIndex, column=columnIndex).value) is not None:
                return rowIndex, value
        return None

    def split(self, columnIndex: int, pattern: str) -> None:
        firstFromColumn = self.getFirstFromColumn(columnIndex)
        if firstFromColumn is None:
            return

        rowIndex, value = firstFromColumn
        newColumns = len(value.strip(pattern).split(pattern))

        if newColumns < 2:
            return

        self.sheet.insert_cols(columnIndex + 1, newColumns)

        for row in self.sheet.iter_rows(min_col=columnIndex, max_col=columnIndex):
            cell = row[0]
            cellSplit = cell.strip(pattern).split(pattern)
            while len(cellSplit) < newColumns:
                cellSplit.append(None)

            for offset in range(1, newColumns + 1):
                self.sheet.cell(row=cell.row, column=(columnIndex + offset)).value = cellSplit[offset - 1]

    def strip(self, cell, pattern: str) -> None:
        cell.value = cell.value.strip(pattern)

    def lstrip(self, cell, pattern: str) -> None:
        cell.value = cell.value.lstrip(pattern)

    def rstrip(self, cell, pattern: str) -> None:
        cell.value = cell.value.rstrip(pattern)

    def save(self):
        self.wb.save(self.outputFile)

    def close(self):
        self.wb.close()
