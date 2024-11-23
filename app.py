import streamlit as st

# Application Header
st.title("Boiler Chemistry Q&A")
st.markdown("This application provides answers to boiler chemistry-related questions. Simply ask a question or select from the examples!")

# Predefined Q&A Data
questions_answers = {
    "Why is boiler chemistry essential for boiler operations?":
        "Boiler chemistry is vital to ensure efficient and safe operation by preventing issues like corrosion, scaling, and excessive buildup of impurities, which can lead to costly repairs and downtime.",
    "What types of water are typically used in boiler systems?":
        "The main types of water used are Raw Water, Make-Up Water, Feed Water, and Condensate Return. Each serves a unique purpose, from replacing water losses to maintaining water quality in the system.",
    "What is the role of 'Make-Up Water' in a boiler system?":
        "Make-Up Water is added to replace water lost due to steam production and leaks, ensuring the boiler has a consistent water level and proper functionality.",
    "What does 'water softening' do in boiler treatment?":
        "Water softening reduces hardness caused by minerals like calcium and magnesium, which can cause scale buildup. This helps to maintain heat transfer efficiency and reduce wear on the boiler.",
    "Why is deaeration necessary for boiler water?":
        "Deaeration removes dissolved gases, such as oxygen and carbon dioxide, that can lead to corrosion of the boiler's metal parts. This process helps extend the life of the boiler system.",
    "What are the optimal pH levels for boiler water, and why are they important?":
        "Boiler water should have a pH between 10 and 12 to prevent corrosion. Maintaining this range minimizes the risk of acidic or alkaline corrosion in the system.",
    "How does 'Total Dissolved Solids' (TDS) affect boiler performance?":
        "High TDS can lead to scaling and foaming, which reduce efficiency and cause overheating. Regular blowdowns help control TDS levels within safe limits, ensuring smoother operation.",
    "Why is monitoring dissolved oxygen important in boiler water?":
        "Dissolved oxygen should be kept below 7 ppb to avoid corrosion. Excessive oxygen in the boiler can corrode metal surfaces, which can lead to system failures.",
    "What are some best practices for maintaining good boiler water chemistry?":
        "Best practices include regular testing and monitoring, routine blowdowns to remove dissolved solids, and proper chemical dosing to maintain balanced pH and reduce impurities.",
    "How does proper boiler chemistry help improve efficiency?":
        "Maintaining proper chemistry prevents scale buildup and corrosion, allowing for better heat transfer, lower fuel consumption, and reduced maintenance costs, all of which enhance overall efficiency."
}

# User Input
st.markdown("### Enter your question or pick from examples:")
options = ["Type your own question"] + list(questions_answers.keys())
selected_question = st.selectbox("Scroll through the examples or type your own question:", options)

# Display Answer
if selected_question != "Type your own question":
    user_question = selected_question
else:
    user_question = st.text_input("Type your question below:")

if user_question:
    answer = questions_answers.get(user_question.strip(), "Sorry, I don't have an answer for that question.")
    st.markdown(f"**Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("### Developed by mak3.15")
