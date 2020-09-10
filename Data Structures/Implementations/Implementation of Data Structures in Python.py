#!/usr/bin/env python
# coding: utf-8

# In[1]:


#stack

from collections import deque 

stack= deque() 





# adding to stack 

stack.append("apple") 

stack.append("ball") 

stack.append("cat") 

print("full stack") 

print(stack) 





# poping from stack 

stack.pop() 

stack.pop() 

stack.pop() 

print("empty stack") 

print(stack) 


# In[4]:


#using array -on queue 

queue = []  

 

 

#adding stuff to element  

queue.append('apple')  

queue.append('ball')  

queue.append('cat')  

print("queue with elements")  

print(queue)  

print("\nElements removing or dequeued from queue")  

#removing stuff from queue 

print(queue.pop(0))  

print(queue.pop(0))  

print(queue.pop(0))  

print("\nQueue after removing elements")  

print(queue) 


# In[5]:


#traversing linked list
class Node: 
    def __init__(self, dataval=None): 
        self.dataval = dataval 
        self.nextval = None 
 
class SLinkedList: 
    def __init__(self): 
        self.headval = None 
 
    def listprint(self): 
        printval = self.headval 
        while printval is not None: 
            print (printval.dataval) 
            printval = printval.nextval 
 
list = SLinkedList() 
list.headval = Node("Mon") 
e2 = Node("Tue") 
e3 = Node("Wed") 
 
# Link first Node to second node 
list.headval.nextval = e2 
 
# Link second Node to third node 
e2.nextval = e3 
 
list.listprint() 


# In[6]:


#Inserting at beginning  linked list

 

class Node: 
    def __init__(self, dataval=None): 
        self.dataval = dataval 
        self.nextval = None 
 
class SLinkedList: 
    def __init__(self): 
        self.headval = None 
 
# Print the linked list 
    def listprint(self): 
        printval = self.headval 
        while printval is not None: 
            print (printval.dataval) 
            printval = printval.nextval 
    def AtBegining(self,newdata): 
        NewNode = Node(newdata) 
 
# Update the new nodes next val to existing node 
        NewNode.nextval = self.headval 
        self.headval = NewNode 
 
list = SLinkedList() 
list.headval = Node("Mon") 
e2 = Node("Tue") 
e3 = Node("Wed") 
 
list.headval.nextval = e2 
e2.nextval = e3 
 
list.AtBegining("Sun") 
 
list.listprint() 

 


# In[8]:


#Inserting at the End of the Linked List: 

 

class Node: 
    def __init__(self, dataval=None): 
        self.dataval = dataval 
        self.nextval = None 
 
class SLinkedList: 
    def __init__(self): 
        self.headval = None 
 
# Function to add newnode 
    def AtEnd(self, newdata): 
        NewNode = Node(newdata) 
        if self.headval is None: 
            self.headval = NewNode 
            return 
        laste = self.headval 
        while(laste.nextval): 
            laste = laste.nextval 
        laste.nextval=NewNode 
 
# Print the linked list 
    def listprint(self): 
        printval = self.headval 
        while printval is not None: 
            print (printval.dataval) 
            printval = printval.nextval 
 
 
list = SLinkedList() 
list.headval = Node("Mon") 
e2 = Node("Tue") 
e3 = Node("Wed") 
 
list.headval.nextval = e2 
e2.nextval = e3 
 
list.AtEnd("Thu") 
 
list.listprint() 


# In[10]:


#Inserting in between two Data Nodes: 

 

class Node: 
    def __init__(self, dataval=None): 
        self.dataval = dataval 
        self.nextval = None 
 
class SLinkedList: 
    def __init__(self): 
        self.headval = None 
 
# Function to add node 
    def Inbetween(self,middle_node,newdata): 
        if middle_node is None: 
            print("The mentioned node is absent") 
            return 
 
        NewNode = Node(newdata) 
        NewNode.nextval = middle_node.nextval 
        middle_node.nextval = NewNode 
 
