head = {
    "value":11,
    "next": {
                "value":3,
                "next": {
                            "value":23,
                            "next": {
                                        "Value":7,
                                        "next": {
                                                    "Value":4, # tail
                                                    "next":None
                                        }
                            }
                }
    }
}

print(head['next']['next']['value'])

# This will only run with a linked list
# print(my_linked_list.head.next.next.value)