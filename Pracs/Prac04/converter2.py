#
# converter2.py - convert degrees between Fahrenheit, Celsius and Kelvin
#

from conversions import *

BOLD = '\033[1m'
RESET = '\033[0m'
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
func_list = [fahr2cel, kelv2cel, cel2fahr,
        kelv2fahr, cel2kelv, fahr2kelv]
conv_desc = [
        ("Fahr", "Cel"), ("Kelv", "Cel"), ("Cel", "Fahr"),
        ("Kelv", "Fahr"), ("Cel", "Kelv"), ("Fahr", "Kelv"),
        ]
exit_key="q"
input_key=""
while(exit_key != input_key.lower()):
    print(BOLD, '\nWelcome to the temperature converter', RESET)
    for idx, func_item in enumerate(func_list):
        print(f"[{idx+1}] {func_item.__doc__}")
    inputselect = int(input('Which convert would you like? '))
    if inputselect >= 1 and inputselect <= len(func_list):
        selected = inputselect-1
        input_str = input('Input all temperatures: ')
        if not input_str.strip():
            input_key = "q"
        else:
            input_values = input_str.split()
            for input_value in input_values:
                input_value = float(input_value.strip())
                output_value = func_list[selected](input_value)
                print(f"{func_list[selected].__name__} {conv_desc[selected][0]}={input_value}"
                        f" {conv_desc[selected][1]}={output_value}")
            input_key = input('Press "q" to exit, other key to continue... ')
            for l in range(len(func_list)*2+6+ len(input_values)-1):
                pass #print(LINE_UP, end=LINE_CLEAR)
    else:
        for l in range(len(func_list)*2+3):
            pass #print(LINE_UP, end=LINE_CLEAR)
print('Bye')
