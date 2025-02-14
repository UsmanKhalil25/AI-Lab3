from node import Node
from enum import Enum

class FrontierType(Enum):
    QUEUE = 1
    STACK = 2
    
class Frontier:
    def __init__(self, frontier_type: FrontierType):
        self.frontier = []
        self.frontier_type = frontier_type

    def __len__(self):
        return len(self.frontier)

    def add(self, item):
        self.frontier.append(item)

    def remove(self):
        if self.frontier_type == FrontierType.STACK:
            return self.frontier.pop()
        elif self.frontier_type == FrontierType.QUEUE:
            return self.frontier.pop(0)

    def is_empty(self):
        return len(self.frontier) == 0