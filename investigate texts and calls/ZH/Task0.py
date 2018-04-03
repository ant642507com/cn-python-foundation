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

""" 以下我之前的答案（20180403_0906）
texts 和 calls 是 二维List
first_text 和 last_call 是List

first_text = texts[0]
last_call = calls[-1]

# 参考资料: http://www.runoob.com/w3cnote/python3-print-func-b.html
print("First record of texts, %s texts %s at time %s" % (first_text[0], first_text[1], first_text[2]))
print("Last record of calls, %s calls %s at time %s, lasting %s seconds" % (last_call[0], last_call[1], last_call[2], last_call[3]))
"""


""" 以下是我接受审阅建议之后的答案
参考建议：https://pyformat.info/#simple 
"""
print("First record of texts, {} texts {} at time {}".format(
    texts[0][0],
    texts[0][1],
    texts[0][2]
))

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    calls[-1][0],
    calls[-1][1],
    calls[-1][2],
    calls[-1][3]
))
