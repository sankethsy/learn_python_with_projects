marks=[]

for x in range(5):
    mark=int(input("Enter the Marks: "))
    marks.append(mark)

print(marks)

highest=max(marks)
print(f"Your highest Marks is {highest}")

lowest=min(marks)
print(f"Your Lowest marks is {lowest}")
averae=int(sum(marks)/len(marks))
print(f"Your Avg is {averae}")