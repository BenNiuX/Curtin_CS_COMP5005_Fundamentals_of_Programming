#
# bucket2.py - bucket list builder
#
print('\nBUCKET LIST BUILDER\n')
bucket = []
choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete...')
while choice[0].upper() != 'X':
    if choice[0].upper() == 'A':
        print('Enter list item... ')
        newitem = input()
        bucket.append(newitem)
    elif choice[0].upper() == 'L':
        for item in bucket:
            print(item)
    elif choice[0].upper() == 'D':
        delitem = int(input('Delete item index:'))
        if delitem >= 0 and delitem < len(bucket):
            print(f"Delete index: {delitem} item: {bucket[delitem]}")
            del bucket[delitem]
        else:
            print('Out of range')
    else:
        print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete...')
print('\nGOODBY!\n')
