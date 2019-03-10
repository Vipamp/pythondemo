import random

gradeNames = ["一年级", "二年级"]
gradeClassMap = {"一年级":"卓越材料1801,卓越材料1802", "二年级":"卓越材料1701,卓越材料1702"}
classes = {"卓越材料1801":47, "卓越材料1802":48, "卓越材料1701":47, "卓越材料1702":52}
 
# 1、统计每个年级有多少人：
for i in range(0, len(gradeNames)):
    sum = 0
    classname = gradeClassMap[gradeNames[i]].split(",")
    for j in range(0, len(classname)):
        sum += classes[classname[j]]
    print(gradeNames[i] + "一共有" + str(sum) + "人")
 
# 2、打印每个班有多少人
for i in range(0, len(gradeNames)):
    classname = gradeClassMap[gradeNames[i]].split(",")
    for j in range(0, len(classname)):
        print(classname[j] + "有" + str(classes[classname[j]]) + "人")
 
# 3、为每个人随机分配成绩
score = {"卓越材料1801":[], "卓越材料1802":[], "卓越材料1701":[], "卓越材料1702":[] }

# 4、为每个人生成随机分数
for i in range(0, len(gradeNames)):
    classname = gradeClassMap[gradeNames[i]].split(",")
    for j in range(0, len(classname)):
        num = classes[classname[j]]
        list = []
        for k in range(0, num):
            list.append(random.randint(0, 50) + 50)
        score[classname[j]] = list
 
# 5、统计分数
scoreMap = {5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

for i in range(0, len(gradeNames)):
    classname = gradeClassMap[gradeNames[i]].split(",")
    for j in range(0, len(classname)):
        list = score[classname[j]]
        for k in range(0, len(list)):
            level = list[k] // 10
            scoreMap[level] = scoreMap[level] + 1

for i in range(5, 11):
    if i < 10:
        print("从" + str(i * 10) + "到" + str(i * 10 + 9) + "一共有：" + str(scoreMap[i]) + "人")
    else:
        print("100分有" + str(scoreMap[i]) + "人")
