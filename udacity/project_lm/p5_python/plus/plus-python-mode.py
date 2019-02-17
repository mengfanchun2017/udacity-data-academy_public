Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

# 一下是循环方式，i和dic[i]分别表示字典的index和value
#for album_title in Beatles_Discography:
#    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

def most_prolific(dic):
    # 先将每个专辑的出版年集合成一个列表
    pub_year = []
    for i in dic:
        pub_year.append(dic[i])
    
    # 对pub_year做统计（做迭代，次数等于dic的内容数）
    # 生成most字典，索引是年份，值是出现的次数
    most = {}
    for i in range(len(pub_year)):
        if pub_year[i] in most.keys():
             most[pub_year[i]] += 1
        else:
            most.setdefault(pub_year[i], 1)
    maxnum = 0
    maxkey = 0

    # 计算最大的那一个
    # 方式1，用循环完成
    print('---methrod1:normal---')
    for k, v in most.items():
        if v > maxnum:
            maxnum = v
            maxkey = k
    print(maxkey, maxnum)

    # 方式2，用max函数可以输出list中那个出现次数做多
    print('---methrod1:max(fuc)---')
    maxkey_fuc = max(set(pub_year), key=pub_year.count)

    return maxkey, maxnum, maxkey_fuc

print(most_prolific(Beatles_Discography))