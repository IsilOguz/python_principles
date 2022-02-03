"""
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""
def all_equal(a):
    for i in a:
        if i != a[0]:
            return False
            
    return True