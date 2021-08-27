def find(N):
    arr=list(bin(N).replace("0b",""))
    arr.append(arr.pop(0))
    return int("".join(arr),2)

def main():
    for _ in range(int(input())):
        n=int(input())
        print(find(n))
if __name__ == "__main__":
    main()