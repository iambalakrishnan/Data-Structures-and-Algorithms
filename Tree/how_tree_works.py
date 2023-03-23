
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