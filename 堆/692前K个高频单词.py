
import collections
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)

        heap = [(-freq, word) for word, freq in count.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == '__main__':
    a = Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2)
    print(a)


    