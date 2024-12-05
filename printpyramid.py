def print_pyramid(x):
    starcount=1
    for i in range (x,0,-1):
        print(i*" ",starcount*"*")
        starcount=starcount+2

def main():
    height=int(input("Enter pyramid height: "))
    print_pyramid(height)

main()