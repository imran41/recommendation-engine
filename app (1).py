import streamlit as st
import pickle
import pandas as pd

st.title('Food Recommendation')
# breakfast = pd.read_excel("D:\Project\Data\breakfast.xlsx")

food_list = pickle.load(open('food.pkl','rb'))
# food_list = food_list['DishName'].values
data = pd.DataFrame(food_list)
similarity = pickle.load(open('similarity.pkl','rb'))

breakfast_list = pickle.load(open('breakfast.pkl','rb'))
breakfast = pd.DataFrame(breakfast_list)

desserts_list = pickle.load(open('desserts.pkl','rb'))
desserts = pd.DataFrame(desserts_list)

drinks_list = pickle.load(open('drinks.pkl','rb'))
drinks = pd.DataFrame(drinks_list)

nonvegmain_list = pickle.load(open('nonvegmain.pkl','rb'))
nonvegmain = pd.DataFrame(nonvegmain_list)

nonvegstarter_list = pickle.load(open('nonvegstarter.pkl','rb'))
nonvegstarter = pd.DataFrame(nonvegstarter_list)

vegmain_list = pickle.load(open('vegmain.pkl','rb'))
vegmain = pd.DataFrame(vegmain_list)

vegstarter_list = pickle.load(open('vegstarter.pkl','rb'))
vegstarter = pd.DataFrame(vegstarter_list)


def recommend(food):
    food_index = data[data["DishName"] == food].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:11] 


    recommended_foods= []
    for i in food_list:
        recommended_foods.append(data.iloc[i[0]].DishName)
    return recommended_foods
    





meal_type = st.selectbox('Select Meal Type',('Select Meal Type','Breakfast','MainCourse','Starters','Desserts') )
if meal_type is ('Breakfast'):
    food_break = breakfast.Breakfast
    for i in food_break:
        st.write(i)

if meal_type is ('Desserts'):
    food_desserts = desserts.Desserts
    for i in food_desserts:
        st.write(i)

veg = st.selectbox('Choose Veg or Non-Veg', ('Select','Vegetarian','NonVegetarian'))

if meal_type is ('MainCourse') and  veg is ('Vegetarian'):
    # if veg is ('Vegetarian'):
    food_veg = vegmain.Vegmain
    for i in food_veg:
        st.write(i)

if meal_type is ('MainCourse') and  veg is ('NonVegetarian'):
    food_nonveg = nonvegmain.NonvegMain
    for i in food_nonveg:
        st.write(i)

if meal_type is ('Starters') and  veg is ('NonVegetarian'):
    food_nonvegsta = nonvegstarter.NonvegStarters
    for i in food_nonvegsta:
        st.write(i)

if meal_type is ('Starters') and  veg is ('Vegetarian'):
    food_vegsta = vegstarter.VegStarters
    for i in food_vegsta:
        st.write(i)
    
st.balloons()





selected_food = st.selectbox('What would you like to Order?',food_list)
if st.button('Recommend'):
    recommendations = recommend(selected_food)
    st.subheader("Also try this")
    for i in recommendations:
        st.write(i)
 
st.balloons()