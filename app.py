
import streamlit as st

st.set_page_config(page_title="ROI Calculator - Throuput increase of beer production",
                   page_icon= "assets/favicon.png")

st.markdown(""" <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .ea3mdgi5 {padding-top: 16px;}
</style> """, unsafe_allow_html=True)


st.image(image="assets/logo_page.jpg", width= 180)

st.container(height=8, border=False)

st.image(image="assets/form_image.jpg")

#st.container()

st.header(" Throughput Increase Calculator",
          anchor= False)

###### Tank Data

st.divider()

c1_0,c1_1 = st.columns(2)

with st.container():
    tank_capacity = c1_0.number_input(label= "Tank Capacity (Litres)",
                value= 10_000,
                step= 1_000)
    
    #%0.1f
    
    tank_quantity = c1_1.number_input(label = "Tank Quantity (units)",
                    value = 1)

total_volume = tank_capacity*tank_quantity

st.metric(label="Total Volume", value=f"{total_volume:,} l")


######## Capacity Calculation

st.divider()

tank_cycle_hours = st.number_input(label ="Tanks Cycle (hours)",
                                   value= 396)
yearly_non_productive_days = st.number_input(label = "Yearly Non-Productive Days (days)",
                                             value= 30)

yearly_days = 365
productive_days = yearly_days - yearly_non_productive_days
productive_hours = productive_days *24

yearly_batches_per_tank = productive_hours/tank_cycle_hours

yearly_production_capacity = yearly_batches_per_tank*tank_capacity*tank_quantity


c2_0, c2_1, c2_2 = st.columns(3)
c2_0.metric(label="Yearly Productive Hours", value= f"{productive_hours:,} h")
c2_1.metric(label = "Yearly Batches per tank", value = f"{round(yearly_batches_per_tank,2):,}")
c2_2.metric(label = "Yearly Production Capacity", value = f"{round(yearly_production_capacity):,} l")


st.divider()

#### Potential Time reduction in Tank Cycle

time_reduction = st.number_input("Potential time reduction in tank cycle (Hours)",
                                 value= 2)

improved_tank_cycle = tank_cycle_hours - time_reduction
improved_yearly_batches_per_tank = productive_hours/improved_tank_cycle
improved_yearly_production_capacity = improved_yearly_batches_per_tank*tank_capacity*tank_quantity
yearly_volume_increase = improved_yearly_production_capacity - yearly_production_capacity

c3_0, c3_1, c3_2 = st.columns(3)

c3_0.metric(label="Improved Tank Cycle", value= f"{improved_tank_cycle:,} h")
c3_1.metric(label = "Improved Yearly Batches per Tank", value = f"{round(improved_yearly_batches_per_tank,2):,}", delta = round(improved_yearly_batches_per_tank - yearly_batches_per_tank,3))
c3_2.metric(label = "Improved Yearly Production Capacity", value = f"{round(improved_yearly_production_capacity):,} l",
            delta = f"{round(yearly_volume_increase,2):,}")

st.divider()

profit_litre = st.number_input("Profit per litre ($)",
                value= 1.00)
investment = st.number_input("Project Investment ($)",
                value=1_000)

yearly_profit = profit_litre*yearly_volume_increase

roi = investment/yearly_profit

c4_0, c4_1= st.columns(2)

c4_0.metric(label="Yearly Profit Increase", value= f"${round(profit_litre*yearly_volume_increase,2):,}")
c4_1.metric(label = "Return on Investiment (ROI)", value = f"{round(roi,2):,} years")



