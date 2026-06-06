"""
力学测试数据分析模块

用于处理万能试验机输出的应力-应变数据,
自动计算弹性模量、断裂强度、断裂伸长率等参数。
"""

import numpy as np
import pandas as pd
from .plot_utils import PlotUtils


class MechAnalyzer:
    """力学测试数据分析器"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None
        self.params = {}

    def load_data(self) -> pd.DataFrame:
        """读取万能试验机输出数据（支持 CSV / Excel）"""
        if self.filepath.endswith(".csv"):
            self.data = pd.read_csv(self.filepath)
        else:
            self.data = pd.read_excel(self.filepath)
        return self.data

    def calc_modulus(self, strain_range=(0.05, 0.15)) -> float:
        """计算弹性模量（应力-应变曲线线性段斜率）"""
        # TODO: 根据实际数据列名调整
        strain = self.data["strain"]
        stress = self.data["stress"]
        mask = (strain >= strain_range[0]) & (strain <= strain_range[1])
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        self.params["modulus"] = coeffs[0]
        return self.params["modulus"]

    def calc_strength(self) -> float:
        """计算断裂强度（最大应力值）"""
        stress = self.data["stress"]
        self.params["strength"] = stress.max()
        return self.params["strength"]

    def calc_elongation(self) -> float:
        """计算断裂伸长率"""
        strain = self.data["strain"]
        self.params["elongation"] = strain.max()
        return self.params["elongation"]

    def plot_stress_strain(self, save_path: str = None):
        """绘制应力-应变曲线"""
        PlotUtils.plot_line(
            x=self.data["strain"],
            y=self.data["stress"],
            xlabel="Strain",
            ylabel="Stress (MPa)",
            title="Stress-Strain Curve",
            save_path=save_path,
        )

    def batch_compare(self, folder_path: str):
        """批量对比多个配方的力学性能"""
        # TODO: 批量读取文件夹内所有数据文件，绘制对比图
        pass
