"""
溶胀率与降解数据分析模块

处理水凝胶溶胀率、降解率随时间变化的实验数据。
"""

import numpy as np
import pandas as pd
from .plot_utils import PlotUtils


class SwellAnalyzer:
    """溶胀率分析器"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_data(self) -> pd.DataFrame:
        """读取溶胀实验数据"""
        if self.filepath.endswith(".csv"):
            self.data = pd.read_csv(self.filepath)
        else:
            self.data = pd.read_excel(self.filepath)
        return self.data

    def calc_swelling_ratio(self) -> pd.Series:
        """计算溶胀率 SR = (Wt - Wd) / Wd * 100%"""
        # TODO: 根据实际数据列名调整
        dry_weight = self.data["dry_weight"]
        wet_weight = self.data["wet_weight"]
        swelling_ratio = (wet_weight - dry_weight) / dry_weight * 100
        self.data["swelling_ratio"] = swelling_ratio
        return swelling_ratio

    def plot_swelling_curve(self, save_path: str = None):
        """绘制溶胀率-时间曲线"""
        PlotUtils.plot_line(
            x=self.data["time"],
            y=self.data["swelling_ratio"],
            xlabel="Time (h)",
            ylabel="Swelling Ratio (%)",
            title="Swelling Curve",
            save_path=save_path,
        )


class DegradationAnalyzer:
    """降解数据分析器"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_data(self) -> pd.DataFrame:
        """读取降解实验数据"""
        if self.filepath.endswith(".csv"):
            self.data = pd.read_csv(self.filepath)
        else:
            self.data = pd.read_excel(self.filepath)
        return self.data

    def calc_mass_remaining(self) -> pd.Series:
        """计算质量剩余百分比"""
        # TODO: 根据实际数据列名调整
        initial_mass = self.data["initial_weight"]
        current_mass = self.data["current_weight"]
        mass_remaining = current_mass / initial_mass * 100
        self.data["mass_remaining"] = mass_remaining
        return mass_remaining

    def plot_degradation_curve(self, save_path: str = None):
        """绘制降解曲线"""
        PlotUtils.plot_line(
            x=self.data["time"],
            y=self.data["mass_remaining"],
            xlabel="Time (days)",
            ylabel="Mass Remaining (%)",
            title="Degradation Curve",
            save_path=save_path,
        )
