"""
class (成人の)BMI:
     関連しそうな属性：
　　　　　 -身長
       -体重
       -BMIという値そのもの
   　　ルール：
   　　　 -10以上40以下<--常識的な範囲
   　　　　-表示するときは、少数第2位まで
   　　　　-ex:23.678 -> 23.67
   　　できること：
   　　　　-？？
"""
# クラス名はUpperCamelClassが普通
class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 40):
            raise ValueError('BMIの値が正常値の範囲外です')

    def __str__(self):
        return f'{self.value:.2f}'


# BMIクラスのインスイタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)
print(hibiki_bmi)

ohira_bmi = BMI(height=1.78, weight=75.0)
print(ohira_bmi)

yabai_bmi = BMI(height=1.78, weight=75000.0)
print(ohira_bmi)
