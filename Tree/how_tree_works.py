
# {
#     "value": 4,
#     "left": None,
#     "right": None
# }

# tree = {
#     "value": 4,
#     "left": {
#                 "value": 3,
#                 "left": None,
#                 "right": None
#             },
#     "right": {
#                 "value": 5,
#                 "left": None,
#                 "right": None
#             },
# }

# Full node
                #         15
                #       /  \
                #      4    16
                #     / \
                #    2   6

# Not a Full node
                #         15
                #       /  \
                #      4    16
                #     / \
                #    2   6
                    #   /
                    #  5

# Full node & Perfect Tree
                #        15
                #       /  \
                #      4    16

# Full node & Perfect Tree & Complete tree
                #        15
                #       /  \
                #      4    18
                #     / \   /\
                #    2   6 16 19

# Complete Tree -> we are filling it from left to right but no longer perfect and full

                #         15
                #       /    \
                #      4      18
                #     / \    / \
                #    2   6  16  19
                #   /
                #  1

# Full node & Perfect Tree & Complete tree 

                #           15
                #         /    \   
                #       /        \
                #      10         19
                #     /\        /   \
                #    6  12     16   21
                #   /\  /\     /\    /\
                #  1  7 9  13 14 17 20 23

# Bio O of Tree
                #         15   -> 2^1 - 1

                #         15
                #       /  \
                #      4    16     -> 2^2 - 1


                #           15
                #         /    \   
                #       /        \
                #      10         19
                #     /\        /   \
                #    6  12     16   21       -> 2^3 - 1



                #           15                  -> 2^1
                #         /    \   
                #       /        \
                #      10         19            -> 2^2
                #     /\        /   \
                #    6  12     16   21          -> 2^3
                #   /\  /\     /\    /\
                #  1  7 9  13 14 17 20 23       -> 2^4 - 1 # 2^4 = 16,  1 is insignificant so we can remove 1  

#  All of this is O(log n)  -> Divide and conquer

# lookup, insert, remove  -> O( log n)
# Insert
