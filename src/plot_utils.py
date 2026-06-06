"""
可视化工具函数
"""

import matplotlib.pyplot as plt
import seaborn as sns


class PlotUtils:
    """科学绘图工具"""

    @staticmethod
    def set_style():
        """设置统一的图表风格"""
        sns.set_theme(style="whitegrid", font_scale=1.2)
        plt.rcParams["figure.figsize"] = (8, 6)
        plt.rcParams["figure.dpi"] = 150

    @staticmethod
    def plot_line(x, y, xlabel="", ylabel="", title="", save_path=None):
        """绘制折线图"""
        PlotUtils.set_style()
        plt.figure()
        plt.plot(x, y, marker="o", linewidth=2)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()

    @staticmethod
    def plot_comparison(data_dict, xlabel="", ylabel="", title="", save_path=None):
        """绘制多条曲线对比图"""
        PlotUtils.set_style()
        plt.figure()
        for label, (x, y) in data_dict.items():
            plt.plot(x, y, marker="o", linewidth=2, label=label)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()
