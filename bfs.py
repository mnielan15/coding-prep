#bfs implementation

def bfs(root):
    stack = [root]
    seen = []
    while stack != []:
        current_node = stack.pop()
        seen.append(current_node)
        for child in current_node.children:
            if child not in seen:
                stack.append(child)
    return seen