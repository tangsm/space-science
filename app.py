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
    
    /* --- EXPANDER (REVIEW SECTION) --- */
    .streamlit-expanderHeader {
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        color: #002C59;
        background-color: #A5F2F3;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 2. THE 200-QUESTION SPACE POOL
# ==========================================
QUESTION_BANK = [
    # --- The Sun ---
    {"q": "What is the Sun?", "options": ["A Star", "A Planet", "A Moon", "A Comet"], "a": "A Star", "info": "The Sun is a medium-sized star at the center of our solar system."},
    {"q": "What is the Sun mostly made of?", "options": ["Gas (Hydrogen & Helium)", "Rock", "Lava", "Gold"], "a": "Gas (Hydrogen & Helium)", "info": "It is a giant ball of burning gas."},
    {"q": "How many Earths could fit inside the Sun?", "options": ["One Million", "One Hundred", "Fifty", "Two"], "a": "One Million", "info": "The Sun is super duper huge!"},
    {"q": "What gives the Sun its energy?", "options": ["Nuclear Fusion", "Fire", "Batteries", "Electricity"], "a": "Nuclear Fusion", "info": "It smashes atoms together to make light and heat."},
    {"q": "How long does it take sunlight to reach Earth?", "options": ["8 Minutes", "1 Second", "1 Hour", "1 Day"], "a": "8 Minutes", "info": "Light travels super fast, but the Sun is very far away."},
    {"q": "Will the Sun shine forever?", "options": ["No, it will burn out one day", "Yes, forever", "Only at night", "Only in summer"], "a": "No, it will burn out one day", "info": "But don't worry, it has fuel for another 5 billion years!"},
    {"q": "What is the surface of the Sun called?", "options": ["Photosphere", "Chromosphere", "Crust", "Mantle"], "a": "Photosphere", "info": "This is the part of the Sun we can see."},
    {"q": "Is the Sun the biggest star in the universe?", "options": ["No, there are much bigger stars", "Yes, the biggest", "It is the smallest", "It is the only star"], "a": "No, there are much bigger stars", "info": "Some stars, like UY Scuti, are much, much bigger."},
    {"q": "Does the Sun move?", "options": ["Yes, it orbits the galaxy", "No, it stays still", "It spins but doesn't move", "It falls down"], "a": "Yes, it orbits the galaxy", "info": "The Sun travels around the center of the Milky Way."},
    {"q": "Why shouldn't you look directly at the Sun?", "options": ["It can hurt your eyes", "It is too dark", "It will disappear", "It is scary"], "a": "It can hurt your eyes", "info": "The light is so strong it can damage your vision."},

    # --- The Planets (General) ---
    {"q": "How many planets are in our solar system?", "options": ["8", "9", "10", "100"], "a": "8", "info": "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune."},
    {"q": "What keeps the planets orbiting the Sun?", "options": ["Gravity", "Magnetism", "Wind", "Ropes"], "a": "Gravity", "info": "The Sun's heavy gravity pulls on the planets."},
    {"q": "Which planets are the 'Gas Giants'?", "options": ["Jupiter & Saturn", "Earth & Mars", "Venus & Mercury", "Pluto & Eris"], "a": "Jupiter & Saturn", "info": "They are huge and made mostly of gas."},
    {"q": "Which planets are the 'Ice Giants'?", "options": ["Uranus & Neptune", "Jupiter & Saturn", "Earth & Venus", "Mars & Mercury"], "a": "Uranus & Neptune", "info": "They are very cold and made of icy materials."},
    {"q": "What shape are orbits?", "options": ["Oval (Ellipse)", "Perfect Circle", "Square", "Triangle"], "a": "Oval (Ellipse)", "info": "Planets travel in a stretched-out circle shape."},
    {"q": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "a": "Mercury", "info": "It is the first planet from the Sun."},
    {"q": "Which planet is farthest from the Sun?", "options": ["Neptune", "Uranus", "Saturn", "Pluto"], "a": "Neptune", "info": "It is the 8th and final planet."},
    
    # --- Mercury ---
    {"q": "Is Mercury hot or cold?", "options": ["Both hot and cold", "Only hot", "Only cold", "Room temperature"], "a": "Both hot and cold", "info": "It is super hot in the day and freezing at night because it has no air."},
    {"q": "What does Mercury look like?", "options": ["A grey rock with craters", "Blue and watery", "Red and dusty", "Green and grassy"], "a": "A grey rock with craters", "info": "It looks a lot like our Moon."},
    {"q": "How fast does Mercury orbit the Sun?", "options": ["Very fast (88 days)", "Slow (10 years)", "Same as Earth", "1 day"], "a": "Very fast (88 days)", "info": "It has the shortest year of all planets."},
    
    # --- Venus ---
    {"q": "Why is Venus the hottest planet?", "options": ["Thick clouds trap heat", "It is closest to the Sun", "It is on fire", "It has volcanoes"], "a": "Thick clouds trap heat", "info": "Its atmosphere acts like a thick blanket."},
    {"q": "What direction does Venus spin?", "options": ["Backwards (East to West)", "Forwards", "Up and Down", "It doesn't spin"], "a": "Backwards (East to West)", "info": "On Venus, the Sun rises in the West!"},
    {"q": "Is Venus visible from Earth?", "options": ["Yes, it looks like a bright star", "No, never", "Only with a telescope", "Only in winter"], "a": "Yes, it looks like a bright star", "info": "It is often called the Morning Star or Evening Star."},
    {"q": "What is Venus sometimes called?", "options": ["Earth's Sister", "Earth's Enemy", "The Red Planet", "The Gas Giant"], "a": "Earth's Sister", "info": "Because it is almost the same size as Earth."},

    # --- Earth ---
    {"q": "How long does it take Earth to orbit the Sun?", "options": ["365 days", "24 hours", "1 month", "10 years"], "a": "365 days", "info": "This is one year."},
    {"q": "What makes Earth unique?", "options": ["It has life", "It is round", "It has gravity", "It has rocks"], "a": "It has life", "info": "It is the only place we know of with living things."},
    {"q": "Why is Earth called the 'Blue Planet'?", "options": ["Because of the oceans", "Because of the sky", "Because of ice", "Because of blue rocks"], "a": "Because of the oceans", "info": "Water covers 70% of Earth's surface."},
    {"q": "What protects us from space rocks?", "options": ["The Atmosphere", "The Moon", "Clouds", "Mountains"], "a": "The Atmosphere", "info": "Most rocks burn up in the air before hitting the ground."},
    {"q": "How many moons does Earth have?", "options": ["1", "2", "0", "50"], "a": "1", "info": "We just call it 'The Moon'."},

    # --- Mars ---
    {"q": "Why is Mars red?", "options": ["Rusty dust", "Fire", "Red plants", "Strawberry juice"], "a": "Rusty dust", "info": "Iron in the soil rusts and turns red."},
    {"q": "What is the tallest volcano in the solar system?", "options": ["Olympus Mons", "Mount Everest", "Mauna Kea", "Mount Fuji"], "a": "Olympus Mons", "info": "It is on Mars and is 3 times taller than Everest."},
    {"q": "Did Mars use to have water?", "options": ["Yes, ancient rivers", "No, never", "It still has oceans", "Only ice cream"], "a": "Yes, ancient rivers", "info": "Scientists see dry river beds on the surface."},
    {"q": "How many moons does Mars have?", "options": ["2", "1", "0", "10"], "a": "2", "info": "They are named Phobos and Deimos."},
    {"q": "What are the robots on Mars called?", "options": ["Rovers", "Transformers", "Wall-E", "Droids"], "a": "Rovers", "info": "Like Curiosity and Perseverance."},

    # --- Jupiter ---
    {"q": "What is the biggest planet?", "options": ["Jupiter", "Saturn", "Sun", "Earth"], "a": "Jupiter", "info": "It is the King of Planets."},
    {"q": "What is the Great Red Spot?", "options": ["A giant storm", "A crater", "A volcano", "A landing spot"], "a": "A giant storm", "info": "It has been spinning for hundreds of years."},
    {"q": "Does Jupiter have rings?", "options": ["Yes, thin ones", "No", "Only on Tuesdays", "Yes, made of gold"], "a": "Yes, thin ones", "info": "They are hard to see, but they are there."},
    {"q": "How fast does Jupiter spin?", "options": ["Very fast (10 hour day)", "Slow", "Same as Earth", "It doesn't spin"], "a": "Very fast (10 hour day)", "info": "It has the shortest day of all planets."},
    
    # --- Saturn ---
    {"q": "What is Saturn famous for?", "options": ["Its big rings", "Being red", "Being hot", "Having no moons"], "a": "Its big rings", "info": "They are the most beautiful rings in the solar system."},
    {"q": "What are Saturn's rings made of?", "options": ["Ice and rock", "Dust only", "Gas", "Metal"], "a": "Ice and rock", "info": "Millions of chunks of ice orbit the planet."},
    {"q": "Could Saturn float in water?", "options": ["Yes, if the bathtub was big enough", "No, it's too heavy", "It would explode", "It would sink"], "a": "Yes, if the bathtub was big enough", "info": "Saturn is less dense than water!"},
    {"q": "What is Saturn's biggest moon?", "options": ["Titan", "Luna", "Europa", "Phobos"], "a": "Titan", "info": "Titan is the only moon with thick clouds."},

    # --- Uranus ---
    {"q": "How does Uranus spin?", "options": ["On its side", "Upright", "Backwards", "It doesn't"], "a": "On its side", "info": "It rolls around the Sun like a ball."},
    {"q": "Why is Uranus blue?", "options": ["Methane gas", "Water oceans", "Blue ice", "Blue paint"], "a": "Methane gas", "info": "The gas absorbs red light and reflects blue."},
    {"q": "Is Uranus hot or cold?", "options": ["Very cold", "Very hot", "Warm", "Boiling"], "a": "Very cold", "info": "It is the coldest planet in the solar system."},

    # --- Neptune ---
    {"q": "What color is Neptune?", "options": ["Deep Blue", "Red", "Yellow", "Green"], "a": "Deep Blue", "info": "It is a beautiful dark blue color."},
    {"q": "Is it windy on Neptune?", "options": ["Yes, supersonic winds", "No, it is calm", "Only a breeze", "There is no air"], "a": "Yes, supersonic winds", "info": "The winds are faster than sound!"},
    {"q": "What was the Great Dark Spot?", "options": ["A storm", "A hole", "A shadow", "A moon"], "a": "A storm", "info": "It was a storm that disappeared later."},

    # --- Dwarf Planets ---
    {"q": "How many official dwarf planets are there?", "options": ["5", "1", "9", "100"], "a": "5", "info": "Pluto, Eris, Haumea, Makemake, and Ceres."},
    {"q": "Which used to be the 9th planet?", "options": ["Pluto", "Eris", "Ceres", "Charon"], "a": "Pluto", "info": "It was reclassified in 2006."},
    {"q": "Where is the dwarf planet Ceres located?", "options": ["Asteroid Belt", "Kuiper Belt", "Near the Sun", "Outside the galaxy"], "a": "Asteroid Belt", "info": "It sits between Mars and Jupiter."},
    {"q": "What shape is the dwarf planet Haumea?", "options": ["Egg-shaped (Oval)", "Round", "Square", "Flat"], "a": "Egg-shaped (Oval)", "info": "It spins so fast it got stretched out."},
    {"q": "Are dwarf planets smaller than regular planets?", "options": ["Yes", "No", "They are bigger", "Same size"], "a": "Yes", "info": "They are too small to clear their orbit of other rocks."},

    # --- The Moon ---
    {"q": "Does the Moon shine with its own light?", "options": ["No, it reflects the Sun", "Yes, like a lamp", "Yes, it is fire", "Only at night"], "a": "No, it reflects the Sun", "info": "The Moon is like a giant mirror."},
    {"q": "What are the dark spots on the Moon?", "options": ["Flat plains of dried lava", "Oceans", "Holes", "Forests"], "a": "Flat plains of dried lava", "info": "Ancient astronomers thought they were seas."},
    {"q": "How long does it take the Moon to orbit Earth?", "options": ["About 27 days", "1 day", "1 year", "1 hour"], "a": "About 27 days", "info": "This gives us our months."},
    {"q": "What causes the tides in the ocean?", "options": ["The Moon's gravity", "The Sun's heat", "Whales", "Wind"], "a": "The Moon's gravity", "info": "The Moon pulls the water towards it."},
    {"q": "Has anyone visited the Moon?", "options": ["Yes, astronauts", "No, never", "Only robots", "Aliens"], "a": "Yes, astronauts", "info": "12 humans have walked on the Moon."},
    {"q": "What creates the craters on the Moon?", "options": ["Space rocks hitting it", "Volcanoes", "Digging", "Wind"], "a": "Space rocks hitting it", "info": "Since there is no air, the craters stay forever."},
    {"q": "Why do we only see one side of the Moon?", "options": ["It is tidally locked", "The back is dark", "It doesn't spin", "It is shy"], "a": "It is tidally locked", "info": "It spins at the exact same speed it orbits."},

    # --- Stars & Constellations ---
    {"q": "What is a constellation?", "options": ["A picture made of stars", "A type of planet", "A galaxy", "A shooting star"], "a": "A picture made of stars", "info": "Like connect-the-dots in the sky."},
    {"q": "What is the North Star called?", "options": ["Polaris", "Sirius", "Vega", "Orion"], "a": "Polaris", "info": "It helps travelers find North."},
    {"q": "What color are the hottest stars?", "options": ["Blue", "Red", "Yellow", "Orange"], "a": "Blue", "info": "Blue fire is hotter than red fire!"},
    {"q": "What color are the coolest stars?", "options": ["Red", "Blue", "White", "Green"], "a": "Red", "info": "Red stars are cooler than blue or yellow ones."},
    {"q": "What happens when a star dies?", "options": ["It can explode (Supernova)", "It turns into a planet", "It melts", "It falls"], "a": "It can explode (Supernova)", "info": "Big stars explode; small stars fade away."},
    {"q": "What is a nebula?", "options": ["A cloud of dust and gas", "A planet", "A black hole", "A star"], "a": "A cloud of dust and gas", "info": "It is a nursery where new stars are born."},
    {"q": "Which constellation looks like a hunter?", "options": ["Orion", "Ursa Major", "Leo", "Draco"], "a": "Orion", "info": "He has a famous belt of three stars."},
    {"q": "Which constellation looks like a Big Bear?", "options": ["Ursa Major", "Orion", "Cassiopeia", "Gemini"], "a": "Ursa Major", "info": "It contains the Big Dipper."},

    # --- Space Travel ---
    {"q": "What is an astronaut?", "options": ["A space explorer", "A star doctor", "A planet builder", "A pilot"], "a": "A space explorer", "info": "Someone trained to travel into space."},
    {"q": "Who was the first human in space?", "options": ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "John Glenn"], "a": "Yuri Gagarin", "info": "He orbited Earth in 1961."},
    {"q": "Who was the first person on the Moon?", "options": ["Neil Armstrong", "Yuri Gagarin", "Michael Collins", "Buzz Lightyear"], "a": "Neil Armstrong", "info": "He said: 'One small step for man.'"},
    {"q": "What do astronauts wear?", "options": ["Space suits", "T-shirts", "Diving suits", "Armor"], "a": "Space suits", "info": "To protect them and give them air."},
    {"q": "What is the ISS?", "options": ["International Space Station", "Interstellar Star Ship", "Ice Space Station", "Igloo Space Station"], "a": "International Space Station", "info": "A giant lab orbiting Earth."},
    {"q": "How do astronauts sleep in space?", "options": ["In sleeping bags strapped to walls", "In beds", "Floating in the middle", "On the floor"], "a": "In sleeping bags strapped to walls", "info": "So they don't float away while sleeping!"},
    {"q": "What do rockets use to fly?", "options": ["Fuel and fire", "Batteries", "Wind", "Magnets"], "a": "Fuel and fire", "info": "The burning fuel pushes the rocket up."},
    {"q": "What was the first animal in space?", "options": ["A dog named Laika", "A monkey", "A cat", "A mouse"], "a": "A dog named Laika", "info": "She went to space in 1957."},
    {"q": "What is gravity?", "options": ["A pulling force", "A pushing force", "A type of cloud", "A magnet"], "a": "A pulling force", "info": "It keeps our feet on the ground."},
    {"q": "Do you weigh less on the Moon?", "options": ["Yes", "No", "You weigh more", "Same weight"], "a": "Yes", "info": "The Moon has less gravity than Earth."},

    # --- The Universe ---
    {"q": "What is the universe?", "options": ["Everything that exists", "Just Earth", "The Solar System", "The Galaxy"], "a": "Everything that exists", "info": "All stars, planets, galaxies, and space."},
    {"q": "How did the universe begin?", "options": ["The Big Bang", "The Big Crunch", "The Big Whisper", "It appeared"], "a": "The Big Bang", "info": "A huge explosion created everything 14 billion years ago."},
    {"q": "What is a galaxy?", "options": ["A huge city of stars", "A planet", "A solar system", "A nebula"], "a": "A huge city of stars", "info": "It holds billions of stars together with gravity."},
    {"q": "What is the name of our galaxy?", "options": ["Milky Way", "Snickers", "Andromeda", "Whirlpool"], "a": "Milky Way", "info": "We live in one of its spiral arms."},
    {"q": "What is a black hole?", "options": ["A place with super strong gravity", "A hole in the ground", "A dark star", "A planet"], "a": "A place with super strong gravity", "info": "Nothing, not even light, can escape it."},
    {"q": "What is at the center of the Milky Way?", "options": ["A supermassive black hole", "The Sun", "Earth", "A giant star"], "a": "A supermassive black hole", "info": "It holds the galaxy together."},
    {"q": "Are there other galaxies?", "options": ["Yes, billions", "No, only ours", "Maybe one or two", "We don't know"], "a": "Yes, billions", "info": "The universe is full of them!"},
    {"q": "What is a light year?", "options": ["A measure of distance", "A measure of time", "A fast year", "A bright year"], "a": "A measure of distance", "info": "How far light travels in one year (very far!)."},

    # --- Small Bodies (Asteroids, Comets, Meteors) ---
    {"q": "What is an asteroid?", "options": ["A large space rock", "A star", "A moon", "A planet"], "a": "A large space rock", "info": "Most live in the Asteroid Belt."},
    {"q": "Where is the Asteroid Belt?", "options": ["Between Mars and Jupiter", "Near the Sun", "Past Pluto", "Near Earth"], "a": "Between Mars and Jupiter", "info": "It is full of rocky leftovers from planet building."},
    {"q": "What is a comet?", "options": ["A dirty snowball", "A burning rock", "A star", "A planet"], "a": "A dirty snowball", "info": "It is made of ice and dust and has a tail."},
    {"q": "What happens when a comet gets close to the Sun?", "options": ["It gets a tail", "It melts completely", "It freezes", "It stops"], "a": "It gets a tail", "info": "The Sun's heat turns the ice into gas."},
    {"q": "What is a shooting star?", "options": ["A meteor burning up", "A falling star", "A comet", "A spaceship"], "a": "A meteor burning up", "info": "It is a tiny rock hitting Earth's atmosphere."},
    {"q": "What is a meteorite?", "options": ["A space rock that hits the ground", "A shooting star", "A comet", "A planet"], "a": "A space rock that hits the ground", "info": "If it survives the fall, it's a meteorite."},
    {"q": "What killed the dinosaurs?", "options": ["A giant asteroid impact", "The ice age", "Volcanoes", "Aliens"], "a": "A giant asteroid impact", "info": "It hit Earth 65 million years ago."},

    # --- Fun Facts ---
    {"q": "Is there sound in space?", "options": ["No, it is silent", "Yes, very loud", "Only radio", "Only explosions"], "a": "No, it is silent", "info": "Sound needs air to travel, and space is empty."},
    {"q": "How old is the solar system?", "options": ["4.5 billion years", "2024 years", "1 million years", "100 years"], "a": "4.5 billion years", "info": "It's extremely old!"},
    {"q": "What is the Goldilocks Zone?", "options": ["Not too hot, not too cold", "A place with bears", "The center of the sun", "Deep space"], "a": "Not too hot, not too cold", "info": "It's the perfect distance from a star for water."},
    {"q": "Can you see the Great Wall of China from the Moon?", "options": ["No", "Yes", "Maybe", "With binoculars"], "a": "No", "info": "That is a myth. It's too thin to see from that far."},
    {"q": "Which planet floats in water?", "options": ["Saturn", "Jupiter", "Mars", "Earth"], "a": "Saturn", "info": "It is less dense than water."},
    {"q": "What color is a sunset on Mars?", "options": ["Blue", "Red", "Yellow", "Green"], "a": "Blue", "info": "Dust in the air makes the sunset look blue."},
    {"q": "How many stars are in the Milky Way?", "options": ["Billions", "Millions", "Thousands", "Hundreds"], "a": "Billions", "info": "100 to 400 billion stars!"},
    {"q": "What is an exoplanet?", "options": ["A planet orbiting another star", "A dead planet", "A moon", "An asteroid"], "a": "A planet orbiting another star", "info": "We have found thousands of them."},
    {"q": "What is the speed of light?", "options": ["Super fast", "Slow", "Instant", "Like a car"], "a": "Super fast", "info": "Nothing is faster than light."},
    {"q": "Who was the first woman in space?", "options": ["Valentina Tereshkova", "Sally Ride", "Mae Jemison", "Leia Organa"], "a": "Valentina Tereshkova", "info": "She launched in 1963."},
    {"q": "What planet rains diamonds?", "options": ["Neptune & Uranus", "Mars & Earth", "Mercury", "Venus"], "a": "Neptune & Uranus", "info": "High pressure turns carbon into diamonds!"},
    {"q": "Which planet has the longest day?", "options": ["Venus", "Earth", "Jupiter", "Mars"], "a": "Venus", "info": "A day on Venus is longer than a year on Venus!"},
    {"q": "What is a solar eclipse?", "options": ["Moon blocks the Sun", "Sun blocks the Moon", "Earth blocks the Sun", "Sun turns off"], "a": "Moon blocks the Sun", "info": "The Moon casts a shadow on Earth."},
    {"q": "What is a lunar eclipse?", "options": ["Earth blocks the Sun's light to the Moon", "Moon disappears", "Sun blocks Earth", "Moon explodes"], "a": "Earth blocks the Sun's light to the Moon", "info": "The Moon turns red!"},
    {"q": "Which planet is Earth's twin?", "options": ["Venus", "Mars", "Neptune", "Mercury"], "a": "Venus", "info": "They are almost the same size."},
    {"q": "How many people are in space right now?", "options": ["A few (on the ISS)", "None", "Thousands", "Millions"], "a": "A few (on the ISS)", "info": "Usually between 3 and 10 people."},
    {"q": "What do stars start as?", "options": ["Nebulas", "Planets", "Rocks", "Black holes"], "a": "Nebulas", "info": "Gas and dust clump together to form a star."},
    {"q": "What is the hottest color of a star?", "options": ["Blue", "Red", "Yellow", "White"], "a": "Blue", "info": "Blue means super hot energy!"},
    {"q": "What is the coolest color of a star?", "options": ["Red", "Blue", "White", "Yellow"], "a": "Red", "info": "Red stars are cooler than the Sun."},
    {"q": "Is the Sun a yellow dwarf?", "options": ["Yes", "No", "It is a red giant", "It is a white dwarf"], "a": "Yes", "info": "That is the type of star it is."},
    {"q": "What planet has the most moons?", "options": ["Saturn", "Jupiter", "Mars", "Earth"], "a": "Saturn", "info": "It has over 140 moons!"},
    {"q": "What is the biggest moon in the solar system?", "options": ["Ganymede", "Titan", "Luna", "Europa"], "a": "Ganymede", "info": "It orbits Jupiter and is bigger than Mercury."},
    {"q": "What planet has a hexagon storm on top?", "options": ["Saturn", "Jupiter", "Mars", "Neptune"], "a": "Saturn", "info": "A six-sided storm at the north pole."},
    {"q": "Which planet is the windiest?", "options": ["Neptune", "Earth", "Mars", "Jupiter"], "a": "Neptune", "info": "Winds blow at 1,200 miles per hour."},
    {"q": "What does 'Solar' mean?", "options": ["Related to the Sun", "Related to the Moon", "Related to Earth", "Related to Stars"], "a": "Related to the Sun", "info": "Like 'Solar System' or 'Solar Power'."},
    {"q": "What does 'Lunar' mean?", "options": ["Related to the Moon", "Related to the Sun", "Related to Mars", "Related to Stars"], "a": "Related to the Moon", "info": "Like 'Lunar Eclipse'."},
    {"q": "What is space junk?", "options": ["Old satellites and trash in orbit", "Asteroids", "Comets", "Alien ships"], "a": "Old satellites and trash in orbit", "info": "Humans have left a lot of trash in space."},
    {"q": "How do you become an astronaut?", "options": ["Study science and math", "Eat lots of food", "Sleep a lot", "Run fast"], "a": "Study science and math", "info": "You also need to be fit and healthy."},
    {"q": "What is a telescope?", "options": ["A tool to see far away", "A tool to hear space", "A tool to measure heat", "A toy"], "a": "A tool to see far away", "info": "It makes distant stars look closer."},
    {"q": "What is the Hubble Telescope?", "options": ["A telescope in space", "A telescope on a mountain", "A telescope in a submarine", "A planet"], "a": "A telescope in space", "info": "It takes amazing pictures of the universe."},
    {"q": "What is the James Webb Telescope?", "options": ["A new space telescope", "A person", "A star", "A planet"], "a": "A new space telescope", "info": "It looks at infrared light to see old stars."},
    {"q": "Why do stars twinkle?", "options": ["Earth's air moves the light", "They are flashing", "They are moving", "Aliens"], "a": "Earth's air moves the light", "info": "Atmosphere turbulence makes them sparkle."},
    {"q": "Do planets twinkle?", "options": ["No, they shine steadily", "Yes", "Sometimes", "Only Mars"], "a": "No, they shine steadily", "info": "This helps us tell planets apart from stars."},
    {"q": "What is the zodiac?", "options": ["A belt of constellations", "A planet", "A spaceship", "A black hole"], "a": "A belt of constellations", "info": "The Sun passes through these star signs."},
    {"q": "What is the 'Big Dipper'?", "options": ["A famous star pattern", "A spoon", "A planet", "A galaxy"], "a": "A famous star pattern", "info": "It looks like a ladle or spoon."},
    {"q": "Can you breathe in space?", "options": ["No, there is no air", "Yes, it is fresh", "Only a little", "Yes, if you hold your breath"], "a": "No, there is no air", "info": "Space is a vacuum."},
    {"q": "What happens to water in space?", "options": ["It floats in bubbles", "It falls down", "It disappears", "It turns to fire"], "a": "It floats in bubbles", "info": "Without gravity, surface tension pulls it into a ball."},
    {"q": "What is the largest volcano on Earth?", "options": ["Mauna Loa", "Mount Everest", "Olympus Mons", "Vesuvius"], "a": "Mauna Loa", "info": "It is in Hawaii."},
    {"q": "What is a dwarf star?", "options": ["A small star", "A huge star", "A planet", "A moon"], "a": "A small star", "info": "Our Sun is a yellow dwarf."},
    {"q": "What is a giant star?", "options": ["A very big star", "A small star", "A planet", "A rock"], "a": "A very big star", "info": "When stars get old, they can swell up."},
    {"q": "What is a neutron star?", "options": ["A super dense leftover star", "A new star", "A planet", "A comet"], "a": "A super dense leftover star", "info": "One teaspoon would weigh billions of tons."},
    {"q": "What is a pulsar?", "options": ["A spinning neutron star", "A flashing light", "A battery", "A planet"], "a": "A spinning neutron star", "info": "It shoots beams of energy like a lighthouse."},
    {"q": "What is a quasar?", "options": ["A super bright galaxy center", "A star", "A planet", "A moon"], "a": "A super bright galaxy center", "info": "Powered by a supermassive black hole."},
    {"q": "What is Dark Matter?", "options": ["Invisible stuff in space", "Black rocks", "Space dust", "Shadows"], "a": "Invisible stuff in space", "info": "It has gravity but we can't see it."},
    {"q": "How many galaxies are there?", "options": ["Billions", "One", "Ten", "Hundred"], "a": "Billions", "info": "The universe is unimaginably big."},
    {"q": "What is the Andromeda Galaxy?", "options": ["Our neighbor galaxy", "A candy bar", "A star", "A planet"], "a": "Our neighbor galaxy", "info": "It is the closest spiral galaxy to us."},
    {"q": "Will the Milky Way and Andromeda collide?", "options": ["Yes, in billions of years", "No, never", "Tomorrow", "Last week"], "a": "Yes, in billions of years", "info": "They will merge into a giant galaxy."},
    {"q": "What is a wormhole?", "options": ["A tunnel through space", "A bug", "A black hole", "A star"], "a": "A tunnel through space", "info": "They might let us travel fast, but we haven't found one yet."},
    {"q": "Who was Neil Armstrong?", "options": ["An astronaut", "A singer", "A doctor", "A teacher"], "a": "An astronaut", "info": "First man on the Moon."},
    {"q": "Who was Buzz Aldrin?", "options": ["Second man on the Moon", "A toy", "A pilot", "A scientist"], "a": "Second man on the Moon", "info": "He walked right after Neil Armstrong."},
    {"q": "What was Apollo 11?", "options": ["The mission to land on the Moon", "A movie", "A rocket car", "A satellite"], "a": "The mission to land on the Moon", "info": "It happened in 1969."},
    {"q": "What is the Kennedy Space Center?", "options": ["Where rockets launch in Florida", "A park", "A school", "A museum"], "a": "Where rockets launch in Florida", "info": "NASA launches missions from here."},
    {"q": "What is a cosmonaut?", "options": ["A Russian astronaut", "A space cook", "A star", "A robot"], "a": "A Russian astronaut", "info": "Different countries have different names for space travelers."},
    {"q": "What is gravity?", "options": ["A force that pulls", "A force that pushes", "Magic", "Wind"], "a": "A force that pulls", "info": "It holds the universe together."},
    {"q": "Does air exist in space?", "options": ["No", "Yes", "Sometimes", "Only near stars"], "a": "No", "info": "Space is a vacuum."},
    {"q": "What temperature is deep space?", "options": ["Super cold", "Super hot", "Warm", "Room temp"], "a": "Super cold", "info": "It is roughly -455 degrees Fahrenheit."},
    {"q": "What happens if you take your helmet off in space?", "options": ["You can't breathe", "Nothing", "You fly", "You sleep"], "a": "You can't breathe", "info": "It is very dangerous!"},
    {"q": "Can you grow plants in space?", "options": ["Yes, on the ISS", "No", "Only potatoes", "Only grass"], "a": "Yes, on the ISS", "info": "Astronauts grow lettuce and flowers."},
    {"q": "What is terraforming?", "options": ["Making a planet like Earth", "Building a farm", "Flying", "Mining"], "a": "Making a planet like Earth", "info": "Scientists want to do this to Mars."},
    {"q": "What is a Rover?", "options": ["A robot car", "A dog", "A plane", "A boat"], "a": "A robot car", "info": "It drives on other planets to study them."},
    {"q": "Which planet has the 'Great Dark Spot'?", "options": ["Neptune", "Jupiter", "Sun", "Mars"], "a": "Neptune", "info": "A huge storm similar to Jupiter's Red Spot."},
    {"q": "What is the 'Morning Star'?", "options": ["Venus", "Mars", "Polaris", "Sirius"], "a": "Venus", "info": "It shines bright before sunrise."},
    {"q": "What is the 'Evening Star'?", "options": ["Venus", "Jupiter", "Saturn", "Mercury"], "a": "Venus", "info": "It shines bright after sunset."},
    {"q": "How many stars are in the Big Dipper?", "options": ["7", "10", "5", "100"], "a": "7", "info": "Seven bright stars make the ladle shape."},
    {"q": "What is the closest galaxy to us?", "options": ["Andromeda", "Triangulum", "Whirlpool", "Sombrero"], "a": "Andromeda", "info": "It is 2.5 million light-years away."},
    {"q": "How fast does Earth spin?", "options": ["1000 miles per hour", "1 mile per hour", "100 mph", "It doesn't"], "a": "1000 miles per hour", "info": "That's why we have day and night!"},
    {"q": "Why don't we feel Earth spinning?", "options": ["It moves smoothly", "We are spinning too", "It is slow", "Gravity stops it"], "a": "It moves smoothly", "info": "Like riding in a smooth car."},
    {"q": "What is an annular eclipse?", "options": ["A 'Ring of Fire' eclipse", "A total eclipse", "A moon eclipse", "A rain storm"], "a": "A 'Ring of Fire' eclipse", "info": "The Moon covers the center of the Sun."},
    {"q": "What is a total eclipse?", "options": ["Sun is completely blocked", "Sun is half blocked", "Moon disappears", "Sky turns green"], "a": "Sun is completely blocked", "info": "Day turns into night for a few minutes."},
    {"q": "What are sunspots?", "options": ["Dark cool spots on the Sun", "Holes", "Dirt", "Moons"], "a": "Dark cool spots on the Sun", "info": "They are cooler than the rest of the Sun."},
    {"q": "What is a solar flare?", "options": ["An explosion on the Sun", "A fire", "A comet", "A planet"], "a": "An explosion on the Sun", "info": "It shoots energy into space."},
    {"q": "What causes the Northern Lights?", "options": ["Solar wind hitting Earth's air", "Magic", "Fire", "City lights"], "a": "Solar wind hitting Earth's air", "info": "Also called the Aurora Borealis."},
    {"q": "Where can you see Northern Lights?", "options": ["Near the North Pole", "Equator", "Antarctica", "Everywhere"], "a": "Near the North Pole", "info": "Like in Alaska, Canada, or Norway."},
    {"q": "Where can you see Southern Lights?", "options": ["Near the South Pole", "North Pole", "USA", "Europe"], "a": "Near the South Pole", "info": "Also called Aurora Australis."},
    {"q": "What is the Kuiper Belt?", "options": ["A ring of icy rocks past Neptune", "A belt of asteroids", "A galaxy", "A planet"], "a": "A ring of icy rocks past Neptune", "info": "Pluto lives here."},
    {"q": "What is the Oort Cloud?", "options": ["A shell of comets around the solar system", "A storm", "A nebula", "A planet"], "a": "A shell of comets around the solar system", "info": "It is very, very far away."},
    {"q": "What is Voyager 1?", "options": ["A probe leaving the solar system", "A car", "A plane", "A person"], "a": "A probe leaving the solar system", "info": "It is the farthest human-made object."},
    {"q": "What is the 'Pale Blue Dot'?", "options": ["Earth seen from far away", "Neptune", "A blueberry", "A marble"], "a": "Earth seen from far away", "info": "A famous photo taken by Voyager 1."},
    {"q": "How many constellations are there?", "options": ["88", "12", "50", "1000"], "a": "88", "info": "Astronomers have mapped the whole sky."},
    {"q": "What is your 'Star Sign'?", "options": ["Based on the Zodiac", "Your favorite star", "A planet", "A galaxy"], "a": "Based on the Zodiac", "info": "Like Leo, Gemini, or Pisces."},
    {"q": "What is a space probe?", "options": ["A robot spacecraft", "A doctor", "A tool", "A telescope"], "a": "A robot spacecraft", "info": "It goes where humans cannot go."},
    {"q": "Did Mars ever have life?", "options": ["We are looking for clues", "Yes, dinosaurs", "Yes, people", "No, impossible"], "a": "We are looking for clues", "info": "Microbes might have lived there long ago."},
    {"q": "What is the largest canyon on Mars?", "options": ["Valles Marineris", "Grand Canyon", "Death Valley", "Deep Trench"], "a": "Valles Marineris", "info": "It is as long as the USA is wide!"},
    {"q": "What are Saturn's rings?", "options": ["Billions of ice pieces", "Solid rock", "Light", "Gas"], "a": "Billions of ice pieces", "info": "Some are small as sand, some big as houses."},
    {"q": "Does Jupiter have a solid surface?", "options": ["No, it's gas", "Yes", "Only the core", "Maybe"], "a": "No, it's gas", "info": "You would fall right through it."},
    {"q": "Does Saturn have a solid surface?", "options": ["No, it's gas", "Yes", "Only the core", "Maybe"], "a": "No, it's gas", "info": "It is a Gas Giant."},
    {"q": "Does Uranus have a solid surface?", "options": ["No, it's ice and gas", "Yes", "Maybe", "Only the core"], "a": "No, it's ice and gas", "info": "It is an Ice Giant."},
    {"q": "Does Neptune have a solid surface?", "options": ["No, it's ice and gas", "Yes", "Maybe", "Only the core"], "a": "No, it's ice and gas", "info": "It is an Ice Giant."},
    {"q": "Can you stand on Pluto?", "options": ["Yes, it is rock and ice", "No", "You would sink", "It is gas"], "a": "Yes, it is rock and ice", "info": "It has a solid surface."},
    {"q": "Does Pluto have moons?", "options": ["Yes, 5", "No", "1", "100"], "a": "Yes, 5", "info": "Charon is the biggest one."},
    {"q": "What color is Pluto?", "options": ["Brownish-Red", "Blue", "Green", "Purple"], "a": "Brownish-Red", "info": "New photos show it is reddish."},
    {"q": "What is the heart on Pluto?", "options": ["A giant plain of ice", "A drawing", "A lake", "A cloud"], "a": "A giant plain of ice", "info": "It is called Tombaugh Regio."},
    {"q": "How long is a year on Pluto?", "options": ["248 Earth years", "1 year", "100 years", "10 years"], "a": "248 Earth years", "info": "It takes a long time to orbit the Sun."},
    {"q": "Which planet is the 'Swift Planet'?", "options": ["Mercury", "Mars", "Earth", "Jupiter"], "a": "Mercury", "info": "Because it moves so fast."},
    {"q": "What is a 'Blue Moon'?", "options": ["The second full moon in a month", "A blue colored moon", "A sad moon", "A cold moon"], "a": "The second full moon in a month", "info": "It doesn't actually look blue."},
    {"q": "What is a 'Blood Moon'?", "options": ["A red lunar eclipse", "A scary moon", "A hot moon", "A vampire moon"], "a": "A red lunar eclipse", "info": "The Moon looks red during an eclipse."},
    {"q": "What is a 'Harvest Moon'?", "options": ["Full moon in Autumn", "Orange moon", "Farming moon", "Big moon"], "a": "Full moon in Autumn", "info": "It gives light for farmers to harvest crops."},
    {"q": "How far is the Moon?", "options": ["238,000 miles", "100 miles", "1 million miles", "Close"], "a": "238,000 miles", "info": "It takes 3 days to fly there."},
    {"q": "Can you jump higher on the Moon?", "options": ["Yes, much higher", "No", "Same as Earth", "You can't jump"], "a": "Yes, much higher", "info": "Gravity is 6 times weaker."},
    {"q": "Does the Moon have an atmosphere?", "options": ["No, almost none", "Yes, thick", "Yes, like Earth", "Maybe"], "a": "No, almost none", "info": "That's why astronauts need suits."},
    {"q": "What is moon dust like?", "options": ["Sharp and sticky", "Soft like sand", "Wet", "Smooth"], "a": "Sharp and sticky", "info": "It gets everywhere and is bad to breathe."},
    {"q": "Are there quakes on the Moon?", "options": ["Yes, moonquakes", "No", "Only volcanoes", "Never"], "a": "Yes, moonquakes", "info": "The Moon shrinks as it cools, causing shakes."},
    {"q": "What is the biggest thing in the solar system?", "options": ["The Sun", "Jupiter", "Saturn", "The Asteroid Belt"], "a": "The Sun", "info": "It contains 99.8% of all the mass."},
    {"q": "What is the coldest place in the universe?", "options": ["Boomerang Nebula", "Pluto", "Antarctica", "Deep Space"], "a": "Boomerang Nebula", "info": "It is colder than deep space!"},
    {"q": "What is the hottest planet?", "options": ["Venus", "Mercury", "Mars", "Jupiter"], "a": "Venus", "info": "462 degrees Celsius!"},
    {"q": "What is the brightest star in the night sky?", "options": ["Sirius", "Polaris", "Betelgeuse", "Rigel"], "a": "Sirius", "info": "Also called the Dog Star."},
    {"q": "What galaxy is going to hit us?", "options": ["Andromeda", "Triangulum", "Whirlpool", "None"], "a": "Andromeda", "info": "In about 4 billion years."},
    {"q": "What shape is the Milky Way?", "options": ["Spiral", "Round", "Square", "Irregular"], "a": "Spiral", "info": "It looks like a pinwheel."},
    {"q": "Where is our solar system in the galaxy?", "options": ["On an outer arm", "In the center", "Outside it", "On top"], "a": "On an outer arm", "info": "The Orion Arm."},
    {"q": "How fast is the speed of light?", "options": ["186,000 miles per second", "100 mph", "Speed of sound", "Instant"], "a": "186,000 miles per second", "info": "It's the cosmic speed limit."},
    {"q": "If you yell in space, can anyone hear you?", "options": ["No", "Yes", "Only if close", "Only aliens"], "a": "No", "info": "Sound cannot travel in a vacuum."},
    {"q": "What color is the Sun really?", "options": ["White", "Yellow", "Orange", "Red"], "a": "White", "info": "Our atmosphere makes it look yellow."},
    {"q": "Do stars move?", "options": ["Yes, they orbit the galaxy", "No, they are fixed", "They fall", "They jump"], "a": "Yes, they orbit the galaxy", "info": "Everything in space is moving."},
    {"q": "What is a binary star?", "options": ["Two stars orbiting each other", "A lone star", "A planet", "A moon"], "a": "Two stars orbiting each other", "info": "Tatooine in Star Wars had two suns!"},
    {"q": "What is a trinary star?", "options": ["Three stars together", "Two stars", "One star", "A galaxy"], "a": "Three stars together", "info": "Alpha Centauri is a trinary system."},
    {"q": "Which planet is famous for life?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "a": "Earth", "info": "You live here!"},
    {"q": "How much of the universe is visible?", "options": ["5%", "100%", "50%", "90%"], "a": "5%", "info": "The rest is Dark Energy and Dark Matter."},
    {"q": "What is Dark Energy?", "options": ["Force pushing the universe apart", "Gravity", "Light", "Heat"], "a": "Force pushing the universe apart", "info": "It makes the universe expand faster."},
    {"q": "How many years has the universe existed?", "options": ["13.8 Billion", "2024", "1 Million", "100"], "a": "13.8 Billion", "info": "That is very, very old."},
    {"q": "What was the first thing in space?", "options": ["Hydrogen and Helium", "Planets", "People", "Cars"], "a": "Hydrogen and Helium", "info": "The first elements created."},
    {"q": "What is the Cosmic Microwave Background?", "options": ["Heat left from the Big Bang", "A radio station", "A star", "A microwave"], "a": "Heat left from the Big Bang", "info": "It is everywhere in the sky."},
    {"q": "Can black holes die?", "options": ["Yes, they evaporate slowly", "No, never", "They explode", "They turn into stars"], "a": "Yes, they evaporate slowly", "info": "Hawking Radiation causes them to shrink."},
    {"q": "What happens if you fall into a black hole?", "options": ["You get stretched (Spaghettification)", "You bounce", "You float", "You teleport"], "a": "You get stretched (Spaghettification)", "info": "Gravity pulls your feet harder than your head."},
    {"q": "What is the event horizon?", "options": ["The point of no return", "A party", "The sun", "A line"], "a": "The point of no return", "info": "Once you cross it, you can't escape a black hole."},
    {"q": "Are there rogue planets?", "options": ["Yes, planets without suns", "No", "Maybe", "Only in movies"], "a": "Yes, planets without suns", "info": "They float alone in space."},
    {"q": "What is the Great Attractor?", "options": ["A gravity anomaly pulling galaxies", "A star", "A magnet", "A planet"], "a": "A gravity anomaly pulling galaxies", "info": "It is pulling our galaxy towards it."},
    {"q": "What is Sputnik?", "options": ["The first satellite", "A rocket", "A dog", "A monkey"], "a": "The first satellite", "info": "Launched by Russia in 1957."},
    {"q": "Who won the Space Race?", "options": ["USA (First to Moon)", "Russia", "China", "Nobody"], "a": "USA (First to Moon)", "info": "Landing on the Moon ended the race."},
    {"q": "What is a Shuttle?", "options": ["A reusable spacecraft", "A bus", "A plane", "A boat"], "a": "A reusable spacecraft", "info": "It could land like a plane."},
    {"q": "What is SpaceX?", "options": ["A rocket company", "A planet", "A star", "A food"], "a": "A rocket company", "info": "They make reusable rockets."},
    {"q": "What is the Artemis mission?", "options": ["Return to the Moon", "Go to Mars", "Go to Sun", "Build a base"], "a": "Return to the Moon", "info": "NASA plans to send humans back soon."},
    {"q": "What is a light sail?", "options": ["A sail pushed by light", "A boat", "A wing", "A cloud"], "a": "A sail pushed by light", "info": "A way to travel without fuel."},
    {"q": "Can we live on Mars?", "options": ["Maybe in the future", "Yes, now", "No, never", "It is easy"], "a": "Maybe in the future", "info": "We need to build habitats first."},
    {"q": "How long is the flight to Mars?", "options": ["7 months", "1 day", "1 week", "10 years"], "a": "7 months", "info": "It is a long trip!"},
    {"q": "What do astronauts eat?", "options": ["Dried food", "Pizza", "Burgers", "Ice cream"], "a": "Dried food", "info": "They add water to rehydrate it."},
    {"q": "How do astronauts drink?", "options": ["From a bag with a straw", "From a cup", "From a bottle", "Waterfall"], "a": "From a bag with a straw", "info": "Liquids float in blobs without gravity."},
    {"q": "Do astronauts exercise?", "options": ["Yes, every day", "No", "Sometimes", "Only running"], "a": "Yes, every day", "info": "To keep their muscles strong."},
    {"q": "What happens to bones in space?", "options": ["They get weaker", "They get stronger", "Nothing", "They break"], "a": "They get weaker", "info": "Without gravity, bones lose density."},
    {"q": "Can you see cities from space?", "options": ["Yes, at night (lights)", "No", "Only huge ones", "In daytime"], "a": "Yes, at night (lights)", "info": "Cities glow brightly at night."},
    {"q": "What is the 'Blue Marble'?", "options": ["A photo of Earth", "A toy", "Neptune", "Uranus"], "a": "A photo of Earth", "info": "Taken by Apollo 17 crew."},
    {"q": "How many stars can you see at night?", "options": ["About 2,000-5,000", "Millions", "10", "Billions"], "a": "About 2,000-5,000", "info": "Without a telescope, that is the limit."},
    {"q": "What is light pollution?", "options": ["City lights hiding stars", "Dirty light", "Sunlight", "Moonlight"], "a": "City lights hiding stars", "info": "It makes it hard to see the night sky."},
    {"q": "What is an observatory?", "options": ["A building with telescopes", "A park", "A school", "A rocket"], "a": "A building with telescopes", "info": "Scientists work there to study space."},
    {"q": "What is a planetarium?", "options": ["A theater for space shows", "A real planet", "A museum", "A lab"], "a": "A theater for space shows", "info": "It projects stars on the ceiling."},
    {"q": "Who was Galileo?", "options": ["An astronomer", "A painter", "A king", "A cook"], "a": "An astronomer", "info": "He used a telescope to see Jupiter's moons."},
    {"q": "Who was Copernicus?", "options": ["He said Sun is center", "He discovered Mars", "He invented rockets", "He was an astronaut"], "a": "He said Sun is center", "info": "People used to think Earth was the center."},
    {"q": "What is astrology?", "options": ["Belief in star signs", "Science of space", "Rocket building", "Math"], "a": "Belief in star signs", "info": "It is not the same as Astronomy (science)."},
    {"q": "What is Astronomy?", "options": ["Science of space", "Star signs", "Reading palms", "Magic"], "a": "Science of space", "info": "Real study of the universe."},
    {"q": "What is a Cosmologist?", "options": ["Scientist studying universe origin", "Makeup artist", "Astronaut", "Pilot"], "a": "Scientist studying universe origin", "info": "They study the Big Bang."},
    {"q": "How big is the Earth?", "options": ["8,000 miles wide", "100 miles", "1 million miles", "Small"], "a": "8,000 miles wide", "info": "It is a medium sized planet."},
    {"q": "What is the equator?", "options": ["Line around the middle of Earth", "North Pole", "South Pole", "A country"], "a": "Line around the middle of Earth", "info": "It is the hottest part of Earth."},
    {"q": "Why is it cold at the poles?", "options": ["Less sunlight hits them", "Too much ice", "Windy", "Far from sun"], "a": "Less sunlight hits them", "info": "Sunlight hits at an angle."},
    {"q": "What is an aurora?", "options": ["Glowing lights in sky", "A planet", "A star", "A moon"], "a": "Glowing lights in sky", "info": "Caused by solar wind."},
    {"q": "Does Jupiter have a solid core?", "options": ["We think so", "No", "Yes, iron", "Maybe"], "a": "We think so", "info": "Deep inside the gas."},
    {"q": "What is the weather like on Titan?", "options": ["Rains methane", "Rains water", "Sunny", "Snows"], "a": "Rains methane", "info": "It has lakes of liquid gas."},
    {"q": "Is there water on Europa?", "options": ["Yes, under the ice", "No", "On the surface", "Only vapor"], "a": "Yes, under the ice", "info": "It has a huge ocean beneath the crust."},
    {"q": "What is Enceladus?", "options": ["An icy moon of Saturn", "A planet", "A star", "A comet"], "a": "An icy moon of Saturn", "info": "It shoots ice geysers into space."},
    {"q": "What is Io?", "options": ["A volcanic moon of Jupiter", "A planet", "A star", "A comet"], "a": "A volcanic moon of Jupiter", "info": "It is covered in volcanoes."},
    {"q": "What is the tallest cliff in the solar system?", "options": ["Verona Rupes on Miranda", "Grand Canyon", "Mars cliff", "Earth cliff"], "a": "Verona Rupes on Miranda", "info": "It is 12 miles high!"},
    {"q": "What is a Trojan asteroid?", "options": ["Asteroid sharing a planet's orbit", "A horse", "A moon", "A comet"], "a": "Asteroid sharing a planet's orbit", "info": "Jupiter has many."},
    {"q": "What is a Near-Earth Object?", "options": ["Asteroid crossing Earth's path", "Moon", "Sun", "Star"], "a": "Asteroid crossing Earth's path", "info": "NASA watches them closely."},
    {"q": "What was the Dinosaur Killer asteroid size?", "options": ["6 miles wide", "1 foot", "100 miles", "Size of moon"], "a": "6 miles wide", "info": "It was huge!"},
    {"q": "Where is the Chicxulub crater?", "options": ["Mexico", "USA", "Africa", "China"], "a": "Mexico", "info": "Where the dino-killer hit."},
    {"q": "How many rings does Saturn have?", "options": ["7 groups", "1", "3", "100"], "a": "7 groups", "info": "Named A to G."},
    {"q": "Are rings solid?", "options": ["No, made of particles", "Yes", "Like a road", "Glass"], "a": "No, made of particles", "info": "You could fly through them."},
    {"q": "What is the Cassini mission?", "options": ["Probe that studied Saturn", "Moon lander", "Mars rover", "Telescope"], "a": "Probe that studied Saturn", "info": "It orbited Saturn for years."},
    {"q": "What is the Voyager Golden Record?", "options": ["Message to aliens", "Music album", "Gold coin", "Award"], "a": "Message to aliens", "info": "Sounds and photos of Earth."},
    {"q": "How long will the footprints on the Moon last?", "options": ["Millions of years", "1 day", "1 year", "1 hour"], "a": "Millions of years", "info": "No wind to blow them away."},
    {"q": "What color is the sky on the Moon?", "options": ["Black", "Blue", "Red", "White"], "a": "Black", "info": "Even in daytime, because there is no air."},
    {"q": "Can you see stars on the Moon during the day?", "options": ["Yes", "No", "Sometimes", "Only bright ones"], "a": "Yes", "info": "The sky is black, so stars shine."},
    {"q": "What is a space elevator?", "options": ["Idea to ride a cable to space", "A rocket", "A building", "Stairs"], "a": "Idea to ride a cable to space", "info": "Ideally cheaper than rockets."},
    {"q": "What is zero gravity?", "options": ["Weightlessness", "Heavy", "Falling", "Flying"], "a": "Weightlessness", "info": "You float!"},
    {"q": "What is a G-force?", "options": ["Force of acceleration", "Gravity", "A letter", "A plane"], "a": "Force of acceleration", "info": "Astronauts feel heavy during launch."},
    {"q": "How fast is escape velocity?", "options": ["25,000 mph", "100 mph", "500 mph", "1000 mph"], "a": "25,000 mph", "info": "Speed needed to leave Earth."},
    {"q": "What is the Karman line?", "options": ["Edge of space (62 miles up)", "A finish line", "Equator", "Horizon"], "a": "Edge of space (62 miles up)", "info": "Where space begins."},
    {"q": "What is a suborbital flight?", "options": ["Goes to space but comes right back", "Orbits Earth", "Moon trip", "Mars trip"], "a": "Goes to space but comes right back", "info": "Like Blue Origin flights."},
    {"q": "Who is Elon Musk?", "options": ["Founder of SpaceX", "Astronaut", "President", "Scientist"], "a": "Founder of SpaceX", "info": "He wants to go to Mars."},
    {"q": "What is a Starlink?", "options": ["Internet satellites", "A star", "A chain", "A phone"], "a": "Internet satellites", "info": "Train of lights in the sky."},
    {"q": "What is a UFO?", "options": ["Unidentified Flying Object", "Alien", "Plane", "Bird"], "a": "Unidentified Flying Object", "info": "Something flying we don't recognize."},
    {"q": "Are aliens real?", "options": ["We don't know yet", "Yes", "No", "They are among us"], "a": "We don't know yet", "info": "Scientists are looking for signs."},
    {"q": "What is SETI?", "options": ["Search for Extraterrestrial Intelligence", "A radio", "A TV show", "NASA"], "a": "Search for Extraterrestrial Intelligence", "info": "Listening for alien radio signals."}
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
    st.session_state.wrong_answers = [] # Initialize list for wrong answers
    
    # Initialize the first set of options
    first_q = st.session_state.quiz_session[0]
    st.session_state.current_options = get_shuffled_options(first_q)

def restart_game():
    st.session_state.quiz_session = random.sample(QUESTION_BANK, 10)
    st.session_state.score = 0
    st.session_state.current_index = 0
    st.session_state.game_over = False
    st.session_state.wrong_answers = [] # Reset wrong answers
    
    # Reset the options for the new first question
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
    
    # Use the stored options from session_state
    current_options = st.session_state.current_options
    
    col1, col2 = st.columns(2)
    for i, option in enumerate(current_options):
        col = col1 if i % 2 == 0 else col2
        if col.button(option, use_container_width=True, key=f"q{idx}_opt{i}"):
            
            # Check Answer
            if option == q_data['a']:
                st.session_state.score += 1
                st.toast(f"🌟 Correct! {q_data['info']}", icon="❄️")
            else:
                st.toast(f"🧊 Oops! The answer was {q_data['a']}.", icon="☃️")
                # Record Wrong Answer
                st.session_state.wrong_answers.append({
                    "question": q_data['q'],
                    "your_answer": option,
                    "correct_answer": q_data['a'],
                    "explanation": q_data['info']
                })
                time.sleep(1) 
            
            # Next Question Logic
            if st.session_state.current_index + 1 < 10:
                st.session_state.current_index += 1
                
                # Prepare shuffled options for the NEXT question
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
    
    # --- SHOW WRONG ANSWERS LINK ---
    if len(st.session_state.wrong_answers) > 0:
        st.write("")
        with st.expander("❄️ Click here to see what you missed!"):
            for item in st.session_state.wrong_answers:
                st.markdown(f"**❓ Question:** {item['question']}")
                st.markdown(f"❌ **You said:** {item['your_answer']}")
                st.markdown(f"✅ **Correct Answer:** {item['correct_answer']}")
                st.caption(f"💡 *{item['explanation']}*")
                st.markdown("---")
    
    st.write("")
    if st.button("🚀 Blast Off Again (New Questions)", type="primary", use_container_width=True):
        restart_game()
