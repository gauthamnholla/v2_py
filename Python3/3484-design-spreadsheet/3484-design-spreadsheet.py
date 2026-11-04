class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")
        return self._eval(left) + self._eval(right)

    def _eval(self, token: str) -> int:
        if token[0].isdigit():
            return int(token)            # a plain number like "5"
        return self.cells.get(token, 0)  # a cell like "A1"; unset means 0