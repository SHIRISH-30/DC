# number of the process
n=int(input("Enter the number of the process "))

# time array bana

time=[int(input(f"Enter the time of the process {i+1} ")) for i in range(n)]

#master ka input le

master=int(input(f"Enter the master process "))-1

#now avg the time

avg_diff=(sum(time[i]-time[master] for i in range(n) if i!=master))/(n-1)

#now print the time

print("Average times of the process is ")
for i in range(n):
    print(f"For process {i+1} : {round(avg_diff+time[master])}")