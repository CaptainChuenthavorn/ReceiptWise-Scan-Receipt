from pythainlp.tokenize import sent_tokenize

sentence_1 = "จ่ายเงินสำเร็จ 02 มิ.ย. 2566 18:22"
sentence_2 = "ข้าราชการได้รับการหมุนเวียนเป็นระยะ \
และได้รับมอบหมายให้ประจำในระดับภูมิภาค"

o1 = sent_tokenize(sentence_1, engine="whitespace")
# output: ['ฉันไปประชุมเมื่อวันที่', '11', 'มีนาคม']

o2 = sent_tokenize(sentence_2, engine="whitespace")
# output: ['ข้าราชการได้รับการหมุนเวียนเป็นระยะ',
#   '\nและได้รับมอบหมายให้ประจำในระดับภูมิภาค']
print(o1)
print(o2)