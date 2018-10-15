class Solution:

    def is_cyclic_graph(self, start, end):
        import Queue

        n = 0
        for i in start:
            n = max(n, i)
        for i in end:
            n = max(n, i)
        m = len(start)
        n += 1
        G = [[] for i in range(n) ]
        D = [0 for i in range(n) ]
        for i in range(m):
            G[start[i]].append(end[i])
            D[end[i]] += 1
        queue = Queue.Queue()
        for i in range(n):
            if D[i] == 0:
                queue.put(i)
        while(queue.empty() == False):
            u = queue.get()
            for i in G[u]:
                D[i] -= 1
                if(D[i] == 0):
                    queue.put(i)
        for i in range(n):
            if D[i] != 0:
                return True
        return False