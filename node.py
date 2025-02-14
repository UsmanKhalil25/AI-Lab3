class Node:
    def __init__(
        self,
        state,
        action = None,
        parent = None,
    ):
        self.state = state
        self.action = action
        self.parent = parent