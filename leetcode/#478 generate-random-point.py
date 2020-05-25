class Solution:
    
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self):
        import numpy as np


        xx = 2*self.radius*(np.random.rand()-0.5) + self.x
        yy = 2*self.radius*(np.random.rand()-0.5) + self.y

        
        print(xx,yy)

        if (xx-self.x)**2 + (yy-self.y)**2 <= self.radius:
            return [xx,yy]
        else:
            return self.randPoint()

a = Solution(1,0,0)
print(a.randPoint())





        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()