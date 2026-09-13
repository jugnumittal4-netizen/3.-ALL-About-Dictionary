st = {"id1": {"name": "Alice", "class": "10th", "subject": "math,english,hindi"},
      "id2": {"name": "Bob", "class": "10th", "subject": "science,history,geography"},
      "id3": {"name": "charlie", "class": "10th", "subject": "math,english,hindi"},
      "id4": {"name": "ashu", "class": "10th", "subject": "math,punjabi,hindi"}}
print("Original Dictionary:")
print(st)
print("")
print("id:1",st.get("id1","not found"))
print("")
print("detalis about id:5")
print(st.get("id5","not found"))
st["id2"]["subject"] = "math,english,hindi"
print("")
print("after changing subject of id:2")
print(st.get("id2", "not found"))
st["id5"] = {"name": "david", "class": "10th", "subject": "math,english,hindi"}
print("")
cd = {}
sr = []
for st , i in st.items():
    unique_key = (i['name'], i['class'], i['subject'])
    if unique_key not in sr:
        sr.append(unique_key)
        cd[st] = i
sd = cd
print("after removing duplicates:")
print(sd)
rs = sd.pop("id3", "not found")
print("")
print("after removing id:3")
print(sd)
print("")
print("total students left",len(sd))
print("")
print("========final subject report========")
for si, details in sd.items():
    print(f"{si}: {details}")

