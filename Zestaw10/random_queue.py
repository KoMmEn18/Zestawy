import random

class RandomQueue:

    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        random_index = random.randint(0, len(self.queue) - 1)
        self.queue[-1], self.queue[random_index] = self.queue[random_index], self.queue[-1]
        return self.queue.pop()

    def is_empty(self):
        return not self.queue

    def is_full(self):
        return False

    def clear(self):
        self.queue.clear()
    
    def string_form(self):
        return str(self.queue)