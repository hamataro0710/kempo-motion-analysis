import numpy as np

def calc_segment_length(humans):



def remove_debris(humans, rate):
    heights = [max(h[~np.isnan(h[:, 1])]) - min(h[~np.isnan(h[:, 1])]) for h in humans]
    highest_human = humans[np.argmax(heights)]
