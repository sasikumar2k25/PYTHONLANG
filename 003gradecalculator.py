#garde calculator in decision making ,strings


pcv = int(input("marks in pcv:"))
ssp = int(input("marks in ssp:"))
edc = int(input("marks in edc:"))

total_marks = pcv+ssp+edc
avg_marks = total_marks/3

percentage = (total_marks/300)*100
grade = ""
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <=90:
    garde = "B" 
elif percentage > 70 and percentage <=80:
    grade ="c"
else :
    grade = "p"

print(f"totalmarks={total_marks}\n averagemarks={avg_marks}\n percentage={percentage} \n Grade={grade}")
