from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph=defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])

        for key in graph:
            graph[key].sort(reverse=True)

    
        stack=['JFK']
        result=[]

        while stack:
            node=stack[-1]
            if node in graph and graph[node]:
                nei=graph[node].pop()
                stack.append(nei)
            else:
                stack.pop()
                result.append(node)
        
        return result[::-1]
