# 16.25 LRU Cache
# Design and build a 'least recently used' cache, which evicts the least recently used item. The cache should map from
# keys to values (allowing you to insert and retrieve a value associated with a particular value) and be initialized
# with a max size. When it is full, it should evict the least recently used item. You can assume the keys are integers
# and the values are strings.

# The solution involves combining hash maps with linked list.


class Cache:

    def __init__(self, max_size):
        self.hash_map = {}
        self.listHead = None
        self.listTail = None
        self.max_size = max_size

    class LinkedNode:
        def __init__(self, key, value):
            self.nextNode = None
            self.prevNode = None
            self.key = key
            self.value = value

    def get_value(self, key):
        if key in self.hash_map:
            node = self.hash_map[key]
        else:
            return None

        # Update the node to be the least recently used.
        if node != self.listHead:
            self._remove_from_linked_list(node)
            self._insert_at_front_of_linked_list(node)

        return node.value

    def _remove_from_linked_list(self, node):
        if node is None:
            return False

        if node.prevNode:
            node.prevNode.nextNode = node.nextNode

        if node.nextNode:
            node.nextNode.prevNode = node.prevNode

        if node == self.listHead:
            self.listHead = node.nextNode
        if node == self.listTail:
            self.listTail = node.prevNode

    def _insert_at_front_of_linked_list(self, node):
        if node is None:
            return False

        if self.listHead:
            node.nextNode = self.listHead
            self.listHead.prevNode = node
            self.listHead = node
        else:
            self.listHead = node
            self.listTail = node

    def remove_key(self, key):
        if key in self.hash_map:
            node = self.hash_map[key]
        else:
            return False

        self._remove_from_linked_list(node)
        self.hash_map.pop(key)

        return True

    def set_key_value(self, key, value):
        if key in self.hash_map:
            self.hash_map.pop(key)

        node = self.LinkedNode(key, value)
        if len(self.hash_map) >= self.max_size and self.listTail:
            self.hash_map.pop(self.listTail.key)
            self._remove_from_linked_list(self.listTail)

        self._insert_at_front_of_linked_list(node)
        self.hash_map[key] = node

    def __str__(self):
        node = self.listHead
        my_str = ''
        while node:
            my_str += 'key: ' + str(node.key) + ' value: ' + str(node.value) + '\n'
            node = node.nextNode
        return my_str


if __name__ == '__main__':
    # Create LRU cache object of size e.g. 3 and perform few operations.
    # Print out final result and check if works fine.
    # Example below would print nodes 2 -> 4 -> 3
    cache = Cache(3)
    cache.set_key_value(1, 1)
    cache.set_key_value(2, 2)
    cache.set_key_value(3, 3)
    cache.set_key_value(4, 4)
    cache.get_value(2)

    print cache
