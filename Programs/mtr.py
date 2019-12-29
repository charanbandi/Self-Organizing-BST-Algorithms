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

    def mtr(self,key):
        first_enter = 0
        while(check.check1.data != key):
            current = root
            prev = Node(None)
            dir = 0
            while(key != check.check1.data):
                if(key > current.data):
                    if(current.right != None):
                        if(key == current.right.data):
                            if(first_enter == 0):
                                check.val +=1#search successful
                            current.left_rotate(prev,dir)
                            first_enter = 1
                            if(check.check1 == key):
                                check.val += 1#+1 find the node successful
                                return
                            else:
                                break
                        else:
                            prev = current
                            dir = 1
                            current = current.right
                            #print("-->")
                            if(first_enter == 0):
                                check.val += 1 #traversal cost
                
                elif(key < current.data):
                    if(current.left != None):
                        if(key == current.left.data):
                            if(first_enter == 0):
                                check.val +=1#search successful
                            current.right_rotate(prev,dir)
                            first_enter = 1
                            if(check.check1 == key):
                                check.val += 1#+1 find the node successful
                                return
                            else:
                                break
                        else:
                            prev = current
                            dir = 2
                            current = current.left
                            #print("<--")                            
                            if(first_enter == 0):
                                check.val += 1#traversal cost

                else:
                    print("didnt find")#if this occurs error because all our searches are succesfull only
                    return
            
        
    def right_rotate(self,prev,dir):
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
        check.val += 1
        

    def left_rotate(self,prev,dir):
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
        check.val += 1
   
index = get_index()
root = Node(index[0])
check = Tree(root)
acc_seq = get_accseq()

for i in range(1,len(index)):
    root.insert(index[i])

for x in range(0,len(acc_seq)):
    root.mtr(acc_seq[x])
    root = check.check1
#print(check.val)

def get_mtr():
    return(check.val)