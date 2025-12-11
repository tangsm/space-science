import streamlit as st
import random
import time

# ==========================================
# 1. PAGE CONFIGURATION & FROZEN STYLE
# ==========================================
st.set_page_config(
    page_title="Space Explorer: Into the Unknown",
    page_icon="❄️",
    layout="centered"
)

# Custom CSS for "Frozen" Style (Ice, Magic, Snow)
st.markdown(
    """
    <style>
    /* Import magical fonts */
    @import url('https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@700&family=Quicksand:wght@500;700&display=swap');

    /* --- BACKGROUND: Icy Gradient --- */
    .stApp {
        background: linear-gradient(180deg, #002C59 0%, #1E5799 40%, #A5F2F3 100%);
        color: #FFFFFF;
    }

    /* --- TITLE (Magical & Icy) --- */
    .frozen-header {
        font-family: 'Mountains of Christmas', cursive;
        color: #E0FFFF; /* Light Cyan */
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #00BFFF;
        text-align: center;
        font-size: 60px;
        margin-bottom: 0px;
        line-height: 1.2;
    }
    
    .frozen-sub {
        font-family: 'Quicksand', sans-serif;
        color: #A5F2F3;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }

    /* --- QUESTION BOX --- */
    .question-box {
        background-color: rgba(255, 255, 255, 0.15);
        border: 2px solid #A5F2F3;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        font-family: 'Quicksand', sans-serif;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(165, 242, 243, 0.3);
        backdrop-filter: blur(5px);
    }

    /* --- BUTTONS (Ice Blocks) --- */
    div.stButton > button {
        font-family: 'Quicksand', sans-serif !important;
        font-weight: bold !important;
        font-size: 20px !important;
        color: #002C59 !important; /* Deep Blue Text */
        background-color: #F0FFFF !important; /* Azure/White */
        border: 2px solid #00BFFF !important;
        border-radius: 15px !important;
        height: auto !important;
        padding: 15px !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        transform: scale(1.02);
        background-color: #00BFFF !important;
        color: #FFFFFF !important;
        border-color: #FFFFFF !important;
        box-shadow: 0 0 15px #FFFFFF;
    }

    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #F0FFFF;
        border-right: 2px solid #00BFFF;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #002C59 !important;
        font-family: 'Quicksand', sans-serif !important;
    }
    
    /* --- PROGRESS BAR --- */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #A5F2F3, #FFFFFF);
    }
    
    /* --- GAME OVER TEXT --- */
    .game-over-text {
        text-align: center; 
        font-family: 'Quicksand', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 2. THE 50-QUESTION SPACE POOL
# ==========================================
QUESTION_BANK = [
    # --- Solar System Basics ---
    {"q": "What is the biggest planet in our solar system?", "options": ["Jupiter", "Earth", "Saturn", "Mars"], "a": "Jupiter", "info": "Jupiter is so big that all the other planets could fit inside it!"},
    {"q": "Which planet is known as the 'Red Planet'?", "options": ["Mars", "Venus", "Jupiter", "Mercury"], "a": "Mars", "info": "It looks red because of rusty dust covering the ground."},
    {"q": "What is the Sun?", "options": ["A Star", "A Planet", "A Moon", "A Comet"], "a": "A Star", "info": "The Sun is a medium-sized star that gives us heat and light."},
    {"q": "Which planet has beautiful large rings around it?", "options": ["Saturn", "Mars", "Neptune", "Venus"], "a": "Saturn", "info": "Saturn's rings are made of chunks of ice and rock."},
    {"q": "Which is the hottest planet in the solar system?", "options": ["Venus", "Mercury", "Mars", "Sun"], "a": "Venus", "info": "Thick clouds trap the heat on Venus, making it hotter than an oven!"},
    {"q": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "a": "Mercury", "info": "Mercury zips around the Sun faster than any other planet."},
    {"q": "What is the name of our galaxy?", "options": ["The Milky Way", "Andromeda", "The Snickers", "The Whirlpool"], "a": "The Milky Way", "info": "When you look up at night, the band of stars looks like spilled milk."},
    {"q": "How many Earths could fit inside the Sun?", "options": ["One Million", "One Hundred", "Ten", "Two"], "a": "One Million", "info": "The Sun is super duper huge!"},
    {"q": "Which planet is known as the 'Blue Planet'?", "options": ["Earth", "Neptune", "Uranus", "Mars"], "a": "Earth", "info": "It looks blue from space because it is covered in water."},
    {"q": "What is the farthest planet from the Sun?", "options": ["Neptune", "Uranus", "Saturn", "Pluto"], "a": "Neptune", "info": "It is very cold and windy on Neptune."},
    
    # --- The Moon & Space Travel ---
    {"q": "Who was the first person to walk on the Moon?", "options": ["Neil Armstrong", "Buzz Lightyear", "Albert Einstein", "Elon Musk"], "a": "Neil Armstrong", "info": "He took 'one small step for man, one giant leap for mankind.'"},
    {"q": "What shape is the Earth?", "options": ["A Sphere (Ball)", "Flat", "A Square", "A Donut"], "a": "A Sphere (Ball)", "info": "Earth is round like a ball, slightly squished at the top and bottom."},
    {"q": "What vehicle do astronauts use to go to space?", "options": ["Rocket", "Airplane", "Helicopter", "Car"], "a": "Rocket", "info": "Rockets have powerful engines to escape Earth's gravity."},
    {"q": "What do astronauts wear to stay safe outside?", "options": ["Space Suit", "Swim Suit", "Winter Coat", "Pajamas"], "a": "Space Suit", "info": "Space suits provide air to breathe and protection from the cold."},
    {"q": "What force keeps our feet on the ground?", "options": ["Gravity", "Magnetism", "Glue", "Wind"], "a": "Gravity", "info": "Gravity pulls everything toward the center of the Earth."},
    
    # --- Deep Space & Phenomena ---
    {"q": "What is in the center of the Milky Way?", "options": ["A Black Hole", "A Giant Sun", "A Planet", "Candy"], "a": "A Black Hole", "info": "It's called Sagittarius A* and its gravity is super strong."},
    {"q": "How did the universe begin?", "options": ["The Big Bang", "The Big Crunch", "The Big Sneeze", "It was always there"], "a": "The Big Bang", "info": "About 14 billion years ago, the universe exploded into existence!"},
    {"q": "What is a shooting star?", "options": ["A Meteor burning up", "A falling star", "A comet", "An alien"], "a": "A Meteor burning up", "info": "It's a tiny rock burning up as it hits Earth's air."},
    {"q": "What is a constellation?", "options": ["A group of stars", "A type of planet", "A space ship", "A storm"], "a": "A group of stars", "info": "Like the Big Dipper or Orion the Hunter."},
    {"q": "What is the North Star called?", "options": ["Polaris", "Sirius", "Vega", "Betelgeuse"], "a": "Polaris", "info": "Sailors used Polaris to find their way at night."},

    # --- Specific Prompts ---
    {"q": "How many dwarf planets are officially in our solar system?", "options": ["5", "1", "9", "100"], "a": "5", "info": "They are Pluto, Eris, Haumea, Makemake, and Ceres."},
    {"q": "Which of these is a Dwarf Planet?", "options": ["Pluto", "Mercury", "Titan", "Luna"], "a": "Pluto", "info": "Pluto used to be the 9th planet but is now a dwarf planet."},
    {"q": "What is the Great Red Spot on Jupiter?", "options": ["A giant storm", "A volcano", "A lake", "A crater"], "a": "A giant storm", "info": "It is a hurricane bigger than the entire Earth!"},
    {"q": "What did Mars look like a long time ago?", "options": ["It had water and rivers", "It was on fire", "It was green", "It was made of ice"], "a": "It had water and rivers", "info": "Scientists found dried-up river beds on Mars."},
    {"q": "What are comets made of?", "options": ["Ice and dust", "Fire", "Rock only", "Metal"], "a": "Ice and dust", "info": "Comets are like dirty snowballs flying through space."},

    # --- More Fun Facts ---
    {"q": "How long does it take Earth to go around the Sun?", "options": ["365 days (1 Year)", "24 Hours", "1 Month", "10 Years"], "a": "365 days (1 Year)", "info": "This journey gives us our seasons."},
    {"q": "Why do we have day and night?", "options": ["Earth spins", "Sun turns off", "Moon blocks Sun", "Clouds cover it"], "a": "Earth spins", "info": "When your side faces the Sun, it's day!"},
    {"q": "Which planet spins on its side?", "options": ["Uranus", "Mars", "Earth", "Jupiter"], "a": "Uranus", "info": "Uranus rolls around the Sun like a bowling ball."},
    {"q": "Which planet has the tallest mountain?", "options": ["Mars", "Earth", "Venus", "Mercury"], "a": "Mars", "info": "Olympus Mons on Mars is 3 times taller than Everest!"},
    {"q": "What is the name of the space station humans live on?", "options": ["ISS (International Space Station)", "The Death Star", "Moon Base Alpha", "Skylab"], "a": "ISS (International Space Station)", "info": "Astronauts live there to do science experiments."},
    {"q": "What do we call a rock that hits the ground on Earth?", "options": ["Meteorite", "Meteor", "Asteroid", "Comet"], "a": "Meteorite", "info": "If it survives the fall, it's a meteorite."},
    {"q": "Which is the smallest planet?", "options": ["Mercury", "Mars", "Venus", "Neptune"], "a": "Mercury", "info": "It is only a little bit bigger than our Moon."},
    {"q": "Does the Moon have its own light?", "options": ["No, it reflects the Sun", "Yes, like a lightbulb", "Yes, it is a star", "Sometimes"], "a": "No, it reflects the Sun", "info": "The Moon acts like a mirror for sunlight."},
    {"q": "What causes the ocean tides?", "options": ["The Moon's gravity", "The wind", "Whales jumping", "The Sun's heat"], "a": "The Moon's gravity", "info": "The Moon pulls on Earth's water."},
    {"q": "What is a supernova?", "options": ["An exploding star", "A fast planet", "A new galaxy", "A space hero"], "a": "An exploding star", "info": "It happens when a big star runs out of fuel."},
    {"q": "What gas do stars burn?", "options": ["Hydrogen", "Oxygen", "Carbon Dioxide", "Nitrogen"], "a": "Hydrogen", "info": "Stars turn hydrogen into helium to make energy."},
    {"q": "How old is the solar system?", "options": ["4.5 Billion Years", "2024 Years", "1 Million Years", "100 Years"], "a": "4.5 Billion Years", "info": "That's super old!"},
    {"q": "Which planet has a beautiful 'Great Dark Spot'?", "options": ["Neptune", "Jupiter", "Saturn", "Mercury"], "a": "Neptune", "info": "Neptune is very stormy and blue."},
    {"q": "Can you hear sound in space?", "options": ["No, it is silent", "Yes, very loud", "Only music", "Only explosions"], "a": "No, it is silent", "info": "There is no air in space to carry sound waves."},
    {"q": "What protects Earth from dangerous sun rays?", "options": ["The Atmosphere", "The Moon", "The Ocean", "Clouds"], "a": "The Atmosphere", "info": "It acts like a blanket and a shield."},
    {"q": "What killed the dinosaurs?", "options": ["A giant asteroid", "A flood", "Too much snow", "Aliens"], "a": "A giant asteroid", "info": "It hit Earth 65 million years ago."},
    {"q": "What is the 'Goldilocks Zone'?", "options": ["Just the right temperature for life", "A place with bears", "A hot zone", "A cold zone"], "a": "Just the right temperature for life", "info": "Earth is in this zone - not too hot, not too cold."},
    {"q": "How many moons does Earth have?", "options": ["1", "2", "0", "100"], "a": "1", "info": "We call it 'The Moon'."},
    {"q": "Which planet rotates backwards?", "options": ["Venus", "Earth", "Mars", "Jupiter"], "a": "Venus", "info": "On Venus, the Sun rises in the West!"},
    {"q": "What is an Exoplanet?", "options": ["A planet outside our solar system", "A dead planet", "A dwarf planet", "A moon"], "a": "A planet outside our solar system", "info": "We have found thousands of them!"},
    {"q": "What is the speed of light?", "options": ["Super fast", "Slow", "Same as a car", "Same as sound"], "a": "Super fast", "info": "Light can go around Earth 7 times in 1 second."},
    {"q": "What color is a sunset on Mars?", "options": ["Blue", "Red", "Green", "Yellow"], "a": "Blue", "info": "Dust in the atmosphere makes the sunset look blue."},
    {"q": "What is a light-year?", "options": ["A measure of distance", "A measure of time", "A bright year", "A fast year"], "a": "A measure of distance", "info": "It's how far light travels in one year."},
    {"q": "Who was the first woman in space?", "options": ["Valentina Tereshkova", "Sally Ride", "Elsa", "Anna"], "a": "Valentina Tereshkova", "info": "She went to space in 1963."},
    {"q": "What is the closest star to Earth?", "options": ["The Sun", "Proxima Centauri", "Sirius", "Alpha Centauri"], "a": "The Sun", "info": "It's 93 million miles away!"}
]

# ==========================================
# 3. GAME LOGIC
# ==========================================

def get_shuffled_options(question_data):
    """Helper to shuffle options and ensure they stay shuffled in state"""
    options = question_data['options']
    return random.sample(options, len(options))

# Initialize Session State
if 'quiz_session' not in st.session_state:
    st.session_state.quiz_session = random.sample(QUESTION_BANK, 10)
    st.session_state.score = 0
    st.session_state.current_index = 0
    st.session_state.game_over = False
    
    # FIX: Initialize the first set of options and store them
    first_q = st.session_state.quiz_session[0]
    st.session_state.current_options = get_shuffled_options(first_q)

def restart_game():
    st.session_state.quiz_session = random.sample(QUESTION_BANK, 10)
    st.session_state.score = 0
    st.session_state.current_index = 0
    st.session_state.game_over = False
    
    # FIX: Reset the options for the new first question
    first_q = st.session_state.quiz_session[0]
    st.session_state.current_options = get_shuffled_options(first_q)
    st.rerun()

# ==========================================
# 4. UI DISPLAY
# ==========================================

# Sidebar
with st.sidebar:
    st.markdown("### ☃️ Explorer Tools")
    st.write("Welcome, Astronomer!")
    if st.button("🔄 Restart Adventure"):
        restart_game()

# Header
st.markdown('<p class="frozen-header">Space Explorer</p>', unsafe_allow_html=True)
st.markdown('<p class="frozen-sub">❄️ INTO THE UNKNOWN ❄️</p>', unsafe_allow_html=True)

if not st.session_state.game_over:
    # Get current question
    idx = st.session_state.current_index
    q_data = st.session_state.quiz_session[idx]
    
    # Progress Bar (Ice Blue)
    st.progress((idx) / 10)
    st.caption(f"Mystery {idx + 1} of 10")
    
    # Display Question
    st.markdown(f'<div class="question-box">{q_data["q"]}</div>', unsafe_allow_html=True)
    
    # FIX: Use the stored options from session_state, do NOT shuffle here
    current_options = st.session_state.current_options
    
    col1, col2 = st.columns(2)
    for i, option in enumerate(current_options):
        col = col1 if i % 2 == 0 else col2
        # Using a unique key for each button ensures stability
        if col.button(option, use_container_width=True, key=f"q{idx}_opt{i}"):
            
            # Check Answer
            if option == q_data['a']:
                st.session_state.score += 1
                st.toast(f"🌟 Correct! {q_data['info']}", icon="❄️")
            else:
                st.toast(f"🧊 Oops! The answer was {q_data['a']}.", icon="☃️")
                time.sleep(1) # Small pause to see the result
            
            # Next Question Logic
            if st.session_state.current_index + 1 < 10:
                st.session_state.current_index += 1
                
                # FIX: Prepare shuffled options for the NEXT question before rerunning
                next_q = st.session_state.quiz_session[st.session_state.current_index]
                st.session_state.current_options = get_shuffled_options(next_q)
                
                st.rerun()
            else:
                st.session_state.game_over = True
                st.rerun()

else:
    # --- GAME OVER SCREEN ---
    score = st.session_state.score
    
    st.markdown('<div class="question-box" style="background-color: rgba(255,255,255,0.3);">Journey Complete!</div>', unsafe_allow_html=True)
    
    # Snow Balloons
    st.balloons()
    
    # Result Message based on Frozen Theme
    if score == 10:
        msg = "👑 You are the Queen/King of the Stars! (Perfect Score!)"
    elif score >= 7:
        msg = "✨ The sky is awake, so are you! Great job!"
    elif score >= 4:
        msg = "☃️ Some mistakes are okay. Do you want to build a spaceship?"
    else:
        msg = "❄️ Let it go! Try again and learn more!"
        
    st.markdown(
        f"""
        <div class="game-over-text">
            <h1 style='color: #E0FFFF; font-family: Mountains of Christmas; font-size: 50px;'>{score} / 10 Correct</h1>
            <h3 style='color: #A5F2F3;'>{msg}</h3>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("")
    if st.button("🚀 Blast Off Again (New Questions)", type="primary", use_container_width=True):
        restart_game()
