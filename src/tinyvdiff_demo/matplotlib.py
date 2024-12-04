# Each PDF generated will have different /CreationDate field within metadata
# but visually identical

import importlib.resources as pkg_resources

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np


def generate_plot(output_file):
    font_path = pkg_resources.files("tinyvdiff_demo.fonts") / "Inter-Regular.ttf"
    custom_font = fm.FontProperties(fname=str(font_path))

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label="Sine Wave")
    plt.title("Example Plot", fontproperties=custom_font)
    plt.xlabel("Angle [rad]", fontproperties=custom_font)
    plt.ylabel("sin(x)", fontproperties=custom_font)
    plt.legend(prop=custom_font)
    plt.tight_layout()
    plt.savefig(output_file, format="pdf")
    plt.close()

    return output_file
