def filter(value):
    schoolDistrict = { 'WCES':'100', 'WCMS':'200', 'WCHS':'300'}

    if value in schoolDistrict:
        value = schoolDistrict.get(value)
    else:
        value = '123456'
    result = value
    return value
