import streamlit as st

# Set page config
st.set_page_config(page_title="PCH Login", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .pch-header {
            background-color: #003087;
            padding: 1.5rem;
            color: white;
            font-size: 28px;
            font-weight: bold;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            border-radius: 0px 0px 8px 8px;
        }
        .fdic-box {
            background-color: #f5f5f5;
            padding: 1rem;
            margin: 1.5rem 0;
            border-radius: 8px;
            text-align: center;
            font-size: 14px;
        }
        .login-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .show-password {
            font-size: 12px;
            color: #003087;
            text-align: right;
            margin-top: -10px;
            margin-bottom: 10px;
        }
        .security-info {
            text-align: center;
            margin-top: 2rem;
            color: gray;
            font-size: 13px;
        }
        .login-button {
            background-color: #003087;
            color: white;
            border: none;
            padding: 0.75rem;
            width: 100%;
            font-size: 16px;
            border-radius: 4px;
        }
        .link-style {
            color: #003087;
            font-size: 13px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Header with PCH and logo
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("1B415255-50D2-4A2B-BF08-7CB889510F86.jpeg", width=40)
with col2:
    st.markdown('<div class="pch-header">PCH</div>', unsafe_allow_html=True)

# FDIC Notice
st.markdown('<div class="fdic-box">FDIC-Insured - Backed by the full faith and credit of the U.S. Government.</div>', unsafe_allow_html=True)

# Login section
st.markdown('<div class="login-title">Account Login</div>', unsafe_allow_html=True)
username = st.text_input("Username")
password = st.text_input("Password", type="password")
st.markdown('<div class="show-password">🔒 Show</div>', unsafe_allow_html=True)

# Remember checkbox
st.checkbox("Remember my username")

# Login button
st.markdown('<button class="login-button">Log In</button>', unsafe_allow_html=True)

# Links
st.markdown("""
<div class="link-style">
    <a href="#">Forgot username or password?</a><br>
    <a href="#">Enroll in online banking</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="security-info">🔒 Connection Secured</div>', unsafe_allow_html=True)
