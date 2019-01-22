# -*- coding: utf-8 -*-
from datetime import *
import random,os,copy,time
import logging
import math
import itertools
#
# base:
#     Author:Kuzaman
#     Time:2017-07-18
#     link:https://www.cnblogs.com/kuzaman/p/7202146.html?utm_source=tuicool&utm_medium=referral
# extend:
#     区分合法等价类与非法等价类，并生成不超过1个非法参数的所有组合
#     不再使用全枚举，基于AETG，PICT算法的思想，简易实现，选择未覆盖的对增加测试用例
#     Author: jzc
#     Time: 2019-01-22     

class utils2 :

    def __init__(self):
        self.empty_index = []
        self.empty_value = []
        self.allpair = {}
        self.all_count = 0

    def get_er(self, allparams, index1, k1):
        if k1 in allparams[index1][1]:
            return 1
        return 0
    # 去除唯一值，提高算法效率  
    # 计算所有组合

    def init(self, allparams, er):
        self.all_count = len(allparams)
        nall = []
        for i, x in enumerate(allparams):
            va, inva = x
            al = va + inva
            if len(al) == 1:
                self.empty_index.append(i)
                self.empty_value.append(al[0])
                if al[0] in inva:
                    er -= 1
            else:
                nall.append(x)
        for (i, x) in enumerate(nall):
            for (j, y) in enumerate(nall):
                if i >= j:
                    continue
                vax, invax = x
                ax = vax + invax
                
                vay, invay = y
                ay = vay + invay

                if er == 0:
                    ax = vax
                    ay = vay

                for a1 in ax:
                    for a2 in ay:
                        if a1 in invax and a2 in invay:
                            continue
                        self.allpair.setdefault((i, j), [])
                        self.allpair[(i, j)].append((a1, a2))
        return nall, er
    # 将去除的唯一值补充
    def result(self, ans0):
        ans = []
        k = 0
        z = 0
        kmax = len(self.empty_index)
        for i in range(0, self.all_count):
            if k < kmax and i == self.empty_index[k]:
                ans.append(self.empty_value[k])
                k += 1
            else:
                ans.append(ans0[z])
                z += 1
        return ans

    # 迭代器模式下，需要用另一种方式求出全排列个数
    # 简单动态规划实现
    def get_num(self, allparams, k):
        f = [0] * (k+1)
        f[0] = 1
        for para in allparams:
            va, inva = para
            la = len(va)
            li = len(inva)
            for i in range(k, 0, -1):
                f[i] = f[i-1] * li + f[i] * la
            f[0] = f[0] * la
        return sum(f)

    # 改进笛卡尔积，找到恰好k个异常的全排列，修改为迭代器模式，使用栈模拟递归

    def get_next(self, cur, va, iva):
        v, iv = cur
        v += 1
        if len(va) > v:
            return va[v], (v, iv), 1
        iv += 1
        if len(iva) > iv:
            return iva[iv], (v, iv), 0
        return 0, (v, iv), -1

    def get_product(self, allpair, allparams, er, para):
    
        if len(para) == len(allparams):
            l = len(para)
            p = []
            # print(para)
            for i in range(0, l):
                p.append(para[i])
            
            return p

        # 至少扩展一个, 希望能覆盖其他pair
        for x in list(allpair):
            i, j = x
   
            if i in para:
                for a, b in allpair[x]:
                    
                    if a != para[i]:
                        continue
                    err = self.get_er(allparams, j, b)
                    if er < err:
                        continue
                    para[j] = b
                    allpair.pop(x)
                    return self.get_product(allpair, allparams, er-err, para)
            if j in para:
                for a, b in allpair[x]:
                    if b != para[j]:
                        continue
                    err = self.get_er(allparams, i, a)
                    if er < err:
                        continue
                    para[i] = a
                    allpair.pop(x)
                    return self.get_product(allpair, allparams, er-err, para)
            for a, b in allpair[x]:
                err = self.get_er(allparams, i, a)
                err += self.get_er(allparams, j, b)
                if er < err:
                    continue
                para[i] = a
                para[j] = b
                allpair.pop(x)
                return self.get_product(allpair, allparams, er-err, para)
            allpair.pop(x)
        
        # 可以增加异常
        for i, x in enumerate(allparams):
            va, inva = x
            if i not in para:
                para[i] = va[random.randint(0, len(va)-1)]
                return self.get_product(allpair, allparams, er, para)
        # print(para)

    #1、找到一个未覆盖的p，并生成一个覆盖尽可能多的测例
    
    def product(self,allparams, er=0):
        flag = True
        while flag:
            flag = False
            para = {}
            for x in self.allpair:
                if len(self.allpair[x]) > 0:
                    # print(self.allpair)
                    flag = True
                    i, j = x
                    a, b = self.allpair[x][0]
                    para[i] = a
                    para[j] = b

                    ap = copy.deepcopy(self.allpair)
                    ap.pop(x)
                    # print(ap)
                    # print(para)
                    yield self.get_product(ap, allparams, er - self.get_er(allparams, i, a) - self.get_er(allparams, j, b), para)
                    # input()
                    # print(ap)
                    break

    #2、对笛卡尔积处理后的二维原始数据进行N配对处理，得到Pairwise计算之前的数据
    def get_pairslist(self, product, pairlen):
        # pwlist = []
        # for i in productedlist:
        subtemplist = []
        for sublista in itertools.combinations(product,pairlen):
            subtemplist.append(sublista)
        # pwlist.append(subtemplist)
        return subtemplist
    
    # 每一个测例的配对数， c(n, m)
    def get_paralen(self, n, m):
        ans = 1
        for i in range(0, m):
            ans *= n-i
        for i in range(0, m):
            ans /= (i+1)
        return int(ans)

    # 更新测例集
    def update(self, cow, ans, anscow, para):
        flag = False
        for index, column in enumerate(cow):      # 检查每一对
            if column not in anscow[index]:
                flag = True
                break
        # print ('下标%d,子元素 %s 双匹配对比结果flag:%s'%(listb.index(cow),cow,flag))
        if flag:    #如果对比列表中都是1，表明该行的所有结对都在同列的对应位置找到了
            for index, column in enumerate(cow):
                if column not in anscow[index]:
                    anscow[index].append(column)
            ans.append(copy.deepcopy(para))
        
            for i, x in enumerate(para):
                for j, y in enumerate(para):
                    if i >= j:
                        continue
                    if (x, y) in self.allpair[(i,j)]:
                        # print(x, y)
                        self.allpair[(i,j)].remove((x, y))    
        return ans, anscow

    
    # 生成随机测例
    def random_product(self, allparams, er0):
        er = copy.deepcopy(er0)
        para = []
        er_flag = random.randint(0, len(allparams))
        for i, x in enumerate(allparams):
            # print(x)
            va, inva = x
            al = copy.deepcopy(va)
            if er > 0 and i >= er_flag:
                al += inva
            k = random.randint(0, len(al)-1)
            if k >= len(va):
                para.append(inva[k-len(va)])
                er -= 1
            else:
                para.append(va[k])
        # print(er)
        return para
    #3、进行Pirwise算法计算
    def pairwise(self,allparams,pairlen, er = 0, seed = None):
        
        allparams, er = self.init(allparams, er)

        if er < 0:
            return []

        allnum = self.get_num(allparams, er)
        logger = logging.getLogger('generator')
        logger.info(allparams)
        logger.info(allnum)
        # print ('笛卡尔积全排列组合数量：', allnum,'--'*11)

        # 增加随机的初始测例

        anscow = []
        
        cl = self.get_paralen(len(allparams), pairlen)    # 有效测试用例结对情况, 每一维用一个数组表示这一列的情况
        for x in range(0, cl):
            anscow.append([])
        ans0 = []     # 有效测试用例
        
        if seed == None:
            seed = int(math.log(allnum, 2))
        # print('seed个数: %d' %(seed))
        # print(self.allpair[(0, 2)]) 
        for i in range(0, seed):
            para = self.random_product(allparams, er)
            cow = self.get_pairslist(para, pairlen)
            ans0, anscow = self.update(cow, ans0, anscow, para)

            # print(self.allpair[(0, 2)]) 

        cnt = 0
        for para in self.product(allparams, er):           # 依次遍历所有测例
            # print(self.allpair)
            # print(para)
            # cnt += 1
            # if cnt % 10000 == 0:
            #     print(cnt, len(ans0))
            cow = self.get_pairslist(para, pairlen)
            ans0, anscow = self.update(cow, ans0, anscow, para)

        for x in range(0, cl):
            anscow[x] = []
        
        ans = []
        # print ('顺序筛数量：', len(ans0),'--'*11)

        # random.shuffle(ans0)
        ans0 = reversed(ans0)

        for para in ans0:           # 依次遍历所有测例
            # print(para)
            cow = self.get_pairslist(para, pairlen)
            ans, anscow = self.update(cow, ans, anscow, para)


        # logger.info('生成组数: %d'%(len(ans)))
        for i, x in enumerate(ans):
            logger.debug(x)
            ans[i] = self.result(x)
        
        return ans

    def pwresult(self,slist,holdmenu):
        holdparamslist = []
        for  item in holdmenu:
            holdparamslist.append(slist[item])
        return holdparamslist

    def pprint(self,list):
        for item in list:
            print ('line %d:'%(list.index(item)+1),item)
            # print (item) 


