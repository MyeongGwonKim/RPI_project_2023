#정수 엔이 주어질 떄, 엔 이하의 짝수를 ㅁ두 더한 값을 리턴하도록 솔루션 함수를 작성해주셍.

num=input('n값을 입력하세요.')
sum=0
for i in range(int(num)+1):
    if(i%2==0):
        sum = i + sum

print(sum)