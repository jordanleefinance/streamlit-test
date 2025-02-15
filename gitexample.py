# import required libraries
import streamlit as st
import yfinance as yf
from datetime import datetime


# function calling local css sheet
def local_css(file_name):
    with open(file_name) as f:
        st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

today = datetime.today()
# local css sheet
#local_css("../css/custom.css")

# ticker search feature in sidebar
st.sidebar.subheader("""Stock Search Web App""")
selected_stock = st.sidebar.text_input("Enter a valid stock ticker...", "AAPL")
start_date = st.sidebar.date_input("Start Date", datetime(day=1, month=1, year=2016))
end_date = st.sidebar.date_input("End Date", today)
button_clicked = st.sidebar.button("GO")


# main function
def main():
    st.subheader("""Daily **closing price** for """ + selected_stock)
    # get data on searched ticker
    stock_data = yf.Ticker(selected_stock)
    # get historical data for searched ticker
    stock_df = stock_data.history(period='1d', start=start_date, end=end_date)
    # print line chart with daily closing prices for searched ticker
    st.line_chart(stock_df.Close)

    st.subheader("""Last **closing price** for """ + selected_stock)
    # define variable today
    today = datetime.today().strftime('%Y-%m-%d')
    # get current date data for searched ticker
    stock_lastprice = stock_data.history(period='1d', start=today, end=today)
    # get current date closing price for searched ticker
    last_price = (stock_lastprice.Close)
    # if market is closed on current date print that there is no data available
    if last_price.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(last_price)

    # get daily volume for searched ticker
    st.subheader("""Daily **volume** for """ + selected_stock)
    st.line_chart(stock_df.Volume)

    # additional information feature in sidebar
    st.sidebar.subheader("""Display Additional Information""")
    # checkbox to display stock actions for the searched ticker
    actions = st.sidebar.checkbox("Stock Actions")
    if actions:
        st.subheader("""Stock **actions** for """ + selected_stock)
        display_action = (stock_data.actions)
        if display_action.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_action)

    

    # checkbox to display list of institutional shareholders for searched ticker
    major_shareholders = st.sidebar.checkbox("Institutional Shareholders")
    if major_shareholders:
        st.subheader("""**Institutional investors** for """ + selected_stock)
        display_shareholders = (stock_data.institutional_holders)
        if display_shareholders.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_shareholders)


if button_clicked == "GO":
    main()

if __name__ == "__main__":
    main()

