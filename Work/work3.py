# -*- coding: utf-8 -*-

# 编写一个py脚本，运行脚本，从一个五道选择题的题库中随机抽取三道题，
# 并要求为每道题输入正确答案，正确率百分比大于等于60%输出结果pass，
# 否则输出结果fail。将结果写入文件，文件名由答题者自定义。

import os
import random
from random import sample

score = 0
questions = {
    1: '\n题目1(单选题)\n\nA\nB\nC\nD\n',
    2: '\n题目2(单选题)\n\nA\nB\nC\nD\n',
    3: '\n题目3(单选题)\n\nA\nB\nC\nD\n',
    4: '\n题目4(单选题)\n\nA\nB\nC\nD\n',
    5: '\n题目5(单选题)\n\nA\nB\nC\nD\n'
}
correct_answer = {1: 'A', 2: 'B', 3: 'D', 4: 'A', 5: 'C'}
id_list = sample([1, 2, 3, 4, 5], k=3)

for i in range(3):
    index_key = id_list[i]
    current_answer = input(questions[index_key] + '\n请输入答案：')
    if current_answer == correct_answer[index_key]:
        score = score + 1
    else:
        pass

file_name = input('\n答题已结束，请输入成绩单的文件名：')
print('\n您的成绩已打印到成绩单中，请查看成绩单文件：{}'.format(file_name))

if score/3 >= 0.6:
    exam_result = ('PASS')
else:
    exam_result = ('FAIL')

with open(file_name, mode='w', encoding='utf-8') as score_file:
    score_file.write(exam_result)