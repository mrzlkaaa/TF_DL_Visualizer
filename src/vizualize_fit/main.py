from __future__ import annotations
from matplotlib import pyplot as plt
import numpy as np
import os

class FitVisualizer:
    #* kwargs are title, scale format
    def __init__(self, figsize:list=[6.4, 4.8],
        **kwargs:dict) -> None:
        self.plt = plt
        self.plt.figure(figsize=figsize, layout='constrained')

    @staticmethod
    def data_to_dict(keys, *data):
        if keys is None:
            keys = np.arange(1, len(data)+1)
        zipped = zip(keys, data)
        to_dict = {str(key): data for key, data in zipped}
        return to_dict

    #* enables for lr plotting for better visualizing
    def secondary_axis(self):  
        return

    def add_labels(self, labels) -> None:
        x,y = labels
        self.plt.xlabel(x)
        self.plt.ylabel(y)

    def add_title(self, title:str) -> None:
        self.plt.title(title)

    def get_fig_num(self) -> str: #* shares result with savefig, save_fit_process
        files = os.listdir(os.getcwd())
        figs = [i for i in files if ".png" in i]
        # if len(figs) == 0:
        #     return "0"
        return str(len(figs))

    #* the idea to write fitting process to file
    #* file name generates upon cwd analysis (check files, generates name (key))
    def save_fit_process(self):
        with open(f"model_fitting_{}.txt", "w") as f:
            for k,v in history.items():
                f.write() #*write with delimeter... (creates columns like style)
        return

    def savefig(self):
        num = self.get_fig_num() 
        self.plt.savefig(f"model_res_{num}.png")

    def plot(self, history:dict, epochs, X=None) -> None: #todo move history to __init__
        if X is None:
            X = np.arange(0, epochs)
        for k,v in history.items():
            self.plt.plot(X, v, label=k)
        self.plt.legend()
        self.plt.show()
