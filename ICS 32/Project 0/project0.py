def cubism():
    x = int(input())

    x -= 1

    A = '+-+'
    B = '| |'
    C = '+-+-+'

    print(A)

    for i in range(x):
        print((i*'  ') + B)
        print((i*'  ') + C)

    print((x*'  ') + B)
    print((x*'  ') + A)

if __name__ == '__main__':
    cubism()
              
