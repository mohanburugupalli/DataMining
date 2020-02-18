import numpy as np
import math

######################################################################################################################################
#   Function to calculate first 'k' minimum distances of each record in testing dataset to all the recordins in training dataset, and return classlabel by majority'''         #
######################################################################################################################################

def minimum_distance(arr,k):
    classlabel_array=[]
    for i in range(50):
        sub_arr1=arr[i]
        sub_arr=sorted(arr[i])
        sub_arr1=arr[i]
        l=k/2
        min = sub_arr[0:k]
        count=0
        for m in range(k):
            z=min[m]
            a=sub_arr1.index(z)
            b=arr2_class[a]
            if (b == 1.):
                count+=1
        if (count<=l):
            class_label = -1
        else:
            class_label = 1
        classlabel_array.append(class_label)
    return classlabel_array


###############################################################################################################################
#       Function to compare predicted class labels with the given class labels and evalute True Positive ,False Positive,True Negative,False Negative'''            #
###############################################################################################################################

def values(arr):
    tp=0
    fp=0
    tn=0
    fn=0
    for i in range(50):
        k = arr[i]
        if ((k == arr1_class[i]) and (k ==1)):
            tp=tp+1
        elif((k != arr1_class[i]) and (k ==1)):
             fp=fp+1
        elif((k == arr1_class[i]) and (k == -1)):
             tn=tn+1
        elif((k != arr1_class[i]) and (k == -1)):
             fn=fn+1
        else:
             print("Please check again")
    return tp,fp,tn,fn

##########################################################################################
#                                                Function to calculate performance of the given classifier                                    #
##########################################################################################
def performance(arr):
    tp=arr[0]
    fp=arr[1]
    tn=arr[2]
    fn=arr[3]
    m=float(tp+fp+tn+fn)
    ac = ((tp+tn)/m)*100
    se = ((float(tp))/(tp+fn))*100
    sp = ((float(tn))/(fp+tn))*100
    pr = ((float(tp))/(tp+fp))*100
    print("Accuracy : "+str(ac)+"%"+"\n"+"Sensitivity : "+str(se)+"%"+"\n"+"Specificity : "+str(sp)+"%"+"\n"+"Precision : "+str(pr)+"%")
    

##############################################################################################
#                                                                           MAIN PROGRAM                                                                                  #
##############################################################################################

data = input("Enter 1 for performance of 'irisTesting' dataset or\nEnter 2 for performance of 'irisPCTesting' dataset: " )
if data==1:
    arr1 = np.genfromtxt('irisTesting.txt', delimiter=' ')
    arr2 = np.genfromtxt('irisTraining.txt', delimiter=' ')
elif data==2:
    arr1 = np.genfromtxt('irisPCTesting.txt', delimiter=' ')
    arr2 = np.genfromtxt('irisPCTraining.txt', delimiter=' ')
else:
    print "Please enter either 1 or 2 only:"
q=len(arr1[0])
p=q-1
r=len(arr1)
arr1_data = arr1[:,0:p]
arr1_class = arr1[:,p:]
arr2_data = arr2[:,0:p]
arr2_class = arr2[:,p:]
new_distances=[]
for i in range(r):
    l=0
    distances=[]
    for k in arr2_class:
        d=0
        for j in range(p):
            b=arr1_data[i][j] - arr2_data[l][j]
            a=round(b,2)
            c=a**2
            d=d+c
        e=math.sqrt(d)
        l+=1
        distances.append(e)
    new_distances.append(distances)

knn=input("Enter number of nearest neighbours, K=")
classlabel_array1=minimum_distance(new_distances,knn)
values = values(classlabel_array1)
performance(values)









