from typing import Optional

from self import self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cursor = head

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next

            cursor = cursor.next

        if list1 != None:
            cursor.next = list1
        else:
            cursor.next = list2

        return head.next


print(Solution.mergeTwoLists(self, list1, list2))


