#
# list_comp.py: Using both loops and list comprehensions
#

def triple(n):
    return n*3

numbers = range(1, 5)

print(numbers)

numbers_triple = []
for num in numbers:
    numbers_triple.append(triple(num))

print(numbers_triple)

print([triple(n) for n in numbers])

tmp_str = "Abc def  gH 16 ijk 131 lmn 4 o "

print('input str=('+tmp_str+')')

splits = tmp_str.split()
ext_nums = []
ext_words = []

for ext in splits:
    if ext.isdigit():
        ext_nums.append(ext)
    else:
        ext_words.append(ext)
print(ext_nums)
print(ext_words)

print([n for n in splits if n.isdigit()])
print([n for n in splits if not n.isdigit()])

ext_words_cap = []
for word in ext_words:
    ext_words_cap.append(word[0].upper()+word[1:])

print(ext_words_cap)

print([word[0].upper()+word[1:] for word in ext_words])
