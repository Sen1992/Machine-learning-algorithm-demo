#-*-coding=UTF-8-*-
#/usr/bin/python
import numpy as np
import os
try:
    import cpickle as pickle
except:
    import pickle

class Bayes():
    def __init__(self,data,label):
        
        if os.path.isfile("prior.txt") and os.path.isfile("feature.txt") and os.path.isfile("category.txt"):
            print "不需要再计算，直接从本地读取"
            
            with open("prior.txt","r") as f:
                prior = f.read()
            self.priorProbability = pickle.loads(prior)
                         
            with open("feature.txt","r") as f:
                feature = f.read()
            self.FeatureDict = pickle.loads(feature)
            
            with open("category.txt","r") as f:
                category = f.read()
            self.Categories = pickle.loads(category)
        
        else:
            print "文件不存在，需要从新计算"

            #贝叶斯估计，为了避免极大似然估计，要估计的概率为0的情况，我们采用np.ones(range)来初始化
            dataMat = np.asarray(data)
            SampleNum = dataMat.shape[0]
            X1List = dataMat[:,0]
            X2List = dataMat[:,1]

            self.Categories = list(set(label))
            CNum = len(self.Categories)
            CategoryDict = dict(zip(self.Categories,np.ones(CNum,dtype=np.float)))
                
            for i in label:
                CategoryDict[i] +=1
            
            self.X1Set = list(set(X1List))
            self.X2Set = list(set(X2List))
            X1Num = len(self.X1Set)
            X2Num = len(self.X2Set)
            
            X1Dict = dict(zip(self.X1Set,np.ones(X1Num,dtype=np.float))) 
            X2Dict = dict(zip(self.X2Set,np.ones(X2Num,dtype=np.float)))

            self.priorProbability = dict()
            # 存储先验概率，即每个分类的概率
            for i in CategoryDict.keys():
                self.priorProbability[i] = round(CategoryDict.get(i)/(SampleNum+CNum*1),3)
            
            # 记录在某一类别下条件概率
            self.FeatureDict = {}        
            for i in self.Categories:
                self.FeatureDict[i] = dict(X1Dict.items()+X2Dict.items())
            
            for i in range(SampleNum):
                for j in self.Categories:
                    if label[i]==j:
                        self.FeatureDict[j][X1List[i]] +=1
         
            for i in range(SampleNum):
                for j in self.Categories:
                    if label[i]==j:
                        self.FeatureDict[j][X2List[i]] +=1
            
            ## 因为上面的初始值是1
            for i in self.X1Set:
                for j in self.Categories:
                    self.FeatureDict[j][i] = round(self.FeatureDict[j][i]/(CategoryDict.get(j)-1+X1Num*1),3)
                    
            for i in self.X2Set:
                for j in self.Categories:
                    self. FeatureDict[j][i] = round(self.FeatureDict[j][i]/(CategoryDict.get(j)-1+X2Num*1),3)
            
            priorTXT = pickle.dumps(self.priorProbability)
            featureTXT = pickle.dumps(self.FeatureDict)
            categoryTXT = pickle.dumps(self.Categories)

            with open("prior.txt","w") as f:
                f.write(priorTXT)
            with open("feature.txt","w") as f:
                f.write(featureTXT)
            with open("category.txt","w") as f:
                f.write(categoryTXT)
                
    def predict(self,data):
        d = np.asarray(data)
        pList = []
        for i in self.Categories:
            temp = self.FeatureDict.get(i)
            p = round(self.priorProbability.get(i)*temp.get(d[0])*temp.get(d[1]),4)
            pList.append(p)

        print pList
        print "The Category of",data,"is",self.Categories[pList.index(max(pList))]



def main():
    data = [[1,'S'],[1,'M'],[1,'M'],[1,'S'],[1,'S'],[2,'S'],[2,'M'],[2,'M'],[2,'L'],[2,'L'],[3,'L'],[3,'M'],[3,'M'],[3,'L'],[3,'L']]
    label = [-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]
    B = Bayes(data,label)
    d = [2,'S']
    B.predict(d)

if __name__ == '__main__':
    
    main()    
