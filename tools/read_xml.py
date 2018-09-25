# author:sheng.Gw
# -*- coding: utf-8 -*-
# @Date :  2018/9/25
"""
工具：用来实现XML文件的读取
"""
config = {
    'filepath' : '/Users/sheng/PycharmProjects/KG_and_sentiment/semeval_data/Restaurants_Train_Data/ABSA15_RestaurantsTrain/ABSA-15_Restaurants_Train_Final.xml'

}



from xml.dom import minidom

dom = minidom.parse(config['filepath'])

root = dom.documentElement


#print(root.nodeName)
#print(root.nodeValue)

#print(root.getElementsByTagName("sentence")[0].getAttribute('id'))


#for eachline in root.getElementsByTagName("sentence"):


result_rid = []
result_id  = []
result_text = []

result_category_first = []
result_category_second = []

result_polarity = []
result_target = []

result_from = []
result_to = []


for eachline in root.getElementsByTagName("Review"):

    print(eachline.getAttribute("rid"))

    eachline1 =eachline.childNodes[1].childNodes

    index = 1
    while index < len(eachline1):

        each = eachline1[index]
        index += 2

        print(each.getAttribute('id'))

        print(each.childNodes[1].childNodes[0].data)



        result_rid.append(eachline.getAttribute("rid"))
        result_id.append (each.getAttribute('id'))
        result_text.append(each.childNodes[1].childNodes[0].data)

        if each.getElementsByTagName("Opinion") != []:
            print(each.getElementsByTagName("Opinion")[0].getAttribute('category'))
            print(each.getElementsByTagName("Opinion")[0].getAttribute('polarity'))


            result_category_first.append(each.getElementsByTagName("Opinion")[0].getAttribute('category').split('#')[0])
            result_category_second.append(each.getElementsByTagName("Opinion")[0].getAttribute('category').split('#')[1])

            result_polarity.append(each.getElementsByTagName("Opinion")[0].getAttribute('polarity'))

            result_target.append(each.getElementsByTagName("Opinion")[0].getAttribute('target'))

            result_from.append(each.getElementsByTagName("Opinion")[0].getAttribute('from'))
            result_to.append(each.getElementsByTagName("Opinion")[0].getAttribute('to'))

        else:
            result_category_first.append(None)
            result_category_second.append(None)

            result_polarity.append(None)
            result_target.append(None)

            result_from.append(None)
            result_to.append(None)


import pandas as pd

result = pd.DataFrame({'rid':result_rid,'id':result_id,'text':result_text,'category_first':result_category_first,'category_second':result_category_second,'polarity':result_polarity,'from':result_from,'to':result_to})

result.to_csv('result.csv')