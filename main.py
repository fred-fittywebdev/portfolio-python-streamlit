from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SECTION ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
js_file = current_dir / "js" / "main.js"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Fred Guerra"
PAGE_ICON = ":wave"
NAME = "Fred Guerra"
DESCRIPTION = "Junior web developer, I bring designs to life by transforming them into accessible, modern and beautiful websites. No unnecessary stuff, UX stays the core of my process."
EMAIL = "loulou.fg@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/",
    "Linkedin": "https://www.linkedin.com/in/fr%C3%A9d%C3%A9ricguerra/",
    "GitHub": "https://github.com/fred-fittywebdev",
    "Twitter": "https://github.com/fred-fittywebdev",
}
PROJECTS = {
    "🏄‍♀️ Roxy swim guide": "https://www.roxy.fr/maillot-bain-guide-coupes/",
    "🏄‍♀️ Roxy Warmlink technologie": "https://www.roxy.fr/collection-warmlink-snow/",
    "🛹 Element Sustainability": "https://www.elementbrand.fr/responsabilite/",
    "🧑‍🎓 Oh My Food - Study project with Css animations": "https://fred-fittywebdev.github.io/FredericGuerra_3_01112021.io/",
    "🧑‍🎓 Reservia- Study project for travel agency landing page": "https://fred-fittywebdev.github.io/FredericGuerra_2_17092021.io/",
    "🧑‍🎓 Groupomania - study social network project": "https://github.com/fred-fittywebdev/groupomaniagit",
    "🖥️ Fred Guerra - Html, Css, and Js version of the portfolio.": "https://www.roxy.fr/maillot-bain-guide-coupes/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF AND PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(js_file) as f:
    st.markdown("<script>{}</script>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFByte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFByte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📭", EMAIL)

# --- SOCIAL LINKS ---
st.write("#") # empty paragraph
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write("#") # empty paragraph
st.subheader("My Skills")
st.write("---")
st.write(
    """
    - 🖱️ Programming: HTML, CSS, JavaScript, Python,
    - 🖼️ Front: Tailwind, Bootstrap, React, 
    - 📊 Back: NodeJs, Express, Php, Symfony
    - 🗄️ Databases: MongoDb, Mysql, Wordpress
    """
)

# --- WORK HISTORY ---
st.write("#") 
st.subheader("Work History")
st.write("---")

# JOB 1
st.write("FRONT END DEVELOPPER | BOARDRIDERS")
st.write("09/2021 - 09/2022")
st.write("""
I worked for the Boardriders company for a year on an apprenticeship contract. I created and integrated various landing pages and components for brands such as Roxy, Quiksilver, Billabong or Element.
- Creation of modern websites with technologies like Html, Css, Javascript, Jquery, in accordance with the mockups provided by our designers.
- Integrated within an international team, work in collaboration with designers in France but also in the USA or in England.
- Improvement and maintenance of the Boardriders website created with Wordpress.
""")
st.write("#")
st.write("#")

# JOB 2
st.write("STUDENT | OPENCLASSROOMS")
st.write("09/2021 - 09/2022")
st.write("""
Web Developer Training Program. What i learned ...
- Transforming a mockup into a website - Html, Css.
- Make a web page dynamic with Css animations.
- Optimize an existing website (Accessibility, Seo ).
- Building an E-commerce with javascript.
- Build a secure API for a food review application.
- Building a fully functionnal enterprise social network from sratch with React Framework.
""")


# --- PROJECT ---
st.write("#")
st.subheader("Projects")
st.write("---")
for projects, link in PROJECTS.items():
    st.write(f"[{projects}]({link})")