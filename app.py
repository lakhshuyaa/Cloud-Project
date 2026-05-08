import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7ff;
}
h1 {
    color: #4b0082;
    text-align: center;
}
.stButton>button {
    background-color: #6a5acd;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 Student Evaluation System")

st.write("### Enter Student Details")

# Student Details
name = st.text_input("👤 Student Name")
roll = st.text_input("🆔 Roll Number")
department = st.selectbox(
    "🏫 Department",
    ["CSE", "AI & DS", "IT", "ECE", "EEE", "MECH"]
)

year = st.selectbox(
    "📚 Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# Subject Marks
st.write("### 📖 Enter Subject Marks")

python_marks = st.slider("Python", 0, 100, 50)
ml_marks = st.slider("Machine Learning", 0, 100, 50)
cloud_marks = st.slider("Cloud Computing", 0, 100, 50)
dbms_marks = st.slider("DBMS", 0, 100, 50)
os_marks = st.slider("Operating Systems", 0, 100, 50)

# Attendance
attendance = st.slider("📅 Attendance Percentage", 0, 100, 75)

# Button
if st.button("Generate Report"):

    total = (
        python_marks +
        ml_marks +
        cloud_marks +
        dbms_marks +
        os_marks
    )

    average = total / 5

    # Grade Calculation
    if average >= 90:
        grade = "A+"
        performance = "Outstanding 🌟"
    elif average >= 75:
        grade = "A"
        performance = "Excellent 🎉"
    elif average >= 60:
        grade = "B"
        performance = "Good 👍"
    elif average >= 50:
        grade = "C"
        performance = "Average 🙂"
    else:
        grade = "F"
        performance = "Needs Improvement ❌"

    # Result
    result = "PASS ✅" if average >= 50 else "FAIL ❌"

    st.write("---")

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.subheader("📋 Student Report Card")

    st.write(f"### 👤 Name: {name}")
    st.write(f"### 🆔 Roll Number: {roll}")
    st.write(f"### 🏫 Department: {department}")
    st.write(f"### 📚 Year: {year}")

    st.write("---")

    st.write(f"## 📊 Total Marks: {total}/500")
    st.write(f"## 📈 Average: {average:.2f}%")
    st.write(f"## 🏅 Grade: {grade}")
    st.write(f"## 🎯 Performance: {performance}")
    st.write(f"## 📌 Result: {result}")

    st.write(f"## 📅 Attendance: {attendance}%")

    # Suggestions
    st.write("### 💡 Suggestions")

    if attendance < 75:
        st.warning("Improve attendance for better academic performance.")

    if average < 60:
        st.info("Focus more on practical learning and daily revision.")

    if average >= 90:
        st.balloons()
        st.success("Excellent work! Keep shining!")

    st.markdown('</div>', unsafe_allow_html=True)

    # Subject Comparison Table
    st.write("### 📚 Subject-wise Comparison")

    data = {
        "Subject": [
            "Python",
            "Machine Learning",
            "Cloud Computing",
            "DBMS",
            "Operating Systems"
        ],
        "Marks": [
            python_marks,
            ml_marks,
            cloud_marks,
            dbms_marks,
            os_marks
        ]
    }

    df = pd.DataFrame(data)

    st.table(df)

    # Bar Chart
    st.write("### 📊 Marks Visualization")
    st.bar_chart(df.set_index("Subject"))