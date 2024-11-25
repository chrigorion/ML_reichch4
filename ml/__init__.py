__version__ = "0.2"
__author__ = "Norman Juchler"

from .plotting import (save_figure,
                       setup_plotting,
                       plot_decision_boundary,
                       display_image,
                       show_image,
                       show_image_pair,
                       PALETTE,
                       PALETTE_CMAP_CONT_BR,
                       PALETTE_CMAP_CONT_RG,
                       PALETTE_CMAP_CONT_BRG,
                       PALETTE_CMAP_CONT_RBG,
                       PALETTE_CMAP,
                       PALETTE_PLOTLY)
from .colors import (color_palette, 
                     colors2plotly, 
                     color_transition, 
                     color_transitions)
from .fileio import ensure_dir

def print_title(title, level=1, sep=None):
    if sep is None:
        sep = "#" if level == 1 else "-"
        
    if level == 1:
        width = max(60, len(title))
    else:
        width = len(title)
    
    if level == 1:
        print()
        print(sep * width)
        print(title)
        print(sep * width)
    else:
        print()
        print(title)
        print(sep * width)
    