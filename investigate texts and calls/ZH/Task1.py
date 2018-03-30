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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.
"""

# 发送短信号码列表
send_sms_phone_list = []
# 接收短信号码列表
recv_sms_phone_list = []

# 主叫电话号码列表
call_originate_phone_list = []
# 被叫电话号码列表
call_terminate_phone_list = []


for text_info in texts:
    send_sms_phone_list.append(text_info[0])
    recv_sms_phone_list.append(text_info[1])

for call_info in calls:
    call_originate_phone_list.append(call_info[0])
    call_terminate_phone_list.append(call_info[1])

# 不重复的号码集合
sets_phones = set()

#print("==================================")

#参考资料：https://www.cnblogs.com/whatisfantasy/p/5956775.html

sets_phones.update(send_sms_phone_list)

sets_phones.update(recv_sms_phone_list)

sets_phones.update(call_originate_phone_list)

sets_phones.update(call_terminate_phone_list)

print("There are %s different telephone numbers in the records." % len(sets_phones))


