* 深度优先搜索（DFS，depth first search）
基于递归，基于一个点，不等一层走完就朝更深度的方向递归到更深层。
代码模板(二叉树）
```
def dfs(node):
    if node in visited:
        # already visited
        return
    visited.add(node)
    
    # process current node
    # ... # logic here
    dfs(node.left)
    dfs(node.right)
```
代码模板(多叉树）

```
visited = set()
def dfs(node,visited):
    visited.add(node)
    
    # process current node
    # ... # logic here
    
    for next_node in node.children():
        if not next_node in visited:
            dfs(next node,visited)
```
非递归模板
```
def dfs(self,tree):
    if tree.root is not None:
        return []
    visited,stack = [],[tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process (node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
```
岛屿数量习题使用DFS，访问过的点标记为0，从4个方向向深处处理找到边界并且消除掉整个岛屿。如果使用BFS方法就使用队列存所有的四个方向的点，处理完一层再处理下一层。
* 广度优先搜索（BFS，breadth first search）
一层层扩散，先访问一层的所有节点，再访问深一层。所以广度优先是不是不能用递归实现？
非递归模板
```
def BFS (graph,start,end):
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```