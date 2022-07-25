import os
 def __init__(self,n):
        self.n=n
        self.st=[None]*n
        self.top=-1
    def isFull(self) :
        return self.top==n-1
    def isEmpty(self):
        return self.top==n+1
    def push(self):
        if self.isFull():
            print("the stack is full")
        else:
            self.top+=1
            x=int(input("enter the data to be inserted"))
            self.st[self.top]=x
    def pop(self):
        if self.isEmpty():
             self.top-=1       
        else:    
            self.st.pop()
    def display(self):
        for i in range(self.top+1):
              final=self.st
        print(final)        
    def peek(self):
        print(self.st[-1])
n =int(input("enter the size of stack"))
s1=stack1(n)
while(1):
    print("1.push\n2.pop\n3.display\n4.peek\n5.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        s1.push()
    elif ch==2:
        s1.pop()
    elif ch==3:
        s1.display()
    elif ch==4:
        s1.peek()
    else:
         break
