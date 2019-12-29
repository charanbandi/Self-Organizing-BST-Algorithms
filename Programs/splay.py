from Req_Func import get_index, get_accseq
class Node:
    #Node Initialization
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    #Tree Initializations
    def __init__(self):
        self.root = Node(None)
        self.peer = Node(None)#
        self.val = 0

    #inserting into tree randoly creating a BST
    def insert(self, key):
        if (self.root.key == None):
            self.root = Node(key)
            return

        n = Node(key)
        n = self.root
        while(n.key != key):
            if(key < n.key):
                if(n.left is None):
                    n.left = Node(key)
                    n = n.left
                else:
                    n = n.left
            elif(key > n.key):
                if(n.right is None):
                    n.right = Node(key)
                    n = n.right
                else:
                    n = n.right

    #Searching the key in the tree and splay it to root along the path
    def splay(self, key):
        if(self.root == key):
            return
        walker = Node(None)
        walker = self.root
        while(walker.key != key):
            if(key > walker.key):
                walker = walker.right
                self.val += 1#cost to find node
            elif(key < walker.key):
                walker = walker.left
                self.val += 1#cost to find node
        
        leftinit = self.peer
        rightinit = self.peer
        temp = self.root
        self.peer.left = None
        self.peer.right = None
        while True:
            if key < temp.key:
                if temp.left == None:
                    break
                if key < temp.left.key:
                    #right rotate
                    current = temp.left
                    temp.left = current.right
                    current.right = temp
                    temp = current
                    self.val += 1#rotate1 cost
                    if temp.left == None:
                        break
                rightinit.left = temp
                rightinit = temp
                temp = temp.left
                self.val += 1#rotate2 cost
            elif key > temp.key:
                if temp.right == None:
                    break
                if key > temp.right.key:
                    #left rotate
                    current = temp.right
                    temp.right = current.left
                    current.left = temp
                    temp = current
                    self.val += 1#rotate3 cost
                    if temp.right == None:
                        break
                leftinit.right = temp
                leftinit = temp
                temp = temp.right
                self.val += 1#rotate4 cost
            else:
                break
        #final linking 
        leftinit.right = temp.left
        rightinit.left = temp.right
        temp.left = self.peer.right
        temp.right = self.peer.left
        self.root = temp

def get_splay():
    index = get_index()
    root = SplayTree()
    for i in range(len(index)):
        root.insert(index[i])

    acc_seq = get_accseq()
    for i in range(len(acc_seq)):
        root.splay(acc_seq[i])
    #print(root.val) #printing the total count after splays
    return(root.val)
