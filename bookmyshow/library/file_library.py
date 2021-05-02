"""Has functions to read object data and test data"""
import xlrd
# from config import XL_PATH, TEST_SHEET2, LOC_VALS2


class ReadFile:
    """ReadFile class has functions that read object data and test data"""
    @staticmethod
    def read_objects(file_path, sheet_name):
        """read_excel reads object data"""
        book = xlrd.open_workbook(file_path)
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.get_rows()
        next(rows)
        d_data, i = {}, 1
        for _ in rows:
            values = tuple(cell.value for cell in sheet.row(i))
            i += 1
            d_data[values[0]] = values[1:]
        return d_data, list(d_data.keys())

    @staticmethod
    def read_data(data_book, sheet_name, test_case):
        """read_data reads test data"""
        book = xlrd.open_workbook(data_book)
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.get_rows()
        next(rows)
        d_data, i = {}, 1
        for _ in rows:
            values = tuple(cell.value for cell in sheet.row(i))
            i += 1
            d_data[values[0]] = values[1:]
        return d_data[test_case]
