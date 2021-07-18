class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        gap = sorted(costs, key = lambda d : abs(d[0] - d[1]),reverse=True)
        a = []
        b = []
        for person in gap :
            if len(a) < len(gap)/2 and len(b) < len(gap)/2 :
                if person[0] < person[1] :
                    a.append(person[0])
                else :
                    b.append(person[1])
            else :
                if len(a) < len(gap)/2 :
                    a.append(person[0])
                else :
                    b.append(person[1])
        return sum(a) + sum(b)

a = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
print(a.twoCitySchedCost(costs))