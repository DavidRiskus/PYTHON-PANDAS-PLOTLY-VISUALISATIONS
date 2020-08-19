import plotly.express as px
import pandas as pd

#DISCLAIMER WHY NOT POSSIBLE REMOVOE REDUNDANT DEFAULTS IN HOVER https://stackoverflow.com/questions/57402050/plotly-express-hover-options

df = pd.read_csv("Safety_Submissions2.csv")


fig = px.bar(df, x="Percentage ", y="Weight Division ", text="Percentage ", color="Weight Division ", orientation='h',hover_data=["Percentage ", "Division Amount ", "Total Year Submissions "],
  animation_frame="Year ", animation_group="Weight Division ", range_x=[0,100],color_discrete_sequence=["#AEFF7E","#3A3838","#9D226F","#140ABB","#FFC72C","#A974FA","#24D8A8","#EE4848","#88AEBE"],
    labels={"Weight Division ":"<b>Weight Division</b>", "Percentage ":"<b>W.D.'s Submission % Against All Year's Fights</b>"}).update_yaxes(categoryorder="total ascending")


fig.update_layout(
    height=800,
    title_text="<b>1993 - 2016 Submissions Per Weight Division (W.D.) - Bar Chart Race </b>",
    font=dict(
        family="Gravitas One",
        size=16,
        color="#000000"
    )
)

fig.update_layout(
    hoverlabel=dict(
        bgcolor="grey",
        font_size=14,
        font_family="Gravitas One",
        font_color="white"
    )
)

# fig.update_layout(uniformtext_minsize=20, uniformtext_mode='show')
# fig.update_traces(texttemplate='%{text}', textposition='inside')

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500

fig.show()
