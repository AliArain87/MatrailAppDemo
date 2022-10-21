import streamlit as st 
import plotly.express as px
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
from plotly.subplots import make_subplots




# Modify app name and Icon
# Config Function 
st.set_page_config(page_title='Matrial Selection Demo APP', page_icon='🔨', layout='wide', initial_sidebar_state='auto')



# Hide Menu and Footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """   
st.markdown(hide_menu_style, unsafe_allow_html=True)







with st.sidebar:
    st.title("Matrial selection")
    option = st.selectbox("Select material", ["Matrial Selection","Aggregates","Aluminium", "Antimony"])
    
    
if option == "Matrial Selection":
    st.title("💥Matrial Selection💥")
    st.write("Select the matrial from the sidebar")
    
elif option == "Aggregates":
    st.title("Aggregates")
    plt.figure(figsize=(10, 5))
    df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    fig = px.bar(df.head(5), y='pop', x='country', text_auto='.2s', color='country',
                title="Default: various text sizes, positions and angles")
    st.write(fig)
    plt.figure(figsize=(10, 5))
    df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    fig2 = px.bar(df.tail(5), y='pop', x='country', text_auto='.2s', color='country',
                title="Default: various text sizes, positions and angles")
    st.write(fig2)
    
    

    labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
            "Rest of World"]

    # Create subplots: use 'domain' type for Pie subplot
    fig3 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig3.add_trace(go.Pie(labels=labels, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"),
                1, 1)
    fig3.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
                1, 2)

    # Use `hole` to create a donut-like pie chart
    fig3.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig3.update_layout(
        title_text="Global Emissions 1990-2011",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
                    dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])
    st.write(fig3)
    
    
    fig4 =go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    ))
    fig4.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    st.write(fig4)
    
    
    
    
elif option == "Aluminium":
    st.title("Aluminium")

    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]

    # pull is given as a fraction of the pie radius
    fig5 = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0])])
    st.write(fig5)

    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]

    # Use `hole` to create a donut-like pie chart
    fig6 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    st.write(fig6)
    
    
    years = ['2016','2017','2018']

    fig7 = go.Figure()
    fig7.add_trace(go.Bar(x=years, y=[500, 600, 700],
                    base=[-500,-600,-700],
                    marker_color='crimson',
                    name='expenses'))
    fig7.add_trace(go.Bar(x=years, y=[300, 400, 700],
                    base=0,
                    marker_color='lightslategrey',
                    name='revenue'
                    ))

    st.write(fig7)
    
    
elif option == "Antimony":
    st.title("Antimony")
    x = [
    ["BB+", "BB+", "BB+", "BB", "BB", "BB"],
    [16, 17, 18, 16, 17, 18,]]
    fig8 = go.Figure()
    fig8.add_bar(x=x,y=[1,2,3,4,5,6])
    fig8.add_bar(x=x,y=[6,5,4,3,2,1])
    fig8.update_layout(barmode="relative")
    st.write(fig8)
    
    
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig9 = px.pie(df, values='pop', names='country', title='Population of European continent')
    st.write(fig9)
    
    
    
    df = px.data.tips()
    fig10 = px.pie(df, values='tip', names='day', color='day',
                color_discrete_map={'Thur':'lightcyan',
                                    'Fri':'cyan',
                                    'Sat':'royalblue',
                                    'Sun':'darkblue'})
    st.write(fig10)
    
    
    
    
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig11 = go.Figure(data=[go.Pie(labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'],
                                values=[4500,2500,1053,500])])
    fig11.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                    marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    st.write(fig11)
    
    
    
    
    labels = ['1st', '2nd', '3rd', '4th', '5th']

    # Define color sets of paintings
    night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)',
                    'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
    sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                        'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
    irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                    'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
    cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                    'rgb(175, 51, 21)', 'rgb(35, 36, 21)']

    # Create subplots, using 'domain' type for pie charts
    specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
    fig12 = make_subplots(rows=2, cols=2, specs=specs)

    # Define pie charts
    fig12.add_trace(go.Pie(labels=labels, values=[38, 27, 18, 10, 7], name='Starry Night',
                        marker_colors=night_colors), 1, 1)
    fig12.add_trace(go.Pie(labels=labels, values=[28, 26, 21, 15, 10], name='Sunflowers',
                        marker_colors=sunflowers_colors), 1, 2)
    fig12.add_trace(go.Pie(labels=labels, values=[38, 19, 16, 14, 13], name='Irises',
                        marker_colors=irises_colors), 2, 1)
    fig12.add_trace(go.Pie(labels=labels, values=[31, 24, 19, 18, 8], name='The Night Café',
                        marker_colors=cafe_colors), 2, 2)

    # Tune layout and hover info
    fig12.update_traces(hoverinfo='label+percent+name', textinfo='none')


    fig12 = go.Figure(fig12)
    st.write(fig12)