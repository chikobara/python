lar = -1
sml = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if num > lar:
        lar = num
    if sml is None:
        sml = num
    elif num < sml:
        sml = num
print("Maximum is", lar)
print("Minimum is", sml)
