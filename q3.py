#STACKED BAR CHART CHOICE REASONING: https://chartio.com/learn/charts/stacked-bar-chart-complete-guide/

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


######## FIRST DATA SET - FIGHT EVENTS ##########
data = pd.read_csv("Safety_Submissions.csv")
# data = data.dropna()

data = data.reindex(columns = data.columns.tolist() + ['Percentage'])

####### CREATING A YEAR COLUMN ################
data['year'] = pd.DatetimeIndex(data['event_date']).year #https://www.interviewqs.com/ddi_code_snippets/extract_month_year_pandas
data.head()


###### CAPTURE YEARS ################
csv_year = data['year']

years =[]
for i in csv_year:
    if i not in years:
        years.append(int(i))

years.sort()


def calculations(heading, listcategory,submission_size):
    for year in years:
        category = len(data[(data["class"]==heading) & (data["year"]==year) & (data["method"].isin(["Submission", "Technical"]))])
        total_fights = len(data[data["method"].isin(["Submission", "Technical"]) & (data["year"]==year)])
        fight_perc = category / total_fights
        text=f"{category} / {total_fights}"
        submission_size.append(text)
        listcategory.append(fight_perc)


###### Category Submission values ################
lightweight = []
featherweight = []
heavyweight = []
welterweight = []
middleweight = []
lightheavyweight =[]
flyweight =[]
bantamweight =[]
strawweight = []

#TOTAL VALUE PER CATEGORY / TOTAL SUBMISSIONS IN THE YEAR#
lightweight_size = []
featherweight_size = []
heavyweight_size = []
welterweight_size = []
middleweight_size = []
lightheavyweight_size =[]
flyweight_size =[]
bantamweight_size =[]
strawweight_size = []


calculations("Flyweight",flyweight,flyweight_size)
calculations("Lightweight",lightweight,lightweight_size)
calculations("Featherweight",featherweight,featherweight_size)
calculations("Heavyweight",heavyweight,heavyweight_size)
calculations("Welterweight",welterweight,welterweight_size)
calculations("Middleweight",middleweight,middleweight_size)
calculations("Light Heavyweight",lightheavyweight,lightheavyweight_size)
calculations("Bantamweight",bantamweight,bantamweight_size)
calculations("Strawweight",strawweight,strawweight_size)



#============================================== V I S U A L I S A T I O N ================================#


######## MAKE THE BACKGROUND TRANSPERANT #####
layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    annotations=[
        dict(
            x=1.07,
            y=1.05,
            align="right",
            valign="top",
            text='<b>Weight Division:</b>',
            showarrow=False,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="top"
        )
    ]
)
name0 = 'Heavyweight'
name1 = 'Light Heavyweight'
name2 = 'Middleweight'
name3 = 'Welterweight'
name4 = 'Lightweight'
name5 = 'Featherweight'
name6 = 'Bantamweight'
name7 = 'Flyweight'
name8 = 'Straweight'
######## PLOT THE DATA ##############



fig = go.Figure(data=[

    go.Bar(name='Heavyweight', x=years, y=heavyweight, text=heavyweight_size, marker_color="#88AEBE",hovertemplate=
        f"<b>{name0}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Light Heavyweight', x=years, y=lightheavyweight, text=lightheavyweight_size,marker_color="#EE4848", hovertemplate=
        f"<b>{name1}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Middleweight', x=years, y=middleweight, text=middleweight_size,marker_color="#24D8A8" , hovertemplate=
        f"<b>{name2}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Welterweight', x=years, y=welterweight, text=welterweight_size,marker_color= "#A974FA", hovertemplate=
        f"<b>{name3}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Lightweight', x=years, y=lightweight, text=lightweight_size,marker_color= "#FFC72C", hovertemplate=
        f"<b>{name4}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Featherweight', x=years, y=featherweight, text=featherweight_size,marker_color= "#140ABB", hovertemplate=
        f"<b>{name5}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Bantamweight', x=years, y=bantamweight, text=bantamweight_size,marker_color= "#9D226F", hovertemplate=
        f"<b>{name6}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Flyweight', x=years, y=flyweight, text=flyweight_size,marker_color= "#3A3838", hovertemplate=
        f"<b>{name7}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Straweight', x=years, y=strawweight, text=strawweight_size, marker_color= "#AEFF7E",hovertemplate=
        f"<b>{name8}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "W.D.'s amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),


], layout=layout)

# Y AXIS TO BE PERCENTAGE
fig.layout.yaxis.tickformat = ',.1%' # NEED HOVER TO HAVE THIS, WHILE AXIS 0%


######## TITLE AND AXIS LABELS ####
fig.update_layout( # https://plotly.com/python/figure-labels/
    title="<b>1993 - 2016 Submissions Per Weight Division (W.D.) - Relative Distributions</b>",
#     width=1030,
    xaxis_title="<b>Years</b>",
    yaxis_title="<b>W.D.'s Submission % Against All Year's Fights</b>",
    font=dict(
        family="Gravitas One",
        size=16,
        color="#000000"
    )

)
# fig.update_layout(#https://plotly.com/python/hover-text-and-formatting/#selecting-a-hovermode-in-a-figure-created-with-plotlygraphobjects
#     hoverlabel=dict(
#         # bgcolor="white",
#         font_size=16,
#         font_family="Rockwell"
#     )
# )

fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 1,
        dtick = 1
    )
)

# Change the bar mode
fig.update_layout(barmode='stack')

fig.show()
