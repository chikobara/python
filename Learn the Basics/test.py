print('Enter your numbers : ')
lst = list()
while True:
    try:
        x = input()
        if x == 'q':
            break
        else:
            int(x)
    except:
        continue
    lst.append(x)
lst.sort(reverse=True)
print('largest num is : ', lst[0])