# -*- coding: utf-8 -*-

import pandas as pd


def csv2dict(path):
    '''
    目的：将数据框转换成字典形式{index1：[index2]}，避免结果排序混乱
    :param path:
    :return:
    '''
    df = pd.read_csv(path)
    dict = {}
    id1 = list(df['index1'])
    id2 = list(df['index2'])
    for i in range(len(id1)):
        key = str(id1[i])
        if key in dict.keys():
            dict[key].append(id2[i])
        else:
            dict[key] = [id2[i]]
    return dict

def evaluate(A,B):
    '''
    目的：对1条测试集新闻进行评分
    :param A: 实际的相似新闻标号列表
    :param B: 选手给出的相似新闻标号列表
    :return score:这条新闻的得分
    '''
    A = sorted(list(set(A)),key=A.index) #新闻去重保持顺序不变
    B = sorted(list(set(B)),key=B.index)
    print(A,B)
    count = 0
    f_sum = 0
    for i in range(len(B)):
        item = B[i]
        if item in A:
            count += 1
            f = count/(i+1)
        else:
            f = 0
        f_sum += f
    score = f_sum/len(A)
    return score

def evaluate_all(path_truth,path_pred):
    '''
    :param path_truth: 测试集的结果路径
    :param path_pred: 选手提交的路径
    :return mAP:整体评分
    '''
    dict_truth = csv2dict(path_truth)
    dict_pred = csv2dict(path_pred)
    AP = 0
    for key in dict_pred.keys():
        list_pred = list(set(dict_pred[key]))
        if (key not in dict_truth.keys()) or (len(list_pred) != 20):
            mAP = -1
            print('请检查提交格式：1、测试样本数量是否正确；2、每条样本是否提交大于或小于20条数据。')
            return mAP
        else:
            A = dict_truth[key]
            B = dict_pred[key]
            ap = evaluate(A,B)
            print(ap)
            AP += ap
    mAP = AP/len(dict_truth)

    return mAP

if __name__ == '__main__':

    path_truth = r'C:\Users\Administrator\Desktop\result.csv'
    path_pred = r'C:\Users\Administrator\Desktop\pred.csv'
    mAP = evaluate_all(path_truth,path_pred)
    print(mAP)

    # A = [1,2,3,4,5]
    # B = [1,2,3,0,4,8,9,7]
    # C = [1,2,3]
    # score1 = evaluate(A,B)
    # score2 = evaluate(A,C)
    # print(score1,score2)

