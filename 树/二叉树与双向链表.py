


'''
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};*/
class Solution {
public:
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        //用于记录双向链表尾结点
        TreeNode* pLastNodeInList = NULL;

        //开始转换结点
        ConvertNode(pRootOfTree, &pLastNodeInList);

        //pLastNodeInList指向双向链表的尾结点，我们需要重新返回头结点
        TreeNode* pHeadOfList = pLastNodeInList;
        while(pHeadOfList != NULL && pHeadOfList->left != NULL){
            pHeadOfList = pHeadOfList->left;
        }
        return pHeadOfList;
    }

    void ConvertNode(TreeNode* pNode, TreeNode** pLastNodeInList){
        //叶结点直接返回
        if(pNode == NULL){
            return;
        }
        TreeNode* pCurrent = pNode;
        //递归左子树
        # if(pCurrent->left != NULL)
        #     ConvertNode(pCurrent->left, pLastNodeInList);

        //左指针
        pCurrent->left = *pLastNodeInList;
        //右指针
        if(*pLastNodeInList != NULL){
            (*pLastNodeInList)->right = pCurrent;
        }
        //更新双向链表尾结点
        *pLastNodeInList = pCurrent;
        //递归右子树
        # if(pCurrent->right != NULL){
        #     ConvertNode(pCurrent->right, pLastNodeInList);
        # }
    }
};
'''