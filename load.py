def print_load(process,server):
    each = process // server
    extra = process % server

    for i in range(extra):
        print(f"Server {i+1} has process {each+1}")
    for i in range(extra, server):
        print(f"Server {i+1} has process {each}")


def main():
    process = int(input("Enter number of the processes "))
    server=int(input("Enter number of the servers "))

    while True:
        print_load(process,server)
        print("1)Add server")
        print("2)Remove server")
        print("3)Add process")
        print("4)Remove process")
        print("5)Exit")
        ch=int(input("Enter a choice "))

        if ch==1:
            add=int(input("Enter the server to add "))
            server+=add
        elif ch==2:
            remove=int(input("Enter the server to remove "))
            server=server-remove
        elif ch==3:
            add_p=int(input("Enter the process to add "))
            process=process+add_p
        elif ch==4:
            remove_p=int(input("Enter the process to remove "))
            process=process-remove_p
        elif ch==5:
            break


if __name__ == "__main__":
    main()