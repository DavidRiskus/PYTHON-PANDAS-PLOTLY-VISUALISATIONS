#STACKED BAR CHART CHOICE REASONING: https://chartio.com/learn/charts/stacked-bar-chart-complete-guide/
#BAR COLORS CATEGORIES SELECTED TO CATER FOR VARIOUS TYPES OF COLOR BLINDNESS, BY USING COLOR SELECTING TOOL:
#https://davidmathlogic.com/colorblind/#%23000000-%23E69F00-%2356B4E9-%23009E73-%23F0E442-%230072B2-%23D55E00-%23CC79A7

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#============================================== D A T A   A N A L Y S I S ================================#


######## FIRST DATA SET - FIGHT EVENTS ##########
data = pd.read_csv("ALL UFC FIGHTS.csv")

data = data.reindex(columns = data.columns.tolist() + ['Percentage'])

####### CREATING A YEAR COLUMN ################

#Method adopted based on: https://www.interviewqs.com/ddi_code_snippets/extract_month_year_pandas

data['year'] = pd.DatetimeIndex(data['event_date']).year


###### CAPTURE ALL YEARS ################
csv_year = data['year']

years =[]
for i in csv_year:
    if i not in years:
        years.append(int(i))

#SORT YEARS FROM 1993 to 2016
years.sort()


#Takes Method name as heading, takes empty list dedicated to specific method type, lastly takes Method size list,
#which represents the absolute values, used inside hover labels.

def calculations(heading, listcategory,method_size):
    for year in years:
        #filter the data set and take the amount of rows with the particular method name and coresponding year
        category = len(data[(data["method"].isin([heading])) & (data["year"]==year)])

        #total fight absolute value on the same year
        total_fights = len(data[data["year"]==year])

        #count the fraction (later converted to percentage)
        fight_perc = category / total_fights

        #convert it to a string, which will be used in the hover label
        text=f"{category} / {total_fights}"

        #append to the hover label list
        method_size.append(text)

        #append for the data plotting list
        listcategory.append(fight_perc)


#TOTAL VALUE PER CATEGORY / TOTAL FIGHTS IN THE YEAR#
Submissions_size =[]
KOs_size =[]
TKOs_size=[]
Decisions_size=[]
Draws_size=[]
Others_size=[]


###### SUBMISSIONS ################
submissions = []

for year in years:
    submission = len(data[(data["method"].isin(["Submission", "Technical"])) & (data["year"]==year)])
    total_fights = len(data[data["year"]==year])
    fight_perc = submission / total_fights
    text=f"{submission} / {total_fights}"
    Submissions_size.append(text)
    submissions.append(fight_perc)

###### Other ################
Others = []

for year in years:
    Other = len(data[((data["method"]!="Decision") & (data["method"]!="KO") & (data["method"]!="TKO") & (data["method"]!="Draw") & (data["method"]!="Submission") & (data["method"]!="Technical") ) & (data["year"]==year)])
    total_fights = len(data[data["year"]==year])
    fight_perc = Other / total_fights # multiply by 100 if old way
    text=f"{Other} / {total_fights}"
    Others_size.append(text)
    Others.append(fight_perc)

###### KOs ################
KOs = []

calculations("KO",KOs,KOs_size)

###### TKOs ################
TKOs = []

calculations("TKO",TKOs,TKOs_size)

###### Draws ################
Draws = []

calculations("Draw",Draws,Draws_size)

###### Decision ################
Decisions = []

calculations("Decision",Decisions,Decisions_size)


#============================================== V I S U A L I S A T I O N ================================#


######## MAKE THE BACKGROUND TRANSPERANT #####
layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
        annotations=[ #POSITION THE LEGEND
        dict(
            x=1.07,
            y=1.05,
            align="right",
            valign="top",
            text='<b>Method Types:</b>',
            showarrow=False,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="top"
        )
    ]
)

#METHOD NAMES USED INSIDE THE HOVER LABELS
name0 = 'DQ or NC'
name1 = 'Decision'
name2 = 'Draw'
name3 = 'TKO'
name4 = 'KO'
name5 = 'Submission'

######## PLOT THE DATA ##############
fig = go.Figure(data=[
    go.Bar(name='Submission', x=years, y=submissions, text=Submissions_size, marker_color="#88AEBE", hovertemplate=
        f"<b>{name5}</b>, " + #Hover label
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "Method's amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='KO', x=years, y=KOs, text=KOs_size, marker_color="#EE4848", hovertemplate=
        f"<b>{name4}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "Method's amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='TKO', x=years, y=TKOs, text=TKOs_size,marker_color="#24D8A8" ,hovertemplate=
        f"<b>{name3}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "Method's amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Draw', x=years, y=Draws,text=Draws_size,marker_color= "#A974FA", hovertemplate=
        f"<b>{name2}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "Method's amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='Decision', x=years, y=Decisions, text=Decisions_size,marker_color= "#FFC72C", hovertemplate=
        f"<b>{name1}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "Method's amount/Total: <b>%{text}</b>" +
        "<extra></extra>"),
    go.Bar(name='DQ or NC', x=years, y=Others, text=Others_size,marker_color= "#140ABB", hovertemplate=
        f"<b>{name0}</b>, " +
        "<b>%{y}</b>, " +
        "%{x}<br>" +
        "Method's amount/Total: <b>%{text}</b>" +
        "<extra></extra>")
], layout=layout)

# Y AXIS TO BE PERCENTAGE
fig.layout.yaxis.tickformat = ',.1%'


######## TITLE AND AXIS LABELS ########

fig.update_layout( #Source: https://plotly.com/python/figure-labels/
    title="<b>1993 - 2016 Fight Ending Methods - Relative Distributions</b>",
    xaxis_title="<b>Years</b>",
    yaxis_title="<b>Method's % Against All Year's Fights</b>",
    # height=650,
    font=dict(
        family="Gravitas One",
        size=16,
        color="#000000"
    )

)
# fig.update_layout(#Source: https://plotly.com/python/hover-text-and-formatting/#selecting-a-hovermode-in-a-figure-created-with-plotlygraphobjects
#     hoverlabel=dict(
#         bgcolor="white",
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
