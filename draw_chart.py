from termgraph import termgraph as tg
    def draw_bar_chart(labels, values):
        data = []
        normal_data = []
        total_pronouns = 0
        for x in values:
            total_pronouns += x
        for value in values:
            data.append([value])
            normalized_value = value/4000
            normal_data.append([normalized_value])
        len_categories = 1
        args = {'filename': 'data/ex4.dat', 'title': None, 'width': 10,
            'format': '{:<5.2f}', 'suffix': '', 'no_labels': False,
            'color': None, 'vertical': False, 'stacked': True,
            'different_scale': False, 'calendar': False,
            'start_dt': None, 'custom_tick': '', 'delim': '',
            'verbose': False, 'version': False}
        colors = [91]
        tg.stacked_graph(labels, data, normal_data, len_categories, args, colors)