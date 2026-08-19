# -*- coding: utf-8 -*-
"""
模拟学生成绩数据，进行数据清洗、统计分析和可视化展示。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置随机种子
np.random.seed(42)

# ==================== 1. 生成模拟数据 ====================
n_students = 1000

student_ids = np.arange(1, n_students + 1)
classes = np.random.choice(['A', 'B', 'C', 'D'], size=n_students)
genders = np.random.choice(['M', 'F'], size=n_students)

math_scores = np.random.normal(70, 15, n_students)
math_scores = np.clip(math_scores, 0, 100).astype(int)

chinese_scores = np.random.normal(65, 12, n_students)
chinese_scores = np.clip(chinese_scores, 0, 100).astype(int)

english_scores = np.random.normal(75, 10, n_students)
english_scores = np.clip(english_scores, 0, 100).astype(int)

physics_scores = np.random.normal(68, 14, n_students)
physics_scores = np.clip(physics_scores, 0, 100).astype(int)

# ==================== 2. 创建 DataFrame ====================
df = pd.DataFrame({
    'StudentID': student_ids,
    'Class': classes,
    'Gender': genders,
    'Math': math_scores,
    'Chinese': chinese_scores,
    'English': english_scores,
    'Physics': physics_scores
})

df['Class'] = df['Class'].astype('category')
df['Gender'] = df['Gender'].astype('category')

# 添加缺失值
missing_math_idx = np.random.choice(df.index, size=10, replace=False)
df.loc[missing_math_idx, 'Math'] = np.nan
missing_eng_idx = np.random.choice(df.index, size=8, replace=False)
df.loc[missing_eng_idx, 'English'] = np.nan

print("===== 前5行数据 =====")
print(df.head(), "\n")

# ==================== 3. 数据清洗 ====================
print("===== 数据集信息 =====")
print(df.info(), "\n")

print("===== 描述性统计 =====")
print(df.describe(), "\n")

print("===== 缺失值统计 =====")
print(df.isnull().sum(), "\n")

# 中位数填充
df['Math'] = df['Math'].fillna(df['Math'].median())
df['English'] = df['English'].fillna(df['English'].median())

print("===== 填充后缺失值统计 =====")
print(df.isnull().sum(), "\n")

# 添加总分和平均分
df['Total'] = df[['Math', 'Chinese', 'English', 'Physics']].sum(axis=1)
df['Average'] = df[['Math', 'Chinese', 'English', 'Physics']].mean(axis=1)

# 分组统计
grouped = df.groupby(['Class', 'Gender'])[['Math', 'Chinese', 'English',
                                           'Physics', 'Average']].mean().round(2)
print("===== 按班级和性别的各科平均分 =====")
print(grouped, "\n")

pivot = df.pivot_table(values='Total', index='Class', columns='Gender',
                       aggfunc='mean').round(2)
print("===== 各班级不同性别平均总分 =====")
print(pivot, "\n")

# ==================== 4. 可视化（修正版） ====================
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('学生成绩数据分析可视化', fontsize=20)

# ---- 子图1: 各科成绩分布直方图（改用 ax.hist） ----
ax1 = axes[0, 0]
# 分别绘制每科，避免 pandas hist 的冲突
subjects = ['Math', 'Chinese', 'English', 'Physics']
colors = ['blue', 'orange', 'green', 'red']
for i, subject in enumerate(subjects):
    ax1.hist(df[subject], bins=20, alpha=0.5, label=subject, color=colors[i], edgecolor='black')
ax1.set_title('各科成绩分布直方图')
ax1.set_xlabel('分数')
ax1.set_ylabel('频数')
ax1.legend()

# ---- 子图2: 各班级数学成绩箱线图（移除 palette） ----
ax2 = axes[0, 1]
sns.boxplot(x='Class', y='Math', data=df, ax=ax2)  # 移除 palette
ax2.set_title('各班级数学成绩箱线图')
ax2.set_xlabel('班级')
ax2.set_ylabel('数学分数')

# ---- 子图3: 各班级总分小提琴图（移除 palette） ----
ax3 = axes[0, 2]
sns.violinplot(x='Class', y='Total', data=df, ax=ax3, inner='quartile')  # 移除 palette
ax3.set_title('各班级总分小提琴图')
ax3.set_xlabel('班级')
ax3.set_ylabel('总分')

# ---- 子图4: 数学 vs 英语 散点图 ----
ax4 = axes[1, 0]
sns.scatterplot(x='Math', y='English', hue='Gender', data=df, ax=ax4,
                palette={'M': 'blue', 'F': 'red'}, alpha=0.6)
ax4.set_title('数学 vs 英语 散点图 (按性别)')
ax4.set_xlabel('数学分数')
ax4.set_ylabel('英语分数')
ax4.legend(title='性别')

# ---- 子图5: 相关性热力图 ----
ax5 = axes[1, 1]
corr = df[['Math', 'Chinese', 'English', 'Physics']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', square=True,
            ax=ax5, cbar=True, linewidths=0.5)
ax5.set_title('各科成绩相关性热力图')

# ---- 子图6: 分组条形图 ----
ax6 = axes[1, 2]
grouped_mean = df.groupby(['Class', 'Gender'])['Average'].mean().unstack()
grouped_mean.plot(kind='bar', ax=ax6, color=['#1f77b4', '#ff7f0e'])
ax6.set_title('各班级不同性别的平均分')
ax6.set_xlabel('班级')
ax6.set_ylabel('平均分')
ax6.legend(title='性别')
ax6.grid(axis='y', linestyle='--', alpha=0.7)

# ---- 调整布局，避免 tight_layout 警告 ----
# 使用 fig.tight_layout 并传入 rect，或使用 subplots_adjust
fig.tight_layout(rect=[0, 0, 1, 0.96])  # 直接作用于 figure 对象

plt.show()

# ==================== 5. Pairplot ====================
cols = ['Math', 'Chinese', 'English', 'Physics', 'Total', 'Average', 'Gender']
sns.pairplot(df[cols], hue='Gender', diag_kind='hist', palette='Set2')
plt.suptitle('所有数值变量的配对关系图', y=1.02)
plt.show()

print("示例教学代码执行完毕（无警告）！")