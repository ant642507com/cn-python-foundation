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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""



# 获取拨出电话电话列表
call_originate_phone_list = set()

# 获得收到来电电话列表
call_terminate_phone_list = set()

for call_info in calls:
    originate_phone = call_info[0]
    terminate_phone = call_info[1]

    call_originate_phone_list.add(originate_phone)
    call_terminate_phone_list.add(terminate_phone)



# 获得发送短信电话列表
text_send_phone_list = set()

# 获得接收短信电话列表
text_recv_phone_list = set()

for text_info in texts:
    send_phone = text_info[0]
    recv_phone = text_info[1]

    text_send_phone_list.add(send_phone)
    text_recv_phone_list.add(recv_phone)



# 从拨出电话的列表中电话号码，排除发送短信的电话号码，接收短信的电话号码，收到来电的电话号码
remain_phone_list = call_originate_phone_list - call_terminate_phone_list - text_send_phone_list - text_recv_phone_list

# 排序
sorted_phone_list = sorted(remain_phone_list, key = lambda x:x[1])

print("These numbers could be telemarketers: ")
for phone_num in sorted_phone_list:
    print(phone_num)