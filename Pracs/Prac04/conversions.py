#
# conversions.py - module with functions to convert between units #
# fahr2cel : Convert from Fahrenheit to Celsius.
# kelv2cel : Convert from Kelvin to Celsius.
# cel2fahr : Convert from Celsius to Fahrenheit.
# kelv2fahr: Convert from Kelvin to Fahrenheit.
# cel2kelv : Convert from Celsius to Kelvin.
# fahr2kelv: Convert from Fahrenheit to Kelvin.

def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius. Argument:
    fahr - the temperature in Fahrenheit """
    cel = (fahr - 32) * (5/9)
    return cel

def kelv2cel(kelv):
    """Convert from Kelvin to Celsius. Argument:
    kelv - the temperature in Kelvin """
    cel = kelv - 273.15
    return cel

def cel2fahr(cel):
    """Convert from Celsius to Fahrenheit. Argument:
    cel - the temperature in Celsius """
    fahr = (9/5) * cel + 32
    return fahr

def kelv2fahr(kelv):
    """Convert from Kelvin to Fahrenheit. Argument:
    kelv - the temperature in Kelvin """
    fahr = kelv * 9 / 5 - 459.67
    return fahr

def cel2kelv(cel):
    """Convert from Celsius to Kelvin. Argument:
    cel - the temperature in Celsius """
    kelv = cel + 273.15
    return kelv

def fahr2kelv(fahr):
    """Convert from Fahrenheit to Kelvin. Argument:
    fahr - the temperature in Fahrenheit """
    kelv = (5/9) * (fahr + 459.67)
    return kelv

def main():
    print(f'\nTesting {__file__}')
    # put your testing code in here
    INDEX_FAHR = 0
    INDEX_KELV = 1
    INDEX_CEL = 2
    PASS_CRIT = 0.8
    test_datas = [
            # Degrees Fahrenheit, Kelvin, Degrees Celsius
            [212, 373, 100], # Boiling point of water
            [98.6, 310, 37], # Body temperature
            [68, 293, 20], # Room temperature
            [32, 273, 0], # Freezing point of water
            [-459, 0, -273], # Absolute zero
            ]
    test_configs = [
            # Test function, input index, golden index
            [fahr2cel, INDEX_FAHR, INDEX_CEL],
            [kelv2cel, INDEX_KELV, INDEX_CEL],
            [cel2fahr, INDEX_CEL, INDEX_FAHR],
            [kelv2fahr, INDEX_KELV, INDEX_FAHR],
            [cel2kelv, INDEX_CEL, INDEX_KELV],
            [fahr2kelv, INDEX_FAHR, INDEX_KELV],
            ]
    for test_data in test_datas:
        for test_config in test_configs:
            result = test_config[0](test_data[test_config[1]])
            delta = abs(result - test_data[test_config[2]])
            if delta > PASS_CRIT:
                print(f"{test_config[0].__name__}: input={test_data[test_config[1]]} delta={delta} PASS_CRIT={PASS_CRIT} fail")
            else:
                print(test_config[0].__name__, "Pass")
    print('Testing complete')

if __name__ == '__main__':
    main()
