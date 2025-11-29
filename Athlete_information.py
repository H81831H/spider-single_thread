import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#数据读取与清洗
def read_and_clear():
    #读取csv并转为dataframe
    path="D:\\1-工作文件\\python大作业\\运动员信息表(清洗后的).csv"
    data = pd.read_csv(path, encoding='gbk')
    data = pd.DataFrame(data)

    #查重
    data = data.drop_duplicates()
    #检查缺失值
    columns = ["性别","出生年份（年）","年龄（岁）","身高(cm)","体重(kg)","项目","省份"]
    missing_amount = {}
    for j in columns:
        #输入每列的缺失值数量
        missing_amount[j] = int(data[j].isnull().sum())
    #检查身高异常值(140, 230)cm
    height_error = []
    for i in range(0, len(data)):
        height = data.loc[i, "身高(cm)"]
        if height not in range(140, 230):
            data.loc[i, "身高(cm)"] = f"#{height}#"
            height_error.append((data.loc[i, "姓名"],height))
    #省份格式化
    for i in range(0, len(data)):
        province = data.loc[i, "省份"]
        data.loc[i, "省份"] = province[:2]
    
    #删除出生年份后面的年
    data["出生年份（年）"] = data["出生年份（年）"].str.replace("年", "").astype(int)
    #出生年月与年龄校准
    error = 0
    error_list = []
    for i in range(1,len(data)):
        age = 2018 - data.loc[i, "出生年份（年）"]
        if age != data.loc[i, "年龄（岁）"]:
            data.loc[i, "年龄（岁）"] = age
            error += 1
            error_list.append(data.loc[i, "姓名"])

    
    path_new = "D:\\1-工作文件\\python大作业\\运动员信息表(清洗后的).csv"
    data.to_csv(path, index=False)

    return missing_amount, height_error, error_list, path_new, data

#描述性统计
def descriptive_statistics(data):
    results = []
    index_table = {
            '': ["年龄（岁）", "身高(cm)", "体重(kg)","BMI"],
            '均值': [],
            '中值': [],
            '众数': [],
            '最大': [],
            '最小': [],
            '标准差': [],
            '方差': [],
            '极差': [],
            '四分位数范围': [],
            '偏度': [],
            '峰度': []
        }
    columns = ["年龄（岁）", "身高(cm)", "体重(kg)", "BMI"]
    for item in columns:
        column_data = data[item]
        #均值
        mean = column_data.mean()
        #中位数
        median =column_data.median()
        #众数
        mode = column_data.mode()
        #最小值
        min = column_data.min()
        #最大值
        max = column_data.max()
        #标准差
        standard = column_data.std()
        #方差
        variance = column_data.var()
        #极差
        extremely_poor = max - min
        #四分位数范围
        q1 = column_data.quantile(0.25)
        q3 = column_data.quantile(0.75)
        interquartile_range = q3 - q1
        #偏度
        skewness = column_data.skew()
        #峰度
        kurtosis = column_data.kurtosis()
        #统一为float类型.2f
        results = [mean,median,min,max,standard,variance,extremely_poor,interquartile_range,skewness,kurtosis]
        results = [round(float(i), 2) for i in results]
        #众数返回series类型单独处理
        mode = round(float(mode.iloc[0]), 2)
        results.insert(2, mode)
        
        #输入进字典
        i = 0
        for key in index_table.keys():
            if key != "":
                index_table[key].append(results[i])
                i += 1
            else:
                continue
    #转为dataframe
    path_statistics = "D:\\1-工作文件\\python大作业\\描述性统计.xlsx"
    index_table = pd.DataFrame(index_table).to_excel(path_statistics)

    return path_statistics

#年龄校准
def year_age(data):
    #删除出生年份后面的年
    data["出生年份（年）"] = data["出生年份（年）"].str.replace("年", "").astype(int)

    #出生年月与年龄校准
    error = 0
    error_list = []
    for i in range(1,len(data)):
        age = 2018 - data.loc[i, "出生年份（年）"]
        if age != data.loc[i, "年龄（岁）"]:
            data.loc[i, "年龄（岁）"] = age
            error += 1
            error_list.append(data.loc[i, "姓名"])

    return error_list

#获所有项目与总数
def events_amount(data):
    sports_events = data["项目"].unique()
    sports_events_amount = len(sports_events)
    return sports_events, sports_events_amount

