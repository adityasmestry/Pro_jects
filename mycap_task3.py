#Different set of operations.
setA={1,2,3,4,5}
setB={4,5,6,7,8}
union_set=setA.union(setB)
print(f'Union of A and B: {union_set}')
intersection_set=setA.intersection(setB)
print(f'Intersection of A and B: {intersection_set}')
difference_set=setA.difference(setB)
print(f'Difference of A and B: {difference_set}')
symmetric_diff_set=setA.symmetric_difference(setB)
print(f'Symmetric difference of A and B: {symmetric_diff_set}')
