import pytest
import numpy as np
from matplotlib import pyplot as plt
from src.fit.main import FitVisualizer

X = np.linspace(0, 20)
y1 = np.linspace(100, 500)
y2 = np.linspace(120, 235)
y3 = np.linspace(330, 485)
epochs = 50 #* default number for linspace

def test_data_to_dict():
    to_dict = FitVisualizer.data_to_dict(None, y1, y2, y3)
    print(to_dict)
    assert type(to_dict) == dict

@pytest.fixture
def fv():
    return FitVisualizer()

def test_plot(fv):
    dic = fv.data_to_dict(None, y1, y2, y3)
    fv.plot(dic, epochs)
    fv.add_title("Test Title")
    fv.add_labels(["lolx", "loly"])
    fv.savefig()
