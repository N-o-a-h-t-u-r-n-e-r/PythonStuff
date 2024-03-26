import numpy as np

nums = np.array([2, 7, 11, 15])
target = 9

#Empty Dictionary
hashMap = {}

#Loop through the array once
for i in range(len(nums)):
    #checks if the target minus the current value is in the hashmap, if so then we have the indexes for the answer
    if(target - nums[i]) in hashMap:
        print(nums[hashMap[target-nums[i]]], nums[i])
    #Otherwise add the index to the hashmap with the key being the value at i
    else:
      hashMap[nums[i]] = i;  
