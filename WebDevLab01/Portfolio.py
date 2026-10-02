import streamlit as st
import info
import pandas as pd


def education_section(education_data, course_data):

    st.header("Education")

    st.subheader(f"{education_data['Institution']}")

    st.write(f"**Degree:** {education_data['Degree']}")

    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")

    st.write(f"**GPA:** {education_data['GPA']}")


    st.subheader("Coursework")

    coursework = pd.DataFrame(course_data)

    st.dataframe(coursework, column_config={

        "code": "Course Code",

        "names": "Course Names",

        "semester_taken": "Semester Taken",

        "skills": "What I Learned"

    }, hide_index=True)

    st.write("---")
education_section(info.education_data, info.course_data)

def experience_section(experience_data):

    st.header("Professional Experience")

    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(job_title)
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)

experience_section(info.experience_data)

def projects_section(projects_data):

    st.header("Projects")

    for project_name, project_description in projects_data.items():

        expander = st.expander(project_name)

        expander.write(project_description)
projects_section(info.projects_data)

def skills_section(programming_data, spoken_data):

    st.header("Skills")

    st.subheader("Programming Languages")

    for skill, percentage in programming_data.items():
        st.write(f'{skill} {info.programming_icons.get(skill, "")}')
        st.progress(percentage)


    st.subheader("Spoken Languages")

    for language, fluency in spoken_data.items():

        st.write(f'{info.spoken_icons.get(language, "")} {language}: {fluency}')

skills_section(info.programming_data, info.spoken_data)

def activities_section(leadership_data, activity_data):

    st.header("Activities")


    tab1, tab2 = st.tabs(["Leadership", "Community Service"])


    with tab1:
        st.subheader("Leadership")

        for title, (details, image) in leadership_data.items():
            expander = st.expander(title)
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)


    with tab2:
        st.subheader("Community Service")

        for title, details in activity_data.items():
            expander = st.expander(title)
            for bullet in details:
                expander.write(bullet)

                
activities_section(info.leadership_data, info.activity_data)
