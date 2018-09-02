import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projexts'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {
        'value': 1601,
        'label': 'Description of httpie.'
    },
    {
        'value': 1601,
        'label': 'Description of httpie.'
    },
    {
        'value': 1601,
        'label': 'Description of httpie.'
    }
]

chart.add('', plot_dicts)
chart.render_to_file('bar_decriptions.svg')