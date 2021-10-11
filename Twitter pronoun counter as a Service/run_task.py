from tasks import pronoun_count
from draw_chart import draw_bar_chart

result = pronoun_count.delay('./tweet_pronoun_files/data/')
while(not (result.status == 'SUCCESS')):
    pass
pronouns = []
values = []
result_dict = result.get()
for x in result_dict:
    pronouns.append(x)
    values.append(result_dict[x])
draw_bar_chart(pronouns, values)