# 토이 프로젝트 목표: 일정한 구조로 작성된 확장 가능한 설명 데이터를, 3가지 이상의 다양한 복잡도로 사용자에게 표시한다.
# 1단계 : 최고 수준으로 복잡한 설명
# 2단계 : 최고 수준으로 간단한 설명
# 3단계 : 쌈@뽕한 수준으로 작성된 설명

# SUPER_MAXLINE: 코드 전체에서 설명 데이터의 최대 행 개수 제약
SUPER_MAXLINE = 5


class ExplainData:
    def __init__(self):
        # data: 이차원 리스트
        #   rows: "그리고"로 구분 가능한 하나의 설명 묶음, [설명 키워드, (키워드, 값), (키워드, 값), ...]
        self.data = []
        self.MAXLINE = SUPER_MAXLINE

    # pushRows(self, rowKeyword, key, value)
    # rowKeyword가 일치하는 행이 존재하면, 리스트에 (key, value) 튜플을 삽입한다.
    # rowKeyword가 일치하는 행이 없으면, rowKeyword를 첫 원소로 하는 행을 추가한다.
    def pushRow(self, rowKeyword, key, value):

        if not self.data:
            self.data = []

        for row in self.data:
            if row[0] == rowKeyword:
                row.append((key, value))
                return

        if self.MAXLINE > len(self.data):
            self.data.append([rowKeyword, (key, value)])
        else:
            print("explain overflow")

    def getRow(self, rowNumber):
        # print("rowNum: ", rowNumber, "length: ", len(self.data))

        if self.data and self.data != []:
            if rowNumber < len(self.data):
                explainKey = self.data[rowNumber][0]
                explains = self.data[rowNumber][1:]
                return explainKey, explains

        return None, None

    # 행 개수 반환
    def getCardinality(self):
        return len(self.data)


    def isEmpty(self):
        return self.data is None or self.data == []


