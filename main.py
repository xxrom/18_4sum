from typing import List


class Solution:

  def twoSum(self, nums, startIndex, target, c, d):
    # time O(N)
    # memory O(N)
    # a + b = target
    # a = target - b

    seen = set()

    for i in range(startIndex, len(nums)):

      diff = target - nums[i]

      if diff in seen:
        print('found solution', c, d, diff, nums[i])
        self.ans.add((c, d, diff, nums[i]))

      seen.add(nums[i])

  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    # time O(N*N)
    # memory O(N)

    # a + b + c + d = target

    size = len(nums)
    self.ans = set()

    for i in range(size):
      for j in range(i + 1, size):
        c = nums[i]
        d = nums[j]

        twoSumTarget = target - c - d
        startIndex = j + 1
        self.twoSum(nums, startIndex, twoSumTarget, c, d)

    self.ans = [list(x) for x in list(self.ans)]

    return list(self.ans)


my = Solution()
n = [1, 0, -1, 0, -2, 2]
t = 0

trueAns = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

ans = my.fourSum(n, t)

print("ans", ans, ans == trueAns)
'''
a + b + c + d = target

a + b = target - c - d

[1, 0, -1, 0, -2, 2]
[-2, -1, 0, 0,1, 2]

a + b + c + e = t

a + b = t - c - e

a + b = t - c

{}
-2, 2

{-2, 2}
-1, 1

{-2, 2, -1, 1}
0, 0
0 + 0 = 0 - c - e
a + b - t = -c - e

c + (a + b - t) = -e

# find c / -e in { -2, 2, -1, 1}
'''
