
#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

#Your backtracking function implementation
Assigned = []
Value = []
Var = []
Domain = []
Constraints = []
CurrDomain = []
CutDomain = []
BT_Conflict = 0

def BT_Recursion(level):
    flag = False
    flag_var = True
    if len(Assigned) == len(Var):
        for j in Value:
            if j == -1:
                flag_var = False
        if flag_var:
            #All variables are assigned
            flag = True

    if (flag):
        optimalLength = Value[len(Var) - 1]
        return optimalLength,Value


    V = len(Assigned)
    Assigned.append(True)

    for d in Domain:

        Value[V] = d

        OK = True
        #for each constraint C i.e. ((x, y),(p, q)) such that V is a variable of C and all other variables of C are assigned.
        #new_Constraints=(x for x in Constraintsr",x,V if any(V in y for y in x))
        for ((x, y),(p, q)) in Constraints:
            if ((x == V) or (y == V) or (p == V) or (q == V)):
                if ((Value[x] != -1) and (Value[y] != -1) and (Value[p] != -1) and (Value[q] != -1)):
                    if abs(Value[x] - Value[y]) == abs(Value[p] - Value[q]):
                        #BT_Conflict += 1
                        OK = False
                        Value[V] = -1
                        break
        if OK:
            length,Markers = BT_Recursion(level+1)
            if length != -1 and Markers != []:
                return length,Markers

    Assigned.pop()
    return -1,[]

def BT(L, M):
    #Variables are as below:
    for j in range(0,M):
        Var.append(j)

    #Domain is as below:
    for j in range(0,L+1):
        Domain.append(j)

    for j in range(0, M):
        Value.append(-1)

    Constraints_temp=[]
    for j in range(0,M-1):
        for k in range(j+1,M):
            Constraints_temp.append((j,k))
    for j in range(0,len(Constraints_temp)-1):
        for k in range(j+1,len(Constraints_temp)):
            Constraints.append((Constraints_temp[j],Constraints_temp[k]))
    return BT_Recursion(0)


def Restore(level, V):
    print "in restore, V :", V
    for i in CutDomain:
        (CurrDomain[V]).append(i)
    (CurrDomain[V]).sort()

def FCCheck(V, d):
    #We have just assigned a value to V
    #We need to check every value from the CurrDomain of neighbor to see if it is not violating
    #any Constraints
    """
    print "constraint : ",x, y, p, q
    print "V, V1, level : ", V, V1, level
    CutDomain = []
    temp = CurrDomain[V1]
    for d in CurrDomain[V1]:
        Value[V1] = d
        if abs(Value[x] - Value[y]) == abs(Value[p] - Value[q]):
            temp.remove(d)
            CutDomain.append(d)
            print CurrDomain[V1]
            print d
            print CutDomain

    if temp == []:
        #Restore(level, V1)
        return True

    CurrDomain[V1] = temp[:]
    return False
    """
    for i in range(V+1, len(CurrDomain)):
        if(d in CurrDomain[i]):
            CurrDomain[i].remove(d)

def FC_Recursion(level):

    flag = False
    flag_var = True

    if len(Assigned) == len(Var):
        for j in Value:
            if j == -1:
                flag_var = False
        if flag_var:
            #print "All variables are assigned"
            flag = True

    if (flag):
        #print "Returning to caller"
        optimalLength = Value[len(Var) - 1]
        return optimalLength,Value

    V = len(Assigned)
    Assigned.append(True)

    for d in CurrDomain[V]:
        temp2 = []
        Value[V] = d

        OK = False
        for ((x, y),(p, q)) in Constraints:
            if ((x == V) or (y == V) or (p == V) or (q == V)):
                if ((Value[x] != -1) and (Value[y] != -1) and (Value[p] != -1) and (Value[q] != -1)):
                    if abs(Value[x] - Value[y]) == abs(Value[p] - Value[q]):
                        #BT_Conflict += 1
                        OK = True
                        Value[V] = -1
                        break


        if (OK == False):
            #Here we remove the assigned value i.e.

            FCCheck(V, d)
            length,Markers = FC_Recursion(level+1)
            if length != -1 and Markers != []:
                return length,Markers

        #Restore(level, V)

    Assigned.pop()
    return -1,[]

#Your backtracking+Forward checking function implementation
def FC(L, M):

    for j in range(0,M):
        Var.append(j)
    #print "Variable : ", Var

    for j in range(0,L+1):
        Domain.append(j)
    #print "Domain : ", Domain

    for j in range(0, M):
        Value.append(-1)

    Constraints_temp=[]
    for j in range(0,M-1):
        for k in range(j+1,M):
            Constraints_temp.append((j,k))
    for j in range(0,len(Constraints_temp)-1):
        for k in range(j+1,len(Constraints_temp)):
            Constraints.append((Constraints_temp[j],Constraints_temp[k]))

    for i in range(len(Var)):
        CurrDomain.append(Domain[:])


    return FC_Recursion(0)

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

if __name__ == "__main__":
    L = input( "Enter Length:")
    M = input( "Enter Marker:")

    Choice = input( "Enter your choice: 1.BT(Optimal Solution)  2.FC+BT   : ")

    Length_list = []
    Markers_list = []

    if (Choice == 1):
        i = L
        while(i > 0):
            (Length, Markers) = BT(i, M)
            Assigned = []
            Value = []
            Var = []
            Domain = []
            Constraints = []
            Length_list.append(Length)
            Markers_list.append(Markers)
            if (Length == -1):
                break
            i -= 1
        #We calculated all possible Golomb Rulers for given number of Markers and a length <= user provided Length

        if (len(Length_list) >= 2):
            print "The optimal Length and Markers are : "
            print "Length : ", Length_list[len(Length_list) - 2]
            print "Markers : ", Markers_list[len(Markers_list) - 2]
        else:
            print "No Golomb ruler exist for given Length and Markers"
            if (len(Length_list) > 0):
                print "Length : ", Length_list[0]
            else:
                print "Length : 0 "
            if (len(Markers_list) > 0):
                print "Markers : ", Markers_list[0]
            else:
                print "Markers : []"

    elif (Choice == 2):
        i = L
        while(i > 0):
            (Length, Markers) = FC(i, M)
            Assigned = []
            Value = []
            Var = []
            Domain = []
            Constraints = []
            Length_list.append(Length)
            Markers_list.append(Markers)
            if (Length == -1):
                break
            i -= 1
        #We calculated all possible Golomb Rulers for given number of Markers and a length <= user provided Length

        if (len(Length_list) >= 2):
            print "The optimal Length and Markers are : "
            print "Length : ", Length_list[len(Length_list) - 2]
            print "Markers : ", Markers_list[len(Markers_list) - 2]
        else:
            print "No Golomb ruler exist for given Length and Markers"
            if (len(Length_list) > 0):
                print "Length : ", Length_list[0]
            else:
                print "Length : 0 "
            if (len(Markers_list) > 0):
                print "Markers : ", Markers_list[0]
            else:
                print "Markers : []"

    else:
        print "Invalid Choice"
