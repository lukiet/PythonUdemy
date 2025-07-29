marks = [22,98,59,34,56,78,12,34,56,78,90]

our_iter = iter(marks)

print(our_iter)

print(next(our_iter))

print(next(our_iter))

print(our_iter.__next__())

print(our_iter.__next__())

# Creating a custom iterator class

class PowOfTwo:
    """An iterator that generates powers of two up to a specified maximum."""
    def __init__(self, max=0):
        self.max = max
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.max:
            result = 2 ** self.num
            self.num += 1
            return result
        else:
            raise StopIteration

print(PowOfTwo.__doc__)
a = PowOfTwo(9)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))


