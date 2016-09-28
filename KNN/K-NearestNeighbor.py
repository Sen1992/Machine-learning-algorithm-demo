#-*-coding=UTF-8-*-
#/usr/bin/python
import numpy as np
import math
class KD_node:
    def __init__(self,point=None,split=None,Left=None,Right=None):
        """
        point:数据点
        split: 划分域
        """
        self.point = point
        self.split = split
        self.Left = Left
        self.Right = Right

def createKDTree(root,data):
    """
    root:当前树的根节点
    return :构造树的KDTree的树根
    """
    print "data:",data 
    Len = np.asarray(data).shape[0]
    if Len == 0:
        return 
    print "Len ",Len

    # The dimension of data point
    dim = np.asarray(data).shape[1]
    # The selected divided domain
    print "Dim:",dim

    #获得数据集中每个维度的方差
    variance = [np.asarray(data)[:,i].var() for i in range(dim)]
    print "Variance:",variance

    
    
    
    #将numpy的矩阵转成列表,可获得一些相关API,然后调用列表的index()函数，返回最大方差的索引
    split = variance.index(max(variance))
    print "Split ",split
    
#    median = sorted(data[:,split])[Len/2]
 #   point = data[data[:,split].tolist().index(median)]
  #  print "Point:"
   # print point
    #对列表进行按第split列排序，关键点key
    data.sort(key = lambda x : x[split])
    ##取中位数
    point = data[Len/2]
    print "Point:",point

    root = KD_node(point,split)
    root.Left = createKDTree(root.Left,data[0:Len/2])
    root.Right = createKDTree(root.Right,data[Len/2+1:Len])
    
    return root

def preorder(root):
    if root is None:
        return 
    print root.point,root.split
    
    if root.Left:
        preorder(root.Left)
    if root.Right:
        preorder(root.Right)

def inorder(root):
    if root is None:
        return
    if root.Left:
        inorder(root.Left)
    print root.point,root.split
    if root.Right:
        inorder(root.Right)


def findNN(root,query):
    NN = root.point
    min_dist = computerDist(query,NN) 
    
    # record the node visited
    nodeList = []
    
    temp_root = root
    while temp_root:
        # 模拟栈，记录经过的点
        nodeList.append(temp_root)
        currentDist = computerDist(query,temp_root.point)
        if min_dist > currentDist:
            min_dist = currentDist
            NN = temp_root.point

        # 找到查询点所在的区域
        if query[temp_root.split] < temp_root.point[temp_root.split] :
            temp_root = temp_root.Left
        else :
            temp_root = temp_root.Right
           
    
    # 计算查询点的到分割平面的距离，与当前最短距离相比，判断是否进去相邻平面
    # 回溯算法
    while nodeList :
        backPoint = nodeList.pop()
        if abs(query[backPoint.split]-backPoint.split) < min_dist:
            # 因为距离比最短距离小，因此要进入相邻空间搜索，接下来判断进入左还是右空间
            if query[backPoint.split] < backPoint.point[backPoint.split] :
                temp_root = backPoint.Right
            else :
                temp_root = backPoint.Left

            if temp_root : 
                nodeList.append(temp_root)
                currentDist = computerDist(query,temp_root.point)
                if currentDist < min_dist:
                    min_dist = currentDist
                    NN = temp_root.point
    
#    print NN,min_dist
    return NN,min_dist            

def computerDist(p1,p2):
    result = 0.0
    for i in range(len(p1)):
        result = result + (p1[i]-p2[i])**2
    return math.sqrt(result)

def KNN(list,query):
    min_dist = 1000.0
    NN = list[0]
    for i in list:
        dist = computerDist(query,i)
        if dist < min_dist:
            NN = i
            min_dist = dist
    
    return NN,min_dist




def main():
    data = [[2,1,3],[2,3,7],[1,4,4],[2,4,5],[3,1,4],[0,5,7],[6,1,4],[4,3,4],[4,0,6],[5,2,5],[7,1,6]]
    root = createKDTree(None,data)
    print "先序遍历"
    preorder(root)
    print "中序遍历"
    inorder(root)
    queryList = [[3,4,2],[1,2,3],[3,2,7],[1,6,2],[3,3,4]]
    for query in queryList:
        (NearestPoint,Dist) = findNN(root,query)
        (validateNN,validateDist) = KNN(data,query)
        print "The nearest point of ",query," is",NearestPoint,"its distince is ",Dist
        print "Validate is ",validateNN,"Dist is",validateDist
        print ""    
    
if __name__ == '__main__':
    main()







