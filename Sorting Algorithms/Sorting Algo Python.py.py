#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bubble_sort(sort_list): 

    for j in range(len(sort_list)): 

        for k in range(len(sort_list) - 1): 

            if sort_list[k] > sort_list[k + 1]: 

                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k] 

    print(sort_list) 

  

  

lst = [] 

size = int(input("Enter size of the list: \t")) 

  

for i in range(size): 

    elements = int(input("Enter the element: \t")) 

    lst.append(elements) 

  

bubble_sort(lst) 


# In[3]:


def selection_sort(alist): 

    for i in range(0, len(alist) - 1): 

        smallest = i 

        for j in range(i + 1, len(alist)): 

            if alist[j] < alist[smallest]: 

                smallest = j 

        alist[i], alist[smallest] = alist[smallest], alist[i] 

  

  

alist = input('Enter the list of numbers: ').split() 

alist = [int(x) for x in alist] 

selection_sort(alist) 

print('Sorted list: ', end='') 

print(alist) 


# In[4]:


def insertion_sort(alist): 

    for i in range(1, len(alist)): 

        temp = alist[i] 

        j = i - 1 

        while (j >= 0 and temp < alist[j]): 

            alist[j + 1] = alist[j] 

            j = j - 1 

        alist[j + 1] = temp 

  

  

alist = input('Enter the list of numbers: ').split() 

alist = [int(x) for x in alist] 

insertion_sort(alist) 

print('Sorted list: ', end='') 

print(alist) 

 


# In[5]:


def bucket_sort(alist): 

    largest = max(alist) 

    length = len(alist) 

    size = largest/length 

  

    buckets = [[] for _ in range(length)] 

    for i in range(length): 

        j = int(alist[i]/size) 

        if j != length: 

            buckets[j].append(alist[i]) 

        else: 

            buckets[length - 1].append(alist[i]) 

  

    for i in range(length): 

        insertion_sort(buckets[i]) 

  

    result = [] 

    for i in range(length): 

        result = result + buckets[i] 

  

    return result 

  

def insertion_sort(alist): 

    for i in range(1, len(alist)): 

        temp = alist[i] 

        j = i - 1 

        while (j >= 0 and temp < alist[j]): 

            alist[j + 1] = alist[j] 

            j = j - 1 

        alist[j + 1] = temp 

  

  

alist = input('Enter the list of (nonnegative) numbers: ').split() 

alist = [int(x) for x in alist] 

sorted_list = bucket_sort(alist) 

print('Sorted list: ', end='') 

print(sorted_list) 

 


# In[6]:


def radix_sort(alist, base=10): 

    if alist == []: 

        return 

  

    def key_factory(digit, base): 

        def key(alist, index): 

            return ((alist[index]//(base**digit)) % base) 

        return key 

    largest = max(alist) 

    exp = 0 

    while base**exp <= largest: 

        alist = counting_sort(alist, base - 1, key_factory(exp, base)) 

        exp = exp + 1 

    return alist 

  

def counting_sort(alist, largest, key): 

    c = [0]*(largest + 1) 

    for i in range(len(alist)): 

        c[key(alist, i)] = c[key(alist, i)] + 1 

  

    # Find the last index for each element 

    c[0] = c[0] - 1 # to decrement each element for zero-based indexing 

    for i in range(1, largest + 1): 

        c[i] = c[i] + c[i - 1] 

  

    result = [None]*len(alist) 

    for i in range(len(alist) - 1, -1, -1): 

        result[c[key(alist, i)]] = alist[i] 

        c[key(alist, i)] = c[key(alist, i)] - 1 

  

    return result 

  

alist = input('Enter the list of (nonnegative) numbers: ').split() 

alist = [int(x) for x in alist] 

sorted_list = radix_sort(alist) 

print('Sorted list: ', end='') 

print(sorted_list) 


# In[7]:


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


# In[8]:


def quicksort(alist, start, end): 

    '''Sorts the list from indexes start to end - 1 inclusive.''' 

    if end - start > 1: 

        p = partition(alist, start, end) 

        quicksort(alist, start, p) 

        quicksort(alist, p + 1, end) 

  

  

def partition(alist, start, end): 

    pivot = alist[start] 

    i = start + 1 

    j = end - 1 

  

    while True: 

        while (i <= j and alist[i] <= pivot): 

            i = i + 1 

        while (i <= j and alist[j] >= pivot): 

            j = j - 1 

  

        if i <= j: 

            alist[i], alist[j] = alist[j], alist[i] 

        else: 

            alist[start], alist[j] = alist[j], alist[start] 

            return j 

  

  

alist = input('Enter the list of numbers: ').split() 

alist = [int(x) for x in alist] 

quicksort(alist, 0, len(alist)) 

print('Sorted list: ', end='') 

print(alist) 


# In[ ]:




