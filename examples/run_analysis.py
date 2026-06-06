"""
使用示例：水凝胶力学性能分析
"""

import os
import sys

# 将 src 目录加入 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.mech_analyzer import MechAnalyzer


def main():
    # 请将你的万能试验机数据 CSV 放到 data/ 目录下
    data_path = "data/sample_001.csv"

    if not os.path.exists(data_path):
        print(f"请先将实验数据放入 {data_path}")
        print("数据格式要求：CSV 文件，包含 'strain' 和 'stress' 两列")
        return

    # 创建分析器并加载数据
    analyzer = MechAnalyzer(data_path)
    analyzer.load_data()

    # 计算力学参数
    modulus = analyzer.calc_modulus()
    strength = analyzer.calc_strength()
    elongation = analyzer.calc_elongation()

    # 输出结果
    print(f"弹性模量:   {modulus:.2f} MPa")
    print(f"断裂强度:   {strength:.2f} MPa")
    print(f"断裂伸长率: {elongation:.2f} %")

    # 绘制应力-应变曲线
    analyzer.plot_stress_strain(save_path="output/stress_strain_curve.png")
    print("应力-应变曲线已保存至 output/stress_strain_curve.png")


if __name__ == "__main__":
    main()
