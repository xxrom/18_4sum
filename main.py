from typing import List


class Solution:

  def twoSum(self, startIndex, target, c, d):
    # a + b = target
    seen = set()

    for i in range(startIndex, self.size):

      diff = target - self.nums[i]

      if diff in seen:
        # print('found solution', c, d, diff, self.nums[i])
        self.ans.add((c, d, diff, self.nums[i]))

      seen.add(self.nums[i])

  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

    nums.sort()
    self.nums = nums

    self.size = len(self.nums)
    self.ans = set()

    for i in range(self.size - 3):
      # Skip same values for first letter
      if i > 0 and self.nums[i - 1] == self.nums[i]:
        continue

      for j in range(i + 1, self.size - 2):
        # Skip same values for second letter
        if j > i + 1 and self.nums[j - 1] == self.nums[j]:
          continue

        c = self.nums[i]
        d = self.nums[j]

        twoSumTarget = target - c - d
        startIndex = j + 1

        self.twoSum(startIndex, twoSumTarget, c, d)

    # convert to list from List[set(int)]
    return [list(setItem) for setItem in list(self.ans)]


my = Solution()

n = [-2, -1, -1, 1, 1, 2, 2]
t = 0
trueAns = [[-2, -1, 1, 2], [-1, -1, 1, 1]]

ans = my.fourSum(n, t)

print("ans", ans, ans == trueAns)
'''
a + b + c + d = target

a + b = target - c - d

[1, 0, -1, 0, -2, 2]
[-2, -1, 0, 0,1, 2]

a + b + c + e = t

a + b = t - c - e


for (i) first letter (c)
  for (j) second letter (e)
    twoSum () {
      faind a + b = target (target = t - c - e)
    }
'''
