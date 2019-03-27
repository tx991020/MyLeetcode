class Node(object):
    """链表节点实现"""

    def __init__(self,item):
        """创建一个节点"""
        self.pre=None
        self.next=None
        self.item=item

class DLinkList(object):
    """双向链表的实现"""
    def __init__(self):
        self._head=None

    def is_empty(self):
        """链表是否为空"""
        return self._head==None

    def length(self):
        """链表长度"""
        count=1
        if not self._head:
            return 0
        cur=self._head
        while cur.next!=None:
            count+=1
            cur=cur.next
        return count


    def travel(self):
        """遍历链表"""
        if not self._head:
            print("空链表")
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        """链表头部添加元素"""
        node=Node(item)
        if self.is_empty():
            self._head=node
            return
        node.next=self._head
        self._head=node
        self._head.next.pre=node



    def append(self,item):
        """链表尾部添加元素"""
        node=Node(item)
        if self.is_empty():
            self._head = node
        cur=self._head
        while cur.next!=None:
            cur=cur.next
        cur.next=node
        node.pre=cur
        node.next=None

    def insert(self,pos,item):
        """在指定位置添加元素"""
        if pos<=0:
            self.add(item)
            return
        elif pos>self.length()-1:
            self.append(item)
            return
        node = Node(item)
        cur_p=self._head
        cur=cur_p.next
        while pos:
            cur_p=cur
            cur=cur.next
            pos-=1

        node.pre=cur_p
        cur_p.next=node
        node.next=cur

    def remove(self,item):
        """删除节点"""
        if not self._head:
            print("空链表")
            return
        cur= self._head
        while cur.next!=None:
            if cur.item==item:
                #要删除的是第一个结点
                if cur.pre==self._head:
                    cur.next.pre=None
                    self._head=cur.next
                    return
                # 要删除的是中间结点
                else:
                   cur.pre.next=cur.next
                   cur.next.pre=cur.pre
                   cur.next=None
                   cur.pre=None
                   return
            cur=cur.next
        #要删除的是尾结点
        if cur.item==item:
            cur.pre.next=None
            cur.pre=None
        else:
            print("未找到需要删除的元素")

    def search(self,item):

        cur = self._head
        while cur!=None:
            if cur.item==item:
                return True
            cur=cur.next

        return False



if __name__ == "__main__":
    ll = DLinkList()
    ll.add(5)

    ll.add(2)
    ll.add(4)
    ll.add(6)

    ll.travel()
    print(1111111)
    ll.insert(-1,10)
    ll.travel()
