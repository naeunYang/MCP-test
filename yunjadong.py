# Ctrl + I : AI 채팅
# Ctrl + k : 코드 요청
# 구구단 출력
end = int(input("몇 단까지 출력할까요? "))
for i in range(2, end + 1):
    print(f"\n{i}단:")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")