# Print the linked list 
    def listprint(self): 
        printval = self.headval 
        while printval is not None: 
            print (printval.dataval) 
            printval = printval.nextval 
 
 
list = SLinkedList() 
list.headval = Node("Mon") 
e2 = Node("Tue") 
e3 = Node("Thu") 
 
list.headval.nextval = e2 
e2.nextval = e3 
 
list.Inbetween(list.headval.nextval,"Fri") 
 
list.listprint() 

 


# In[11]:


#Removing an Item from a Linked List: 

 
class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 
 
class SLinkedList: 
    def __init__(self): 
        self.head = None 
 
    def Atbegining(self, data_in): 
        NewNode = Node(data_in) 
        NewNode.next = self.head 
        self.head = NewNode 
 
# Function to remove node 
    def RemoveNode(self, Removekey): 
 
        HeadVal = self.head 
 
        if (HeadVal is not None): 
            if (HeadVal.data == Removekey): 
                self.head = HeadVal.next 
                HeadVal = None 
                return 
 
        while (HeadVal is not None): 
            if HeadVal.data == Removekey: 
                break 
            prev = HeadVal 
            HeadVal = HeadVal.next 
 
        if (HeadVal == None): 
            return 
 
        prev.next = HeadVal.next 
 
        HeadVal = None 
 
    def LListprint(self): 
        printval = self.head 
        while (printval): 
            print(printval.data), 
            printval = printval.next 
 
 
llist = SLinkedList() 
llist.Atbegining("Mon") 
llist.Atbegining("Tue") 
llist.Atbegining("Wed") 
llist.Atbegining("Thu") 
llist.RemoveNode("Tue") 
llist.LListprint() 

 


# In[12]:


class CircularQueue():  

   

    # constructor  

    def __init__(self, size): # initializing the class  

        self.size = size  

           

        # initializing queue with none  

        self.queue = [None for i in range(size)]   

        self.front = self.rear = -1 

   

    def enqueue(self, data):  

           

        # condition if queue is full  

        if ((self.rear + 1) % self.size == self.front):   

            print(" Queue is Full\n")  

               

        # condition for empty queue  

        elif (self.front == -1):   

            self.front = 0 

            self.rear = 0 

            self.queue[self.rear] = data  

        else:  

               

            # next position of rear  

            self.rear = (self.rear + 1) % self.size   

            self.queue[self.rear] = data  

               

    def dequeue(self):  

        if (self.front == -1): # codition for empty queue  

            print ("Queue is Empty\n")  

               

        # condition for only one element  

        elif (self.front == self.rear):   

            temp=self.queue[self.front]  

            self.front = -1 

            self.rear = -1 

            return temp  

        else:  

            temp = self.queue[self.front]  

            self.front = (self.front + 1) % self.size  

            return temp  

   

    def display(self):  

       

        # condition for empty queue  

        if(self.front == -1):   

            print ("Queue is Empty")  

   

        elif (self.rear >= self.front):  

            print("Elements in the circular queue are:",   

                                              end = " ")  

            for i in range(self.front, self.rear + 1):  

                print(self.queue[i], end = " ")  

            print ()  

   

        else:  

            print ("Elements in Circular Queue are:",   

                                           end = " ")  

            for i in range(self.front, self.size):  

                print(self.queue[i], end = " ")  

            for i in range(0, self.rear + 1):  

                print(self.queue[i], end = " ")  

            print ()  

   

        if ((self.rear + 1) % self.size == self.front):  

            print("Queue is Full")  

   

# Driver Code  

ob = CircularQueue(5)  

ob.enqueue(14)  

ob.enqueue(22)  

ob.enqueue(13)  

ob.enqueue(-6)  

ob.display()  

print ("Deleted value = ", ob.dequeue())  

print ("Deleted value = ", ob.dequeue())  

ob.display()  

ob.enqueue(9)  

ob.enqueue(20)  

ob.enqueue(5)  

ob.display()  


# In[ ]:




