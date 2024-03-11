# 가게당 팀장 1명, 팀원은 여러명
# 팀장 필수, 팀원만 존재하는 경우 없음
# n개 식당 고객들의 체온을 측정하기 위해 필요한 검사자 수 최솟값

N = int(input())
CUST = list(map(int, input().split()))
LDR, MBR = map(int, input().split())

ans = 0
for i in range(N):
    num = CUST[i]
    num -= LDR
    ans += 1 # 팀장 1명은 고정
    if num <= 0:    # 팀장 1명으로 모든 고객 커버될 때
        continue
    
    ans += (num // MBR)
    if num % MBR != 0:
        ans += 1

print(ans)