import timing

count = 10**6
nums = []
timing.log('Start append')
for i in range(count):
    nums.append(i)
nums.reverse()
timing.endlog()

timing.log('Start insert')
nums = []
for i in range(count):
    nums.insert(0, i)
timing.endlog()

