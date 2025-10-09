'''

cosine similarity:
A measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. It is commonly used in various applications such as text analysis, recommendation systems, and clustering.

'''

def cosine_similarity(vec1, vec2):

    '''
    formula, dot_product escalar: A * B = (x1 * y1) + (x2 * y2) 
    '''
    dot_product = sum(
        [a * b for a, b in zip(vec1, vec2)]
    )
    print(f"dot_product: {dot_product}")

cosine_similarity([5, 1], [6, 2])


'''
zip: it is a built-in function in Python that takes multiple iterable objects (like lists or tuples) as input and returns an iterator of tuples, where each tuple contains elements from the input iterables that are at the same index.

what is an iterator of tuples: An iterator of tuples is an object that allows you to traverse through a sequence of tuples one at a time. Each tuple contains elements from the input iterables that are at the same index.


'''
print("testing zip")
for a, b, c in zip([1, 2], [3, 4], [6, 8]):
    print('a:', a, end=' ')
    print('b:', b, end=' ')
    print('c:', c, end=' ')
  
