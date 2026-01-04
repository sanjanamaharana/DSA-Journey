for i in range(0,3):
    for j in range (0,11):
        print("*", end=" ")
    print("")
for i in range(0,2):
    for j in range (0,2):
        print("*", end=" ")
    print("")
for i in range(0,2):
    for j in range (0,11):
        print("*", end=" ")
    print("")
for i in range(0,2):
    for j in range (0,9):
        print(" ", end=" ")
    for j in range (0,2):
        print("*", end=" ")
    print("")
for i in range(0,3):
    for j in range (0,11):
        print("*", end=" ")
    print("")
#       * * * * * * * * 
#       * * * * * * * * 
#       * * * * * * * * 
#       * * 
#       * * 
#       * * * * * * * * 
#       * * * * * * * * 
#                   * * 
#                   * * 
#       * * * * * * * * 
#       * * * * * * * * 
#       * * * * * * * * 
for i in range(0,11):
    for j in range(0,11-i):
        print("*", end="")
    for j in range(0,(2*i)+1):
        if(i==6 or i ==5):
            print("*", end="")
            continue 
        print(" ", end="")
    for j in range(0,11-i):
        print("*", end="")
    print("")

#        *********** ***********
#        **********   **********
#        *********     *********
#        ********       ********
#        *******         *******
#        ***********************
#        ***********************
#        ****               ****
#        ***                 ***
#        **                   **
#        *                     *

for i in range(0,11):
    for j in range(0,11-i,2):
        print("*", end="")
    for j in range(0,(2*i)+1):
        print(" ", end="")
    for j in range(0,4):
        print("*", end="")
    for j in range(0,9-i):
         print(" ", end="")
    for j in range(0,11-i):
        print("*", end="")
    print("")

#         ****** ****         ***********
#         *****   ****        **********
#         *****     ****       *********
#         ****       ****      ********
#         ****         ****     *******
#         ***           ****    ******
#         ***             ****   *****
#         **               ****  ****
#         **                 **** ***
#         *                   ******
#         *                     *****

for i in range(0,2):
    for j in range (0,14):
        print("*", end=" ")
    print("")
for i in range(0,6):
    for j in range (0,6):
        print(" ", end=" ")
    for j in range (0,3):
        print("*", end=" ")
    print("")
for i in range(0,3):
    for j in range (0,9):
        print("*", end=" ")
    print("")

#          * * * * * * * * * * * * * * 
#          * * * * * * * * * * * * * * 
#                      * * * 
#                      * * * 
#                      * * * 
#                      * * * 
#                      * * * 
#                      * * * 
#          * * * * * * * * * 
#          * * * * * * * * * 
#          * * * * * * * * * 

for i in range(0,11):
    for j in range(0,11-i):
        print("*", end="")
    for j in range(0,(2*i)+1):
        if(i==6 or i ==5):
            print("*", end="")
            continue 
        print(" ", end="")
    for j in range(0,11-i):
        print("*", end="")
    print("")

#        *********** ***********
#        **********   **********
#        *********     *********
#        ********       ********
#        *******         *******
#        ***********************
#        ***********************
#        ****               ****
#        ***                 ***
#        **                   **
#        *                     *

for i in range(0,11):
    for j in range(0,11-i,2):
        print("*", end="")
    for j in range(0,(2*i)+1,2):
        print(" ", end="")
    for j in range(0,4):
        print("*", end="")
    for j in range(0,9-i):
         print(" ", end="")
    for j in range(0,11-i):
        print("*", end="")
    print("")

#          ****** ****         ***********
#          *****  ****        **********
#          *****   ****       *********
#          ****    ****      ********
#          ****     ****     *******
#          ***      ****    ******
#          ***       ****   *****
#          **        ****  ****
#          **         **** ***
#          *          ******
#          *           *****

for i in range(0,11):
    for j in range(0,11-i):
        print("*", end="")
    for j in range(0,(2*i)+1):
        if(i==6 or i ==5):
            print("*", end="")
            continue 
        print(" ", end="")
    for j in range(0,11-i):
        print("*", end="")
    print("")

#        *********** ***********
#        **********   **********
#        *********     *********
#        ********       ********
#        *******         *******
#        ***********************
#        ***********************
#        ****               ****
#        ***                 ***
#        **                   **
#        *                     *
