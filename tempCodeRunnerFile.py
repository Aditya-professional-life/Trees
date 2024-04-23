    if root == None:
        return 
    q = deque()
    q.append(root)

    while len(q)>0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            print(curr.key,end = " ")
            if curr.left is not None:
                q.append(curr.left)

            if curr.right is not None:
                q.append(curr.right)


        print()




