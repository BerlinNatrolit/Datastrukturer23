import random
import time

arr = []
for i in range(0,10000):
    # Driver code to test above
    arr.append(random.randint(1,10000))

start = time.time()
sorted(arr)
end = time.time()

print('Sorted Array in Ascending Order:')
print(arr)
print("Sorted took: " + str(end-start))