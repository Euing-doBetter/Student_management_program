import random

student =[]   
class Person:
    grade = random.randint(0,100)
    name=[]
    year = []
    aStudent = ["이름 :",name,"학년 :",year,"점수 :",grade]
    student = aStudent.append(aStudent)

def print_menu():
    print("1.학생 리스트출력")
    print("2.학생검색")
    print("3.학생 신규 등록")
    print("4.최우수 점수 학생정보 출력")
    print("5.학생정보 파일로 저장")
    print("6.학생정보 파일 LOAD")
    print("7.프로그램 종료")

def print_student():
    #ran_score= random.randint(0,100)
    print("name,year,grade")
    for i in range(len(student)):
        print("이름 :",Person.name[i],"학년 :",Person.year[i],"점수 :",Person.grade)

def search():
    search_name=input("학생이름입력")     
    for i in range(len(student)):
        if(search_name==student[i]):
            print("%s를 찾았습니다.",student[i])
        else:
            print("해당이름을 찾지못했습니다.")

def add():
    #new_student = input("학생이름입력")
    Person.name = input("학생이름입력")
    
    Person.year = int(input("학년입력"))
    
    Person.aStudent=Person.year.append(),Person.name.append()
    #new_grade = random.randint(0,100)

def best_score():
    for i in len(student):
        best_score=Person.grade[0]
        if(best_score<Person.grade[i]):
            best_score=Person.grade[i]
            print(best_score)
            print(Person.name[i])
            print(Person.year[i])

def save():
    f=open("student.txt","w")
    data=f.write(Person.aStudent)
    f.close

def load():
    f=open("student.txt","r")
    data=f.read()
    print(data)
    f.close

while True:
    print_menu()
    select_num=int(input("메뉴번호 입력"))
    if(select_num==1):
        print_student()
    elif(select_num==2):
        search()
    elif(select_num==3):
        add()
    elif(select_num==4):
        best_score()
    elif(select_num==5):
        save()
    elif(select_num==6):
        load()
    elif(select_num==7):
        exit()