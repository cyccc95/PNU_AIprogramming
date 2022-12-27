import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations

def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환
    p = createProblem()   # 'p': (expr, domain)

    # Call the search algorithm
    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    # solution, minimum = steepestAscent(p)
    # init = steepestAscent(p)
    # # Show the problem and algorithm settings
    # describeProblem(p)
    # displaySetting()

    # # Report results
    # displayResult(solution, minimum)

def createProblem(): ###
    fileName = input("Enter the file name of a TSP: ")
    infile = open(fileName, 'r')
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()

    while line != '':
        locations.append(eval(line))
        line = infile.readline()

    table = calDistanceTable(numCities, locations)
    return numCities, locations, table

def calDistanceTable(numCities, locations):
    table = []
    for i in range(numCities):
        row = []
        for j in range(numCities):
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]

def steepestAscent(p):
    # Random한 초기값을 생성
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True:
        # mutant를 생성
        neighbors = mutants(current, p)
        # mutant 중 가장 좋은 solution을 선택
        # 각각의 neighbor에 대해서 함수 값을 계산해보고,
        # 현재 값보다 좋은 것이 있으면 거기로 이동
        # best solution 업데이트
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
            # print(valueC)
            # print(current)
    
    # Best solution과 그때의 Cost를 반환
    return current, valueC

def randomInit(p):
    # Return a random initial point
    # as a list of values
    # 초기 값을 만들기 위해 랜덤한 값들을 만들기
    domain = p[1]
    low, up = domain[1], domain[2]
    init = []

    # domain의 low, up 정보를 이용해
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환
    # for l, u in zip(low, up):
    #     init.append(round(random.uniform(l, u), 1))
    for i in range(len(low)):
        init.append(random.uniform(low[i], up[i]))

    return init    

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables

    # Number of evaluation을 기록하기 위해 global 변수 이용
    global NumEval
    NumEval += 1

    # expression과 variable name을 읽어오고
    # 이를 이용해 x=value 형태의 string을 만든 뒤,
    # exec 를 이용해 실제로 실행하여 값을 할당 후
    # expression에 eval을 이용해 함수 값을 계산
    expression = p[0]
    domain = p[1]
    varName = domain[0]
    
    for i in range(len(current)):
        exec(varName[i] + '=' + str(current[i]))
    
    valueC = eval(expression)   
    
    return valueC

def mutants(current, p):
    # Return a set of successors
    # mutate 함수를 사용해 +DELTA, -DELTA 두가지 경우에 대한 mutant 생성
    # 모든 변수에 대해 mutation 실시하여 list 형태로 저장하여 반환
    neighbors = []
    for i in range(len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors     

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    # 현재 값에대한 복사본을 slicing을 이용해 생성
    neighbor = current[:]
    # 복사 된 값에 mutation을 실시하며, 이 때 domain 정보를 이용해
    # low <= value <= up 사이의 유효한 값이 얻어지도록 확인
    domain = p[1]
    low, up = domain[1], domain[2]
    if low[i] <= neighbor[i] + d <= up[i]:
        neighbor[i] += d
    # neighbor : 값이 5개 들어있는 list (current와 동일한 형태)
    return neighbor

def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환
    
    # 1. 가장 처음 sample을 best라고 가정한다.
    best = neighbors[0]
    bestValue = evaluate(best, p)
    # 2. 두 번째부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
    # 3. 모두 다 비교가 끝났으면 best를 반환
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
