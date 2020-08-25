from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    ans = 0
    merged = nums1[:] + nums2[:]
    print(merged)

    merged.sort()
    print(merged)

    if len(merged) < 2:
      if len(merged) == 0:
        return ans

      return merged[0]


    middle = (len(merged) - 1) // 2

    if len(merged) % 2 == 0:
      ans = (merged[middle] + merged[middle + 1]) / 2
    else:
      ans = merged[middle]

    return ans


my = Solution()
n0 = [2,1]
n1 = [4,3]
trueAns=2.5

ans = my.findMedianSortedArrays(n0, n1)

print("ans", ans, ans == trueAns)

# Runtime: 100 ms, faster than 69.22% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.2 MB, less than 9.36% of Python3 online submissions for Median of Two Sorted Arrays.