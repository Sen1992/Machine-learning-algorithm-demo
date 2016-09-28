#-*-coding=UTF-8-*-
#/usr/bin/python
import GL

#计算仅有people人能在前mine_num个矿最多获得多少金子

def get_max_gold(people,mine_num):
    #这个问题是否计算过，对应着备忘录的记录
    if(GL.max_gold[people][mine_num]!=-1):
        ret_max_gold = GL.max_gold[people][mine_num]
    #如果只有一个金矿时，对应着动态规划中的边界
    elif(mine_num==0):
        if(people>=GL.people_need[mine_num]):
            ret_max_gold = GL.gold[mine_num]
        else:
            ret_max_gold = 0
    #如果给出的人能后开采这个金矿，对应着最优子结构
    elif(people>=GL.people_need[mine_num]):
        ret_max_gold = max(get_max_gold(people-GL.people_need[mine_num],mine_num-1)+GL.gold[mine_num],get_max_gold(people,mine_num-1))
    else:
        ret_max_gold = get_max_gold(people,mine_num-1)
    #做备忘录，同时递归操作表示了子问题重叠
    GL.max_gold[people][mine_num] = ret_max_gold
    return ret_max_gold
    
def main():

    print "result = ",get_max_gold(GL.people_total-1,GL.mine_total-1)


if __name__ =='__main__':
    main()
