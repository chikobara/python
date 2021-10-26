import random
num = random.randint(1,6)
print("\n\n\n")
print('|{:^60}|'.format("Welcome to YU GI OH HELPER"))
print("\n\n\n")
print("You can go with: Roll dice / HP calculator ")
modechoice = input("Enter what do want: ")
modechoice = modechoice.lower()
if modechoice == "roll dice":
    print('|{:^60}|'.format("you're about to roll a dice"))
    print('\n')
    print('|{:^60}|'.format("prepare you self "))
    print('\n')
    print('|{:^60}|'.format(num))
    print('\n')
    agn = input("Would you roll a dice again? (yes/no) ")
    agn = agn.lower()
    while agn == "yes":
        num = random.randint(1,6)
        print('\n')
        print('|{:^60}|'.format(num))
        agn = input("Would you roll a dice again? ")
        agn = agn.lower()
        if agn == "no":
            break


#first we would def a function to change the hp
#def myhpchange():
#    pass
#def ophpchange():
#    pass

myhp = 8000
ophp = 8000


elif modechoice == "hp calculator":
    print('|{:^60}|'.format(f"Your HP now is : {myhp}"))
    print('|{:^60}|'.format(f"Your opponent's hp is {ophp}"))
    # now this input is to taking what changes you need
    tc = input(f"Enter what you need to do \n changes on your hp press(myhp) \n changes on your opponent's hp press(ophp) ")
    if tc == "myhp":
        #choosing add or minus
        caom = input("You want to add or t")
        pass
    elif tc == "ophp":
        pass