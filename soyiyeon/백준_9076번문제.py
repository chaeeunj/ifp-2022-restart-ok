# 한국 체조협회에서는 심판의 오심을 막기 위하여 점수 집계 시스템을 고치기로 하였다.
# 이전에는 5명의 심판이 1점부터 10점까지 정수의 점수를 주면 최고점과 최저점을 하나씩 제외한 점수의 합을 총점으로 하였다.
# 이를 보완하기 위해서 최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상 나게 되면 점수 조정을 거쳐서 다시 점수를 매기려고 한다.
# 점수를 집계하여 총점을 계산하거나, 점수 조정을 거쳐서 다시 점수를 매기려고 하는 경우에는 총점 대신 KIN(Keep In Negotiation)을 출력하는 프로그램을 작성하시오.

x = int(input())
for i in range(x):
    points = list(map(int, input().split()))
    points.remove(max(points))
    points.remove(min(points))
    if max(points) - min(points) >= 4:
        print('KIN')
    else:
        print(sum(points))
