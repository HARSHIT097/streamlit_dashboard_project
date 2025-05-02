import streamlit as st
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import RtfFormatter, ImageFormatter
from PIL import Image
from io import BytesIO
import matplotlib.font_manager as fm


st.set_page_config(page_title="Code to RTF/Image Formatter", layout="wide")
st.title("🧠 Code & Text Beautifier → Download as Image or RTF")

# --- Sidebar options ---
st.sidebar.header("🛠️ Format Settings")

language_map = {
    "Python": "python",
    "Java": "java",
    "C++": "cpp",
    "C": "c",
    "JavaScript": "javascript",
    "HTML": "html",
    "CSS": "css",
    "SQL": "sql",
    "JSON": "json",
    "Bash": "bash",
    "YAML": "yaml",
    "Markdown": "markdown"
}

# List all available system fonts using matplotlib
def get_fonts():
    fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')
    font_names = [fm.FontProperties(fname=font).get_name() for font in fonts]
    return sorted(font_names)

#available_fonts= get_fonts()
#print(available_fonts)
# Safe cross-platform monospaced fonts
available_fonts = [
    "Arial", "Calibri", "Courier New", "Georgia", "Impact", "Lucida Console",
    "Segoe UI", "Times New Roman", "Verdana", "Comic Sans MS", "Consolas",
    "Tahoma", "Trebuchet MS", "Palatino Linotype", "Gill Sans MT"
]

language = st.sidebar.selectbox("Select Language", list(language_map.keys()))
#font_name = st.sidebar.selectbox("Font", ["Courier New", "Consolas", "Lucida Console"])
font_name = st.sidebar.selectbox("Font", available_fonts)
font_size = st.sidebar.slider("Font Size", min_value=10, max_value=24, value=14)
line_numbers = st.sidebar.checkbox("Show Line Numbers", value=True)

# --- Main input ---
st.subheader("📝 Paste your code or text below:")
code_input = st.text_area("Code/Text Input", height=200)

# --- Output buffers ---
image_buf = BytesIO()
rtf_buf = BytesIO()

def convert_code():
    """Converts the input code to syntax-highlighted RTF and image formats."""
    # Reset buffers
    image_buf.truncate(0)
    image_buf.seek(0)
    rtf_buf.truncate(0)
    rtf_buf.seek(0)

    # Lexer
    lexer_name = language_map[language]
    lexer = get_lexer_by_name(lexer_name)

    # Image conversion
    img_formatter = ImageFormatter(
        font_name=font_name,
        font_size=font_size,
        line_numbers=line_numbers,
        image_format="PNG",
        line_pad=2,
        style="default"
    )

    image_bytes = highlight(code_input, lexer, img_formatter)
    image_buf.write(image_bytes)
    image_buf.seek(0)
    preview_image = Image.open(BytesIO(image_bytes))

    # RTF conversion
    rtf_formatter = RtfFormatter(fontface=font_name, fontsize=font_size, linenos=line_numbers)
    rtf_data = highlight(code_input, lexer, rtf_formatter)
    rtf_buf.write(rtf_data.encode('utf-8'))
    rtf_buf.seek(0)

    return preview_image

# --- Convert button ---
if st.button("⚙️ Convert & Preview"):
    if code_input.strip() == "":
        st.warning("Please enter some code or text to convert.")
    else:
        preview_image = convert_code()
        st.success("✅ Conversion successful!")
        st.image(preview_image, caption="🖼️ Preview", use_container_width=True)

        st.markdown("### 📥 Download Your Files:")
        st.download_button("⬇️ Download as RTF", rtf_buf, file_name="formatted_code.rtf")
        st.download_button("⬇️ Download as Image (PNG)", image_buf, file_name="formatted_code.png", mime="image/png")
