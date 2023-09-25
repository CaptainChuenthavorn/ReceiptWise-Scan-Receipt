from pythainlp.tokenize import word_tokenize


import deepcut

text = '''โอนเงินสำเร็จ 3 ธ.ค. 62 20:25 น
i(+
นาย พร้อมบุญฺจ ธ.กสิกรไทย xxx-x-x8519-x
นาย อนุสิทธิ์ เลิศธนวงศ์ prompt  pay รหัสพร้อมเพย์ x xxxx xxxx4-41-9
เลขที่รายการ: 019337202548433549
จำนวน:
loo.00 บาท ค่าธรรมเนียม: o.00 บาท
verifed by k+
'''
engine="deepcut"
a=word_tokenize(text,engine='icu') # ['ผม', 'รัก', 'คุณ', 'นะ', 'ครับ', 'โอ', 'เค', 'บ่', 'พวก', 'เรา', 'เป็น', 'คน', 'ไทย', 'รัก', 'ภาษา', 'ไทย', 'ภาษา', 'บ้าน', 'เกิด']
# b=word_tokenize(text,engine='dict') # ['ผม', 'รัก', 'คุณ', 'นะ', 'ครับ', 'โอเค', 'บ่', 'พวกเรา', 'เป็น', 'คนไทย', 'รัก', 'ภาษาไทย', 'ภาษา', 'บ้านเกิด']
c=word_tokenize(text,engine='mm') # ['ผม', 'รัก', 'คุณ', 'นะ', 'ครับ', 'โอเค', 'บ่', 'พวกเรา', 'เป็น', 'คนไทย', 'รัก', 'ภาษาไทย', 'ภาษา', 'บ้านเกิด']
# d=word_tokenize(text,engine='pylexto') # ['ผม', 'รัก', 'คุณ', 'นะ', 'ครับ', 'โอเค', 'บ่', 'พวกเรา', 'เป็น', 'คนไทย', 'รัก', 'ภาษาไทย', 'ภาษา', 'บ้านเกิด']
e=word_tokenize(text,engine='newmm') # ['ผม', 'รัก', 'คุณ', 'นะ', 'ครับ', 'โอเค', 'บ่', 'พวกเรา', 'เป็น', 'คนไทย', 'รัก', 'ภาษาไทย', 'ภาษา', 'บ้านเกิด']

#import deepcut
f= deepcut.tokenize(text)
print(f) 


img_prefix_name=[a,c,e,f]
# Write the desired texts to a file
for i,x in enumerate(img_prefix_name):
    output_filename = f"text_ocr{i}.txt"
    with open(output_filename, 'w', encoding='utf-8') as file:
        for text in x:
            file.write(text + '\n')

print("Desired texts have been written to", output_filename)