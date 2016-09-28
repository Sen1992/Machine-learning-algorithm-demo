#-*-coding-UTF-8-*-
#/usr/bin/python

import numpy as np
goods_num = 5
weights = [2,2,6,5,4]
values = [6,3,5,4,6]
weight_total = 10
max_values = np.zeros((weight_total,goods_num),dtype=int)-np.ones((weight_total,goods_num),dtype=int)

def max_weigh_value(weight_total,weight_num):
    if(max_values[weight_total][weight_num]!=-1):
        ret_max_value = max_values[weight_total][weight_num]
    elif(weight_num==0):
        if(weight_total>=weights[weight_num]):
            ret_max_value = values[weight_num]
        else:
            ret_max_value = 0
    elif(weight_total>=weights[weight_num]):
        ret_max_value = max(max_weigh_value(weight_total-weights[weight_num],weight_num-1)+values[weight_num],max_weigh_value(weight_total,weight_num-1))
    else:
        ret_max_value = max_weigh_value(weight_total,weight_num-1)
    return ret_max_value

def main():
    print "max weigh this backpack can take is ",max_weigh_value(weight_total-1,goods_num-1)


if __name__ == "__main__":
    main()
