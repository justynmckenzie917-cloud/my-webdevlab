

import streamlit as st


# Embedded SVG images keep the quiz self-contained without image downloads.
lightsaber_image = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="240" viewBox="0 0 600 240">
<rect width="600" height="240" fill="#0f172a"/>
<path d="M190 120 H520" stroke="#14532d" stroke-width="36" stroke-linecap="round"/>
<path d="M190 120 H520" stroke="#4ade80" stroke-width="22" stroke-linecap="round"/>
<path d="M190 120 H520" stroke="#dcfce7" stroke-width="10" stroke-linecap="round"/>
<rect x="65" y="99" width="130" height="42" rx="8" fill="#94a3b8"/>
<path d="M85 100 V140 M105 100 V140 M125 100 V140" stroke="#334155" stroke-width="8"/>
<circle cx="166" cy="113" r="6" fill="#ef4444"/>
</svg>'''

death_star_image = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="240" viewBox="0 0 600 240">
<rect width="600" height="240" fill="#0f172a"/>
<g fill="white"><circle cx="65" cy="45" r="2"/><circle cx="125" cy="180" r="2"/>
<circle cx="500" cy="60" r="2"/><circle cx="550" cy="190" r="2"/></g>
<circle cx="300" cy="120" r="100" fill="#94a3b8"/>
<path d="M201 120 H399" stroke="#334155" stroke-width="8"/>
<path d="M224 60 H350 M210 85 H300 M220 155 H380 M240 185 H360" stroke="#64748b" stroke-width="4"/>
<circle cx="335" cy="77" r="28" fill="#64748b" stroke="#cbd5e1" stroke-width="3"/>
<circle cx="335" cy="77" r="10" fill="#334155"/>
</svg>'''

droid_image = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="240" viewBox="0 0 600 240">
<rect width="600" height="240" fill="#0f172a"/>
<path d="M245 85 A55 55 0 0 1 355 85" fill="#94a3b8"/>
<rect x="245" y="85" width="110" height="120" rx="5" fill="#e2e8f0"/>
<rect x="220" y="100" width="20" height="110" fill="#e2e8f0"/>
<rect x="360" y="100" width="20" height="110" fill="#e2e8f0"/>
<path d="M210 215 H245 M355 215 H390 M280 215 H320" stroke="#94a3b8" stroke-width="15"/>
<rect x="262" y="88" width="76" height="17" fill="#2563eb"/>
<rect x="265" y="120" width="70" height="12" fill="#2563eb"/>
<rect x="285" y="145" width="30" height="43" fill="#2563eb"/>
<circle cx="300" cy="67" r="12" fill="#2563eb"/>
<circle cx="300" cy="67" r="6" fill="#0f172a"/>
</svg>'''

st.title("Star Wars Quiz")
st.write("Test your Star Wars knowledge! Answer all five questions, then submit. Each question is worth one point.")

st.image(lightsaber_image, caption="A lightsaber", width=450)

q1 = st.radio(  #NEW
    "1. Who is Luke Skywalker's father?",
    ["Choose an answer", "Darth Vader", "Obi-Wan Kenobi", "Han Solo", "Yoda"],
)

q2 = st.number_input(  #NEW
    "2. How many suns does Tatooine have?",
    min_value=0, max_value=20, value=0, step=1,
    help="Enter a whole number. Zero means you have not answered yet.",
)

st.image(droid_image, caption="R2-D2 illustration", width=450)

q3 = st.multiselect(  #NEW
    "3. Select ALL the droids. You must select at least one option.",
    ["R2-D2", "Chewbacca", "C-3PO", "Yoda", "BB-8"],
)

st.image(death_star_image, caption="The Death Star", width=450)

q4 = st.selectbox(  #NEW
    "4. On which planet does Yoda train Luke in The Empire Strikes Back?",
    ["Choose an answer", "Hoth", "Dagobah", "Tatooine", "Naboo"],
)

q5 = st.number_input(  #NEW
    "5. How many movies are in the original Star Wars trilogy?",
    min_value=0, max_value=20, value=0, step=1,
    help="Enter a whole number. Zero means unanswered.",
)

if st.button("Submit quiz"):
    if (q1 == "Choose an answer" or q2 == 0 or not q3
            or q4 == "Choose an answer" or q5 == 0):
        st.warning("Please answer all five questions before submitting.")
    else:
        correct = [
            q1 == "Darth Vader",
            q2 == 2,
            set(q3) == {"R2-D2", "C-3PO", "BB-8"},
            q4 == "Dagobah",
            q5 == 3,
        ]
        score = sum(correct)
        st.metric("Your score", f"{score}/5")  #NEW
        st.progress(score / 5)  #NEW

        if score >= 4:
            st.success("Jedi Master! The Force is strong with you.")
            st.balloons()  #NEW
        elif score >= 2:
            st.info("Jedi Padawan! Your training is coming along. Keep learning!")
        else:
            st.info("Youngling! Your Jedi journey is just beginning. Review the answers and try again.")

        st.subheader("Answer review")
        answers = [
            "Darth Vader (Anakin Skywalker) is Luke's father.",
            "Tatooine has 2 suns.",
            "R2-D2, C-3PO, and BB-8 are droids.",
            "Yoda trains Luke on Dagobah in The Empire Strikes Back.",
            "The original trilogy has 3 movies: A New Hope, The Empire Strikes Back, and Return of the Jedi.",
        ]
        for number, (is_correct, answer) in enumerate(zip(correct, answers), start=1):
            status = "Correct" if is_correct else "Incorrect"
            st.write(f"{number}. {status}: {answer}")
