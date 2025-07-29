marks = [22,98,59,34,56,78,12,34,56,78,90]

our_iter = iter(marks)

print(our_iter)

print(next(our_iter))

print(next(our_iter))

print(our_iter.__next__())

print(our_iter.__next__())
