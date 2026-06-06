# HydrogelDataAnalyzer

水凝胶力学性能与理化性质自动化分析工具

用于水凝胶材料实验数据的自动化处理与可视化，支持万能试验机力学测试、溶胀率、降解等数据的批量分析。

---

## 功能

- ✅ **力学测试分析** — 自动识别线性弹性段，计算弹性模量、断裂强度、断裂伸长率
- ✅ **批量对比** — 一键处理多个配方/条件的测试数据，输出对比图
- ✅ **溶胀/降解曲线** — 自动绘制溶胀率、质量剩余随时间变化曲线
- ✅ **报告生成** — 自动输出分析结果图表，方便直接用于论文/组会

---

## 技术栈

| 工具 | 用途 |
|---|---|
| Python 3 | 核心开发语言 |
| Pandas | 数据读取与清洗 |
| NumPy | 数值计算（线性拟合、统计） |
| Matplotlib / Seaborn | 科学绘图 |
| SciPy | 曲线拟合与插值 |

---

## 目录结构

```
HydrogelDataAnalyzer/
├── data/                   # 原始实验数据（CSV / Excel）
├── output/                 # 分析结果与图表输出
├── src/                    # 核心代码
│   ├── mech_analyzer.py    # 力学测试数据分析
│   ├── swell_analyzer.py   # 溶胀/降解数据分析
│   └── plot_utils.py       # 可视化工具函数
├── examples/               # 使用示例
│   └── run_analysis.py
├── requirements.txt        # 依赖列表
└── README.md
```

---

## 快速开始

```bash
git clone https://github.com/PlutoDDD/HydrogelDataAnalyzer
cd HydrogelDataAnalyzer
pip install -r requirements.txt
python examples/run_analysis.py
```

---

## 使用示例

```python
from src.mech_analyzer import MechAnalyzer

# 读取万能试验机数据，自动计算力学参数
analyzer = MechAnalyzer("data/sample_001.csv")
analyzer.calc_modulus()        # 弹性模量
analyzer.calc_strength()       # 断裂强度
analyzer.calc_elongation()     # 断裂伸长率
analyzer.plot_stress_strain()  # 绘制应力-应变曲线

# 批量处理多个配方
analyzer.batch_compare("data/experiment_1/")
```

---

## TODO

- [ ] 力学测试数据自动分析模块
- [ ] 溶胀率分析模块
- [ ] 降解曲线分析模块
- [ ] 批量对比功能
- [ ] 图表风格自定义

---

## 致谢

西安交通大学生物医学工程研究所
