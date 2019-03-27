
A =[1,2,3,4]
B =[2,3]


if __name__ == '__main__':

    def merge(A,B):
        result = []
        # 分别为A,B两个数组的遍历指针, 初始指向为0索引位置
        i, j = 0, 0
        while i < len(A) and j < len(B):
            print(i, j)
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        result += A[i:]
        result += B[j:]

        return result

    print(merge(A,B))

