import matplotlib.pyplot as plt

loan = {}
with open("loan_data.csv") as f:
    f.readline()
    for cnt, line in enumerate(f):
        line = line.rstrip().split(',')
        member_id = int(line[0])
        loan_amount = int(line[1])
        loan[member_id] = loan_amount

types = {"MORTGAGE": 0, "OWN": 1, "RENT": 2}
average_loan = [0] * 3
ownership_count = [0] * 3
with open("home_ownership_data.csv") as f:
    f.readline()
    for cnt, line in enumerate(f):
        line = line.rstrip().split(',')
        member_id = int(line[0])
        home_ownership = types[line[1]]
        average_loan[home_ownership] += loan[member_id]
        ownership_count[home_ownership] += 1

for i in range(3):
    average_loan[i] /= ownership_count[i]

print(average_loan)

plt.bar([1,2,3], average_loan)
plt.xticks([1,2,3], ["MORTGAGE", "OWN", "RENT"])
plt.xlabel("Home ownership")
plt.ylabel("Average loan amount ($)")
plt.title("Average loan amounts per home ownership")
plt.show()
        


