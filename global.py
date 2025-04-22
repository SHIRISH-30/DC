
def main():
    n=int(input("Enter the number of the process "))

    clocks=[]
    for i in range(n):
        time=int(input((f"Enter time for process {i+1} ")))
        clocks.append(time)

    print("Initally the time was")
    for i in range(n):
        print(f"Process {i+1} Time {clocks[i]}")

    #calculate avg
    avg=sum(clocks) // n
    print(f"The average is {avg}")

    print("The adjusted time will ")
    for i in range(n):
        offset=avg-clocks[i]
        clocks[i]+=offset
        print(f"Process {i+1} offset is {offset}")
        print(f"Process {i+1} Time {clocks[i]}")



if __name__=="__main__":
    main()