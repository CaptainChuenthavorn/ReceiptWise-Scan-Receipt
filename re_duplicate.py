file_path = 'ชื่อคนทั้งหมด.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()
# Count occurrences of each string
count_dict = {}
for text in data:
    if text in count_dict:
        count_dict[text] += 1
    else:
        count_dict[text] = 1

# Print and remove duplicates
filtered_data = []
for text, count in count_dict.items():
    if count > 1:
        print(f"'{text}' appeared {count} times")
    else:
        filtered_data.append(text)

print("Filtered data after removing duplicates:")
for text in filtered_data:
    print(text)