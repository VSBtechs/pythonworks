from SimpleCV import *
import numpy as np

from sklearn import svm
from sklearn.metrics import accuracy_score

hhfe = HueHistogramFeatureExtractor() #look at color
ehfe = EdgeHistogramFeatureExtractor() #look at edges
haarfe = HaarLikeFeatureExtractor('/home/virat/SimpleCV/SimpleCV/Features/haar.txt') #look at symmetry

extractor = [hhfe,ehfe,haarfe] #put all together

svm = SVMClassifier(extractor)
tree = TreeClassifier(extractor)

trainPaths = ['/home/virat/Desktop/pyw/ML/virat/pro/hand/train1/','/home/virat/Desktop/pyw/ML/virat/pro/hand/train2/']
testPaths = ['/home/virat/Desktop/pyw/ML/virat/pro/hand/test1/','/home/virat/Desktop/pyw/ML/virat/pro/hand/test2/']

classes = ['shapev','faces']

print svm.train(trainPaths,classes,verbose=True)
print tree.train(trainPaths,classes,verbose=True)

print '------------------------------------------------'

print svm.test(testPaths,classes,verbose=True)
print tree.test(testPaths,classes,verbose=True)

import random
test = ImageSet()
for p in trainPaths:
 test += ImageSet(p)
random.shuffle(test)
test = test[0:10]

for t in test :
 className = tree.classify(t)
 t.drawText(classNmae,10,10,fontsize=60,color=Color.RED)
 t.show()
