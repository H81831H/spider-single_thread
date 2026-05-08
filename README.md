# Spider Single Thread 爬虫项目

一个包含多个单线程网络爬虫脚本的集合，用于爬取各大网站数据。所有脚本均采用单线程实现，便于学习和理解爬虫原理。

## 📁 项目结构

### 爬虫脚本

| 脚本名称 | 功能描述 | 目标网站 | 备注 |
|---------|--------|--------|------|
| `163music_comment.py` | 爬取网易云音乐歌曲评论 | music.163.com | 包含AES加密参数处理 |
| `逆向网易云评论.py` | 网易云音乐评论爬虫（中文命名版本） | music.163.com | 同上，逆向工程实现 |
| `spider-douban_TOP250.py` | 爬取豆瓣电影TOP250排行榜 | movie.douban.com | BeautifulSoup解析 |
| `抓取豆瓣电影TOP250.py` | 豆瓣电影爬虫（中文命名版本） | movie.douban.com | 正则表达式提取信息 |
| `spider-book_dangdang_TOP500.py` | 爬取当当网热销书TOP500 | bang.dangdang.com | 图片信息提取 |
| `抓取当当网热销书TOP500.py` | 当当网爬虫（中文命名版本） | bang.dangdang.com | - |
| `spider-nuantang_picture.py` | 爬取暖糖壁纸并下载 | nuantang.net | 包含图片下载功能 |
| `抓取暖糖壁纸.py` | 暖糖壁纸爬虫（中文命名版本） | nuantang.net | API接口爬取 |

### 数据处理脚本

| 脚本名称 | 功能描述 |
|---------|--------|
| `Athlete_information.py` | 运动员信息数据清洗、分析和可视化 |
| `Data_analysis-Athlete_information.py` | 运动员信息数据的描述性统计分析 |
| `os_test.py` | 文件系统操作演示（创建、读取、删除文件） |

## 🚀 快速开始

### 环境要求

- Python 3.7+
- 依赖库：

```bash
pip install requests beautifulsoup4 lxml pycryptodome pandas numpy matplotlib
```

### 安装依赖

```bash
pip install -r requirements.txt
```

## 📖 使用示例

### 1. 爬取网易云音乐评论

```python
python 163music_comment.py
```

**功能特点：**
- 使用AES加密处理请求参数
- 通过cursor实现分页爬取
- 防反爬机制（请求间隔1秒）
- 支持获取指定歌曲的全部评论

### 2. 爬取豆瓣电影TOP250

```python
python spider-douban_TOP250.py
```

**功能特点：**
- 爬取豆瓣电影排行榜
- 使用正则表达式提取电影标题
- 自动保存结果到CSV文件

### 3. 爬取暖糖壁纸并下载

```python
python spider-nuantang_picture.py
```

**功能特点：**
- 调用API接口获取壁纸数据
- 自动下载高清壁纸到本地
- 按标签分类保存

### 4. 运动员信息数据分析

```python
python Athlete_information.py
```

**功能特点：**
- CSV数据读取与清洗
- 缺失值和异常值处理
- 描述性统计分析
- 数据可视化（matplotlib）

## ⚠️ 注意事项

1. **遵守法律法规**：请遵守各网站的`robots.txt`和用户协议
2. **反爬机制**：脚本已包含延迟机制，请勿过度请求
3. **User-Agent**：已配置浏览器标识，避免被识别为爬虫
4. **数据隐私**：爬取的数据仅供学习使用，不得用于商业目的

## 🔒 技术要点

### 加密处理
- 使用`pycryptodome`库实现AES-CBC加密
- 网易云音乐API参数加密解析

### 数据提取
- BeautifulSoup HTML解析
- 正则表达式pattern匹配
- JSON API响应处理

### 数据处理
- pandas数据清洗（去重、缺失值处理）
- numpy统计分析
- matplotlib数据可视化

## 📊 输出示例

### 爬虫脚本输出
```
正在爬取第 1 页...
评论内容: 这是一条评论
评论内容: 这是另一条评论
...
共爬取 100 条评论
```

### 数据分析输出
- CSV格式的清洗后数据
- Excel格式的描述性统计表
- 可视化图表

## 🛠️ 自定义配置

### 修改爬取参数

以网易云音乐为例，修改以下部分：

```python
"rid": "R_SO_4_3320292186",  # 歌曲ID
"threadId": "R_SO_4_3320292186",  # 线程ID
"pageSize": "20",  # 每页评论数
```

### 修改文件路径

数据处理脚本中的文件路径需要根据本地环境修改：

```python
path = "D:\\1-工作文件\\python大作业\\运动员信息表(清洗后的).csv"
# 修改为你的本地路径
```

## 📝 脚本详解

### 163music_comment.py
- **加密方式**：双重AES-CBC加密
- **分页方式**：基于时间戳cursor
- **反爬策略**：1秒延迟 + User-Agent伪装

### Athlete_information.py
- **数据清洗**：去重、缺失值检测、异常值处理
- **统计分析**：均值、中位数、众数、标准差等
- **分析维度**：省份分布、项目分布、身高范围、BMI评估

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 👤 作者

H81831H

## 📮 联系方式

如有问题，欢迎通过GitHub Issues进行讨论。

---

**最后更新**：2026年5月8日

**提示**：本项目仅供学习和研究使用，使用者需自行承担使用本代码产生的一切后果。
