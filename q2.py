import plotly.express as px
import pandas as pd


data_frame = pd.read_csv("pivoted.csv")

#PLOTING THE DATA WITH PLOTLY EXPRESS METHOD
barchart = px.bar(data_frame, x="Percentage", y="Method", color="Method",
    orientation='h', #CHANGE Bars to Horizontal view
    text="Percentage", #Bar values used from Percentage column in the CSV

    hover_data=["Percentage", "Method Amount", "Total Fights"], #Hover Data taken from these column headings in CSV

    labels={"Method":"<b>Method Types</b>","Percentage":"<b>Method's % Against All Year's Fights</b>"},
    #Change the names of Column names in CSV on the Legend and X Axis label

    animation_frame="Year", animation_group="Method", range_x=[0,100], #Animate 100% length

    #COLOR SCHEME FOR THE BARS
    color_discrete_sequence=["#140ABB","#FFC72C","#A974FA","#24D8A8","#EE4848","#88AEBE"]).update_yaxes(categoryorder="total ascending") #ORDER CATEGORIES BY THEIR PERCENTAGE SIZE

barchart.update_layout(#LAYOUT
    height=700,
    title_text="<b>1993 - 2016 Fight Ending Methods - Bar Chart Race</b>",
    font=dict(
        family="Gravitas One",
        size=18,
        color="#000000"
    ),

)

#DISCLAIMER WHY NOT USED LABELS INSIDE. MESSES UP ANIMATION TRANSITION SMOOTHNESS.
# barchart.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')#
# barchart.update_traces(texttemplate='%{text}', textposition='inside')

#HOVER LABEL COLOR AND SIZE
barchart.update_layout(
    hoverlabel=dict(
        bgcolor="grey",
        font_size=14,
        font_family="Gravitas One",
        font_color="white"
    )
)

#BACKGROUND COLOR
barchart.update_layout(
    paper_bgcolor="white",
    # plot_bgcolor="white"
)

#ANIMATION DURATION
barchart.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
barchart.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500




barchart.show()
