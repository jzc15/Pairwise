from easy_pairwise import utils2

if __name__ == '__main__':
    u2 = utils2()
    # allparams=[(['M','O','P'], []),(['W','L','I'], []),(['C','E'], [])]
    # allparams=[(['M', 'P', 'Q', 'R', 'S', 'T', 'x', 'y'], []), (['M', 'N', "O", "P"], []), (['A', 'B', 'E', 'F', 'c'], [])]

    # allparams=[(['M', 'P', 'Q', 'R', 'S', 'T'], ['x', 'y']), (['M', 'N', "O", "P"], []), (['A', 'B', 'E', 'F'], ['c'])]
    allparams = [([0, 1, 2], [3, 4, 8]), ([0, 1, 2], [3, 4, 8]), 
        ([0], [8]), ([0], [8]), ([0, 1, 2], [3, 4, 8]), 
        ([0], [1]), ([0, 1, 2], [3, 4, 8]), 
        ([0, 1, 2], [3, 4, 5]), ([0, 1, 2], [3, 4, 8]), ([0], []),
        ([0], [8]), ([0, 1, 2], [3, 4, 7]), ([0, 1, 2], [3, 4, 7]), 
        ([0], [8]), ([0], [8]), 
        ([0], [8]),
        ([0], [8]), ([0], [8]),
        ([0], [8]), 
        ([0, 1], [4]), ([0, 1], [4]), ([0], [8]), ([0], [8]), ([0, 1], [4]),
    ]
    # allparams = [([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0, 1, 2], [3, 4, 8]), ([0, 1, 2], [3, 4, 8]), ([0], [8]), ([0], [8]), ([0, 1, 2], [3, 4, 8]), ([0], [1]), ([0], []), ([0, 1, 2], [3, 4, 8]), ([0, 1, 2], [3, 4, 5]), ([0, 1, 2], [3, 4, 8]), ([0], []), ([0], [8]), ([0, 1, 2], [3, 4, 7]), ([0, 1, 2], [3, 4, 7]), ([0], []), ([0], [8]), ([0], []), ([0], []), ([0], [8]), ([0], []), ([0], []), ([0], [8]), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], [8]), ([0], [8]), ([0], []), ([0], []), ([0], []), ([0], [8]), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0, 1], [4]), ([0, 1], [4]), ([0], [8]), ([0], [8]), ([0], []), ([0, 1], [4]), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], []), ([0], [])]
    # print(u2.get_num(allparams, 1))
    # for x in u2.get_product(allparams, 1):
    #     print(x)
    for i, x in enumerate(allparams):
        text = "%d: "%(i)
        va, inva = x
        for a in va:
            text += str(a) + ','
        for a in inva:
            text += '~' + str(a) + ','
        
        print(text[:-1])
    finallist = u2.pairwise(allparams,2, 1)
    print('最终保留测试用例个数：%d 个'%(len(finallist)))
    u2.pprint(finallist)
