'''

cosine similarity:
A measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. It is commonly used in various applications such as text analysis, recommendation systems, and clustering.

'''

def cosine_similarity(v1, v2):

    '''
    formula, dot_product escalar: A * B = (x1 * y1) + (x2 * y2) 
    '''
    dot_product = sum(
        [a * b for a, b in zip(v1, v2)]
    )
    print(f"dot_product: {dot_product}")


    print("magnitude of v1: ", [a**2 for a in v1])
    print("magnitude of v2: ", [a**2 for a in v2])

    magnitude = (
        sum([a**2 for a in v1]) *
        sum([a**2 for a in v2])
        ) ** 0.5
    print(f"magnitude of v1 and v2: {magnitude}")

    return dot_product / magnitude

result = cosine_similarity([2, 4], [4, 2])
print(f"cosine similarity: {result}")

'''
zip: it is a built-in function in Python that takes multiple iterable objects (like lists or tuples) as input and returns an iterator of tuples, where each tuple contains elements from the input iterables that are at the same index.

what is an iterator of tuples: An iterator of tuples is an object that allows you to traverse through a sequence of tuples one at a time. Each tuple contains elements from the input iterables that are at the same index.


'''
print("\ntesting zip: ")
for a, b, c in zip([1, 2], [3, 4], [6, 8]):
    print('a:', a, end=' ')
    print('b:', b, end=' ')
    print('c:', c, end=' ')
  
