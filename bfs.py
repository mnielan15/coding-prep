
import TreeCreator
def bfs(root):
    stack = [root]
    seen = set()
    while len(stack) > 0 :
        current_node = stack.pop(0)
        print(current_node.val)
        seen.add(current_node)
        #for child in current_node.children:
        if current_node.left:
            if current_node.left not in seen:
                stack.append(current_node.left)
        if current_node.right:
            if current_node.right not in seen:
                stack.append(current_node.right)
                #stack.append(child)
    return seen

arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
root = TreeCreator.getRoot(arr)
bfs(root)