import xlrd

def extract(filename):
    wb = xlrd.open_workbook(filename)

    dic = {'by_pos':{}}

    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    
    for i in range(1,sheet.ncols):
        col = sheet.col_values(i)
        if col[8] is not '':
            dic['by_pos'][int(col[7])] = col[8]
            dic[col[8]] = {
                'pos': int(col[7]),
                'desc': col[9],
                'type': col[10],
                'origin': col[11],
                'context': col[12],
                'conversion': col[13]
            }
    return dic


if __name__ == '__main__':
    try:
        extract('telemetry2.xlsx')

    except Exception as e:
        raise e
