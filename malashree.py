import streamlit as st

st.set_page_config(page_title="CRAZY PIZZA", page_icon=":tada:", layout="wide")

st.title("CRAZY PIZZA")
st.header("Make a slice of happiness :pizza:")
st.subheader("Explore your favorite pizza ")
st.markdown("Pizza+Party=Fun")

name = st.text_input("Enter your name:")
adr = st.text_input("Enter your address:")
ph = st.text_input("Enter your mobile number:")

button = st.button("Done")
if button:
    st.markdown(f"""
    name:{name}
    address:{adr}
    ph:{...}
    class:{classmethod}
    topping:{...}
    """)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Address")
        st.markdown("""
        * Green Harvest ,No 01,140/11 & 13,Bldg,Magarpatta
        ,Hadapsar,Pune,Maharashtra 411028""")

    with right_column:
        st.subheader("Contact")
        st.markdown("""
        * 8237256415/9663288730
        """)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Regular pizza")
        st.markdown("""
      * Margherita pizza
      * Pepperoni pizza
      * Pesto pizza
      * Hawaiian pizza
      """)

    with right_column:
        st.subheader("Price")
        st.markdown("""
      * 150
      * 170
      * 179
      * 185
      """)

    with left_column:
        st.subheader("Specialty pizza")
        st.markdown("""
        * BBQ pizza
        * Supper Veg Delight
        * Spicy Chicken pizza
        * Chicken Sausage
        """)
    with right_column:
        st.subheader("price")
        st.markdown("""
        * 250
        * 300
        * 345
        * 370
        """)

st.subheader("You can also make your won personal pizza too...")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Size for the pizza")
        st.markdown("""
        * M (1)
        * L (2)
        * XL (3)
        * XXL (4)
        """)

    with right_column:
        st.subheader("Choose your toppings on pizza ")
        st.markdown("""
        * capsicum
        * Pepperoni
        * Onion
        * Chicken
        * Olives
        * Paneer
        * Corn
        * Cheese
        * Tomato
        """)

topping = st.text_input("Enter the toppings you need on your pizza:")

classmethod = st.selectbox("Enter your pizza size:", (1, 2, 3, 4))

st.subheader("Fun facts about crazy pizza")
st.markdown("""
       * What is crazy pizza?:Crazy Pizza is a sleek and playful new dining concept that brings 
       the passion and spirit of Italy to your table with a stylish spin on the quintessential
       Italian staple and a chilled yet vibrant atmosphere

       * Where did pizza come from?:mala Similar items that just weren’t called pizza have been around since the Neolithic age.
        History shows they made flatbreads and other bread with different sorts of toppings. 
        True pizza showed up in Naples, Italy in the 1600s. Bakers made it on the street and sold it to the poor people.
        They would eat it as they walked around the streets.

      * When was the first pizza made?:shevanti American Heritage. April–May 2006. Archived from the original on July 12, 2009.
        Retrieved July 4, 2009. Cheese, the crowning ingredient,
        was not added until 1889, when the Royal Palace commissioned the Neapolitan pizzaiolo, Raffaele Esposito, 
         to create a pizza in honor of the visiting Queen Margherita.

       """)

st.subheader(
    "   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ ")