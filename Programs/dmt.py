from Req_Func import get_index, get_accseq
class Tree:
    def __init__(self,Node):
        self.check1 = Node
        self.val = 0
class Node:
    def __init__(self,data):                            #node intilialize
        self.left = None
        self.right = None
        self.data = data
        self.counter = 0

    def insert(self,data):                              #data is lesser than current node
        if (data < self.data):
            if (self.left is None):                     
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif (data > self.data):                        #data is greater than current node
            if (self.right is None):
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:                                           #data is equal to the current node
            self.data = data

    def dmt(self,key):
        first_time = 0
        if(check.check1.data == key):
            check.check1.counter += 1
            check.val += 1
            return
        while(check.check1.data != key):
            current = root
            prev = Node(None)
            dir = 0
            while(key != check.check1.data):
                if(key > current.data):
                    if(current.right != None):
                        if(key == current.right.data):
                            if(first_time == 0):
                                check.val += 1 #+1 operation of search
                                current.right.counter += 1
                                first_time = 1
                            if(prev.data == None):
                                prev = check.check1
                            if(current.right.counter >= prev.counter):                                
                                x = current.left_rotate(prev,dir)
                            else:
                                x = current.right
                            if(prev.counter > x.counter):
                                return 
                            else:
                                break
                        else:
                            if(first_time == 0):
                                check.val += 1
                            prev = current
                            dir = 1
                            current = current.right
                            #print("-->")
                
                elif(key < current.data):
                    if(current.left != None):
                        if(key == current.left.data):
                            if(first_time == 0):
                                check.val += 1  #+1 operation of search
                                current.left.counter += 1
                                first_time = 1
                            if(prev.data == None):
                                prev = check.check1
                            if(current.left.counter >= prev.counter):                                
                                x = current.right_rotate(prev,dir)
                            else:
                                x = current.left
                            if(prev.counter > x.counter):
                                return 
                            else:
                                break
                        else:
                            if(first_time == 0):
                                check.val += 1
                            prev = current
                            dir = 2
                            current = current.left
                            #print("<--")

                else:
                    print("didnt find") #if this occurs error because all our searches are successful only
                    return

        
    def right_rotate(self,prev,dir):
        check.val += 1
        a = self
        b = self.left
        t = b.right       
        self = b
        b.right = a
        a.left = t 
        if(dir == 1):
            prev.right = b
        elif(dir == 2):
            prev.left = b
        if(a.data == root.data):
            check.check1 = b
        return b
        

    def left_rotate(self,prev,dir):
        check.val += 1
        a = self
        b = self.right 
        t = b.left    
        self = b
        b.left = a
        a.right = t
        if(dir == 1):
            prev.right = b
        elif(dir == 2):
            prev.left = b
        if(a.data == root.data):
            check.check1 = b
        return b
    
index = get_index()
root = Node(index[0])
check = Tree(root)
acc_seq = get_accseq()

for i in range(1,len(index)):
    root.insert(index[i])

for x in range(0,len(acc_seq)):
    root.dmt(acc_seq[x])
    root = check.check1
    #print("waiting for debug")
#print(check.val)

def get_dmt():
    return(check.val)