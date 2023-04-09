from segment_tree import SegmentTree

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = SegmentTree(arr)

a = t.query(3, 8, "sum")
print("The sum of this range is: ", a)
