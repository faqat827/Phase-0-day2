def input_():
    data = []
    name = str(input("Name?"))
    data.append(name)
    grades_ch = int(input("checmistry score: "))
    data.append(grades_ch)
    grades_bio = int(input("biology score: "))
    data.append(grades_bio)
    grades_maths = int(input("maths score: "))
    data.append(grades_maths)

    return data


def print_n(data):
    print(f"Name: {data[0]}")
    print(f"Chemistry score: {data[1]}")
    print(f"Biology score: {data[2]}")
    print(f"Maths score: {data[3]}")

def grades(data):
    stu_name = data[0]

    ch_grades = data[1]
    if 90 <= ch_grades <= 100:
        print(f"Your marks are: {ch_grades} and you got A grade in Chemistry")

    elif 80 <= ch_grades <= 89:
        print(f"Your marks are: {ch_grades} and you got B grade in Chemistry ")

    elif 70 <= ch_grades <= 79:
        print(f"Your marks are: {ch_grades} and you got C grade in Chemistry")

    elif 40 <= ch_grades <= 69:
        print(f"Your marks are: {ch_grades} and you got D grade in Chemistry")

    elif 0 <= ch_grades <= 39:
        print(f"Your marks are: {ch_grades} and you are fail in Chemistry")

    
    bio_grades = data[2]
    if 90 <= bio_grades <= 100:
        print(f"Your marks are: {bio_grades} and you got A grade in Biology")

    elif 80 <= bio_grades <= 89:
        print(f"Your marks are: {bio_grades} and you got B grade in Biology ")

    elif 70 <= bio_grades <= 79:
        print(f"Your marks are: {bio_grades} and you got C grade in Biology")

    elif 40 <= bio_grades <= 69:
        print(f"Your marks are: {bio_grades} and you got D grade in Biology")

    elif 0 <= bio_grades <= 39:
        print(f"Your marks are: {bio_grades} and you are fail in Biology")


    
    maths_grades = data[3]
    if 90 <= maths_grades <= 100:
        print(f"Your marks are: {maths_grades} and you got A grade in maths")

    elif 80 <= maths_grades <= 89:
        print(f"Your marks are: {maths_grades} and you got B grade in maths ")

    elif 70 <= maths_grades <= 79:
        print(f"Your marks are: {maths_grades} and you got C grade in maths")

    elif 40 <= maths_grades <= 69:
        print(f"Your marks are: {maths_grades} and you got D grade in maths")

    elif 0 <= maths_grades <= 39:
        print(f"Your marks are: {maths_grades} and you are fail in maths")




## calling the function
data=input_()
print_n(data)
grades(data)