'''
work for text that not list read line by line and make into list
[[[438, 84], [804, 84], [804, 210], [438, 210]], 'oscb']
[[[501, 381], [789, 381], [789, 449], [501, 449]], 'โอนเงินสำเร็จ']
[[[447, 487], [841, 487], [841, 536], [447, 536]], '02 มิ.ย. 2566 22:39']
[[[255, 552], [1032, 552], [1032, 610], [255, 610]], ' รหัสอ้างอิง: 2023060294pt5zbi3rnzoujv']
[[[67, 723], [147, 723], [147, 767], [67, 767]], ' จาก']
[[[789, 716], [1231, 716], [1231, 857], [789, 857]], 'นาย กฤษฎา สารวิทย์  xxx-xxx588-5']
[[[62, 912], [162, 912], [162, 966], [62, 966]], 'ไปยัง']
[[[773, 911], [1229, 911], [1229, 1053], [773, 1053]], 'นาย ดุษฎี ส่งเกษรชาติ  xxx-xxx-7661']
[[[64, 1196], [254, 1196], [254, 1250], [64, 1250]], ' จำนวนเงิน']
[[[1060, 1198], [1224, 1198], [1224, 1252], [1060, 1252]], '269.00']
[[[61, 1398], [770, 1398], [770, 1549], [61, 1549]], 'ผู้รับเงินสามารกสแกนคิวอาร์โคัดนี้เพื่อ ตรวจสอบสถานะการโอนเงิน']

to 
result_text =['oscb', 'โอนเงินสำเร็จ', '02 มิ.ย. 2566 22:39', ' รหัสอ้างอิง: 2023060294pt5zbi3rnzoujv', ' จาก', 'นาย กฤษฎา สารวิทย์  xxx-xxx588-5', 'ไปยัง', 'นาย ดุษฎี ส่งเกษรชาติ  xxx-xxx-7661', ' จำนวนเงิน', '269.00', 'ผู้รับเงินสามารกสแกนคิวอาร์โคัดนี้เพื่อ ตรวจสอบสถานะการโอนเงิน']
'''

import re
filename = r'D:\Programming\ReceiptWise\ReceiptWise-Scan-Receipt\Pre_text_ocr_scb_IMG_0703.JPG.txt'

result_text=[]
with open(filename,'r',encoding='utf-8') as file:
    for line in file:
        # Define a regular expression pattern to match text inside single quotes
        pattern = r"'([^']*)'"
        # Use re.findall to find all matches of the pattern in the input text
        matches = re.findall(pattern, line)
        # If there are matches, 'scb' will be in the first match, so you can access it like this:
        if matches:
            result = matches[0]
        result_text.append(result)

print(result_text)

'''
[[[501, 381], [789, 381], [789, 449], [501, 449]], 'โอนเงินสำเร็จ']
[[[455, 485], [833, 485], [833, 535], [455, 535]], '01 มิ.ย. 2566 08:11']
if found date in array get with regex len of matchdate will be 1 

'''
date_pattern_intermedate=r'(\d{2}\s(?:[ก-๛]\.[ก-๛]\.|[ก-๛][ก-๛]\.[ก-๛]\.)\s\d{4}\s\d{2}:\d{2})'
match_date= re.findall(date_pattern_intermedate, result_text[1])
print(match_date)
print(len(match_date))