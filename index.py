median = 0
x = 0
y = 0
def maximum(nums1, nums2):
    return nums1 if nums1 > nums2 else nums2

def minimum(nums1, nums2):
    return nums1 if nums1 < nums2 else nums2

def findMedianSortedArrays(nums1, n, nums2, m):
    # i: The number of elements to be inserted from nums1 into the first half
    # j: The number of elements to be inserted from nums2 into the first half
    global median, x, y
    minimum_index = 0
    maximum_index = n # length of the smaller array
    while(minimum_index <= maximum_index):
        x = int((minimum_index + maximum_index)/2)
        y = int(((n + m + 1)/2) - x)
        if(x < n and y > 0 and nums2[y - 1] > nums1[x]):
            minimum_index = x + 1
            print("1")
        elif(x > 0 and y < m and nums2[y] < nums1[x - 1]):
            maximum_index = x - 1
            print("2")
        else:
            if(x == 0):
                median = nums2[y - 1]
                print("3")
            elif(y == 0):
                median = nums1[x - 1]
                print("4")
            else:
                median = maximum(nums1[x - 1], nums2[y - 1])
                print("5")
            break

    if((n + m) % 2 == 1):
        print("6")
        return median

    if(x == n):
        print("7")
        return ((median + nums2[y])/2.0)

    if(y == m):
        print("8")
        return ((median + nums1[x]) / 2.0)

    print("9")
    return ((median + minimum(nums1[x], nums2[y])) / 2.0)


nums1 = [6,7,8]
nums2 = [1,2,3,4,5]
n = len(nums1)
m = len(nums2)

if (n < m):
    print(f"The median value is: {findMedianSortedArrays(nums1, n, nums2, m)}")
else:
    print(f"The median value is: {findMedianSortedArrays(nums2, m, nums1, n)}")
