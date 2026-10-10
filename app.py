
import streamlit as st

st.set_page_config(
    page_title="SkillSwap | Student Skill Exchange",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f3ff, #eff6ff, #f8fafc);
    color: #1e1b4b;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #24134f, #43318b);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(120deg, #4338ca, #7c3aed, #2563eb);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 10px;
}

.hero p {
    color: #ede9fe;
    font-size: 17px;
}

.profile {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e0e7ff;
    box-shadow: 0 5px 18px rgba(67, 56, 202, 0.08);
    min-height: 245px;
}

.profile h3 {
    color: #312e81;
}

.skill-tag {
    display: inline-block;
    background: #ede9fe;
    color: #5b21b6;
    padding: 5px 10px;
    border-radius: 20px;
    margin: 4px 3px 4px 0;
    font-size: 13px;
}

.small-text {
    color: #64748b;
    font-size: 14px;
}

div.stButton > button {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 15px;
    font-weight: 600;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #312e81;
    color: white;
    border: none;
}

h1, h2, h3 {
    color: #312e81;
}

[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #e0e7ff;
}
</style>
""", unsafe_allow_html=True)


# # ---------- SAMPLE STUDENT DATA ----------
# students = [
#     {
#         "id": 1,
#         "name": "Ravi Kumar",
#         "emoji": "👨‍💻",
#         "department": "Computer Science",
#         "teaches": ["HTML", "CSS", "JavaScript"],
#         "learns": ["Python", "SQL"],
#         "rating": 4.8,
#         "level": "Intermediate",
#         "availability": "Weekends"
#     },
#     {
#         "id": 2,
#         "name": "Pooja",
#         "emoji": "👩‍💻",
#         "department": "Information Technology",
#         "teaches": ["Python", "SQL"],
#         "learns": ["HTML", "CSS"],
#         "rating": 4.9,
#         "level": "Intermediate",
#         "availability": "Evenings"
#     },
#     {
#         "id": 3,
#         "name": "Anu Sharma",
#         "emoji": "👩‍🎓",
#         "department": "Computer Science",
#         "teaches": ["Java", "Python"],
#         "learns": ["CSS", "UI Design"],
#         "rating": 4.7,
#         "level": "Advanced",
#         "availability": "Weekends"
#     },
#     {
#         "id": 4,
#         "name": "Kiran Reddy",
#         "emoji": "🧑‍🎨",
#         "department": "Electronics",
#         "teaches": ["UI Design", "CSS"],
#         "learns": ["JavaScript", "Python"],
#         "rating": 4.6,
#         "level": "Beginner",
#         "availability": "Evenings"
#     },
#     {
#         "id": 5,
#         "name": "Sneha",
#         "emoji": "👩‍💼",
#         "department": "Business Studies",
#         "teaches": ["Communication", "Excel"],
#         "learns": ["Python", "SQL"],
#         "rating": 4.8,
#         "level": "Intermediate",
#         "availability": "Weekends"
#     },
    # {
    #     "id": 6,
    #     "name": "Arjun",
    #     "emoji": "👨‍🎓",
    #     "department": "Computer Science",
    #     "teaches": ["SQL", "Python"],
    #     "learns": ["Java", "HTML"],
    #     "rating": 4.5,
    #     "level": "Advanced",
    #     "availability": "Evenings"
    # }
    
    # {
    # "id": 1,
    # "name": "Ravi Kumar",
    # "emoji": "👨‍💻",
    # "department": "Computer Science",
    # "teaches": ["Python", "HTML"],
    # "learns": ["SQL"],
    # "rating": 4.8,
    # "level": "Intermediate",
    # "availability": [
    #     "10:00 AM - 11:00 AM",
    #     "6:00 PM - 7:00 PM"
    # ]
    # }


    
# students = [
#     {
#         "id": 6,
#         "name": "Arjun",
#         "emoji": "👨‍🎓",
#         "department": "Computer Science",
#         "teaches": ["SQL", "Python"],
#         "learns": ["Java", "HTML"],
#         "rating": 4.5,
#         "level": "Advanced",
#         "availability": [
#             "10:00 AM - 11:00 AM",
#             "6:00 PM - 7:00 PM"
#         ]
#     },
#     {
#         "id": 1,
#         "name": "Ravi Kumar",
#         "emoji": "👨‍💻",
#         "department": "Computer Science",
#         "teaches": ["Python", "HTML"],
#         "learns": ["SQL"],
#         "rating": 4.8,
#         "level": "Intermediate",
#         "availability": [
#             "10:00 AM - 11:00 AM",
#             "6:00 PM - 7:00 PM"
#         ]
#     }
# ]

# ]

# ---------- SAMPLE STUDENT DATA ----------
students = [
    {
        "id": 1,
        "name": "Ravi Kumar",
        "emoji": "👨‍💻",
        "department": "Computer Science",
        "teaches": ["HTML", "CSS", "JavaScript"],
        "learns": ["Python", "SQL"],
        "rating": 4.8,
        "level": "Intermediate",
        "availability": ["Weekends", "10:00 AM - 11:00 AM", "6:00 PM - 7:00 PM"]
    },
    {
        "id": 2,
        "name": "Pooja",
        "emoji": "👩‍💻",
        "department": "Information Technology",
        "teaches": ["Python", "SQL"],
        "learns": ["HTML", "CSS"],
        "rating": 4.9,
        "level": "Intermediate",
        "availability": ["Evenings", "6:00 PM - 7:00 PM"]
    },
    {
        "id": 3,
        "name": "Anu Sharma",
        "emoji": "👩‍🎓",
        "department": "Computer Science",
        "teaches": ["Java", "Python"],
        "learns": ["CSS", "UI Design"],
        "rating": 4.7,
        "level": "Advanced",
        "availability": ["Weekends", "10:00 AM - 11:00 AM"]
    },
    {
        "id": 4,
        "name": "Kiran Reddy",
        "emoji": "🧑‍🎨",
        "department": "Electronics",
        "teaches": ["UI Design", "CSS"],
        "learns": ["JavaScript", "Python"],
        "rating": 4.6,
        "level": "Beginner",
        "availability": ["Evenings", "6:00 PM - 7:00 PM"]
    },
    {
        "id": 5,
        "name": "Sneha",
        "emoji": "👩‍💼",
        "department": "Business Studies",
        "teaches": ["Communication", "Excel"],
        "learns": ["Python", "SQL"],
        "rating": 4.8,
        "level": "Intermediate",
        "availability": ["Weekends", "10:00 AM - 11:00 AM"]
    },
    {
        "id": 6,
        "name": "Arjun",
        "emoji": "👨‍🎓",
        "department": "Computer Science",
        "teaches": ["SQL", "Python"],
        "learns": ["Java", "HTML"],
        "rating": 4.5,
        "level": "Advanced",
        "availability": ["Evenings", "10:00 AM - 11:00 AM", "6:00 PM - 7:00 PM"]
    }
]



# ---------- SESSION STATE ----------
if "requests" not in st.session_state:
    st.session_state.requests = []

if "my_name" not in st.session_state:
    st.session_state.my_name = ""


# ---------- SIDEBAR ----------
# with st.sidebar:
#     st.markdown("# 🎓 SkillSwap")
#     st.caption("LEARN • SHARE • GROW")
#     st.divider()

#     page = st.radio(
#         "NAVIGATION",
#         ["🏠 Dashboard", "🔍 Explore Students",
#          "🤝 My Requests", "ℹ️ About Project"]
#     )

#     st.divider()
#     st.markdown("### 👤 Your Profile")

#     my_name = st.text_input(
#         "Your name",
#         value=st.session_state.my_name,
#         placeholder="Enter your name"
#     )
#     st.session_state.my_name = my_name.strip()

#     st.caption("Connect with students and exchange knowledge.")




# ---------- SIDEBAR ----------
# with st.sidebar:
#     st.markdown("# 🎓 SkillSwap")
#     st.caption("LEARN • SHARE • GROW")
#     st.divider()

#     page = st.radio(
#         "NAVIGATION",
#         [
#             "🏠 Dashboard",
#             "🔍 Explore Students",
#             "🤝 My Requests",
#             "ℹ️ About Project"
#         ]
#     )

#     st.divider()
#     st.markdown("### 👤 Your Profile")

#     # Initialize session state
#     if "my_name" not in st.session_state:
#         st.session_state.my_name = ""

#     my_name = st.text_input(
#         "Your name",
#         value=st.session_state.my_name,
#         placeholder="Enter your name",
#         key="profile_name_input"
#     )

#     st.session_state.my_name = my_name.strip()
#     st.session_state.current_student = my_name.strip()

#     if not my_name.strip():
#         st.warning("Please enter your name before sending a request.")

#     st.caption("Connect with students and exchange knowledge.")
#     my_name = st.text_input(
#     "Your name",
#     value=st.session_state.my_name,
#     placeholder="Enter your name"
# )

# ---------- SESSION STATE ----------
if "my_name" not in st.session_state:
    st.session_state.my_name = ""

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("# 🎓 SkillSwap")
    st.caption("LEARN • SHARE • GROW")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Dashboard",
            "🔍 Explore Students",
            "🤝 My Requests",
            "ℹ️ About Project"
        ]
    )

    st.divider()
    st.markdown("### 👤 Your Profile")

    my_name = st.text_input(
        "Your name",
        key="my_name_input",
        placeholder="Enter your name"
    )

    st.session_state.my_name = my_name.strip()
    st.session_state.current_student = my_name.strip()

    st.caption("Connect with students and exchange knowledge.")



# ---------- DASHBOARD ----------
if page == "🏠 Dashboard":
    
    st.divider()
    st.header("🤝 Smart Skill Matching")
    st.write(
        "Find students who teach your interested skill "
        "and are available at your preferred time."
    )

    all_skills = sorted(
        set(skill for student in students
            for skill in student["teaches"])
    )

    skill_to_learn = st.selectbox(
        "Which skill do you want to learn?",
        all_skills,
        key="match_skill"
    )

    my_time = st.selectbox(
        "Select your available time",
        [
            "10:00 AM - 11:00 AM",
            "2:00 PM - 3:00 PM",
            "6:00 PM - 7:00 PM",
            "7:00 PM - 8:00 PM"
        ],
        key="match_time"
    )

    if st.button("✨ Find My Match"):
        matches = []

        for student in students:
            teaches_skill = any(
                skill.lower() == skill_to_learn.lower()
                for skill in student["teaches"]
            )

            wants_skill = any(
                skill.lower() == skill_to_learn.lower()
                for skill in student["learns"]
            )

            time_matches = my_time in student["availability"]

            is_self = (
                st.session_state.my_name.lower()
                == student["name"].lower()
            ) if st.session_state.my_name else False

            if teaches_skill and time_matches and not is_self:
                matches.append((student, wants_skill))

        if matches:
            st.success(f"Found {len(matches)} matching student(s)!")

            for student, wants_skill in matches:
                with st.container(border=True):
                    st.subheader(
                        f"{student['emoji']} {student['name']}"
                    )
                    st.write("📚 Can teach:", skill_to_learn)
                    st.write("🕒 Available:", my_time)
                    st.write("⭐ Rating:", student["rating"])

                    if wants_skill:
                        st.info(
                            "🎉 Great exchange! This student also "
                            "wants to learn " + skill_to_learn + "."
                        )
                    else:
                        st.write(
                            "You can learn this skill from this student."
                        )

                    if st.button(
                        "🤝 Connect",
                        key=f"smart_{student['id']}"
                    ):
                        if not st.session_state.my_name:
                            st.warning(
                                "Enter your name in the sidebar first."
                            )
                        elif any(
                            r["student_id"] == student["id"]
                            and r["from"] == st.session_state.my_name
                            for r in st.session_state.requests
                        ):
                            st.info("Request already sent.")
                        else:
                            st.session_state.requests.append({
                                "student_id": student["id"],
                                "name": student["name"],
                                "from": st.session_state.my_name,
                                "status": "Pending"
                            })
                            st.success("Connection request created!")
        else:
            st.warning(
                "No exact skill and time match found. "
                "Try another time or skill."
            )


    st.markdown("""
    <div class="hero">
        <h1>Learn Together. Grow Together. 🚀</h1>
        <p>Share what you know. Discover what you can learn.
        Find your perfect learning partner!</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    c1.metric("👩‍🎓 Students", len(students))
    c2.metric(
        "💡 Skills",
        len(set(skill for s in students for skill in s["teaches"]))
    )
    c3.metric("🤝 My Requests", len(st.session_state.requests))

    st.divider()

    st.subheader("✨ Featured Learning Partners")
    st.write("Explore students who are ready to share their knowledge.")

    cols = st.columns(3)

    for i, student in enumerate(students[:3]):
        with cols[i]:
            with st.container(border=True):
                st.markdown(
                    f"## {student['emoji']} {student['name']}"
                )
                st.caption(student["department"])
                st.write("⭐", student["rating"], "/ 5")
                st.write("**Can teach**")
                st.write(", ".join(student["teaches"]))
                st.write("**Wants to learn**")
                st.write(", ".join(student["learns"]))

                st.button(
                    "🤝 Connect",
                    key=f"home_{student['id']}",
                    use_container_width=True
                )
                if not st.session_state.my_name:
                        st.warning("Enter your name in the sidebar first.")
                elif st.session_state.my_name.lower() == student["name"].lower():
                        st.warning("You cannot connect with yourself.")
                elif any(
                        r["student_id"] == student["id"]
                        and r["from"] == st.session_state.my_name
                        for r in st.session_state.requests
                    ):
                        st.info("You already sent a request to this student.")
                else:
                        st.session_state.requests.append({
                            "student_id": student["id"],
                            "name": student["name"],
                            "from": st.session_state.my_name,
                            "status": "Pending"
                        })
                        st.success("Request created!")
                        st.rerun()

    if st.button("🔍 Explore All Students"):
        st.session_state.go_explore = True
        st.info("Select Explore Students from the sidebar.")



