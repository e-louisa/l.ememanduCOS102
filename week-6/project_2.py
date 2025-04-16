print("Welcome to the PAU Admissions Department. There are two courses available: ")
print("1.Computer Science 2.Mass Communication")
course = int(input("What course do you want to enter?"))

#creating list for admitted and non-admitted candidates
admitted = []
not_admitted = []

#checking conditions for computer science students
if course == 1:
    while True:
        #asking computer science candidates for their inputs
        name = input("What is your name? ")
        score = int(input("Enter your JAMB score: "))
        math = int(input("Enter how many credits you got in maths: "))
        eng = int(input("Enter how many credits you got in english: "))
        phy = int(input("Enter how many credits you got in physics: "))
        chem = int(input("Enter how many credits you got in chemistry: "))
        bio = int(input("Enter how many credits you got in biology: "))
        interview = input("Did you pass the interview? Enter yes/no: ")

        cand_info = []

        #checking against condition
        if score >= 250 and all(x >= 5 for x in [eng, bio, phy, chem, math]) and interview.lower() == "yes":
            print("Congratulations, you are qualified for admission!")
            cand_info.append(name)
            cand_info.append("computer science")
            cand_info.append(score)
            cand_info.append(math)
            cand_info.append(eng)
            cand_info.append(phy)
            cand_info.append(chem)
            cand_info.append(bio)
            cand_info.append("passed interview")
            admitted.append(cand_info)

        elif score < 250 or any(x < 5 for x in [eng, bio, phy, chem, math]) or interview.lower() == "no":
            print("Sorry, you are not qualified for admission into Computer Science.")
            cand_info.append(name)
            cand_info.append("computer science")
            cand_info.append(score)
            cand_info.append(math)
            cand_info.append(eng)
            cand_info.append(phy)
            cand_info.append(chem)
            cand_info.append(bio)
            cand_info.append("failed interview")
            not_admitted.append(cand_info)

        print("The candidates that have been admitted are: ")
        print(admitted)
        print("The candidates that have not been admitted are: ")
        print(not_admitted)

#checking conditions for mass communication students
elif course == 2:
    while True:
        #asking mass comm candidates for their inputs
        name = input("What is your name? ")
        score = int(input("Enter your JAMB score: "))
        math = int(input("Enter how many credits you got in maths: "))
        eng = int(input("Enter how many credits you got in english: "))
        lit = int(input("Enter how many credits you got in literature: "))
        crs = int(input("Enter how many credits you got in CRS: "))
        govt = int(input("Enter how many credits you got in government: "))
        interview = input("Did you pass the interview? Enter yes/no: ")

        cand_info = []

        #checking against condition
        if score >= 230 and all(x >= 5 for x in [eng, govt, crs, lit, math]) and interview.lower() == "yes":
            print("Congratulations, you are qualified for admission!")
            cand_info.append(name)
            cand_info.append("mass communication")
            cand_info.append(score)
            cand_info.append(math)
            cand_info.append(eng)
            cand_info.append(lit)
            cand_info.append(crs)
            cand_info.append(govt)
            cand_info.append("passed interview")
            admitted.append(cand_info)

        elif score < 220 or any(x < 5 for x in [eng, lit, govt, crs, math]) or interview.lower() == "no":
            print("Sorry, you are not qualified for admission.")
            cand_info.append(name)
            cand_info.append("mass communication")
            cand_info.append(score)
            cand_info.append(math)
            cand_info.append(eng)
            cand_info.append(crs)
            cand_info.append(govt)
            cand_info.append(lit)
            cand_info.append("failed interview")
            not_admitted.append(cand_info)

        print("The candidates that have been admitted are: ")
        print(admitted)
        print("The candidates that have not been admitted are: ")
        print(not_admitted)





    


