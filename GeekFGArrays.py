def alternateElements(x,i,n):
    if(i==n-1):
        if i%2:
            return(1)
        else:
            print(x[i])
            return(1)
    if(i%2):
        alternateElements(x,i+1,n)
    else:
        print(x[i])
        alternateElements(x,i+1,n)

def productOfArray(x,n):
    if(n==-1):
        return(1)
    else:
        return(x[n]*productOfArray(x,n-1))

def SearchElement(x, y, n):
    ''''I want you to learn and write all search algos in here but since searching is altogether another topic in the list of topics to be covered so
    just do it somehow'''
    if n==-1:
        return(0)

    if(x[n]==y):
        return(1)
    else:
        SearchElement(x,y,n-1)

def rotateN(x, n):
    y = [0 for i in range(len(x))]
    for i in range(len(x)):
        j = (i+n)%len(x)
        y[j] = x[i]
    return(y)

def sort(x):
    pass

def pendulum(x):
    sort(x)

    y = [0 for i in range(len(x))]
    for i in range(len(x)):
        y[i] = x[i]
        y[len(x)-1-i] = x[i+1]
        i = i+1

def reverse(x):
    y = [x[-i-1] for i in range(len(x))]
    return(y)

def reverse_in_groups(x,n):
    for i in range(len(x)):
        if(i+n<len(x)-1):
            reverse(x[i:i+n])
            i=i+n+1
        else:
            reverse(x[i:len(x)-1])
            i=i+n+1
    return(x)

def leaders(x):

    y = sort(x) #descending
    print(x[-1])
    j=0
    for i in range(len(x)-1):
        if x[i] == y[j]:
            print(x[i])
            j=j+1
        i=i+1

def closest_num(x,n):
    y= sort(x) #ascending
    if(abs(y[0]-n) == abs(y[1]-n)):
        if(y[0]>y[1]):
            print(y[0])
        else:
            print(y[1])
    else:
        print(y[0])

def distinct_numbers(x):
    '''Solve this problem by hash table'''
    pass

def check_prefix(x,s):
    n = len(s)
    i = 1
    for i in range(len(x)):
        if x[i][0:n-1] != s:
            return(None)
    return(check_prefix())


def common_prefix(x):
    y = [len(x[i] for i in range(len(x)))]
    smallest_i = y.index(min(y))
    smallest_s = x[smallest_i]

    for i in range(len(smallest_s)-1):
        smallest_s=smallest_s[0:len(smallest_s)-1]
        y = check_prefix(x,smallest_s)
        if y:
            print(y)
            break

def Type_of_Array(x):
    max_i = x.index(max(x))
    min_i = x.index(min(x))
    if max_i==len(x)-1:
        return("Ascending")
    elif max_i==0:
        return("Descending")
    elif max_i<min_i:
        return("Descending Rotated")
    else:
        return("Ascending Rotated")


def AbsoluteDiff1(x,k):
    y = []

    for i in range(len(x)):
        pass




if __name__=="__main__":

    x=[1,2,3,4,5,6,7,8,9,10]
    n = len(x)
    #alternateElements(x,0,n)
    #print(productOfArray(x, n-1))
    #print(SearchElement(x,5,n-1))
    #print(rotateN(x,3))


