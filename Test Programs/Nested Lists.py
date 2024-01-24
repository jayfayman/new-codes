if __name__ == '__main__':
    students =int(input ("Enter the total number of students: "))
    stu=[]
    record=[]
    for i in range(0,students):
        name = (input(f"Enter the name of student {i+1}: "))
        marks = (input(f"Enter the marks of student {i+1}: "))
        stu.append(name)
        stu.append (marks)
        record.append(stu)
        stu = []
    min_mark = min(x[1] for x in record)
    record = [x for x in record if x[1] > min_mark]
    #print (record)
    min2_mark = min(x[1] for x in record)
    record = sorted([x[0] for x in record if x[1] == min2_mark])
    #print (record)
    for x in record:
        print(x)

