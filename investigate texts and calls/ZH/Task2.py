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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

tel_totaltime_map = {}

#组织map数据结构 key 为手机号，value为手机号对应的通话时长
for call_info in calls:
    # 主叫电话
    originate_phone = call_info[0]
    # 被叫电话
    terminate_phone = call_info[1]
    # 通话时长
    time_in_sec = int(call_info[3])
    
    if tel_totaltime_map.__contains__(originate_phone):
        tel_totaltime_map[originate_phone] = tel_totaltime_map[originate_phone] + time_in_sec
    else:
        tel_totaltime_map[originate_phone] = time_in_sec
    
    
    if tel_totaltime_map.__contains__(terminate_phone):
        tel_totaltime_map[terminate_phone] = tel_totaltime_map[terminate_phone] + time_in_sec
    else:
        tel_totaltime_map[terminate_phone] = time_in_sec

#将 map 按照 value值排序
tel_sorted_dict = dict(sorted(tel_totaltime_map.items(), key = lambda x:x[1], reverse=True))

#取得第一个key值
max_totaltime_phone = list(tel_sorted_dict.keys())[0]
#获取第一个key值对应的value
max_totaltime = tel_sorted_dict[max_totaltime_phone]

print("%s spent the longest time, %s seconds, on the phone during September 2016." % (max_totaltime_phone, max_totaltime))
