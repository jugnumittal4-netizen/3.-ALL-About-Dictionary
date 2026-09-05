st = {"id1":{"name":"sam","class":"10th","subject":"math,english,hindi"},"id2":{"name":"john","class":"9th","subject":"math,english,hindi"},"id3":{"name":"sam","class":"10th","subject":"math,english,hindi"},"id4":{"name":"vedansh","class":"10th","subject":"math,english,sst"}}
result={}
seen_keys = []
for student_id,details in st.items():
    unique_key = (details['name'], details['class'], details['subject'])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k, v in result.items():
    print(f"{k}: {v}")