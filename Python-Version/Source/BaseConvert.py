import math

print(" ______________________________________________________________ ")
print("|                                                              |")
print("| In the Name of God, the Most Gracious and the Most Merciful. |")
print("|______________________________________________________________|")
print(" ________________________________ ")
print("|                                |")
print("| Name   :  Muhammad Omar Farooq |")
print("| Roll No:  20-CP-33             |")
print("|________________________________|")
print("")

while True:
    while True:
        try:
            N = int(input("Enter the number: "))
        except ValueError:
            print("Error: Only number is accepted as input.")
            print("")
            continue
        else:
            break
    while True:
        try:
            B = int(input("Enter the base: "))
        except ValueError:
            print("Enter between 2 and 36.")
            print("")
            continue
        else:
            break
    recall_N = N
    remain_N = []
    i = 0
    output = []

    if N>=B or N<=B:
        while True:
            Q = math.floor(N/B)
            R = N%B
            if R<10:
                remain_N.append(R)
                if B>N :
                    break
                N = Q
            elif R>=10:
                m = R+55
                remain_N.append(m)
                if B>N :
                    break
                N = Q
                    
        b = ((len(remain_N))-1)
        j = b
            
        while True:
            k = remain_N[j]
            if k>=10:
                z = chr(k)
                output.append(z)
                if j<=0:
                    break
            elif (k<10):
                output.append(k)
                if j <= 0:
                    break
            j -= 1
    l = str(output)[1:-1]
    y = l.replace(", ","")
    M = y.replace("'","")
    print(recall_N," in base ",B,"is: ",M)
    print("")
    print("")
    command = str(input(" >> Type 'exit' and press enter to exit || Enter any key to continue >>"))
    state = command.title()
    if state == 'Exit':
        break
    else:
        continue
    last = input("")

