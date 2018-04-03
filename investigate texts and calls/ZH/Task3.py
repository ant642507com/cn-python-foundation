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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

"""被叫电话 列表"""
call_terminate_code_list = []

"""主叫电话是080的数量"""
originate_phone_080_count = 0
"""被叫电话是080的数量"""
terminate_phone_080_count = 0


for phone_info in calls:
    originate_phone = phone_info[0]
    terminate_phone = phone_info[1]
    if "(080)" in originate_phone:
        # 主叫电话数量增加
        originate_phone_080_count += 1
        #call_terminate_phone_list.append(terminate_phone)
        #固定电话以"(0"开头
        if terminate_phone.startswith("(0"):
            #print(terminate_phone)
            tmp = terminate_phone[0:terminate_phone.index(")")+1]
            call_terminate_code_list.append(tmp)
            pass
        
        if (" " in terminate_phone) and (terminate_phone.startswith("7") \
            or terminate_phone.startswith("8") \
            or terminate_phone.startswith("9")):
            #print(terminate_phone)
            tmp = terminate_phone[0:4]
            #print(tmp)
            call_terminate_code_list.append(tmp)
            pass
        if terminate_phone.startswith("140"):
            pass
            #print(terminate_phone)
        if "(080)" in terminate_phone:
            terminate_phone_080_count += 1
    
# 被叫电话列表去重
unique_code_list = set(call_terminate_code_list)
# 去重后的电话列表排序
sorted_unique_code_list = sorted(unique_code_list)

print("The numbers called by people in Bangalore have codes:")
for itm in sorted_unique_code_list:
    print(itm)

percent = round(terminate_phone_080_count*100/originate_phone_080_count, 2)
print("{} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(percent))
