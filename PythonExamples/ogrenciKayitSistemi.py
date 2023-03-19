students = ["Gülse Yavuz", "Engin Demiroğ", "Halit Kalaycı"]

print(students)

print("*************************")

#Aldığı isim soyisim ile listeye öğrenci ekleyen

def studentAdd():
    name = input("Öğrenci adı giriniz: ")
    surname = input("Öğrenci soyadı giriniz: ")

    students.append(name + " " + surname)
    print("Öğrenci listeye eklendi")
    print(students)
studentAdd()  

print("*************************")

#Aldığı isim soyisim ile eşleşen değeri listeden kaldıran

def studentRemove():
    name = input("Silinecek öğrencinin ismini giriniz: ")
    surname = input("Silinecek öğrencinin soyadını giriniz: ")
    
    students.remove(name + " " + surname)
    print("Öğrenci listeden silindi.")
    print(students)
studentRemove()    

print("*************************")

#Listeye birden fazla öğrenci eklemeyi mümkün kılan

def studentsAdd():
    number = int(input("Kaç tane öğrenci eklenecek: "))
    for i in range(number):
        addStudentInfo = input("Eklenecek öğencinin adı ve soyadı: ")
        students.append(addStudentInfo)
        i = i + 1
        print("Yeni öğrenciler listeye eklendi.")
        print(students)
studentsAdd()

print("*************************")

#Listedeki tüm öğrencileri tek tek ekrana yazdıran

def studentList():
    student = 0
    for student in range(len(students)):
        print(students[student])
        student = student + 1
print("Öğrenciler listelendi.")   
studentList()

print("*************************")

#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrenci numarası öğrenmeyi mümkün kılan fonksiyon

def findStudentNumber():
    student = input("Numarası öğrenilecek öğrencinin adı ve soyadı: ")
    i = 0 
    while i < len(students):
        if students[i] == student:
            print("Öğrenci numarası: ")
            print(i)
            break
        i = i + 1
findStudentNumber()    


print("*************************")

#Listede birden fazla öğrenci silmeyi mümkün kılan fonksiyon

def studentsRemove():
    deleteNumber = int(input("Listeden silinecek öğrenci sayısı: "))
    i = 0
    for i in range(deleteNumber):
        studentDelete = input("Listeden silinecek öğrencinin adı ve soyadı: ")
        students.remove(studentDelete)
        i = i + 1
        print("Öğrenciler silindi.")
        print(students)
studentsRemove()        



    