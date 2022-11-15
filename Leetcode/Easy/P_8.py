"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

    Example 1:

        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

    Example 2:

        Input: list1 = [], list2 = []
        Output: []

    Example 3:

        Input: list1 = [], list2 = [0]
        Output: [0]
"""
#bro this is not it
#! we have to use a bloody linked list smh
list1 = [7,2,5,1]
list2 = [4,6,3,8]
list3 = list1 + list2
list3.sort()
print(list3)