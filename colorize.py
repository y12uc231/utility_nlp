import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def colorize(words, color_array):
    # words is a list of words
    # color_array is an array of numbers between 0 and 1 of length equal to words
    cmap = matplotlib.cm.get_cmap('OrRd')
    template = '<span class="barcode"; style="color: black; background-color: {}">{}</span>'
    colored_string = ''
    for word, color in zip(words, color_array):
        print(word)
        color = matplotlib.colors.rgb2hex(cmap(color)[:3])
        colored_string += template.format(color, '&nbsp' + word + '&nbsp')
    return colored_string
    

words = "he obtained his master's in architecture from the university of tehran and phd in architecture and landscape history at georgia institute of technology".split()

words1 = 'The quick brown fox jumps over the lazy dog'.split()
color_array = [0.01, 0.02, 0.02, 0.1, 0.03, 0.4, 0.03, 0.01, 0.2, 0.02, 0.04, 0.07, 0.4, 0.05, 0.5, 0.01, 0.08, 0.2, 0.03, 0.03, 0.05, 0.06, 0.3]  # np.random.rand(len(words))

#color_array = [0.9, 0.02, 0.9, 0.01, 0.03, 0.04, 0.03, 0.01, 0.1, 0.02, 0.04, 0.07, 0.04, 0.05, 0.5, 0.01, 0.08, 0.02, 0.03, 0.03, 0.05, 0.06, 0.1]  # np.random.rand(len(words))

print(color_array)
s = colorize(words, color_array)

# to display in ipython notebook
from IPython.display import display, HTML
display(HTML(s))

# or simply save in an html file and open in browser
with open('colorize.html', 'w') as f:
    f.write(s)










sentence = "she serves on the executive board of san francisco bay area physicians for social responsibility, is an assistant professor at the ucsf school of medicine and a staff physician at kaiser permanente, northern california. she was a past senior scientist for the nrdc, where she provided scientific expertise for policy and regulatory decisions on a number of toxic chemicals."
