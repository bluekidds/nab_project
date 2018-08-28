from ipywidgets import Layout


class CustomStyling:
	items_layout = Layout(display='flex',
	                    flex_flow='auto',
	                     align_items='stretch',
	                      width='auto')     # override the default width of the button to 'auto' to let the button grow
	box_layout = Layout(display='flex',
	                    flex_flow='auto',
	                    align_items='center',
	                    width='auto')
	textarea_layout = Layout(display='flex',
	                    flex_flow='auto',
	                    align_items='center',
	                    width='auto',
	                    height='120px')
	style = {'description_width': 'initial'}