# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:17:41 2022

@author: Syeda Fatima Zahid
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

        
    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = Node(data, None)
        
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
           raise Exception("Invalid Index")

        if index==0:
           self.insert_at_begining(data)
           return

        count = 0
        temp = self.head
        while temp:
           if count == index - 1:
               node = Node(data, temp.next)
               temp.next = node
               break

           temp = temp.next
           count += 1

        
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Index invalid")
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
           self.insert_at_end(data)
           
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()      
        