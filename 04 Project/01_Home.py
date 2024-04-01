import streamlit as st

st.set_page_config(page_title="Sleep", page_icon=":zzz:", layout="wide")

st.title("Sleep Savvy")
st.markdown("### Your one-stop shop to upgrade your sleep health.")


col = st.columns((3, 3, 3), gap="medium")

with col[0]:
    with st.container(border=True):
        st.markdown(
            "55.64% of people have poor sleep quality, and 62% say they don't sleep as well as they'd like."
        )


with col[1]:
    with st.container(border=True):
        st.markdown(
            "Adults need at least seven hours of sleep per night, but more than one-third sleep less than that."
        )

with col[2]:
    with st.container(border=True):
        st.markdown(
            "Up to two-thirds of adults experience insomnia, and 2–9% have obstructive sleep apnea."
        )

st.markdown("")
st.markdown("")

st.markdown("## Do you want to sleep better? Let's get started!")

from streamlit_carousel import carousel

test_items = [
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        interval=None,
        img="https://www.google.com/url?sa=i&url=https%3A%2F%2Fletsenhance.io%2F&psig=AOvVaw1ju72VFFranBW9HxduaKRh&ust=1711967343209000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNDitr2lnoUDFQAAAAAdAAAAABAD",
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
    ),
]

carousel(items=test_items, width=10)