# ExplainData 클래스 객체와 설명 수준을 미리 정의해야 하는 설명 클래스.
class Explainer:
    def __init__(self, rowData: ExplainData, explainLevel=1):
        # explainLevel은 1 이상의 정수, 1은 최대 복잡도를 의미한다. 커질 수록 단순해진다.
        # rowData는 ExplainData클래스 객체로 제한된다.
        self.explainLevel = explainLevel
        self.rowData = rowData

    def executeRowsMax(self):
        executedExplain = []
        if not self.rowData.isEmpty():
            cardinality = self.rowData.getCardinality()
            for c in range(cardinality):
                rowKeyword, elements = self.rowData.getRow(c)
                executedRow = ""
                if rowKeyword == "normalWeapon":
                    # ("enemy", n), ("spd", 1234), ("atk", 12345678)
                    for elem in elements:
                        if elem[0] == "enemy":
                            executedRow += f"적 {elem[1]}명에게 "
                        if elem[0] == "self":
                            executedRow += f"착용한 캐릭터에게 "
                        if elem[0] == "spd":
                            executedRow += f"{float(elem[1]) / 100.0}초마다 "
                        if elem[0] == "atk":
                            executedRow += f"공격력의 {(float(elem[1]) / 10000):.{3}f}% 대미지를 가한다. "
                if rowKeyword == "healingWeapon":
                    # ("enemy", n), ("spd", 1234), ("heal", 12345678)
                    for elem in elements:
                        if elem[0] == "enemy":
                            executedRow += f"적 {elem[1]}명에게 "
                        if elem[0] == "self":
                            executedRow += f"착용한 캐릭터에게 "
                        if elem[0] == "spd":
                            executedRow += f"{float(elem[1]) / 100.0}초마다 "
                        if elem[0] == "heal":
                            executedRow += f"치유력의 {(float(elem[1]) / 10000):.{3}f}% 치유를 가한다. "
                executedExplain.append(executedRow)

        return "그리고, ".join(executedExplain)

    def executeRowsMin(self):
        executedExplain = []
        if not self.rowData.isEmpty():
            cardinality = self.rowData.getCardinality()
            for c in range(cardinality):
                rowKeyword, elements = self.rowData.getRow(c)
                executedRow = ""
                if rowKeyword == "normalWeapon":
                    # ("enemy", n), ("spd", 1234), ("atk", 12345678)
                    for elem in elements:
                        if elem[0] == "enemy":
                            if elem[1] == 1:
                                executedRow += f"단일 적에게 "
                            else:
                                executedRow += f"여러 명의 적에게 "
                        if elem[0] == "self":
                            executedRow += f"착용한 캐릭터에게 "
                        if elem[0] == "spd":
                            if elem[1] < 51:
                                executedRow += f"매우 빠른 속도로 "
                            elif elem[1] < 101:
                                executedRow += f"빠른 속도로 "
                            elif elem[1] < 201:
                                executedRow += f"보통 속도로 "
                            elif elem[1] < 351:
                                executedRow += f"다소 느린 속도로 "
                            elif elem[1] < 501:
                                executedRow += f"느린 속도로 "
                            else:
                                executedRow += f"매우 느린 속도로 "
                        if elem[0] == "atk":
                            if elem[1] < 1000001:
                                executedRow += f"적은 대미지를 가한다. "  # 100% 이하
                            elif elem[1] < 3000001:
                                executedRow += f"보통 대미지를 가한다. "  # 300% 이하
                            elif elem[1] < 10000001:
                                executedRow += f"강력한 대미지를 가한다. "  # 1000% 이하
                            else:
                                executedRow += f"매우 강력한 대미지를 가한다. "  # 1000% 초과
                if rowKeyword == "healingWeapon":
                    # ("enemy", n), ("spd", 1234), ("heal", 12345678)
                    for elem in elements:
                        if elem[0] == "enemy":
                            if elem[1] == 1:
                                executedRow += f"단일 적에게 "
                            else:
                                executedRow += f"여러 명의 적에게 "
                        if elem[0] == "self":
                            executedRow += f"착용한 캐릭터에게 "
                        if elem[0] == "spd":
                            if elem[1] < 51:
                                executedRow += f"매우 빠른 속도로 "
                            elif elem[1] < 101:
                                executedRow += f"빠른 속도로 "
                            elif elem[1] < 201:
                                executedRow += f"보통 속도로 "
                            elif elem[1] < 351:
                                executedRow += f"다소 느린 속도로 "
                            elif elem[1] < 501:
                                executedRow += f"느린 속도로 "
                            else:
                                executedRow += f"매우 느린 속도로 "
                        if elem[0] == "heal":
                            if elem[1] < 250001:
                                executedRow += f"적은 치유를 가한다. "  # 25% 이하
                            elif elem[1] < 500001:
                                executedRow += f"보통 치유를 가한다. "  # 50% 이하
                            elif elem[1] < 1000001:
                                executedRow += f"강력한 치유를 가한다. "  # 100% 이하
                            else:
                                executedRow += f"매우 강력한 치유를 가한다. "  # 100% 초과
                executedExplain.append(executedRow)

        return "그리고, ".join(executedExplain)
    
    def executeRowsSsam(self):
        executedExplain = []
        if not self.rowData.isEmpty():
            cardinality = self.rowData.getCardinality()
            for c in range(cardinality):
                rowKeyword, elements = self.rowData.getRow(c)
                executedRow = ""
                if rowKeyword == "normalWeapon":
                    # ("enemy", n), ("spd", 1234), ("atk", 12345678)
                    for elem in elements:
                        if elem[0] == "enemy":
                            if elem[1] == 1:
                                executedRow += f"한 놈한테 "
                            else:
                                executedRow += f"여러 놈한테 "
                        if elem[0] == "self":
                            executedRow += f"착용한 놈한테 "
                        if elem[0] == "spd":
                            if elem[1] < 51:
                                executedRow += f"존12나 빠른 속도로 "
                            elif elem[1] < 101:
                                executedRow += f"눈썹 휘날리는 속도로 "
                            elif elem[1] < 201:
                                executedRow += f"그럭저럭한 속도로 "
                            elif elem[1] < 351:
                                executedRow += f"느긋한 속도로 "
                            elif elem[1] < 501:
                                executedRow += f"속 터지는 속도로 "
                            else:
                                executedRow += f"가끔 쌈@뽕하게 "
                        if elem[0] == "atk":
                            if elem[1] < 1000001:
                                executedRow += f"살짝 침. "  # 100% 이하
                            elif elem[1] < 3000001:
                                executedRow += f"세게 침. "  # 300% 이하
                            elif elem[1] < 10000001:
                                executedRow += f"존34나 세게 침. "  # 1000% 이하
                            else:
                                executedRow += f"\'Ak\' 소리 47번 나도록 침 . "  # 1000% 초과
                if rowKeyword == "healingWeapon":
                    # ("enemy", n), ("spd", 1234), ("heal", 12345678)
                    for elem in elements:
                        if elem[0] == "enemy":
                            if elem[1] == 1:
                                executedRow += f"한 놈한테 "
                            else:
                                executedRow += f"여러 놈한테 "
                        if elem[0] == "self":
                            executedRow += f"착용한 놈한테 "
                        if elem[0] == "spd":
                            if elem[1] < 51:
                                executedRow += f"존12나 빠른 속도로 "
                            elif elem[1] < 101:
                                executedRow += f"눈썹 휘날리는 속도로 "
                            elif elem[1] < 201:
                                executedRow += f"그럭저럭한 속도로 "
                            elif elem[1] < 351:
                                executedRow += f"느긋한 속도로 "
                            elif elem[1] < 501:
                                executedRow += f"속 터지는 속도로 "
                            else:
                                executedRow += f"가끔 쌈@뽕하게 "
                        if elem[0] == "heal":
                            if elem[1] < 250001:
                                executedRow += f"침 발라줌. "  # 25% 이하
                            elif elem[1] < 500001:
                                executedRow += f"호 해줌. "  # 50% 이하
                            elif elem[1] < 1000001:
                                executedRow += f"후시딘 발라줌. "  # 100% 이하
                            else:
                                executedRow += f"치료를 해줌 시1봉방거 "  # 100% 초과
                executedExplain.append(executedRow)

        return "그리고, ".join(executedExplain)

    def getExplain(self):
        explain = ""
        if self.explainLevel == 1:
            explain += "자세한 설명: "
            explain += self.executeRowsMax()
        elif self.explainLevel == 2:
            explain += "간단한 설명: "
            explain += self.executeRowsMin()
        elif self.explainLevel == 3:
            explain += "쌈뽕한 설명: "
            explain += self.executeRowsSsam()
        
        else:
            explain += "정의되지 않은 설명 수준"

        return explain

    def printExplain(self):
        print(self.getExplain())

testData: ExplainData = ExplainData()

testData.pushRow("normalWeapon", "enemy", 1)
testData.pushRow("normalWeapon", "spd", 350)
testData.pushRow("normalWeapon", "atk", 12009900)

testData.pushRow("healingWeapon", "self", 1)
testData.pushRow("healingWeapon", "spd", 500)
testData.pushRow("healingWeapon", "heal", 609900)

testExplainer: Explainer = Explainer(testData, 1)
testExplainerEasy: Explainer = Explainer(testData, 2)
testExplainerSsam: Explainer = Explainer(testData, 3)

testExplainer.printExplain()
testExplainerEasy.printExplain()
testExplainerSsam.printExplain()
