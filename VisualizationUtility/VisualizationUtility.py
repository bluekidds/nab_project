import pandas as pd
from ipywidgets import Layout


class Initialization:
    def __init(self):
        self.items_layout = Layout(display='flex',
                                   flex_flow='auto',
                                   align_items='stretch',
                                   width='auto')

        self.box_layout = Layout(display='flex',
                                 flex_flow='auto',
                                 align_items='center',
                                 width='auto')

        self.textarea_layout = Layout(display='flex',
                                      flex_flow='auto',
                                      align_items='center',
                                      width='auto',
                                      height='120px')

        self.style = {'description_width': 'initial'}