#BMI判断
def bmi_process(data):
    # 运动员BMI判断标准字典
    #公式：BMI = 体重kg / 身高m^2
    bmi_standards = {
        # 耐力型项目         
        '铁人三项': (18.5, 22.0),'男子20公里竞走': (18.5, 21.5),'女子20公里竞走': (18.0, 21.0),'女子中长跑': (18.0, 21.0),'女子800米': (18.5, 21.5),
        '女子马拉松': (17.5, 20.5),  
        #力量型项目
        '举重': (24.0, 32.0),'男子三级跳远': (21.0, 25.0),'女子三级跳远': (20.0, 24.0),'女子链球': (22.0, 28.0),'男子跳高': (20.0, 24.0),
        '女子撑杆跳高': (19.0, 23.0),'女子撑杆跳': (19.0, 23.0),'女子铁饼': (22.0, 27.0),'女子标枪': (20.0, 25.0),
        # 球类项目
        '篮球': (20.0, 26.0),'排球': (19.0, 24.0),'羽毛球': (19.0, 23.0),'乒乓球': (19.0, 23.0),'女子曲棍球': (19.0, 24.0),'曲棍球': (19.0, 24.0),
        '女子水球': (20.0, 25.0),'水球': (21.0, 26.0),
        # 技巧型/艺术型项目 
        '跳水': (18.5, 22.5),'花样游泳': (19.0, 23.0),'蹦床': (19.0, 23.0),'体操': (18.0, 22.0),'艺术体操': (17.5, 21.0),'击剑': (19.0, 23.0),
        '花剑': (19.0, 23.0),
        # 水上项目
        '游泳': (20.0, 25.0),'赛艇': (21.0, 26.0),'皮划艇静水': (21.0, 26.0),'皮划艇激流': (21.0, 26.0),
        # 其他项目
        '射击': (19.0, 25.0),'高尔夫': (20.0, 25.0),'帆船': (20.0, 26.0),'马术': (20.0, 26.0),'自行车': (19.0, 24.0),'网球': (19.0, 24.0),
        '拳击': (20.0, 25.0),'跆拳道': (19.0, 24.0),'女子100米栏': (19.0, 23.0),'射箭': (19.0, 25.0),'男子现代五项': (20.0, 25.0),
        '女子现代五项': (19.0, 24.0),'田径': (19.0, 24.0),  '女子短跑': (19.0, 23.0)
    }

    #初始化运动员BMI列表,不正常BMI列表
    bmi_all = []
    bmi_evalution = []
    bmi_error = []
    
    #遍历每一个运动员
    for i in range(0,len(data)):
        #获取该名运动员所属项目标准BMI
        project = data.loc[i, "项目"]
        bmi = bmi_standards[project]
        low_bmi_limit = bmi[0]
        up_bmi_limit = bmi[1]

        #获取身高体重进行计算,并四舍五入小数点后两位
        height = data.loc[i, "身高(cm)"]
        weight = data.loc[i, "体重(kg)"]
        athlete_bmi = (weight / ((height / 100) ** 2)).round(2)

        #进行BMI判断并添加两个列表
        if athlete_bmi >= low_bmi_limit and athlete_bmi <= up_bmi_limit:
            bmi_all.append(athlete_bmi)
            bmi_evalution.append("正常")
        else:
            bmi_error.append(f"{data.loc[i, "姓名"]}")
            if athlete_bmi < low_bmi_limit:
                bmi_all.append(athlete_bmi)
                bmi_evalution.append("偏低")
            elif athlete_bmi > low_bmi_limit:
                bmi_all.append(athlete_bmi)
                bmi_evalution.append("偏高")

    #dataframe新增一列BMI
    data["BMI"] = bmi_all
    data["BMI评估"] = bmi_evalution
    data.to_csv("D:\\1-工作文件\\python大作业\\运动员信息表+bmi.csv", index=False)
    print("成功保存为'运动员信息表+bmi.csv'")

    return bmi_all, bmi_error

#数据分析_省份与项目
def analysis_province_project(data):
    #统计每个项目最多运动员的省份
    project_top_province = data.groupby('项目')['省份'].apply(lambda x: x.value_counts().index[0]).reset_index()
    project_top_province.columns = ['项目', '优势省份']
    #统计项目该省份运动员的数量
    project_top_count = data.groupby('省份')['项目'].apply(lambda x: x.value_counts().iloc[0]).reset_index()
    project_top_count.columns = ['优势省份', '运动员数量']
    #合并三列
    result = pd.merge(project_top_province, project_top_count, on='优势省份')
    print(result)

#数据分析_项目与身高
def analysis_porject_height(data):
    # 计算每个项目的身高范围
    height_range = data.groupby('项目')['身高(cm)'].agg(['min', 'max']).reset_index()
    height_range['身高范围'] = height_range['min'].astype(str) + ' - ' + height_range['max'].astype(str)

    # 只保留需要的列
    height_range = height_range[['项目', '身高范围', 'min', 'max']]
    height_range.columns = ['项目', '身高范围', '最低身高', '最高身高']

    print(height_range)

#项目数量统计
def analysis_project_count(data):
    #统计运动员最多的前十项目
    top_10_df = data['项目'].value_counts().head(10).reset_index()
    top_10_df.columns = ['项目', '数量']

    #画图
    #设置中文解决负号显示
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False    
    # 创建图形和坐标轴
    plt.figure(figsize=(12, 8))
    # 绘制条形图
    bars = plt.bar(top_10_df['项目'], top_10_df['数量'], color='green', alpha=0.7)
    #添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom')

    plt.title('TOP10项目参与人数', fontsize=20)
    plt.ylabel('数量', fontsize=16)
    plt.show()


if __name__ == "__main__":
   print()







