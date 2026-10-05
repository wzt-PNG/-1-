#段位
user_ability = input("你的瓦洛兰特的段位有多高？")
if user_ability in ["赋能","神话"]:
    print("带我飞"+"我的QQ号；3675758919")
elif user_ability in["钻石","铂金"]:
    print("very good")
elif user_ability in["白银","黄金"]:
    print("多练练")
else:
    print("滚")
#评分
user_mark = input("你的最高评分是多少？")
score=int(user_mark)
#判定
if score >=500:
    print("牛b")
elif 150<=score<=400:
    print("一般般")
elif score <=200:
    print("重开")
