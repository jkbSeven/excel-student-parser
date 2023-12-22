import openpyxl as xl

class Formatting:
    def __init__(self, inputFile: str, inplace: bool):
        self.inputFile = inputFile
        if inplace:
            self.outputFile = inputFile
        else:
            self.outputFile = inputFile.split('.')[0] + '_formatted.xlsx'
        self.wb = xl.load_workbook(self.inputFile)
        self.sheet = self.wb.active

    def setSheet(self, sheetName: str) -> None:
        self.sheet = self.wb[sheetName]

    # (row_index, column_index)
    def getCellByIndex(self, cellIndex: tuple[int, int]) -> xl.cell.read_only.ReadOnlyCell:
        return self.sheet[cellIndex[0]][cellIndex[1]]

    @staticmethod
    def clear(cell: xl.cell.read_only.ReadOnlyCell) -> None:
        cell.font = cell.font.DEFAULT_FONT
        cell.border = None
        cell.fill = None
        cell.number_format = None
        cell.protection = None
        cell.alignment = None

    def clearAll(self) -> None:
        for row in self.sheet:
            for cell in row:
                self.clear(cell)

    @staticmethod
    def bold(cell: xl.cell.read_only.ReadOnlyCell) -> None:
        cell.font.b = True

    @staticmethod
    def unbold(cell: xl.cell.read_only.ReadOnlyCell) -> None:
        cell.font.b = False

    @staticmethod
    def titleValue(cell: xl.cell.read_only.ReadOnlyCell) -> None:
        cell.value = cell.value.title()

    def save(self) -> None:
        self.wb.save(self.outputFile)

    def close(self) -> None:
        self.wb.close()

