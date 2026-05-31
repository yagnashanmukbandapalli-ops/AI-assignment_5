import random
import math

class TreeNode:
    def __init__(self):
        self.score = 0
        self.count = 0
        self.nodes = []

    def calculate_uct(self, total_count):
        if self.count == 0:
            return float("inf")

        exploitation = self.score / self.count
        exploration = math.sqrt(
            math.log(total_count) / self.count
        )

        return exploitation + exploration


parent = TreeNode()

for i in range(5):
    node = TreeNode()

    node.score = random.randint(1, 10)
    node.count = random.randint(1, 10)

    parent.nodes.append(node)

parent.count = sum(child.count for child in parent.nodes)

selected = max(
    parent.nodes,
    key=lambda child: child.calculate_uct(parent.count)
)

print("Best Child:")
print("Wins:", selected.score)
print("Visits:", selected.count)
