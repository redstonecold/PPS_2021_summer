class NumArray:
    
    def __init__(self, nums):
        length = len(nums)
        '''
        Using a dictionary data structure based on the actual situation (j>=i) will save half the space compared to a two-dimensional array.
        '''
        self.matrix = {}
        for i in range(length):            
            self.matrix[str(i)+str(i)]= nums[i]
        for i in range(length):
            for j in range(i+1,length):
                self.matrix[str(i)+str(j)] = self.matrix[str(i)+str(j-1)] + nums[j]

    
    def sumRange(self, i, j) :
        return self.matrix[str(i)+str(j)]