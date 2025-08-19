if __name__ == '__main__':
    N = int(input())   
    lst = []           

    for _ in range(N):
        command = input().split()
        action = command[0]

        if action == "insert":
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif action == "print":
            print(lst)
        elif action == "remove":
            e = int(command[1])
            lst.remove(e)
        elif action == "append":
            e = int(command[1])
            lst.append(e)
        elif action == "sort":
            lst.sort()
        elif action == "pop":
            lst.pop()
        elif action == "reverse":
            lst.reverse()
