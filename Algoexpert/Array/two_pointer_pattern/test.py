from solution1 import two_sum as ts1
from solution2 import two_sum as ts2
from solution3 import two_sum as ts3

#testcase 1
nums = [2,7,11,15]
target = 9
assert ts1(nums,target) == [2,7]
assert ts2(nums,target) == [7,2]
assert ts3(nums,target) == [2,7]

#testcase 2
nums = [3,2,4]
target = 6
assert ts1(nums,target) == [2,4]
assert ts2(nums,target) == [4,2]
assert ts3(nums,target) == [2,4]


#testcase 3
nums = [3,3]
target = 6
assert ts1(nums,target) == [3,3]
assert ts2(nums,target) == [3,3]
assert ts3(nums,target) == [3,3]

#testcase 4
nums = [3,2,3]
target = '6'
try:
    ts1(nums,target)
except Exception as e:
    assert str(e) == "Target must be of type int."

try:
    ts2(nums,target)
except Exception as e:
    assert str(e) == "Target must be of type int."

try:
    ts3(nums,target)
except Exception as e:
    assert str(e) == "Target must be of type int."