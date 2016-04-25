def quickSort(alist):
       quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    if first<last:
        pivot=alist[first]
        leftmark=first+1
        rightmark=last
        done =False

    while not done:

        while alist[leftmark]<=pivot and leftmark<=rightmark:
            leftmark=leftmark+1
        while alist[rightmark]>=pivot and leftmark <= rightmark:
            rightmark=rightmark-1

        if leftmark>rightmark:
            done =True
        else:
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp

    temp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp

    return rightmark

alist=[54,30,27,19,13,23,67,31,3,7]

quickSort(alist)

print(alist)
