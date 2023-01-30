import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide") # make horizontal length longer

def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # provide the key of text widget
    # this extract content from new to-do which acts as a key
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
# st.write("<h1>This app is to increase your <b>productivity</b>.</h1>",
#         unsafe_allow_html=True)
# st.write("<h1>This app is to increase your <b>productivity</b>.</h1>",
#          unsafe_allow_html=True) # <h1> will make it bold and increase font as well
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)  # this will bold the text by providing html <>; default is false

# st.checkbox("Buy grocery.")
# st.checkbox("Throw the trash.")

# placement of this widget matter
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # store checkbox in a var
    if checkbox:  # if checkbox is checked
        # print(checkbox)
        # remove selected to-do
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # delete the to-do from session state dictionary
        st.experimental_rerun()  # needed for checkbox/ serve as a refresher

# print("Hi")
#
# st.session_state # sort of dictionary / session state type: use to see the output of web app
# need to be comment at the end


# st.text_input(label="", placeholder="Add new todo...",
#               on_change=add_todo, key='new_todo')
