import timing

count = 10**6

timing.log('Start append')
nums = []
for i in range(count):
    nums.append(i)
nums.reverse()
timing.endlog()
print nums[:20]

timing.log('Start insert')
nums = []
for i in range(count):
    nums.insert(0, i)
timing.endlog()
print nums[:20]

