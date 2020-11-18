"""
1) Use unidirectional edges to represent parent-child relationship
ancestors is a list of edges (parent, child)
2) For this problem, it may be useful to designate an edge as (parent <-- child)
Earlier ancestors have more edges from start node
3) Return the earliest ancestor
- Breadth-first traversal of ancestors to get earliest ancestors
- Use queue to evaluate generation by generation
- If generation has no parents, return ancestor with lowest id
- If no parents, return -1
"""
from collections import deque


def earliest_ancestor(ancestors, starting_node):

    q = deque([[starting_node]])

    while len(q) > 0:
        gen = q.popleft()

        new_gen = list()

        for node in gen:
            new_gen.extend([parent for parent, child in ancestors if child == node])

        if new_gen:
            q.extend([new_gen])
        else:
            return min(gen) if min(gen) != starting_node else -1

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (11, 8), (8, 9), (4, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 5))
