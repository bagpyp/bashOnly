def main():
    with open('hello.txt') as file:
       for line in file:
           print(line)

if __name__ == '__main__':
    main()
