# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Understand:
    Input: 2 heads
    Output: is 1 head node pointing to the merged list
    Edge cases: if one is empty just return the other, if both are empty then return an empty list

    Plan:
    result = none
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    else:
        return list1
    
    if list1.val >= list2.val:
        result = list2
    else:
        result = list1
    
    while list1 or list2:
        if list1 and list2:
            if list1 > list2:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next
        elif list1:
                result.next = list2
                list2 = list2.next
        else:
            result.next = list1
                list1 = list1.next
    return result
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        dummy = ListNode()
        dummy.next = result

        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    result.next = list2
                    list2 = list2.next
                    result = result.next
                else:
                    result.next = list1
                    list1 = list1.next
                    result = result.next
            elif list1:
                    result.next = list1
                    list1 = list1.next
                    result = result.next
            else:
                result.next = list2
                list2 = list2.next
                result = result.next
        return dummy.next.next
        