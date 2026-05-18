student_data= {
"id 1":{"name":"Sara",  "class" : "v" , "subject_integration": "english , math , sci ence"},
"id 2":{"name":"Sara",  "class" : "v" , "subject_integration": "english , math , sci ence"},
"id 3 ":{"name":"Sara",  "class" : "v" , "subject_integration": "english , math , sci ence"},
"id 4 ":{"name":"Sara",  "class" : "v" , "subject_integration": "english , math , sci ence"},

}
result ={}
seen_keys = []

for student_id , details in student_data.items():
    unique_key = (details["name"] , details["class"] , details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for x , y in result.items():
    print(x , ":" ,y)
