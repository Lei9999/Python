# -*- coding: utf-8 -*-

# 编写一个py脚本，运行脚本，从一个五道选择题的题库中随机抽取三道题，
# 并要求为每道题输入正确答案，正确率百分比大于等于60%输出结果pass，
# 否则输出结果fail。将结果写入文件，文件名由答题者自定义。

import random
from random import sample

questions = {'\n题目1\n\nA\nB\nC\nD\n',
'\n题目2\n\nA\nB\nC\nD\n',
'\n题目3\n\nA\nB\nC\nD\n',
'\n题目4\n\nA\nB\nC\nD\n',
'\n题目5\n\nA\nB\nC\nD\n'}
correctanswer = {'A', 'C', 'D', 'A', 'B'}
#len(questions)
#print(len(questions))
questions_list = list(questions)
choice_id = sample([0, 1, 2, 3, 4], k=3)
#print(choice_id)
for i in range(3):
    #print(i)
    choice_index = choice_id[i]
    #print('ID = ', a)
    current_questions = questions_list[choice_index]
    answer = input(current_questions + "\n请输入答案：")