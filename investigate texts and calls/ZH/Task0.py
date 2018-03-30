"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# 参考资料：http://www.runoob.com/python/python-lists.html

''' 
texts 和 calls 是 二维List
first_text 和 last_call 是List
'''
first_text = texts[0]
last_call = calls[-1]

# 参考资料: http://www.runoob.com/w3cnote/python3-print-func-b.html
print("First record of texts, %s texts %s at time %s" % (first_text[0], first_text[1], first_text[2]))
print("Last record of calls, %s calls %s at time %s, lasting %s seconds" % (last_call[0], last_call[1], last_call[2], last_call[3]))