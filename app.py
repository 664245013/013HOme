
import streamlit as st

st.set_page_config(
    page_title="Hotel Recommendation",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;800&display=swap');

.stApp {
    background-color: #07130E;
    background-image:
        radial-gradient(circle at 15% 50%, rgba(16, 185, 129, 0.15) 0%, transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(34, 197, 94, 0.15) 0%, transparent 25%),
        radial-gradient(circle at 50% 80%, rgba(5, 150, 105, 0.10) 0%, transparent 30%);
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'Inter', sans-serif;
    color: #E2E8F0;
}

.hero {
    text-align: center;
    padding: 50px 20px 30px 20px;
}

.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #34D399 0%, #10B981 50%, #4ADE80 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    letter-spacing: -1px;
    line-height: 1.2;
}

.hero p {
    color: #94A3B8;
    font-size: 1.15rem;
    letter-spacing: 0.5px;
    margin-top: 0;
    font-weight: 300;
}

.card {
    background: rgba(20, 45, 34, 0.60);
    border: 1px solid rgba(74, 222, 128, 0.10);
    border-radius: 20px;
    padding: 28px;
    height: 260px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.4s ease;
    margin-bottom: 24px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.10),
                0 2px 4px -1px rgba(0, 0, 0, 0.06);
    position: relative;
    overflow: hidden;
}

.card:hover {
    transform: translateY(-8px);
    border-color: rgba(52, 211, 153, 0.40);
    box-shadow: 0 20px 40px -5px rgba(16, 185, 129, 0.25),
                0 10px 20px -5px rgba(0, 0, 0, 0.30);
    background: rgba(20, 55, 40, 0.80);
}

.card .icon {
    font-size: 2.5rem;
    margin-bottom: 12px;
    display: inline-block;
    filter: drop-shadow(0 0 8px rgba(52, 211, 153, 0.40));
}

.card h3 {
    color: #F1F5F9;
    margin: 0 0 8px 0;
    font-size: 1.25rem;
    font-weight: 600;
}

.card p {
    color: #94A3B8;
    font-size: 0.90rem;
    line-height: 1.6;
    margin: 0;
}

.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 12px 20px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #059669 0%, #10B981 100%);
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.30);
    border: 1px solid rgba(255, 255, 255, 0.10);
}

.btn:hover {
    background: linear-gradient(135deg, #10B981 0%, #34D399 100%);
    box-shadow: 0 8px 25px rgba(16, 185, 129, 0.45);
    transform: translateY(-2px);
}

.section-title {
    text-align: center;
    color: #CBD5E1;
    font-size: 1.15rem;
    margin: 10px 0 28px 0;
    font-weight: 400;
}

.custom-footer {
    text-align: center;
    color: #64748B;
    margin-top: 40px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(74, 222, 128, 0.10);
}

footer, #MainMenu {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    background: #0A1912 !important;
    border-right: 1px solid rgba(74, 222, 128, 0.10) !important;
}
</style>

<div class="hero">
    <h1>HOTEL RECOMMENDATION</h1>
    <p>ระบบแนะนำโรงแรมด้วยกราฟความสัมพันธ์ระหว่าง User และ Hotel</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🏨 รวมโปรเจกต์ระบบ Hotel Recommendation ของเรา</div>',
    unsafe_allow_html=True,
)

APPS = [
    (
        "🏨",
        "โครงสร้างข้อมูล Hotel & User",
        "จัดการข้อมูล User และ Hotel ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1k4c6Iaxotk_5U_4JSEa8sH-gpGVlg8WF?usp=sharing",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ระหว่าง User และประวัติการชอบ Hotel",
        "https://colab.research.google.com/drive/1mCthb9xYtimhEANP4ljIepC2G9y9mp1s?usp=sharing",
    ),
    (
        "🏨",
        "ระบบแนะนำ Hotel",
        "แนะนำ Hotel จากความสัมพันธ์และ Hotel ที่ผู้ใช้ที่มีความสนใจคล้ายกันชอบ",
        "https://eclthdo5ujipj8on9fo2de.streamlit.app/",
    ),
]

# 4 cards: 3 cards on the first row and 1 centered on the second row.
cols = st.columns(3)

for i, (icon, title, desc, url) in enumerate(APPS):
    if i < 3:
        with cols[i]:
            st.markdown(
                f"""
                <div class="card">
                    <div>
                        <div class="icon">{icon}</div>
                        <h3>{title}</h3>
                        <p>{desc}</p>
                    </div>
                    <a class="btn" href="{url}" target="_blank">เปิดระบบ →</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        left, center, right = st.columns([1, 1.0, 1])

        with center:
            st.markdown(
                f"""
                <div class="card">
                    <div>
                        <div class="icon">{icon}</div>
                        <h3>{title}</h3>
                        <p>{desc}</p>
                    </div>
                    <a class="btn" href="{url}" target="_blank">เปิดเว็บไซต์ →</a>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.markdown(
    """
    <div class="custom-footer">
        Made with ❤️ using Streamlit · Hotel Recommendation System 2026
    </div>
    """,
    unsafe_allow_html=True,
)
