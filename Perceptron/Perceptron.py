#-*-coding:utf-8-*-
#!/usr/bin/python
import numpy
import matplotlib.pyplot as plt
class Perceptron:
    #初始化
    def __init__(self,rate,w0,w1,b):
        self.rate = rate
        self.w0 = w0
        self.w1 = w1
        self.b = b
    
    #Model模型
    def model(self,x):
        result = x[2]*(self.w0*x[0]+self.w1 * x[1]+self.b)
        return result

    #Strategy策略
    def isError(self,x):
        result = self.model(x)
        if result <= 0:
            return True
        else:
            return False

    #Algorithm According to loss function partial derivative, get the gradient descent algorithm

    def gradientDescent(self,x):
        self.w0 = self.w0 + self.rate * x[0] * x[2]
        self.w1 = self.w1 + self.rate * x[1] * x[2]
        self.b  = self.b  + self.rate * x[2]

    #Training the model     
    def trainModel(self,data):
        time = 0
        done = False
        while not done:
            for i in range(data.shape[0]):
                if self.isError(data[i]):
                    self.gradientDescent(data[i])
                    lines = self.drawLine(self.w0,self.w1,self.b)
                    time+=1
                    done = False
                    break
                else:
                    done =True
        print time
        print "The final parameters of the model is w0:%d,w1:%d,b:%d" %(self.w0,self.w1,self.b)
    
    # Test the model
    # The output of the model is +1 or -1 
    def testModel(self,x):
        result = self.w0 * x[0] + self.w1 * x[1] + self.b
        if result > 0 :
            return 1
        else :
            return -1
    
    # Draw the line according to coefficient
    def drawLine(self,a,b,c):
        if a == 0 and b == 0:
            x1 = [0,0]; x2 = [0,1]
        elif b == 0:
            x1 = [-c/a,-c/a];x2 = [0,1]
        elif a == 0:
            x1 = [0,1];x2 = [-c/b,-c/b]
        else :
            x1 = [-c/a,0];x2 = [0,-c/b]
        return (x1,x2)
            

def main():
    p = Perceptron(1,0,0,0)
    data = numpy.array([[3,3,1],[4,3,1],[1,1,-1],[2,2,-1],[5,4,1],[1,3,-1]])
    
    plt.figure(1)
    plt.title("Training data set")
    plt.xlabel("x1 axis")
    plt.ylabel("x2 axis")
    plt.xlim(0.0,6)
    plt.ylim(0.0,6)
    
    xTrain = data[:,0]
    yTrain = data[:,1]
    plt.plot(xTrain,yTrain,'or')
    
    p.trainModel(data)    
    lines = p.drawLine(p.w0,p.w1,p.b) 
    plt.plot(lines[0],lines[1])

    testdata = numpy.array([[4,4,-1],[1,2,-1],[1,4,-1],[3,2,-1],[5,5,1],[5,1,1],[5,2,1]])
    xTest = testdata[:,0]
    yTest = testdata[:,1]
    plt.plot(xTest,yTest,'*b')
    
    for r in range(testdata.shape[0]):
            print "input vector(%d,%d) and output:%d, desired output:%d" %(testdata[r][0],testdata[r][1],p.testModel(testdata[r]),testdata[r][2])    

    
    plt.show()
    return 0

if __name__ == '__main__':
    main()
