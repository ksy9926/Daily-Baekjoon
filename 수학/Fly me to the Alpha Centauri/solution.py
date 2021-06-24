T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 1
    while True:
        if cnt ** 2 <= dist < (cnt + 1)**2:
            break
        cnt += 1

    if cnt ** 2 == dist:
        print((cnt*2) - 1)
    elif cnt ** 2 < dist <= cnt ** 2 + cnt:
        print(cnt * 2)
    else:
        print((cnt * 2) + 1)


# 참고자료 https://blog.naver.com/wook2124/222097526971




# https://ooyoung.tistory.com/91

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)