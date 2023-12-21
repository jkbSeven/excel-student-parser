import openpyxl as xl

class Formatter:
    def __init__(self, inputFile: str):
        self.inputFile = inputFile
        self.outputFile = inputFile.split('.')[0] + '_formatted.xlsx'
        self.wb = xl.load_workbook(self.outputFile)
        self.sheet = None

    def setSheet(self, sheetName: str) -> None:
        self.sheet = self.wb[sheetName]

    def clearFormattingByCell(self, cell: xl.cell.read_only.ReadOnlyCell) -> None:
        cell.font = None
        cell.border = None
        cell.fill = None
        cell.number_format = None
        cell.protection = None
        cell.alignment = None

    def clearFormattingByCellIndex(self, cellIndex: tuple[int, int]) -> None:
        cell = self.sheet[cellIndex[0]][cellIndex[1]]
        self.clearFormattingByCell(cell)

    def clearAllFormatting(self) -> None:
        for row in self.sheet:
            for cell in row:
                self.clearFormattingByCell(cell)

    def save(self) -> None:
        self.wb.save(self.outputFile)

    def close(self) -> None:
        self.save()
        self.wb.close()
