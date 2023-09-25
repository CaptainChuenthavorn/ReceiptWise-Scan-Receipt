from newmm_tokenizer.tokenizer import word_tokenize

text = '''โอนเงินสำเร็จ 3 ธ.ค. 62 20:25 น
นาย พร้อมบุญฺจ ธ.กสิกรไทย xxx-x-x8519-x
นาย อนุสิทธิ์ เลิศธนวงศ์ prompt  pay รหัสพร้อมเพย์ x xxxx xxxx4-41-9
เลขที่รายการ: 019337202548433549
จำนวน:
loo.00 บาท ค่าธรรมเนียม: o.00 บาท
verifed by k+
'''
text2='''โอนเงินสำเร็จ 3 ธ.ค. 62 20:25 น.
k+
นาย พร้อมบุญฺจ ธ.กสิกรไทย xxx-x-x8519-x
นาย อนุสิทธิ์ เลิศธนวงศ์  prompt  pay รหัสพร้อมเพย์ x xxxx xxxx4-41-9
เลขที่รายการ: 019337202548433549
จ่านวน:
loo.00 บาท ค่าธรรมเนียม: o.00 บาท
verifed by k+
'''
words = word_tokenize(text)

print(words) 

tid = [0-9]{15,20}
amount = [0-9]\.[0-9]{0,2}
(\d*\.\d+)?\b\s*(\บาท)
name = (นาย|นาง|น.ส.|u.ส.)[ก-๛ ]+
sender_name (string)
sender_account_number (string)
recipient_name (string)
recipient_account_number (string)
amount (float64)
fee (float64)
date (DateTime)
memo (string)	
created_at (DateTime)

scb
date(Date) 01 มิ.ย. 2566 08:11
reference_Number = รหัสอ้างอิง: 20230601243qzddbcfh2xxund
sender_name = นาย กฤษฎา สารวิทย์ 
sender_account_number = xxx-xxx588-5
receiptent_name = นาย อภิสิทธิ เนียมสูงเนิน 
receiptent_account_number = xxx-xxx-9297
amount = 35.00
memo= [yo]
