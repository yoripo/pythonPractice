#BMI
def calculateBMI(weight,height):
    heightInMeter = height / 100 # cm → mに変換
    bmi = weight / (heightInMeter * heightInMeter)
    return bmi #計算結果を返す

def getBMIStatus(bmi):
    if bmi < 18.5:
        return '痩せすぎ'
    elif bmi < 25:
        return '標準'
    elif bmi < 30:
        return 'やや肥満'
    else:
        return 'お肥満'

userWeight = 70  #体重(kg)
userHeight = 168 #身長
bmi = calculateBMI(userWeight,userHeight)
wordBmi = getBMIStatus(bmi)
print (wordBmi)
print (getBMIStatus(calculateBMI(170,170)))



