def filter(value):
    # I believe this function gets called for each record of the dataset, based on the input and the output.
    # Q: Do we always have to use dictionaries for this type of functions? Can we use, case statements, if conditionals, etc...
    schoolDistrict = { 'WCES':'100', 'WCMS':'200', 'WCHS':'300'}

    if value in schoolDistrict:
        value = schoolDistrict.get(value)
    else:
        value = '123456'
    result = value
    return result

#Role IDs

def filter(value):
    roleDistrict = { 'TEA':'8', 'TEACH':'8', 'PRIN':'6'}
    if value in roleDistrict:
        value = roleDistrict.get(value)
    else:
        value = '10'
    result = value
    return result
