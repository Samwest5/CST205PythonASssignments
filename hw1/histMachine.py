import numpy as np
import matplotlib
matplotlib.use('SVG')
import matplotlib.pyplot as plt


def hist_plotter(red_list, green_list, blue_list):

    """Returns three histograms in SVG format from R,G,B lists"""

    if not red_list or not green_list or not blue_list:
        print(f"{'='*42}\nAt least one of your lists is empty.\nPlease check and try again.\n{'='*42}")
        return

    color_lists = list(zip(
        [red_list, green_list, blue_list],
        ["#ff4d4d", "#95ed64", "#6495ed"],
        ["red_hist.svg", "green_hist.svg", "blue_hist.svg"]
    ))

    for i in color_lists:
        plt.xticks([64,128,192,255])
        plt.hist(i[0], bins=256, color=i[1], alpha=0.95)
        plt.savefig(i[2])
        plt.close()
