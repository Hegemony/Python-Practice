# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        res = []
        while q:
            l = len(q)
            for i in range(l):
                tmp = q.pop(0)
                if tmp != None:
                    res.append(str(tmp.val))  # 这里要用字符串的形式
                    q.append(tmp.left)
                    q.append(tmp.right)
                else:
                    res.append('null')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')
        # print(res)
        i = 0
        if res[i] == 'null':
            return None

        root = TreeNode(int(res[i]))
        q = [root]
        while q:
            tmp = q.pop(0)

            i += 1
            if res[i] != 'null':
                tmp.left = TreeNode(int(res[i]))
                q.append(tmp.left)

            i += 1
            if res[i] != 'null':
                tmp.right = TreeNode(int(res[i]))
                q.append(tmp.right)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

q = [None, None, None]
while q:
    tmp = q.pop(0)
    print(q)