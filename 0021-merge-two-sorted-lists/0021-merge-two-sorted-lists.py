# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merge_head= ListNode()
        mnode = merge_head

        if (not list1 and list2):
            return list2
        elif (list1 and not list2):
            return list1
        elif (not list1 and not list2):
            return None
        elif (not list1 or not list2):
            return merge_head


        
        
        
        
        if (list1.val == list2.val):
            mnode.val = list1.val
            list1 = list1.next
        elif (list1.val < list2.val):
            mnode.val = list1.val
            list1 = list1.next
        elif (list2.val < list1.val):
            mnode.val = list2.val
            list2 = list2.next


        
        while (list1 is not None) and (list2 is not None):
            if (list1.val == list2.val):
                mnode.next = ListNode(list1.val)
                mnode.next.next = ListNode(list1.val)
                mnode = mnode.next.next
                list1 = list1.next
                list2 = list2.next
            
            elif (list1.val < list2.val):
                mnode.next = ListNode(list1.val)
                mnode = mnode.next
                list1 = list1.next

            elif (list2.val < list1.val):
                mnode.next = ListNode(list2.val)
                mnode = mnode.next
                list2 = list2.next

        while (list1 or list2):        
            if (list1 is not None):
                mnode.next = ListNode(list1.val)
                mnode = mnode.next
                list1 = list1.next
            elif(list2 is not None):
                mnode.next = ListNode(list2.val)
                mnode = mnode.next
                list2 = list2.next

        return merge_head