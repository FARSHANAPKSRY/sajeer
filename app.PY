import streamlit as st

##st.set_page_config(
##    page_title="Happy Anniversary ❤️",
 ##   page_icon="💖",
 ##   layout="centered"
##)
st.markdown(
    """
    <marquee behavior="scroll" direction="left" scrollamount="10">
    <h1 style="font-size:50PX;">
        💖 Happy Anniversary My Love 💖
        
    </h1>
    </marquee>
    """,
    unsafe_allow_html=True
)






# Initialize page
if "page" not in st.session_state:
    st.session_state.page = 1

# PAGE 1
if st.session_state.page == 1:
    ##st.title("💖 Happy Anniversary 💖")

    st.markdown("""
    ## Dear My Love ❤️

    Today is a special day in our lives.

    I have prepared a small surprise for you.
    """)

    if st.button("Open My Surprise ❤️"):
        st.session_state.page = 2
        st.rerun()

# PAGE 2
elif st.session_state.page == 2:
    st.title(" A Special Message ")

    st.write("""LIFE WITH YOU IS A BEAUTIFUL MIX OF LOVE LAUGHER AND A LITTLE BIT OF MADNESS

    """)

    if st.button("Next ❤️"):
        st.session_state.page = 3
        st.rerun()

# PAGE 3
elif st.session_state.page == 3:
    st.title("📸 Our Beautiful Memories")

    st.write("Photo proof i was behaving ...for 2 seconds!!!!")

    st.image(
        "1.jpeg",
        caption="Our Happy Moments ❤️",
        use_container_width=True
    )
    st.image(
        "2.JPG.jpeg",
        caption="Our Happy Moments ❤️",
        use_container_width=True
    )
    st.image(
        "7.JPG.jpeg",
        caption="Our Happy Moments ❤️",
        use_container_width=True
    )
    st.image(
        "5.JPG.jpeg",
        caption="Our Happy Moments ❤️",
        use_container_width=True
    )
    st.image(
        "6.JPG.jpeg",
        caption="Our Happy Moments ❤️",
        use_container_width=True
    )
    st.image(
        "4.JPG.jpeg",
        caption="iam not naughty...iam just testing patience levels❤️",
        use_container_width=True
    )




    st.write("""
    Every smile,
    every laugh,
    every memory with you
    is precious to me.
    """)

    if st.button("Continue 💕"):
        st.session_state.page = 4
        st.rerun()

# PAGE 4
elif st.session_state.page == 4:
    st.title("💌 Reasons you drive me crazy")

    reasons = [
        "❤️ You never listen",
        "❤️ You laugh at the wrong time",
        "❤️ Your kindness",
        "❤️ You crreate unnecessary drama,but i wouldnt change any of it"
    ]

    for reason in reasons:
        st.write(reason)

    if st.button("Final Surprise 🎁"):
        st.session_state.page = 5
        st.rerun()

# PAGE 5
elif st.session_state.page == 5:
    st.balloons()

    st.title("🎉 Happy Anniversary My Love 🎉")

    st.markdown("""
    # ❤️ Forever Together ❤️

    You are my happiness,
    my best friend,
    and my greatest blessing.

    Thank you for being part of my life.

    ## I Love You ❤️

    Happy Anniversary!
    """)

    st.success("May our love continue forever ❤️")

    st.snow()
