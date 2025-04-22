
n=int(input("Enter the number of the process "))

pro=list(range(n))

sta=[1]*n

co=0

def elec(ele):
    global co
    ele=ele-1
    co=ele+1
    for i in range(n):
        if pro[ele]<pro[i]:
            print(f"Election message is sent from {ele+1} to {i+1}")

            if sta[i]==1:
                print(f"Ok message is sent from {i+1} to {ele+1}")
                elec(i+1)

choice=True
cl=1

while choice:
    print("1)Crash Process")
    print("2)Recover Process")
    print("3)Exit")

    ch=int(input("Enter a choice: "))

    if ch==1:
        c=int(input("Enter the process to crash "))
        sta[c-1]=0
        cl=1
    elif ch==2:
        c=int(input("Enter the process to recover "))
        sta[c-1]=1
        cl=1
    elif ch==3:
        choice=False
        cl=0

    if cl==1:
        e=int(input("whch process will initate the election "))
        elec(e)
        print("Final coordinator is ",co)