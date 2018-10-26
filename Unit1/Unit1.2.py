"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
import numpy as np
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    print ("\nROWS, COLUMNS, and CELLS:")
    print ("Number of rows in the sheet:") 
    print (sheet.nrows)
    print ("Type of data in cell (row 3, col 2):")
    print(sheet.cell_type(3, 2))
    print("Value in cell (row 3, col 2):") 
    print(sheet.cell_value(3, 2))
    print ("Get a slice of values in column 3, from rows 1-3:")
    print (sheet.col_values(3, start_rowx=1, end_rowx=4))
    print(sheet.cell_type(1, 0))
    exceltime = sheet.cell_value(1, 0)
    print("Time in Excel format:") 
    print(exceltime)
    print("Convert time to a Python datetime tuple, from the Excel float:") 
    print(xlrd.xldate_as_tuple(exceltime, 0))

    min_index = np.argmin(sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows+1))
    max_index = np.argmax(sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows+1))
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(sheet.cell_value(max_index+1, 0),0),
            'maxvalue': np.max(sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows+1)),
            'mintime': xlrd.xldate_as_tuple(sheet.cell_value(min_index+1, 0),0),
            'minvalue': np.min(sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows+1)),
            'avgcoast': np.mean(sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows+1))
    }
    return data


def test():
    data = parse_file(datafile)
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
