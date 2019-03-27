
class ListNode(object):
    def __init__(self, x,data=None):
        self.val = x
        self.next =data


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        result = ListNode(-1)
        cur = result
        print(cur.next)
        p = list()
        x = 0
        for i in lists:
            while i:
                heapq.heappush(p, (i.val, x, i))
                i = i.next
                x += 1
        while p:
            cur.next = heapq.heappop(p)[1]
            cur = cur.next

        return result.next




if __name__ == '__main__':

    c = ListNode(1,ListNode(4,ListNode(5)))
    d = ListNode(1,ListNode(3,ListNode(4)))
    e = ListNode(2,ListNode(6))

    b = [c,d,e]
    a = Solution().mergeKLists(b)
    print(a)