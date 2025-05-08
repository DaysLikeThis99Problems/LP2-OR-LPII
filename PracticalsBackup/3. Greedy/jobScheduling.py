
profit = []
jobs = []
deadline = []
heuristics = []  

n = int(input("Enter the number of jobs: "))

for i in range(n):
    p = int(input("Enter the profit of job {}: ".format(i + 1)))
    profit.append(p)
    j = input("Enter the name of job {}: ".format(i + 1))
    jobs.append(j)
    d = int(input("Enter the deadline of job {}: ".format(i + 1)))
    deadline.append(d)
    h = int(input("Enter the heuristic value for job {}: ".format(i + 1)))  
    heuristics.append(h)

profitNJobs = list(zip(profit, jobs, deadline, heuristics))

profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

slot = [0] * (n + 1)
total_profit = 0
ans = ['null'] * (n + 1)

for i in range(n):
    job = profitNJobs[i]
    for j in range(job[2], 0, -1):  
        if slot[j] == 0:
            ans[j] = job[1]
            total_profit += job[0]
            slot[j] = 1
            break

print("Huristic function is the profit according to which job is put")
print("Jobs scheduled with Heuristic Values:")
for i in range(1, n + 1):
    if ans[i] != 'null':
        job_index = jobs.index(ans[i])
        print(f"Job: {ans[i]} | Profit: {profit[job_index]} | Heuristic: {heuristics[job_index]}")

# Output the total profit
print("Total profit:", total_profit)


# Enter the number of jobs:  4
# Enter the profit of job 1:  100
# Enter the name of job 1:  A
# Enter the deadline of job 1:  2
# Enter the heuristic value for job 1:  8
# Enter the profit of job 2:  50
# Enter the name of job 2:  B
# Enter the deadline of job 2:  1
# Enter the heuristic value for job 2:  5
# Enter the profit of job 3:  200
# Enter the name of job 3:  C
# Enter the deadline of job 3:  2
# Enter the heuristic value for job 3:  10
# Enter the profit of job 4:  150
# Enter the name of job 4:  D
# Enter the deadline of job 4:  1
# Enter the heuristic value for job 4:  9
# Huristic function is the profit according to which job is put
# Jobs scheduled with Heuristic Values:
# Job: D | Profit: 150 | Heuristic: 9
# Job: C | Profit: 200 | Heuristic: 10
# Total profit: 350