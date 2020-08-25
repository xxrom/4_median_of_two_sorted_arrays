from typing import List

class Solution:
  def fillDict(self, d: dict, nums: List[int]):
    for num in nums:
      if num not in d:
        d[num] = 1
      else:
        d[num] = d[num] + 1

  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    ans = 0

    dick = {}
    size = len(nums1) + len(nums2)
    middle = size // 2

    self.fillDict(dick, nums1)
    self.fillDict(dick, nums2)

    print(dick)

    keys = list(dick.keys())
    keys.sort()

    # print(keys)
    count = 0

    one = None
    two = None

    for key in keys:
      print(key)
      count = count + dick[key]

      if count >= middle:
        if one == None:
          # print('one %d' % key)
          one = key

      if count > middle:
        if two == None:
          # print('two %d' % key)
          two = key
          break

    if one == None:
      one = 0
    if two == None:
      two = 0

    if size % 2 == 0:
      ans = (one + two) / 2
    else:
      ans = two

    return ans


my = Solution()
n0 = [2,1]
n1 = [3,4]
trueAns=2.5

ans = my.findMedianSortedArrays(n0, n1)

print("ans", ans, ans == trueAns)

# Runtime: 100 ms, faster than 69.22% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.8 MB, less than 99.25% of Python3 online submissions for Median of Two Sorted Arrays.