# ---------- EXPLORE STUDENTS ----------
elif page == "🔍 Explore Students":

    st.title("🔍 Explore Students")
    st.write("Find a student who can teach the skills you want to learn.")

    col1, col2 = st.columns([2, 1])

    with col1:
        search = st.text_input(
            "Search by name or skill",
            placeholder="Try Python, HTML, Ravi..."
        ).strip().lower()

    with col2:
        availability = st.selectbox(
            "Availability",
            ["All", "Weekends", "Evenings"]
        )

    all_skills = sorted(
        set(skill for s in students for skill in s["teaches"])
    )

    selected_skill = st.selectbox(
        "Filter by teaching skill",
        ["All Skills"] + all_skills
    )

    min_rating = st.select_slider(
        "Minimum rating",
        options=[0.0, 3.0, 3.5, 4.0, 4.5, 4.8],
        value=0.0
    )

    filtered = []

    for student in students:
        searchable = (
            student["name"] + " " +
            student["department"] + " " +
            " ".join(student["teaches"]) + " " +
            " ".join(student["learns"])
        ).lower()

        if search and search not in searchable:
            continue

        if selected_skill != "All Skills" and selected_skill not in student["teaches"]:
            continue

        if availability != "All" and student["availability"] != availability:
            continue

        if student["rating"] < min_rating:
            continue

        filtered.append(student)

    st.caption(f"Found {len(filtered)} student(s)")

    if not filtered:
        st.warning("No matching students. Try another search or filter.")

    cols = st.columns(3)

    for i, student in enumerate(filtered):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(
                    f"## {student['emoji']} {student['name']}"
                )
                st.caption(student["department"])
                st.write(f"⭐ {student['rating']} / 5")
                st.write(f"📚 Level: {student['level']}")
                st.write(f"🕒 {student['availability']}")

                st.write("**Skills they teach**")
                st.markdown(
                    " ".join(
                        f'<span class="skill-tag">{skill}</span>'
                        for skill in student["teaches"]
                    ),
                    unsafe_allow_html=True
                )

                st.write("**Skills they want to learn**")
                st.write(", ".join(student["learns"]))

                if st.button(
                    "🤝 Send Connect Request",
                    key=f"explore_{student['id']}",
                    use_container_width=True
                ):
                    if not st.session_state.my_name:
                        st.warning("Enter your name in the sidebar first.")
                    elif st.session_state.my_name.lower() == student["name"].lower():
                        st.warning("You cannot connect with yourself.")
                    elif any(
                        r["student_id"] == student["id"]
                        and r["from"] == st.session_state.my_name
                        for r in st.session_state.requests
                    ):
                        st.info("Request already sent.")
                    else:
                        st.session_state.requests.append({
                            "student_id": student["id"],
                            "name": student["name"],
                            "from": st.session_state.my_name,
                            "status": "Pending"
                        })
                        st.success(f"Request sent to {student['name']}!")
                        st.rerun()





