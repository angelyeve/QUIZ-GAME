attempts = 1
aa = 0
score = 0
while attempts > 0:
    print("********************************")
    AA=input("Enter your name: ")
    print("********************************")
    print("""Select of your choice subject:
A. Math
B. Science""")
    a = input("Enter your choice (A or B): ")
    if a == "A":
        score = 0
        print("*********************************")
        print("""1. What is the place value of 6 in 97 564?
    A. Tens
    B. Tenths
    C. Hundreds 
    D. Hundredths""")
        b = input("Enter (A, B, C, or D): ")
        print("*********************************")
        if b == "A":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            score += 5
        print("*********************************")
        print("""2. What is the greatest common factor of 48 and 60.
    A. 6
    B. 12
    C. 4
    D.24""")
        c = input("Enter (A, B, C, or D): ")
        if c == "B":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            score += 5
        print("*********************************")
        print("""3. What is the missing term in the sequence? 1 4 9 16 __ 36 49
    A. 17
    B. 25
    C. 34
    D. 21""")
        d = input("Enter (A, B, C, or D): ")
        if d == "B":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            score += 5
        print("*********************************")
        print("""4. How many faces does a sphere have?
    A. 4
    B. 0
    C. 3
    D. 1""")
        e = input("Enter (A, B, C, or D): ")
        if e == "D":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            score += 5
        print("*********************************")
        print("""5. What is the 10th term in the sequence 2, 5, 8, 11 . . .?
    A. 35
    B. 30
    C. 29
    D. 33""")
        f = input("Enter (A, B, C, or D): ")
        if f == "C":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            score += 5
        else:
            attempts-=1
            print("*********************************")
            print("Congratulations your score is ", score)
            print("*********************************")
    elif a == "B":
        aa = 0
        print("*********************************")
        print("""1. A spider is an insect?
    A. True
    B. False""")
        g = input("Enter (A or B): ")
        if g == "B":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            aa += 5
        print("*********************************")
        print("""2. What is Earth’s only natural satellite?
    A. Sun
    B. Moon
    C. Venus""")
        h = input("Enter (A, B, or C): ")
        if h == "B":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            aa += 5
            print(" ")
        print("*********************************")
        print("""3. What is the closest planet to the Sun?
    A. Mercury
    B. Venus 
    C. Earth""")
        i = input("Enter (A, B, or C): ")
        if i == "A":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            aa += 5
        print("*********************************")
        print("""4. Can humans breathe normally in space as they can on Earth?
    A. Yes
    B. No""")
        j = input("Enter (A or B): ")
        if j == "B":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            aa += 5
        print("*********************************")
        print("""5. Is the sun a star or a planet?
    A. Star
    B. Planet""")
        k = input("Enter (A or B): ")
        if k == "A":
            print(" ")
            print("""Your answer is Correct!
You've got 5pts.""")
            print(" ")
            aa += 5
        else:
            print("*********************************")
            print("Congratulations your score is ", score)
            print("*********************************")
            attempts-= 1
    else:
        print(" ")
        print("Your answer is Wrong!")
        print(" ")
        attempts-=1
    bbb=input("Do you want to play again? A. Yes B. No (A OR B): ")
    while bbb == "A" or bbb=="a":
        print("********************************")
        AA=input("Enter your name: ")
        print("********************************")
        print("""Select of your choice subject:
A. Math
B. Science""")
        a = input("Enter your choice (A or B): ")
        if a == "A":
            score = 0
            print("*********************************")
            print("""1. What is the place value of 6 in 97 564?
    A. Tens
    B. Tenths
    C. Hundreds 
    D. Hundredths""")
            b = input("Enter (A, B, C, or D): ")
            if b == "A":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                score += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""2. What is the greatest common factor of 48 and 60.
    A. 6
    B. 12
    C. 4
    D.24""")
            c = input("Enter (A, B, C, or D): ")
            if c == "B":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                score += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""3. What is the missing term in the sequence? 1 4 9 16 __ 36 49
    A. 17
    B. 25
    C. 34
    D. 21""")
            d = input("Enter (A, B, C, or D): ")
            if d == "B":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                score += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""4. How many faces does a sphere have?
    A. 4
    B. 0
    C. 3
    D. 1""")
            e = input("Enter (A, B, C, or D): ")
            if e == "D":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                score += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""5. What is the 10th term in the sequence 2, 5, 8, 11 . . .?
    A. 35
    B. 30
    C. 29
    D. 33""")
            f = input("Enter (A, B, C, or D): ")
            if f == "C":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                score += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("Congratulations your score is ", score)
            print("*********************************")
        elif a == "B":
            aa = 0
            print("*********************************")
            print("""1. A spider is an insect?
    A. True
    B. False""")
            g = input("Enter (A or B): ")
            if g == "B":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                aa += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""2. What is Earth’s only natural satellite?
    A. Sun
    B. Moon
    C. Venus""")
            h = input("Enter (A, B, or C): ")
            if h == "B":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                aa += 5
                print(" ")
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""3. What is the closest planet to the Sun?
    A. Mercury
    B. Venus 
    C. Earth""")
            i = input("Enter (A, B, or C): ")
            if i == "A":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                aa += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""4. Can humans breathe normally in space as they can on Earth?
    A. Yes
    B. No""")
            j = input("Enter (A or B): ")
            if j == "B":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                aa += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("""5. Is the sun a star or a planet?
    A. Star
    B. Planet""")
            k = input("Enter (A or B): ")
            if k == "A":
                print(" ")
                print("""Your answer is Correct!
You've got 5pts.""")
                print(" ")
                aa += 5
            else:
                print(" ")
                print("Your answer is Wrong!")
                print(" ")
                attempts-=1
            print("*********************************")
            print("Congratulations your score is ", aa)
            print("*********************************")
        else:
            print(" ")
            print("Your answer is Wrong!")
            print(" ")
            attempts-=1
        bbb=input("Do you want to play again? A. Yes B. No (A OR B): ")
        print("*********************************")
    else:
        print("Thank you for playing")



