'''
  排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''


'''
**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil{
        return head
    }
    slow := head
    fast := head
    pre := head
    
    for fast != nil && fast.Next !=nil{
        pre = slow
        slow = slow.Next
        fast = fast.Next.Next
    }
    pre.Next = nil
    return  merge(sortList(head),sortList(slow))
    
}


func merge(l1,l2 *ListNode)*ListNode{
    if l1 == nil{
        return l2
    }
    if l2 == nil{
        return l1
    }
    if l1.Val <=l2.Val{
        l1.Next = merge(l1.Next,l2)
        return l1
    }else{
         l2.Next = merge(l2.Next,l1)
        return l2
    }
    
}
'''