"""Render a graphic"""
from typing import List

import matplotlib.pyplot as plt


class GraphFunctionGeneticAlgorithm:
    """Renders the graph of the function f(x)=y"""

    @staticmethod
    def plot_fx_graph(arr: List[str]):
        plt.plot(range(len(arr)), arr)
        plt.grid(True, zorder=0)
        plt.title("Function F(x)=y")
        plt.xlabel("Generation")
        plt.ylabel("Value of f(x)")
        plt.show()
