#
# testConversions.py - tests the functions in conversions.py
#
from conversions import *
print("\nTESTING CONVERSIONS\n")
testF = 100
print(fahr2cel.__doc__)
testC = fahr2cel(testF)
print("Fahrenheit is ", testF, " Celsius is ", testC)
print()
print(kelv2cel.__doc__)
print(cel2fahr.__doc__)
print(kelv2fahr.__doc__)
print(cel2kelv.__doc__)
print(fahr2kelv.__doc__)

common_reference_points = [
        # Reference point, Degrees Fahrenheit, Kelvin, Degrees Celsius
        ["Boiling point of water", 212, 373, 100],
        ["Body temperature", 98.6, 310, 37],
        ["Room temperature", 68, 293, 20],
        ["Freezing point of water", 32, 273, 0],
        ["Absolute zero", -459, 0, -273],
        ]
INDEX_FAHR = 1
INDEX_KELV = 2
INDEX_CEL = 3
for idx, ref_point in enumerate(common_reference_points):
    cel = fahr = kelv = conv_cel = conv_fahr = conv_kelv = -1
    gold = -1
    cel = ref_point[INDEX_CEL]
    fahr = ref_point[INDEX_FAHR]
    kelv = ref_point[INDEX_KELV]
    if idx % 3 == 0: # convert to cel
        gold = cel
        conv_fahr = fahr2cel(fahr)
        conv_kelv = kelv2cel(kelv)
        pass
    elif idx % 3 == 1: # convert to fahr
        gold = fahr
        conv_cel = cel2fahr(cel)
        conv_kelv = kelv2fahr(kelv)
        pass
    elif idx % 3 == 2: # convert to kelv
        gold = kelv
        conv_cel = cel2kelv(cel)
        conv_fahr = fahr2kelv(fahr)
        pass
    print(f"gold={gold} cel={cel} fahr={fahr} kelv={kelv} "
        f"conv_cel={conv_cel} conv_fahr={conv_fahr} conv_kelv={conv_kelv}")


