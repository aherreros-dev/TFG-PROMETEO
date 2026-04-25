ACCENT = "#FF5500"
ACCENT_HOVER = "#FF7733"
BG_MAIN = "#141414"
BG_SIDEBAR = "#0F0F0F"
BG_CARD = "#1C1C1C"
BORDER = "#2A2A2A"
TEXT_PRIMARY = "#F0F0F0"
TEXT_MUTED = "#666666"

STYLESHEET = f"""
QMainWindow, QWidget {{
    background-color: {BG_MAIN};
    color: {TEXT_PRIMARY};
    font-family: 'Segoe UI', 'SF Pro Display', sans-serif;
    font-size: 13px;
}}

/* Sidebar */
#sidebar {{
    background-color: {BG_SIDEBAR};
    border-right: 1px solid {BORDER};
}}

#app_title {{
    color: {ACCENT};
    font-size: 18px;
    font-weight: bold;
    letter-spacing: 3px;
    padding: 0px;
}}

#app_subtitle {{
    color: {TEXT_MUTED};
    font-size: 9px;
    letter-spacing: 1px;
    padding: 0px;
}}

/* Nav buttons */
QPushButton#nav_btn {{
    background-color: transparent;
    color: {TEXT_MUTED};
    border: none;
    border-left: 3px solid transparent;
    text-align: left;
    padding: 12px 20px;
    font-size: 12px;
    letter-spacing: 0.5px;
}}

QPushButton#nav_btn:hover {{
    background-color: {BG_CARD};
    color: {TEXT_PRIMARY};
    border-left: 3px solid {BORDER};
}}

QPushButton#nav_btn[active=true] {{
    background-color: #1F1000;
    color: {ACCENT};
    border-left: 3px solid {ACCENT};
    font-weight: bold;
}}

/* Content area */
#content_area {{
    background-color: {BG_MAIN};
    padding: 32px;
}}

#page_title {{
    color: {ACCENT};
    font-size: 22px;
    font-weight: bold;
    letter-spacing: 1px;
}}

#page_description {{
    color: {TEXT_MUTED};
    font-size: 12px;
}}

/* Separator */
#separator {{
    background-color: {BORDER};
    max-height: 1px;
    margin: 8px 16px;
}}

/* Status bar */
#status_bar {{
    background-color: {BG_SIDEBAR};
    border-top: 1px solid {BORDER};
    color: {TEXT_MUTED};
    font-size: 10px;
    padding: 6px 16px;
}}

/* Placeholder card */
#placeholder_card {{
    background-color: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 40px;
}}

#placeholder_card QLabel {{
    color: {TEXT_MUTED};
    font-size: 12px;
}}
"""
