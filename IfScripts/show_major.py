student_name = "Mary Rivera"
student_major = "STATS"

match student_major:
    case "BIOL":
        print(f'''Student Name: {student_name}
Name of major: Biology
Location: Science Bldg, Room 310''')
    case "CSCI":
        print(f'''Student Name: {student_name}
Name of major: Computer Science 
Location: Sheppard Hall, Room 314''')    
    case "ENG":
        print(f'''Student Name: {student_name}
Name of major: English 
Location: Kerr Hall, Room 201''')
    case "HIST":
        print(f'''Student Name: {student_name}
Name of major: History
Location: Kerr Hall, Room 114''')
    case "MKT":
        print(f'''Student Name: {student_name}
Name of major: Marketing
Location: Westly Hall, Room 310''')
    case other:
        print(f'''Student Name: {student_name}
Name of major: <unknown>''')            
