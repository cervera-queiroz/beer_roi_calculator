
import streamlit as st

st.set_page_config(page_title="Beer Fermentation - ROI Calculator ",
                   page_icon= "assets/favicon.png")

st.markdown(""" <style>
    footer {visibility: hidden;}s
    .e1nzilvr5 .p {font-size: 20px;}
</style> """, unsafe_allow_html=True)


st.subheader("ROI calculator - Beer fermentation optimisation", anchor=False)

with st.expander("Increasing production throuput"):

    ###### Tank Data

    c1_0,c1_1 = st.columns(2)

    with st.container():
        tank_capacity = c1_0.number_input(label= "Tank Capacity (Litres)",
                    value= 10_000,
                    step= 1_000)
        tank_quantity = c1_1.number_input(label = "Tank Quantity (units)",
                        value = 1)

    total_volume = tank_capacity*tank_quantity

    st.metric(label="Total Volume", value=f"{total_volume:,} l")


    ######## Capacity Calculation

    tank_cycle_hours = st.number_input(label ="Tanks Cycle (hours)",
                                    value= 396,min_value=1)
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

    st.divider( )

    #### Potential Time reduction in Tank Cycle

    time_reduction = st.number_input("Potential time reduction in tank cycle (Hours)",
                                    value= 2, min_value=1)

    improved_tank_cycle = tank_cycle_hours - time_reduction
    improved_yearly_batches_per_tank = productive_hours/improved_tank_cycle
    improved_yearly_production_capacity = improved_yearly_batches_per_tank*tank_capacity*tank_quantity
    yearly_volume_increase = improved_yearly_production_capacity - yearly_production_capacity

    c3_0, c3_1, c3_2 = st.columns(3)

    c3_0.metric(label="Improved Tank Cycle", value= f"{improved_tank_cycle:,} h")
    c3_1.metric(label = "Improved Yearly Batches per Tank", value = f"{round(improved_yearly_batches_per_tank,2):,}", delta = round(improved_yearly_batches_per_tank - yearly_batches_per_tank,3))
    c3_2.metric(label = "Improved Yearly Production Capacity", value = f"{round(improved_yearly_production_capacity):,} l",
                delta = f"{round(yearly_volume_increase,2):,}")

##############################

with st.expander("Reducing labour costs"):
    
    c5_0,c5_1,c5_2 = st.columns(3)
    number_samples_batch = c5_0.number_input(label= "Number of Samples Per Batch", value=8)
    average_time_analysis = c5_1.number_input(label= "Average analysis time (min)", value=15)
    labour_cost_hour = c5_2.number_input(label = "Labour Cost per Hour ($)", value = 30)    
    yearly_number_samples = number_samples_batch*yearly_batches_per_tank*tank_quantity
    estimated_time_analysis = (yearly_number_samples*average_time_analysis)/60
    yearly_labour_costs = estimated_time_analysis * labour_cost_hour
    
    c6_0, c6_1,c6_2 = st.columns(3)
    
    c6_0.metric(label= "Yearly number of samples", value= round(yearly_number_samples))
    c6_1.metric(label= "Estimated time spent with analysis", value= f"{round(estimated_time_analysis)} h")
    c6_2.metric(label = "Yearly operational costs", value = f"$ {round(yearly_labour_costs,2):,}")
    
    st.divider()
    
    c7_0,c7_1 = st.columns(2)
    
    reduced_number_samples_batch = c7_0.number_input(label= "Improved - Number of Samples Per Batch", value=4)
    reduced_time_analysis = c7_1.number_input(label= "Improved - Average analysis time (min)", value=5)
    
    improved_yearly_number_samples = reduced_number_samples_batch*yearly_batches_per_tank*tank_quantity
    improved_time_analysis = (reduced_time_analysis*improved_yearly_number_samples)/24
    improved_yearly_labour_costs = improved_time_analysis* labour_cost_hour
    labour_cost_savings = (improved_yearly_labour_costs - yearly_labour_costs)* (-1)

    
    
    c8_0, c8_1, c8_2 = st.columns(3)
    c8_0.metric(label= "Improved Yearly Number of Samples", value= round(improved_yearly_number_samples), delta= round(improved_yearly_number_samples - yearly_number_samples))
    c8_1.metric(label= "Improved Analysis Time (Yearly)", value= f"{round(improved_time_analysis)} h", delta= round(improved_time_analysis - estimated_time_analysis))
    c8_2.metric(label= "Improved - Operational costs \n (Yearly)", value= f"$ {round(improved_yearly_labour_costs):,}", delta= f"$ {round(labour_cost_savings):,}")

################################

profit_litre = st.number_input("Profit per litre ($)",
                value= 1.00)
investment = st.number_input("Project Investment ($)",
                value=1_000)

yearly_profit = (profit_litre*yearly_volume_increase) + labour_cost_savings

roi = investment/yearly_profit

c4_0, c4_1= st.columns(2)

c4_0.metric(label="Yearly Profit Increase", value= f"${round(yearly_profit,2):,}")
c4_1.metric(label = "Return on Investiment (ROI)", value = f"{round(roi,2):,} years")


