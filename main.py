import util
import streamlit as st

# Load the model artifacts when the script is run
util.load_temperature_model_artifacts()

# Streamlit components
st.set_page_config(
    page_title="Habeeb Temperature Forecast",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🌍 Habeeb Temperature Forecast for Global Cities")

# Sidebar for user input
st.sidebar.header("Input Parameters")
city = st.sidebar.selectbox("Select city", util.get_city_names())
year = st.sidebar.number_input("Enter year", min_value=1900, max_value=2100, value=2023)
month = st.sidebar.number_input("Enter month", min_value=1, max_value=12, value=1)
tolerance = st.sidebar.number_input("Enter tolerance for range prediction", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

# Month names list
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# Main page for displaying results
tab1, tab2 = st.tabs(["Temperature Prediction", "Temperature Range Prediction"])

with tab1:
    if st.button("Predict Temperature"):
        estimated_temperature = util.predict_temperature(city, year, month)
        month_name = month_names[month - 1]
        current_year = st.session_state['current_year'] if 'current_year' in st.session_state else None

        st.metric(
            label=f"Estimated Temperature for {city.title()} in {month_name} {year}",
            value=f"{estimated_temperature:.2f}°C",
            delta=f"{(estimated_temperature - 0.5):.2f}°C to {(estimated_temperature + 0.5):.2f}°C",
        )
        if year < current_year:
            st.write(f"The temperature for {city.title()} in {month_name} {year} was {estimated_temperature:.2f}°C.")
        else:
            st.write(f"The temperature forecast for {city.title()} for {month_name} in the year {year} is {estimated_temperature:.2f}°C.")

with tab2:
    if tolerance > 3:
        st.error("Tolerance value must not be greater than 3. Please adjust the tolerance value.")
    else:
        if st.button("Predict Temperature Range"):
            lower_bound, upper_bound = util.predict_temp_range(city, year, month, tolerance)
            month_name = month_names[month - 1]
            current_year = st.session_state['current_year'] if 'current_year' in st.session_state else None

            st.metric(
                label=f"Temperature Range for {city.title()} in {month_name} {year}",
                value=f"{lower_bound:.2f}°C to {upper_bound:.2f}°C",
            )
            if year < current_year:
                st.write(f"The temperature range for {city.title()} in {month_name} {year} was {lower_bound:.2f}°C to {upper_bound:.2f}°C.")
            else:
                st.write(f"The temperature forecast range for {city.title()} for {month_name} in the year {year} is {lower_bound:.2f}°C to {upper_bound:.2f}°C.")

# Footer with additional information
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #333;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed by Habeeb | Temperature Prediction Model</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    st.session_state['current_year'] = 2024
    print("Starting Temperature Prediction Application...")
