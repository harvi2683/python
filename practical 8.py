#20CE136_harvisheth
#Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.


class stack:
    def __init__(self):
        self.element=[]
    def push(self,value):
        return self.element.append(value)
    def pop(self):
        return self.element.pop()
    def traversal(self):
        print('elements are presents on the stacks :',self.element)
    def __iter__(self):
        return self

stack=stack()
for i in range(1,5):
 print('Enter 1 for pushing element and 2 for pop the element 3 for display stack content')
 choose=int(input())
 if choose==1:
       print('Enter the element for pushing element on to the stack :')
       ele=int(input())
       stack.push(ele)
 elif choose==2:
      print('pop out element is=',stack.pop())
 elif choose==3:

    stack.traversal()
 else:
     print('wrong choice')
