import time

import openpyxl as openpyxl


class AlgorithmTest:

    def __init__(self, name, path, line):
        self.name = name
        self.report = [name]
        self.start = 0
        self.path = path
        self.line_start = line

    def start_test(self):
        self.start = round(time.time() * 1000)
        return self.start

    def end_test(self):
        diff = round(time.time() * 1000) - self.start
        self.report.append(diff)
        return diff

    def save_result(self):
        wb = openpyxl.load_workbook(self.path)
        sheet = wb.active

        col = 1
        for value in self.report:
            sheet.cell(row=self.line_start, column=col).value = value
            col += 1

        wb.save(self.path)

        print('Тест {} выполнен! Первое время выполнения: {}, последнее: {}.'.format(self.name, self.report[1], self.report[-1]))


