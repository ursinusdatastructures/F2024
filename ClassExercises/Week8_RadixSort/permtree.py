import numpy as np
import matplotlib.pyplot as plt

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def perm(arr, perms=[], idx = 0):
    """
    Print out all N! permutations of the elements in an array
    
    Parameters
    ----------
    arr: list
        This is a list we're permuting in place
    idx: int
        What is the index of the element we are choosing in the array
    """
    if idx == len(arr)-1:
        perms.append(arr.copy())
    else:
        # Assume that everything before idx is fixed, but 
        # we want to take something that's after idx and swap
        # into idx and keep going
        for i in range(idx, len(arr)):
            swap(arr, i, idx) # Swap in arr[i] for arr[idx]
            perm(arr, perms, idx+1) # Keep going recursively to figure out arr[idx+1]
            swap(arr, i, idx) # Swap back, and try something else


class PermNode:
    def __init__(self):
        self.perm = None
        self.left = None
        self.right = None
        self.indices = ""
        self.x = 0
    
    def get_inorder(self, x):
        if self.left:
            self.left.get_inorder(x)
        self.x = x[0]
        x[0] += 1
        if self.right:
            self.right.get_inorder(x)
    
    def draw(self, depth):
        x = self.x
        y = -depth
        plt.scatter([x], [y], 10)
        if not self.left and not self.right:
            plt.text(x, y-0.5, "{}".format(self.perm), rotation=90)
        else:
            if self.left:
                x2 = self.left.x
                y2 = y-1
                plt.plot([x, x2], [y, y2])
                plt.text((x+x2)/2-0.5, (y+y2)/2, self.left.indices)
                self.left.draw(depth+1)
            if self.right:
                x2 = self.right.x
                y2 = y-1
                plt.plot([x, x2], [y, y2])
                plt.text((x+x2)/2-0.5, (y+y2)/2-0.3, self.right.indices)
                self.right.draw(depth+1)




def make_perm_tree(perms, depth=0):
    if len(perms) == 1:
        node = PermNode()
        node.perm = perms[0]
        return node
    else:
        N = len(perms[0])
        for i in range(N):
            for j in range(i+1, N):
                L = []
                R = []
                for p in perms:
                    if p[i] < p[j]:
                        L.append(p)
                    else:
                        R.append(p)
                if abs(len(L) - len(R)) < 2:
                    left = make_perm_tree(L, depth+1)
                    left.indices = "x[{}] < x[{}]".format(i, j)
                    right = make_perm_tree(R, depth+1)
                    right.indices = "x[{}] $\\geq$ x[{}]".format(i, j)
                    node = PermNode()
                    node.left = left
                    node.right = right
                    return node
        print("Found nothing")

class PermTree:
    def __init__(self, N):
        perms = []
        perm(list(range(N)), perms)
        print("There are {} permutations of {} numbers".format(len(perms), N))
        self.root = make_perm_tree(perms)
        self.get_inorder()
    
    def get_inorder(self):
        self.root.get_inorder([0])
    
    def draw(self):
        self.root.draw(0)
        plt.axis("off")


T = PermTree(5)
plt.figure(figsize=(160, 20))
T.draw()
plt.savefig("Tree.svg", facecolor='white', bbox_inches='tight')
