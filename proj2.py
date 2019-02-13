"""
Name: Mohamed Imran Mohamed Siddique
Course: MCS 275
Assignemt: Project 2
"""
class TernaryTree(object):
      def __init__(self, value):
          
          self.value = value
          self.left = None
          self.right= None
          self.middle = None

      def build_tree(self, new_value):

          for val in new_value:
            if str(val) < self.value:
             if self.left == None:
                self.left = TernaryTree(str(val))
             else:
                self.left.build_tree(str(val))
            elif str(val) == self.value:
             if self.middle == None:
                self.middle = TernaryTree(str(val))
             else:
                self.middle.build_tree(str(val))
            else: #new_value > self.value:
             if self.right == None:
                self.right = TernaryTree(str(val))
             else:
                self.right.build_tree(str(val))


      def traverse_LMRW(self):
          if self.left != None: 
             self.left.traverse_LMRW()  #go a level deeper
          if self.middle != None: 
             self.middle.traverse_LMRW() #go a level deeper
          if self.right != None: 
             self.right.traverse_LMRW() #go a level deeper
          print(self.value)
        
def main():
    L = [4,1,2,2,3,1,0,4,6,5,6,4]
    T = TernaryTree(L[0])
    T.build_tree(L[1:])
    T.traverse_LMRW()
    
    
main()
