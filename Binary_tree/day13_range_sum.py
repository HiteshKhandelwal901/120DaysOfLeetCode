# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.summ = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #if the root exists
        if root:
            #if the low is greater than the root then the entire left subtree will be outside range (< low) as wll
            if low > root.val:
                #repeat the seach for range in the right subtree
                return(self.rangeSumBST(root.right, low, high))
            #if the high is < root than all the values in right subtree will be outside range (> high)
            if high < root.val:
                #recurse in the left subtree
                return(self.rangeSumBST(root.left, low, high))

            #if both the condition on the top fails => the node is in range and add the sum
            self.summ = self.summ +root.val

            #since the node is range you cannot say anything about bith left and right subtree, hence recurse both.
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
        #print("result = ", self.result)
        return self.summ
