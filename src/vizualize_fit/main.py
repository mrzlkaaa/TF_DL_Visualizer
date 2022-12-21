from __future__ import annotations
from matplotlib import pyplot as plt
import numpy as np
import os

class FitVisualizer:
    #? title, scale format
    #Todo approach to store files: flat, by folders
    LOG_ERROR = "log option disabled"
    def __init__(self, history:dict, log_files=True, 
        figsize:list=[6.4, 4.8]) -> None:
        self.history = history
        self.log_files = log_files
        self.plt = plt
        self.plt.figure(figsize=figsize, layout='constrained')

    @staticmethod
    def data_to_dict(keys, *data) -> dict:
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

    def get_file_extension(self, file_type):
        match file_type:
            case "txt" | "text" | ".txt":
                return ".txt"
            case "png" | ".png":
                return ".png"
            case "jpg" | ".jpg":
                return ".jpg"

    #* shares result with savefig, save_fit_process
    def get_save_num(self, file_type) -> int:  
        file_type = self.get_file_extension(file_type)
        files = os.listdir(os.getcwd())
        return len([i for i in files if file_type in i and not "summary" in i])+1

    #* call it before calling save_fit_process to keep right model naming
    #? invoke this function from save_fit_process?
    def save_model_summary(self, data):
        if not self.log_files:
            raise AttributeError(self.LOG_ERROR)
        num = self.get_save_num('txt')
        with open(f"model_summary_{num}.txt", "a") as f:
            print(data, file=f)

    #* the idea to write fitting process to file
    #* file name generates upon cwd analysis (check files, generates name (key))
    def save_fit_process(self):
        if not self.log_files:
            raise AttributeError(self.LOG_ERROR)
        num = self.get_save_num("txt")
        with open(f"model_fitting_{num}.txt", "w") as f:
            #* add header to the first line by taking keys from dict
            f.write("epochs" + "\t")
            for header in self.history.keys():
                f.write(header + "\t")
            f.write("\n")
            #* format history array from [[i1, ... i], [j1, ... j]] to [[i1,j1 ...], [i,j, ...]]
            values = list(zip(*self.history.values())) 
            for epoch, v in enumerate(values, start=1):
                #* write with delimeter... (creates column like style)
                f.write(str(epoch) + "\t" + 
                    "\t".join(["{:.4f}".format(i) for i in v]) + "\n")  

    def savefig(self) -> None:
        num = self.get_save_num("png") 
        self.plt.savefig(f"model_res_{num}.png")

    def plot(self, epochs, X=None) -> None:
        if X is None:
            X = np.arange(0, epochs)
        for k,v in self.history.items():
            self.plt.plot(X, v, label=k)
        self.plt.legend()
        self.plt.show()
