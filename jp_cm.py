def jp_cm_converter():
    print('Japanese unit to cm converter')
    print()
    unit = input('Enter JP unit: ').lower()

    jp_units = {
        'shaku': (10/33) * 100,
        'sun': (1/33) * 100,
        'bu': (1/330) * 100
    }

    if unit not in jp_units:
        print('Please enter 1 of the following units:', ', '.join(jp_units))
        return

    multiply = float(input('How many ' + unit + ': '))

    result = jp_units[unit] * multiply
    print()
    print('Answer:', round(result, 3), 'cm')

jp_cm_converter()