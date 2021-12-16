def filter(value):
    schoolDistrict = { 'WCES':'100', 'WCMS':'200', 'WCHS':'300'}

    if value in schoolDistrict:
        value = schoolDistrict.get(value)
    else:
        value = '123456'
    result = value
    return value

#Role IDs

def filter(value):
    roleDicstrict = { 'TEA':'8', 'TEACH':'8', 'PRIN':'6'}

    if value in roleDicstrict:
        value = roleDicstrict.get(value)
    else:
        value = '10'
    result = value
    return value