# ---------- MY REQUESTS ----------
elif page == "🤝 My Requests":

    st.title("🤝 My Connection Requests")
    st.write("Check the requests you have sent during this session.")

    if "requests" not in st.session_state:
        st.session_state.requests = []

    if not st.session_state.requests:
        st.info("No requests yet. Explore students and connect with them!")

    else:
        for request in st.session_state.requests:
            with st.container(border=True):
                st.subheader(f"👤 {request['name']}")

                st.write("Sent by:", request.get("from", "You"))
                st.write("Skill:", request.get("skill", "Not specified"))
                st.write("Status:", request.get("status", "Pending"))

                if st.button(
                    "❌ Cancel Request",
                    key=f"cancel_{request['student_id']}_{request.get('from', 'You')}"
                ):
                    st.session_state.requests.remove(request)
                   
# ---------- ABOUT ----------
elif page == "ℹ️ About Project":

    st.title("ℹ️ About SkillSwap")

    st.markdown("""
    ### Our Mission 🌟

    Student Skill Exchange Platform helps students teach skills
    they already know and learn new skills from their peers.

    ### Key Features

    - 👤 Student profiles
    - 🔍 Search and skill filters
    - ⭐ Student ratings
    - 🤝 Connection requests
    - 📚 Peer-to-peer learning

    ### Future Enhancements

    - Secure registration and login
    - Database integration
    - Real-time messaging
    - AI-powered student matching
    - Verified profiles and feedback

    **Built for the Student Skill Exchange hackathon.**
    """)


