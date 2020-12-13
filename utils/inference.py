import torch
import numpy as np
from utils.model import Model
import matplotlib.pyplot as plt
import cv2


def load_image(path):
    if path.endswith('jpg'):
        image = plt.imread(path)
        image = (2.0 * image / 255) - 1.0
        image = cv2.resize(image, (300, 300))
        image = np.moveaxis(image, 2, 0)
    else:
        raise NotImplementedError

    return image


def predict_class(image):
    model = Model(n=4)
    model.load_state_dict(torch.load('weights/classifier_model.pth'))
    model.eval()

    image = (torch.tensor(image))
    image = torch.unsqueeze(image, 0)

    x = model(image.float())
    x = x.argmax(1).item()

    return x


def predict_amount(image):
    model = Model(n=20)
    model.load_state_dict(torch.load('weights/counter_model.pth'))
    model.eval()

    image = (torch.tensor(image))
    image = torch.unsqueeze(image, 0)

    x = model(image.float())
    x = x.argmax(1).item()

    return x