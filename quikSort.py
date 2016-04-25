def quikSort(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quikSort(alist,first,splitpoint-1)
        quikSort(alist,splitpoint+1,last)

def partition(alist,first,last):
        leftmark=first+1
        rightmark=first+1
        pivot=alist[first]
        while rightmark< last:
            if alist[rightmark]< pivot:
                tmp=alist[rightmark]
                alist[rightmark]=alist[leftmark]
                alist[leftmark]=tmp
                leftmark=leftmark+1
            rightmark=rightmark+1
        alist[first]=alist[leftmark-1]
        alist[leftmark-1]=pivot
        print(leftmark)
        print(alist)
        return leftmark


alist=[15,12,13,17,19,23,44,66,70,7,89,1]
quikSort(alist,0,12)
print(alist)
