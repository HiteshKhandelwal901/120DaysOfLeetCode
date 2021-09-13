#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    in place merging of two binary trees : R1 and R2 - > Merged R1
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        #if both nodes exists in both trees take the sum and update it in root
        if root1 and root2:
            root1.val = root1.val + root2.val
            #recurse to the left subtree of root1. Ex: 10 is say curr root for root1 amd 20 for roo2, then 10.left = recurse(root1 = 10.left, root2 = 20.left)
            root1.left = self.mergeTrees(root1.left, root2.left)
            #once done with left recurse, recurse to the right subtree of root1
            root1.right = self.mergeTrees(root1.right, root2.right)

        #when root1's subtree exists but root2's subtree doesnt exists then do nohtin, just append the same subtree to the calling parent root tree.
        elif root1 and root2==None:
            return root1
        #if root1's subtree doesnt exist but root2's does, then , return root2's subtree to the calling parent root tree.
        else:
            return root2

        #once done return root1 as your final merged tree
        return root1
