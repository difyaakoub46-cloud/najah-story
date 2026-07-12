# -*- coding: utf-8 -*-
"""
اسم الملف: app-ultra-clean-nomusic.py
الوصف: تطبيق كروت النجاح v5.2.0.0 النسخة فائقة النقاء والسرعة (Ultra Clean & Fast No Music)
      تم إزالة كافة الأكواد والملفات والإشارات الخاصة بالموسيقى كلياً لتخفيف حجم السكربت وسرعة الرفع،
      مع دمج تصميم مذهل وجذاب وتفاعلي لزر التحميل بدلاً من الزر الرمادي الممل.
المطور: DevAgent-3.5 & Yaakoub Ali Dif
"""

import streamlit as io_streamlit
import streamlit.components.v1 as components
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageChops
import io
import os
import math
import random
import base64

try:
    import arabic_reshaper
    from bidi.algorithm import get_display

    ARABIC_SUPPORT = True
except ImportError:
    ARABIC_SUPPORT = False

io_streamlit.set_page_config(
    page_title="Najah Story v5.2.0.0 Ultra-Clean",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# تجميل واجهة المستخدم وتصميم زر التنزيل التفاعلي الجذاب بلون متدرج وتوهج ساحر
io_streamlit.markdown("""
    <style>
    .stApp {
        background-color: #080c14;
        color: #f1f5f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .welcome-container {
        text-align: center;
        padding-top: 5px;
        padding-bottom: 5px;
        margin-bottom: 8px;
    }
    .main-title {
        background: linear-gradient(135deg, #10b981, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 38px;
        margin: 0;
        padding: 0;
    }
    .designer-tag {
        font-size: 14px;
        color: #3b82f6;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 2px;
        margin-bottom: 5px;
        text-shadow: 0 0 10px rgba(59, 130, 246, 0.4);
    }
    .sub-title {
        font-size: 14px;
        color: #94a3b8;
        margin-top: 2px;
        margin-bottom: 8px;
    }
    div[data-baseweb="select"], div[data-baseweb="input"], .stNumberInput input {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        color: #f1f5f9 !important;
    }

    /* هندسة وتجميل زر التحميل المخصص ليكون فائق الجاذبية والروعة */
    div[data-testid="stDownloadButton"] button {
        background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        padding: 14px 32px !important;
        border-radius: 16px !important;
        border: 2px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.35), inset 0 2px 4px rgba(255, 255, 255, 0.2) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        cursor: pointer !important;
        width: 100% !important;
        text-align: center !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    }
    div[data-testid="stDownloadButton"] button:hover {
        transform: translateY(-4px) scale(1.01) !important;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.5), inset 0 2px 4px rgba(255, 255, 255, 0.3) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
        background: linear-gradient(135deg, #059669 0%, #2563eb 50%, #7c3aed 100%) !important;
    }
    div[data-testid="stDownloadButton"] button:active {
        transform: translateY(-1px) scale(0.99) !important;
    }

    .ad-top-wrapper {
        width: 100%;
        max-width: 728px;
        min-height: 90px;
        height: auto;
        margin: 0 auto 15px auto;
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 1.5px solid #374151;
        border-left: 5px solid #10b981;
        border-radius: 12px;
        padding: 12px 18px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: right;
        box-sizing: border-box;
    }
    .ad-bottom-wrapper {
        width: 100%;
        max-width: 500px;
        min-height: 250px;
        height: auto;
        margin: 30px auto;
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 2px solid #374151;
        border-left: 6px solid #10b981;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: right;
        box-sizing: border-box;
    }
    .ad-title-tag {
        color: #10b981;
        font-weight: bold;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 4px;
    }

    .dev-profile-card-wrapper {
        max-width: 100%;
        margin: 20px auto 10px auto;
        background: radial-gradient(circle at top left, #0f1c3f, #070d1e);
        border: 2.5px solid #10b981;
        border-radius: 24px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 20px 45px rgba(16, 185, 129, 0.25);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .dev-avatar {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        border: 3.5px solid #10b981;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.5);
        margin-bottom: 10px;
        object-fit: cover;
    }
    .dev-name {
        font-size: 18px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }
    .dev-badge {
        color: #3b82f6;
        font-size: 16px;
    }
    .dev-role {
        font-size: 12px;
        color: #94a3b8;
        margin-bottom: 15px;
        font-weight: 600;
    }
    .instagram-btn {
        background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
        color: #ffffff !important;
        font-weight: 700;
        font-size: 13px;
        text-decoration: none !important;
        padding: 10px 24px;
        border-radius: 50px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 8px 30px rgba(220, 39, 67, 0.45);
        transition: all 0.3s ease;
    }
    .instagram-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(220, 39, 67, 0.5);
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        overflow-x: hidden !important;
    }

    @media (max-width: 768px) {
        .mobile-hide {
            display: none !important;
        }
        .stApp {
            padding: 5px !important;
        }
        .welcome-container {
            margin-bottom: 3px !important;
        }
        .main-title {
            font-size: 26px !important;
        }
        .sub-title, .designer-tag {
            font-size: 11px !important;
        }
        div[data-testid="column"] {
            width: 100% !important;
            min-width: 100% !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

algerian_wilayas_69 = [
    "01 - أدرار", "02 - الشلف", "03 - الأغواط", "04 - أم البواقي", "05 - باتنة",
    "06 - بجاية", "07 - بسكرة", "08 - بشار", "09 - البليدة", "10 - البويرة",
    "11 - تمنراست", "12 - تبسة", "13 - تلمسان", "14 - تيارت", "15 - تيزي وزو",
    "16 - الجزائر", "17 - الجلفة", "18 - جيجل", "19 - سطيف", "20 - سعيدة",
    "21 - سكيكدة", "22 - سيدي بلعباس", "23 - عنابة", "24 - قالمة", "25 - قسنطينة",
    "26 - المدية", "27 - مستغانم", "28 - المسيلة", "29 - معسكر", "30 - ورقلة",
    "31 - وهران", "32 - البيض", "33 - اليزي", "34 - برج بوعريريج", "35 - بومرداس",
    "36 - الطارف", "37 - تندوف", "38 - تسمسيلت", "39 - الوادي", "40 - خنشلة",
    "41 - سوق أهراس", "42 - تيبازة", "43 - ميلة", "44 - عين الدفلى", "45 - النعامة",
    "46 - عين تموشنت", "47 - غرداية", "48 - غليزان", "49 - تيميمون", "50 - برج باجي مختار",
    "51 - أولاد جلال", "52 - بني عباس", "53 - عين صالح", "54 - عين قزام", "55 - تقرت",
    "56 - جانت", "57 - المغير", "58 - المنيعة", "59 - أفلو", "60 - الأبيض سيدي الشيخ",
    "61 - العريشة", "62 - القنطرة", "63 - بريكة", "64 - بوسعادة", "65 - بئر العاتر",
    "66 - قصر البخاري", "67 - قصر الشلالة", "68 - عين وسارة", "69 - مسعد"
]


def get_modern_cairo_font(font_size=50):
    font_filename = "./assets/Cairo-Bold.ttf"
    if os.path.exists(font_filename):
        return ImageFont.truetype(font_filename, font_size)
    return ImageFont.load_default()


if ARABIC_SUPPORT:
    try:
        reshaper_config = {
            'use_unshaped_instead_of_isolated': True
        }
        arabic_reshaper_obj = arabic_reshaper.ArabicReshaper(configuration=reshaper_config)
    except Exception:
        arabic_reshaper_obj = None
else:
    arabic_reshaper_obj = None


def format_arabic_text(text):
    if not text:
        return ""
    if ARABIC_SUPPORT and arabic_reshaper_obj is not None:
        try:
            reshaped_text = arabic_reshaper_obj.reshape(text)
            bidi_text = get_display(reshaped_text)
            return bidi_text
        except Exception:
            return text
    return text


def get_resampling_filter():
    res_obj = getattr(Image, 'Resampling', None)
    if res_obj is not None:
        for attr in ['LANCZOS', 'ANTIALIAS', 'BICUBIC']:
            if hasattr(res_obj, attr):
                return getattr(res_obj, attr)
    for attr in ['LANCZOS', 'ANTIALIAS', 'BICUBIC']:
        if hasattr(Image, attr):
            return getattr(Image, attr)
    return 3


def apply_alpha_gradient_to_monument(img, monument_opacity):
    w, h = img.size
    gradient = Image.new('L', (w, h), 0)
    draw_grad = ImageDraw.Draw(gradient)

    for y in range(h):
        if y < int(h * 0.25):
            factor = y / (h * 0.25)
            alpha_val = int(255 * factor)
        elif y > int(h * 0.60):
            factor = (h - y) / (h * 0.40)
            alpha_val = int(255 * factor)
        else:
            alpha_val = 255

        alpha_val = max(0, min(255, int(alpha_val * monument_opacity)))
        draw_grad.line([(0, y), (w, y)], fill=alpha_val)

    r, g, b, a = img.split()
    new_alpha = ImageChops.multiply(a, gradient)
    img.putalpha(new_alpha)
    return img


def load_and_colorize_monument(tint_color):
    image_path = "./assets/ma9am.png"
    if not os.path.exists(image_path):
        return None

    try:
        monument_img = Image.open(image_path)
        rgba_img = monument_img.convert("RGBA")

        r, g, b, a = rgba_img.split()
        grayscale_eval = Image.merge("RGB", (r, g, b)).convert("L")

        monument_mask = grayscale_eval.point(lambda x: 255 if x < 242 else 0)
        final_mask = ImageChops.multiply(monument_mask, a)
        final_mask = final_mask.filter(ImageFilter.BoxBlur(1))

        tint_rgb = tint_color[:3]
        colorized_img = ImageOps.colorize(grayscale_eval, black=(8, 12, 24), white=tint_rgb)
        colorized_rgba = colorized_img.convert("RGBA")
        colorized_rgba.putalpha(final_mask)

        return colorized_rgba
    except Exception as e:
        print(f"Failed to process monument image: {e}")
        return None


def make_image_circular(input_image, size=(360, 360)):
    resampling_filter = get_resampling_filter()
    img = ImageOps.fit(input_image, size, resampling_filter)
    mask = Image.new('L', size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0) + size, fill=255)

    circular_img = Image.new('RGBA', size, (0, 0, 0, 0))
    circular_img.paste(img, (0, 0), mask=mask)
    return circular_img


def draw_perfect_algerian_flag(draw_target, start_x, start_y, w, h):
    flag_canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    flag_draw = ImageDraw.Draw(flag_canvas)

    flag_draw.rectangle([0, 0, w // 2, h], fill=(0, 102, 51, 255))
    flag_draw.rectangle([w // 2, 0, w, h], fill=(255, 255, 255, 255))

    cx, cy = w // 2, h // 2
    r_outer = h // 3.2
    r_inner = r_outer * 0.82
    offset_x = r_outer * 0.32

    crescent_mask = Image.new("L", (w, h), 0)
    mask_draw = ImageDraw.Draw(crescent_mask)
    mask_draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], fill=255)
    mask_draw.ellipse([cx - r_inner + offset_x, cy - r_inner, cx + r_inner + offset_x, cy + r_inner], fill=0)

    red_color_layer = Image.new("RGBA", (w, h), (210, 16, 52, 255))
    flag_canvas.paste(red_color_layer, (0, 0), mask=crescent_mask)

    def draw_gorgeous_star(draw_obj, center, size, color):
        px, py = center
        points = []
        for i in range(10):
            r = size if i % 2 == 0 else size // 2
            angle = i * math.pi / 5 - math.pi / 2
            points.append((px + r * math.cos(angle), py + r * math.sin(angle)))
        draw_obj.polygon(points, fill=color)

    star_center = (cx + int(r_outer * 0.45), cy)
    draw_gorgeous_star(flag_draw, star_center, int(r_outer * 0.48), (210, 16, 52, 255))

    flag_round_mask = Image.new("L", (w, h), 0)
    fr_draw = ImageDraw.Draw(flag_round_mask)
    fr_draw.rounded_rectangle([0, 0, w, h], radius=15, fill=255)

    rounded_flag = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    rounded_flag.paste(flag_canvas, (0, 0), mask=flag_round_mask)

    flag_layer = Image.new("RGBA", draw_target.size, (0, 0, 0, 0))
    flag_layer.paste(rounded_flag, (start_x, start_y))
    draw_target.alpha_composite(flag_layer)


def draw_soft_shadow(image, x1, y1, x2, y2, corner_radius=30, blur_radius=15, offset=(0, 15),
                     shadow_color=(0, 0, 0, 130)):
    shadow_canvas = Image.new("RGBA", image.size, (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_canvas)

    s_draw.rounded_rectangle(
        [x1 + offset[0], y1 + offset[1], x2 + offset[0], y2 + offset[1]],
        radius=corner_radius,
        fill=shadow_color
    )

    blurred_shadow = shadow_canvas.filter(ImageFilter.GaussianBlur(blur_radius))
    image.alpha_composite(blurred_shadow)


def draw_obsidian_glass_card(image, x1, y1, x2, y2, border_color, corner_radius=30, enable_shine=True):
    draw_soft_shadow(image, x1, y1, x2, y2, corner_radius=corner_radius, blur_radius=25, offset=(0, 20),
                     shadow_color=(0, 0, 0, 150))
    draw_soft_shadow(image, x1, y1, x2, y2, corner_radius=corner_radius, blur_radius=12, offset=(0, 8),
                     shadow_color=(0, 0, 0, 100))

    card_w = x2 - x1
    card_h = y2 - y1

    card_layer = Image.new("RGBA", (card_w, card_h), (10, 16, 32, 235))

    if enable_shine:
        shine_layer = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
        shine_draw = ImageDraw.Draw(shine_layer)
        shine_draw.polygon([(-50, card_h + 50), (100, card_h + 50), (card_w + 50, -50), (card_w - 100, -50)],
                           fill=(255, 255, 255, 18))
        card_layer = Image.alpha_composite(card_layer, shine_layer)

    card_mask = Image.new("L", (card_w, card_h), 0)
    card_mask_draw = ImageDraw.Draw(card_mask)
    card_mask_draw.rounded_rectangle([0, 0, card_w, card_h], radius=corner_radius, fill=255)

    r, g, b, a = card_layer.split()
    new_a = ImageChops.multiply(a, card_mask)
    card_layer.putalpha(new_a)

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay.paste(card_layer, (x1, y1))

    draw_ov = ImageDraw.Draw(overlay)
    draw_ov.rounded_rectangle([x1, y1, x2, y2], radius=corner_radius, outline=border_color, width=3)
    draw_ov.rounded_rectangle([x1 + 3, y1 + 3, x2 - 3, y2 - 3], radius=corner_radius - 3, outline=(255, 255, 255, 45),
                              width=1)

    image.alpha_composite(overlay)


def draw_text_safely(image, text, position, font_style, fill_color, anchor="mm"):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)
    draw_ov.text(position, text, fill=fill_color, font=font_style, anchor=anchor)
    image.alpha_composite(overlay)


def draw_text_with_shadow(image, text, position, font_style, fill_color, shadow_color=(0, 0, 0, 180),
                          shadow_offset=(3, 3)):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)

    tx, ty = position
    if shadow_color:
        draw_ov.text((tx + shadow_offset[0], ty + shadow_offset[1]), text, fill=shadow_color, font=font_style,
                     anchor="mm")
    draw_ov.text((tx, ty), text, fill=fill_color, font=font_style, anchor="mm")

    image.alpha_composite(overlay)


def draw_gradient_text(image, text, position, font, colors, anchor="mm", shadow_color=(0, 0, 0, 180),
                       shadow_offset=(3, 3)):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    if tw <= 0 or th <= 0:
        tw, th = 200, 50

    temp_w, temp_h = tw + 100, th + 100

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)

    if shadow_color:
        tx, ty = position
        draw_ov.text((tx + shadow_offset[0], ty + shadow_offset[1]), text, fill=shadow_color, font=font, anchor="mm")

    text_mask = Image.new("L", (temp_w, temp_h), 0)
    mask_draw = ImageDraw.Draw(text_mask)
    mask_draw.text((temp_w // 2, temp_h // 2), text, fill=255, font=font, anchor="mm")

    grad_image = Image.new("RGBA", (temp_w, temp_h))
    grad_draw = ImageDraw.Draw(grad_image)
    for y in range(temp_h):
        t = y / temp_h
        r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * t)
        g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * t)
        b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * t)
        grad_draw.line([(0, y), (temp_w, y)], fill=(r, g, b, 255))

    canvas_text = Image.new("RGBA", (temp_w, temp_h), (0, 0, 0, 0))
    canvas_text.paste(grad_image, (0, 0), mask=text_mask)

    px = position[0] - temp_w // 2
    py = position[1] - temp_h // 2
    overlay.paste(canvas_text, (px, py), mask=canvas_text)
    image.alpha_composite(overlay)


THEMES = [
    {"name": "الملكي (Royal Gold)", "base_color": (35, 30, 15), "sec_color": (15, 15, 20),
     "border_color": (212, 175, 55, 255), "pattern": "stars"},
    {"name": "السايبر (Cyber Neon)", "base_color": (10, 14, 35), "sec_color": (50, 10, 80),
     "border_color": (0, 220, 255, 255), "pattern": "neon_grid"},
    {"name": "الساكورا (Sakura Pink)", "base_color": (40, 15, 25), "sec_color": (100, 35, 60),
     "border_color": (244, 143, 177, 255), "pattern": "stars"},
    {"name": "الكوزموس (Cosmos Dust)", "base_color": (5, 5, 12), "sec_color": (15, 20, 45),
     "border_color": (150, 120, 255, 255), "pattern": "clouds"},
    {"name": "الزمرد (Emerald Dream)", "base_color": (4, 30, 20), "sec_color": (2, 20, 12),
     "border_color": (46, 204, 113, 255), "pattern": "sparkles"},
    {"name": "الذهبي الوردي (Rose Gold)", "base_color": (35, 20, 25), "sec_color": (95, 60, 68),
     "border_color": (224, 157, 166, 255), "pattern": "sparkles"},
    {"name": "البرونز (Classic Bronze)", "base_color": (25, 20, 15), "sec_color": (55, 45, 35),
     "border_color": (205, 162, 97, 255), "pattern": "stars"},
    {"name": "الغابات (Forest Green)", "base_color": (5, 20, 10), "sec_color": (15, 45, 25),
     "border_color": (205, 220, 57, 255), "pattern": "sparkles"},
    {"name": "المحيط (Deep Ocean)", "base_color": (5, 25, 45), "sec_color": (10, 75, 115),
     "border_color": (0, 180, 216, 255), "pattern": "stars"},
    {"name": "المخملي (Velvet Red)", "base_color": (30, 5, 10), "sec_color": (20, 2, 5),
     "border_color": (233, 69, 96, 255), "pattern": "stars"}
]

STYLES = [
    {"name": "العميق (Deep)", "alpha": 255, "gradient_stops": 2},
    {"name": "المشع (Glowing)", "alpha": 220, "gradient_stops": 3},
    {"name": "الشبكي (Textured)", "alpha": 240, "gradient_stops": 2},
    {"name": "الضبابي (Misty)", "alpha": 210, "gradient_stops": 3},
    {"name": "النيوني (Neon)", "alpha": 230, "gradient_stops": 3},
    {"name": "الكلاسيكي (Classic)", "alpha": 255, "gradient_stops": 2},
    {"name": "الهادئ (Soft)", "alpha": 215, "gradient_stops": 3},
    {"name": "الفني (Artistic)", "alpha": 245, "gradient_stops": 3},
    {"name": "الحالم (Dreamy)", "alpha": 225, "gradient_stops": 2}
]

GENERATED_TEMPLATES = {}
counter = 1
for t in THEMES:
    for s in STYLES:
        key_name = f"{counter:03d}. {t['name']} - {s['name']}"
        GENERATED_TEMPLATES[key_name] = {
            "theme": t,
            "style": s
        }
        counter += 1

LNG = {
    "congrats": "مَبْرُوكِ النَّجَاح",
    "cert_prefix": "شَهَادَة البَكَالُورْيَا 2026",
    "gpa_lbl": "بِمُعَدَّلِ مُمَيَّز قَدْرُهُ",
    "stream_lbl": "الشُّعْبَة:",
    "wilaya_lbl": "الولاية:",
    "dedication_label": "مُهْدَى بِكُلِّ حُبٍّ مِنْ طَرَفِ:",
    "male_prefix": "البَطَلُ",
    "female_prefix": "البَطَلَةُ"
}


def generate_story_v4(name, gpa, stream, template_key, mode, sender_name="", profile_img=None, enable_glow=True,
                      enable_shine=True, enable_gradient=True, wilaya="", honor_badge="بدون وسام",
                      card_ratio="ستوري عمودي 9:16 (Story Portrait)", maquam_option="بدون معلم مقام الشهيد 🚫",
                      custom_footer_text="", monument_opacity=0.85, maquam_color_style="ذهبي ملكي فاخر ✨"):
    is_landscape = (card_ratio == "مستطيل أفقي 7:5 (Horizontal Landscape)")

    if is_landscape:
        width, height = 1400, 1000
    else:
        width, height = 1080, 1920

    story = Image.new("RGBA", (width, height), (8, 12, 20, 255))
    draw = ImageDraw.Draw(story)

    rotation_resample = 3  # BICUBIC default
    res_obj = getattr(Image, 'Resampling', None)
    if res_obj is not None and hasattr(res_obj, 'BICUBIC'):
        rotation_resample = getattr(res_obj, 'BICUBIC')
    elif hasattr(Image, 'BICUBIC'):
        rotation_resample = getattr(Image, 'BICUBIC')

    title_font = get_modern_cairo_font(85)
    subtitle_font = get_modern_cairo_font(48)
    # تصغير حجم خط رقم المعدل في الكرت الأفقي 7:5 من 120 إلى 95 ليتناسق بصرياً
    gpa_font = get_modern_cairo_font(95 if is_landscape else 125)
    name_font = get_modern_cairo_font(58 if is_landscape else (65 if wilaya else 68))
    stream_font = get_modern_cairo_font(36 if is_landscape else (40 if wilaya else 44))
    wilaya_font = get_modern_cairo_font(36 if is_landscape else 40)
    footer_font = get_modern_cairo_font(38)

    template_data = GENERATED_TEMPLATES[template_key]
    theme = template_data["theme"]
    style = template_data["style"]

    base_color = theme["base_color"]
    sec_color = theme["sec_color"]
    border_color = theme["border_color"]
    pattern = theme["pattern"]

    for y in range(height):
        pos = y / height
        if style["gradient_stops"] == 3:
            if pos < 0.5:
                ratio = pos * 2.0
                r = int(base_color[0] + (sec_color[0] - base_color[0]) * ratio)
                g = int(base_color[1] + (sec_color[1] - base_color[1]) * ratio)
                b = int(base_color[2] + (sec_color[2] - base_color[2]) * ratio)
            else:
                ratio = (pos - 0.5) * 2.0
                r = int(sec_color[0] + (base_color[0] - sec_color[0]) * ratio)
                g = int(sec_color[1] + (base_color[1] - sec_color[1]) * ratio)
                b = int(sec_color[2] + (base_color[2] - sec_color[2]) * ratio)
        else:
            r = int(base_color[0] + (sec_color[0] - base_color[0]) * pos)
            g = int(base_color[1] + (sec_color[1] - base_color[1]) * pos)
            b = int(base_color[2] + (sec_color[2] - base_color[2]) * pos)

        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    random.seed(12345)
    if pattern == "stars" or style["name"] == "النيوني (Neon)":
        for _ in range(30):
            st_x = random.randint(50, width - 50)
            st_y = random.randint(50, height - 50)
            st_size = random.randint(3, 8)
            draw.ellipse([st_x, st_y, st_x + st_size, st_y + st_size], fill=(255, 255, 255, 140))
    elif pattern == "neon_grid" or style["name"] == "الشبكي (Textured)":
        grid_space = 50
        for i in range(0, width, grid_space):
            draw.line([(i, 0), (i, height)], fill=(border_color[0], border_color[1], border_color[2], 15), width=1)
        for j in range(0, height, grid_space):
            draw.line([(0, j), (width, j)], fill=(border_color[0], border_color[1], border_color[2], 15), width=1)
    elif pattern == "sparkles":
        for _ in range(12):
            st_x = random.randint(80, width - 80)
            st_y = random.randint(80, height - 80)
            length = random.randint(15, 30)
            draw.line([(st_x - length, st_y), (st_x + length, st_y)], fill=(255, 255, 255, 120), width=2)
            draw.line([(st_x, st_y - length), (st_x, st_y + length)], fill=(255, 255, 255, 120), width=2)
    elif pattern == "clouds":
        for _ in range(6):
            rad = random.randint(250, 400)
            cx_val = random.randint(0, width)
            cy_val = random.randint(0, height)
            draw.ellipse([cx_val - rad, cy_val - rad, cx_val + rad, cy_val + rad],
                         fill=(border_color[0], border_color[1], border_color[2], 18))

    if "أيقونة" in maquam_option:
        monument_tint = (212, 175, 55, 255)
    else:
        if maquam_color_style == "ذهبي ملكي فاخر ✨":
            monument_tint = (212, 175, 55, 255)
        else:
            monument_tint = border_color

    monument_asset = load_and_colorize_monument(monument_tint)

    if ("صرح فني كبير" in maquam_option or "خلفية فنية ضخمة" in maquam_option) and monument_asset is not None:
        if is_landscape:
            scale_h = 920
            scale_w = int(monument_asset.width * (scale_h / monument_asset.height))
            resized_monument = monument_asset.resize((scale_w, scale_h), get_resampling_filter())
            resized_monument = apply_alpha_gradient_to_monument(resized_monument, monument_opacity)

            paste_x = 380 - scale_w // 2
            paste_y = height - scale_h - 35

            mon_layer = Image.new("RGBA", story.size, (0, 0, 0, 0))
            mon_layer.paste(resized_monument, (paste_x, paste_y))
            story.alpha_composite(mon_layer)
        else:
            scale_h = 1880
            scale_w = int(monument_asset.width * (scale_h / monument_asset.height))
            resized_monument = monument_asset.resize((scale_w, scale_h), get_resampling_filter())
            resized_monument = apply_alpha_gradient_to_monument(resized_monument, monument_opacity)

            paste_x = width // 2 - scale_w // 2
            paste_y = (height - scale_h) // 2 + 35

            mon_layer = Image.new("RGBA", story.size, (0, 0, 0, 0))
            mon_layer.paste(resized_monument, (paste_x, paste_y))
            story.alpha_composite(mon_layer)

    draw_soft_shadow(story, 35, 35, width - 35, height - 35, corner_radius=50, blur_radius=20, offset=(0, 15))
    draw.rounded_rectangle([35, 35, width - 35, height - 35], radius=50, outline=border_color, width=8)

    # التعديل الإبداعي: إزالة الإطار الأبيض الداخلي تماماً واستبداله بإطار توهج ذهبي داخلي ناعم وجميل للغاية
    glow_yellow_color = (border_color[0], border_color[1], border_color[2], 120)
    draw.rounded_rectangle([44, 44, width - 44, height - 44], radius=44, outline=glow_yellow_color, width=3)

    flag_w, flag_h = 140, 95
    flag_x, flag_y = width - 215, 65
    draw_perfect_algerian_flag(story, flag_x, flag_y, flag_w, flag_h)

    txt_congrats = format_arabic_text(LNG["congrats"])
    txt_cert = format_arabic_text(LNG["cert_prefix"])

    gold_palette = [(255, 215, 0), (185, 135, 25)]

    if is_landscape:
        if enable_gradient:
            draw_gradient_text(story, txt_congrats, (width // 2, 140), title_font, gold_palette)
        else:
            draw_text_with_shadow(story, txt_congrats, (width // 2, 140), title_font, border_color)

        draw_text_with_shadow(story, txt_cert, (width // 2, 235), subtitle_font, (255, 255, 255, 255))

        cx, cy = 380, 580
        avatar_size = 360

        if enable_glow:
            glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow_layer)
            glow_color = border_color[:3]
            for r_glow in range(avatar_size // 2 + 120, avatar_size // 2, -6):
                alpha = int(60 * (1.0 - (r_glow - avatar_size // 2) / 120))
                glow_draw.ellipse([cx - r_glow, cy - r_glow, cx + r_glow, cy + r_glow],
                                  fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
            story.alpha_composite(glow_layer)

        if profile_img is not None:
            circular_avatar = make_image_circular(profile_img, size=(avatar_size, avatar_size))
            av_layer = Image.new("RGBA", story.size, (0, 0, 0, 0))
            av_layer.paste(circular_avatar, (cx - avatar_size // 2, cy - avatar_size // 2))
            story.alpha_composite(av_layer)
        else:
            draw.ellipse([cx - avatar_size // 2, cy - avatar_size // 2,
                          cx + avatar_size // 2, cy + avatar_size // 2],
                         outline=border_color, width=6, fill=(20, 25, 40, 180))

            def draw_vector_graduation_cap(draw_obj, px, py, cap_size, color):
                pt1 = (px, py - cap_size // 2)
                pt2 = (px + cap_size, py)
                pt3 = (px, py + cap_size // 2)
                pt4 = (px - cap_size, py)
                draw_obj.polygon([pt1, pt2, pt3, pt4], fill=color)
                draw_obj.polygon([
                    (px - cap_size // 2, py + cap_size // 4),
                    (px + cap_size // 2, py + cap_size // 4),
                    (px + cap_size // 3, py + cap_size // 1.4),
                    (px - cap_size // 3, py + cap_size // 1.4)
                ], fill=color)
                draw_obj.line([(px - cap_size // 1.4, py), (px - cap_size // 1.1, py + cap_size // 2.5)], fill=color,
                              width=4)
                draw_obj.ellipse([px - cap_size // 1.1 - 7, py + cap_size // 2.5 - 7, px - cap_size // 1.1 + 7,
                                  py + cap_size // 2.5 + 7], fill=color)

            draw_vector_graduation_cap(draw, cx, cy - 10, 75, border_color)

        draw.ellipse([cx - (avatar_size // 2 + 12), cy - (avatar_size // 2 + 12),
                      cx + (avatar_size // 2 + 12), cy + (avatar_size // 2 + 12)],
                     outline=border_color, width=5)

        glass_w, glass_h = 550, 200 if wilaya else 180
        glass_x = width - glass_w - 120
        glass_y = 380

        draw_obsidian_glass_card(story, glass_x, glass_y, glass_x + glass_w, glass_y + glass_h, border_color,
                                 corner_radius=30, enable_shine=enable_shine)

        reshaped_name = format_arabic_text(name)
        text_center_x = glass_x + glass_w // 2

        if wilaya:
            draw_text_with_shadow(story, reshaped_name, (text_center_x, glass_y + 48), name_font, (255, 255, 255, 255))
            stream_lbl = LNG["stream_lbl"]
            stream_display = f"{stream_lbl} {stream}"
            reshaped_stream = format_arabic_text(stream_display)
            draw_text_safely(story, reshaped_stream, (text_center_x, glass_y + 110), stream_font, border_color)

            wilaya_lbl = LNG["wilaya_lbl"]
            wilaya_display = f"📍 {wilaya_lbl} {wilaya}"
            reshaped_wilaya = format_arabic_text(wilaya_display)
            draw_text_safely(story, reshaped_wilaya, (text_center_x, glass_y + 160), wilaya_font, (255, 255, 255, 210))
        else:
            draw_text_with_shadow(story, reshaped_name, (text_center_x, glass_y + 58), name_font, (255, 255, 255, 255))
            stream_lbl = LNG["stream_lbl"]
            stream_display = f"{stream_lbl} {stream}"
            reshaped_stream = format_arabic_text(stream_display)
            draw_text_safely(story, reshaped_stream, (text_center_x, glass_y + 130), stream_font, border_color)

        badge_w, badge_h = 380, 130
        badge_x = glass_x + (glass_w - badge_w) // 2
        badge_y = 620

        draw_obsidian_glass_card(story, badge_x, badge_y, badge_x + badge_w, badge_y + badge_h, border_color,
                                 corner_radius=30, enable_shine=enable_shine)

        formatted_gpa = f"{float(gpa):.2f}"
        if enable_gradient:
            draw_gradient_text(story, formatted_gpa, (badge_x + badge_w // 2, badge_y + badge_h // 2), gpa_font,
                               gold_palette)
        else:
            draw_text_with_shadow(story, formatted_gpa, (badge_x + badge_w // 2, badge_y + badge_h // 2), gpa_font,
                                  border_color)

    else:
        if enable_gradient:
            draw_gradient_text(story, txt_congrats, (width // 2, 210), title_font, gold_palette)
        else:
            draw_text_with_shadow(story, txt_congrats, (width // 2, 210), title_font, border_color)

        draw_text_with_shadow(story, txt_cert, (width // 2, 315), subtitle_font, (255, 255, 255, 255))

        cx, cy = width // 2, 660
        avatar_size = 360

        if enable_glow:
            glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow_layer)
            glow_color = border_color[:3]
            for r_glow in range(avatar_size // 2 + 120, avatar_size // 2, -6):
                alpha = int(60 * (1.0 - (r_glow - avatar_size // 2) / 120))
                glow_draw.ellipse([cx - r_glow, cy - r_glow, cx + r_glow, cy + r_glow],
                                  fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
            story.alpha_composite(glow_layer)

        if profile_img is not None:
            circular_avatar = make_image_circular(profile_img, size=(avatar_size, avatar_size))
            av_layer = Image.new("RGBA", story.size, (0, 0, 0, 0))
            av_layer.paste(circular_avatar, (cx - avatar_size // 2, cy - avatar_size // 2))
            story.alpha_composite(av_layer)
        else:
            draw.ellipse([cx - avatar_size // 2, cy - avatar_size // 2,
                          cx + avatar_size // 2, cy + avatar_size // 2],
                         outline=border_color, width=6, fill=(20, 25, 40, 180))

            def draw_vector_graduation_cap(draw_obj, px, py, cap_size, color):
                pt1 = (px, py - cap_size // 2)
                pt2 = (px + cap_size, py)
                pt3 = (px, py + cap_size // 2)
                pt4 = (px - cap_size, py)
                draw_obj.polygon([pt1, pt2, pt3, pt4], fill=color)
                draw_obj.polygon([
                    (px - cap_size // 2, py + cap_size // 4),
                    (px + cap_size // 2, py + cap_size // 4),
                    (px + cap_size // 3, py + cap_size // 1.4),
                    (px - cap_size // 3, py + cap_size // 1.4)
                ], fill=color)
                draw_obj.line([(px - cap_size // 1.4, py), (px - cap_size // 1.1, py + cap_size // 2.5)], fill=color,
                              width=4)
                draw_obj.ellipse([px - cap_size // 1.1 - 7, py + cap_size // 2.5 - 7, px - cap_size // 1.1 + 7,
                                  py + cap_size // 2.5 + 7], fill=color)

            draw_vector_graduation_cap(draw, cx, cy - 10, 75, border_color)

        draw.ellipse([cx - (avatar_size // 2 + 12), cy - (avatar_size // 2 + 12),
                      cx + (avatar_size // 2 + 12), cy + (avatar_size // 2 + 12)],
                     outline=border_color, width=5)

        glass_w, glass_h = 760, 240 if wilaya else 220
        glass_x = width // 2 - glass_w // 2
        glass_y = 930

        draw_obsidian_glass_card(story, glass_x, glass_y, glass_x + glass_w, glass_y + glass_h, border_color,
                                 corner_radius=30, enable_shine=enable_shine)

        reshaped_name = format_arabic_text(name)

        if wilaya:
            draw_text_with_shadow(story, reshaped_name, (width // 2, glass_y + 55), name_font, (255, 255, 255, 255))
            stream_lbl = LNG["stream_lbl"]
            stream_display = f"{stream_lbl} {stream}"
            reshaped_stream = format_arabic_text(stream_display)
            draw_text_safely(story, reshaped_stream, (width // 2, glass_y + 125), stream_font, border_color)

            wilaya_lbl = LNG["wilaya_lbl"]
            wilaya_display = f"📍 {wilaya_lbl} {wilaya}"
            reshaped_wilaya = format_arabic_text(wilaya_display)
            draw_text_safely(story, reshaped_wilaya, (width // 2, glass_y + 185), wilaya_font, (255, 255, 255, 210))
        else:
            draw_text_with_shadow(story, reshaped_name, (width // 2, glass_y + 65), name_font, (255, 255, 255, 255))
            stream_lbl = LNG["stream_lbl"]
            stream_display = f"{stream_lbl} {stream}"
            reshaped_stream = format_arabic_text(stream_display)
            draw_text_safely(story, reshaped_stream, (width // 2, glass_y + 155), stream_font, border_color)

        badge_w, badge_h = 545, 165
        badge_x = width // 2 - badge_w // 2
        badge_y = 1240

        draw_obsidian_glass_card(story, badge_x, badge_y, badge_x + badge_w, badge_y + badge_h, border_color,
                                 corner_radius=30, enable_shine=enable_shine)

        formatted_gpa = f"{float(gpa):.2f}"
        if enable_gradient:
            draw_gradient_text(story, formatted_gpa, (width // 2, badge_y + badge_h // 2), gpa_font, gold_palette)
        else:
            draw_text_with_shadow(story, formatted_gpa, (width // 2, badge_y + badge_h // 2), gpa_font, border_color)

    if honor_badge == "إكليل الغار الملكي 🌿":
        r_wreath = avatar_size // 2 + 16
        for angle_deg in range(35, 146, 12):
            for side in [-1, 1]:
                theta = math.radians(90 + side * angle_deg)
                lx = cx + r_wreath * math.cos(theta)
                ly = cy + r_wreath * math.sin(theta)
                leaf_w, leaf_h = 36, 18
                leaf_mask = Image.new("L", (leaf_w, leaf_h), 0)
                lm_draw = ImageDraw.Draw(leaf_mask)
                lm_draw.ellipse([0, 0, leaf_w, leaf_h], fill=255)
                rotated_leaf = Image.new("RGBA", (leaf_w, leaf_h), (212, 175, 55, 255))
                rotated_leaf = rotated_leaf.rotate(-side * (angle_deg - 35), expand=True, resample=rotation_resample)

                leaf_layer = Image.new("RGBA", story.size, (0, 0, 0, 0))
                leaf_layer.paste(rotated_leaf, (int(lx - rotated_leaf.width // 2), int(ly - rotated_leaf.height // 2)),
                                 mask=rotated_leaf)
                story.alpha_composite(leaf_layer)

    elif honor_badge == "ميدالية الشرف والتميز 🎖️":
        theta = math.radians(225)
        mx = cx + (avatar_size // 2) * math.cos(theta)
        my = cy + (avatar_size // 2) * math.sin(theta)

        badge_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        b_draw = ImageDraw.Draw(badge_canvas)
        b_draw.polygon([(mx - 22, my - 45), (mx + 22, my - 45), (mx + 10, my), (mx - 10, my)], fill=(0, 102, 51, 255))
        b_draw.polygon([(mx - 10, my - 45), (mx + 10, my - 45), (mx + 4, my), (mx - 4, my)], fill=(210, 16, 52, 255))
        b_draw.ellipse([mx - 28, my - 10, mx + 28, my + 46], fill=(212, 175, 55, 255), outline=(185, 135, 25, 255),
                       width=3)
        star_pts = []
        for i in range(10):
            r = 16 if i % 2 == 0 else 8
            angle = i * math.pi / 5 - math.pi / 2
            star_pts.append((mx + r * math.cos(angle), my + 18 + r * math.sin(angle)))
        b_draw.polygon(star_pts, fill=(255, 255, 255, 255))

        story.alpha_composite(badge_canvas)

    elif honor_badge == "تاج النصر الذهبي 👑 (للذكور)":
        r_head = avatar_size // 2
        tx, ty = cx, cy - r_head + 15
        base_w = 95

        crown_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        cr_draw = ImageDraw.Draw(crown_canvas)
        cr_draw.rounded_rectangle([tx - base_w, ty - 12, tx + base_w, ty + 12], radius=8, fill=(212, 175, 55, 255),
                                  outline=(185, 135, 25, 255), width=3)
        crown_points = [
            (tx - base_w, ty - 6),
            (tx - base_w - 10, ty - 55),
            (tx - base_w // 2, ty - 22),
            (tx, ty - 80),
            (tx + base_w // 2, ty - 22),
            (tx + base_w + 10, ty - 55),
            (tx + base_w, ty - 6)
        ]
        cr_draw.polygon(crown_points, fill=(212, 175, 55, 255), outline=(185, 135, 25, 255), width=3)
        cr_draw.ellipse([tx - base_w - 18, ty - 63, tx - base_w - 2, ty - 47], fill=(210, 16, 52, 255))
        cr_draw.ellipse([tx - 8, ty - 88, tx + 8, ty - 72], fill=(210, 16, 52, 255))
        cr_draw.ellipse([tx + base_w + 2, ty - 63, tx + base_w + 18, ty - 47], fill=(210, 16, 52, 255))

        story.alpha_composite(crown_canvas)

    elif honor_badge == "تاج الملكة الأنيق 👑✨ (للإناث)":
        r_head = avatar_size // 2
        tx, ty = cx, cy - r_head + 15
        base_w = 85

        crown_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        cr_draw = ImageDraw.Draw(crown_canvas)
        cr_draw.rounded_rectangle([tx - base_w, ty - 8, tx + base_w, ty + 12], radius=10, fill=(244, 143, 177, 255),
                                  outline=(212, 175, 55, 255), width=3)
        crown_points = [
            (tx - base_w, ty - 2),
            (tx - base_w, ty - 45),
            (tx - base_w // 2, ty - 15),
            (tx - base_w // 4, ty - 65),
            (tx, ty - 25),
            (tx + base_w // 4, ty - 65),
            (tx + base_w // 2, ty - 15),
            (tx + base_w, ty - 45),
            (tx + base_w, ty - 2)
        ]
        cr_draw.polygon(crown_points, fill=(255, 215, 0, 255), outline=(244, 143, 177, 255), width=3)
        cr_draw.ellipse([tx - base_w - 6, ty - 51, tx - base_w + 6, ty - 39], fill=(255, 255, 255, 255),
                        outline=(212, 175, 55, 255), width=1)
        cr_draw.ellipse([tx - base_w // 4 - 6, ty - 71, tx - base_w // 4 + 6, ty - 59], fill=(255, 255, 255, 255),
                        outline=(212, 175, 55, 255), width=1)
        cr_draw.ellipse([tx - 6, ty - 31, tx + 6, ty - 19], fill=(255, 255, 255, 255), outline=(212, 175, 55, 255),
                        width=1)
        cr_draw.ellipse([tx + base_w // 4 - 6, ty - 71, tx + base_w // 4 + 6, ty - 59], fill=(255, 255, 255, 255),
                        outline=(212, 175, 55, 255), width=1)
        cr_draw.ellipse([tx + base_w - 6, ty - 51, tx + base_w + 6, ty - 39], fill=(255, 255, 255, 255),
                        outline=(212, 175, 55, 255), width=1)
        cr_draw.regular_polygon((tx, ty - 2), 12, n=4, fill=(233, 30, 99, 255))

        story.alpha_composite(crown_canvas)

    elif honor_badge == "طوق الياسمين الفاخر 🌸 (للإناث)":
        r_wreath = avatar_size // 2 + 8
        jasmine_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        j_draw = ImageDraw.Draw(jasmine_canvas)
        for angle_deg in range(-20, 201, 15):
            theta = math.radians(180 - angle_deg)
            lx = cx + r_wreath * math.cos(theta)
            ly = cy - r_wreath * math.sin(theta)
            j_draw.ellipse([lx - 15, ly - 15, lx + 15, ly + 15], fill=(34, 139, 34, 210))
            j_draw.ellipse([lx - 10, ly - 10, lx + 10, ly + 10], fill=(244, 143, 177, 255))
            j_draw.ellipse([lx - 5, ly - 5, lx + 5, ly + 5], fill=(233, 30, 99, 255))
            j_draw.ellipse([lx - 2, ly - 2, lx + 2, ly + 2], fill=(255, 255, 255, 255))
        story.alpha_composite(jasmine_canvas)

    elif honor_badge == "إكليل الورد البهيج 💐 (للإناث)":
        r_wreath = avatar_size // 2 + 10
        rose_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        j_draw = ImageDraw.Draw(rose_canvas)
        for angle_deg in range(-20, 201, 20):
            theta = math.radians(180 - angle_deg)
            lx = cx + r_wreath * math.cos(theta)
            ly = cy - r_wreath * math.sin(theta)
            j_draw.ellipse([lx - 16, ly - 16, lx + 16, ly + 16], fill=(46, 125, 50, 220))
            j_draw.ellipse([lx - 12, ly - 12, lx + 12, ly + 12], fill=(233, 30, 99, 255))
            j_draw.ellipse([lx - 8, ly - 8, lx + 8, ly + 8], fill=(244, 143, 177, 255))
            j_draw.ellipse([lx - 4, ly - 4, lx + 4, ly + 4], fill=(255, 255, 255, 255))
        story.alpha_composite(rose_canvas)

    elif honor_badge == "وشاح النجاح والتفوق 🎗️":
        sash_y = cy + 130

        sash_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(sash_canvas)
        s_draw.rounded_rectangle([cx - 150, sash_y - 25, cx + 150, sash_y + 25], radius=15, fill=(212, 175, 55, 255),
                                 outline=(185, 135, 25, 255), width=3)
        story.alpha_composite(sash_canvas)

        txt_sash = format_arabic_text("مُتَفَوِّقٌ")
        sash_font = get_modern_cairo_font(28)
        draw_text_safely(story, txt_sash, (cx, sash_y), sash_font, (255, 255, 255, 255))

    elif honor_badge == "درع التميز والريادة 🛡️":
        r_shield = avatar_size // 2 + 25
        shield_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        sh_draw = ImageDraw.Draw(shield_canvas)

        oct_points = []
        for i in range(8):
            angle = i * math.pi / 4 + math.pi / 8
            ox = cx + r_shield * math.cos(angle)
            oy = cy + r_shield * math.sin(angle)
            oct_points.append((ox, oy))
        sh_draw.polygon(oct_points, outline=(0, 220, 255, 255), width=6)

        oct_points_in = []
        for i in range(8):
            angle = i * math.pi / 4 + math.pi / 8
            ox = cx + (r_shield - 8) * math.cos(angle)
            oy = cy + (r_shield - 8) * math.sin(angle)
            oct_points_in.append((ox, oy))
        sh_draw.polygon(oct_points_in, outline=(212, 175, 55, 255), width=2)

        story.alpha_composite(shield_canvas)

    elif honor_badge == "نجمة المتفوق الساطعة ⭐":
        sx, sy = cx, cy - (avatar_size // 2) - 35
        star_canvas = Image.new("RGBA", story.size, (0, 0, 0, 0))
        st_draw = ImageDraw.Draw(star_canvas)

        for r_glow in range(40, 10, -5):
            st_draw.ellipse([sx - r_glow, sy - r_glow, sx + r_glow, sy + r_glow],
                            fill=(212, 175, 55, int(50 * (1 - r_glow / 40))))
        star_pts = []
        for i in range(10):
            r_val = 35 if i % 2 == 0 else 15
            angle = i * math.pi / 5 - math.pi / 2
            star_pts.append((sx + r_val * math.cos(angle), sy + r_val * math.sin(angle)))
        st_draw.polygon(star_pts, fill=(212, 175, 55, 255), outline=(255, 255, 255, 255), width=2)

        story.alpha_composite(star_canvas)

    if "أيقونة" in maquam_option and monument_asset is not None:
        scale_h = 240
        scale_w = int(monument_asset.width * (scale_h / monument_asset.height))
        resized_monument = monument_asset.resize((scale_w, scale_h), get_resampling_filter())

        r_c, g_c, b_c, a_c = resized_monument.split()
        full_alpha = a_c.point(lambda x: int(x * 0.95))
        resized_monument.putalpha(full_alpha)

        if is_landscape:
            paste_x = 95
            paste_y = 50
        else:
            paste_x = 90
            paste_y = height - scale_h - 90

        icon_layer = Image.new("RGBA", story.size, (0, 0, 0, 0))
        icon_layer.paste(resized_monument, (paste_x, paste_y))
        story.alpha_composite(icon_layer)

    if not is_landscape:
        if mode == "لصديقي" and sender_name:
            lbl_dedication = format_arabic_text(LNG["dedication_label"])
            val_sender = format_arabic_text(sender_name)

            draw_text_safely(story, lbl_dedication, (width // 2, height - 310), footer_font, (255, 255, 255, 180))
            draw_text_with_shadow(story, val_sender, (width // 2, height - 245), subtitle_font, border_color)
        else:
            if custom_footer_text:
                clean_footer = format_arabic_text(custom_footer_text)
                draw_text_with_shadow(story, clean_footer, (width // 2, height - 390), footer_font,
                                      (255, 255, 255, 220))

    return story


io_streamlit.markdown("""
    <div class='ad-top-wrapper'>
        <div class='ad-top-wrapper-inner' style='display:flex; flex-direction:column; justify-content:center;'>
            <div class='ad-title-tag'>📢 عرض تمويلي تجريبي • Sponsored Ad</div>
            <div style='font-size: 11px; font-weight:700; color:#ffffff; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;'>🎁 دبلوم هندسة الذكاء الاصطناعي وبايثون 2026</div>
            <div style='font-size: 9.5px; color:#9ca3af; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;'>سجل مجاناً للطلبة الجدد وباشر رحلتك الاحترافية في البكالوريا!</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# العداد التنازلي التفاعلي الممتد لـ 10 أيام ليبدأ الأحد 12 جويلية 2026 الساعة 08:00 صباحاً (ينتهي في 22 جويلية 2026 الساعة 08:00 صباحاً)
countdown_html = """
<div style="
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.18), rgba(59, 130, 246, 0.18));
    border: 2px solid #10b981;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #ffffff;
    box-shadow: 0 10px 35px rgba(16, 185, 129, 0.25);
    margin: 5px auto 20px auto;
    direction: rtl;
">
    <div style="font-size: 14px; font-weight: bold; color: #10b981; margin-bottom: 8px; display: flex; align-items: center; justify-content: center; gap: 8px;">
        📢 موقع مؤقت: ينطلق التشغيل الرسمي الأحد 12 جويلية الساعة 08:00 صباحاً!
    </div>
    <div style="font-size: 11.5px; color: #94a3b8; margin-bottom: 12px; font-weight: 500;">
        الخدمة مجانية ومحدودة المدة. الوقت المتبقي للإغلاق التام لملقم الموقع:
    </div>
    <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: nowrap;">
        <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; min-width: 60px; padding: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
            <div id="days" style="font-size: 20px; font-weight: 900; color: #ffffff; text-shadow: 0 0 10px rgba(255,255,255,0.2);">00</div>
            <div style="font-size: 9.5px; color: #94a3b8; margin-top: 3px;">أيام</div>
        </div>
        <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; min-width: 60px; padding: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
            <div id="hours" style="font-size: 20px; font-weight: 900; color: #10b981; text-shadow: 0 0 10px rgba(16, 185, 129, 0.3);">00</div>
            <div style="font-size: 9.5px; color: #94a3b8; margin-top: 3px;">ساعات</div>
        </div>
        <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; min-width: 60px; padding: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
            <div id="minutes" style="font-size: 20px; font-weight: 900; color: #3b82f6; text-shadow: 0 0 10px rgba(59, 130, 246, 0.3);">00</div>
            <div style="font-size: 9.5px; color: #94a3b8; margin-top: 3px;">دقائق</div>
        </div>
        <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; min-width: 60px; padding: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
            <div id="seconds" style="font-size: 20px; font-weight: 900; color: #8b5cf6; text-shadow: 0 0 10px rgba(139, 92, 246, 0.3);">00</div>
            <div style="font-size: 9.5px; color: #94a3b8; margin-top: 3px;">ثواني</div>
        </div>
    </div>
</div>

<script>
    var targetDate = new Date("2026-07-22T08:00:00").getTime();

    function updateTimer() {
        var now = new Date().getTime();
        var difference = targetDate - now;

        if (difference < 0) {
            document.getElementById("days").innerText = "00";
            document.getElementById("hours").innerText = "00";
            document.getElementById("minutes").innerText = "00";
            document.getElementById("seconds").innerText = "00";
            return;
        }

        var days = Math.floor(difference / (1000 * 60 * 60 * 24));
        var hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((difference % (1000 * 60)) / 1000);

        document.getElementById("days").innerText = days < 10 ? "0" + days : days;
        document.getElementById("hours").innerText = hours < 10 ? "0" + hours : hours;
        document.getElementById("minutes").innerText = minutes < 10 ? "0" + minutes : minutes;
        document.getElementById("seconds").innerText = seconds < 10 ? "0" + seconds : seconds;
    }

    setInterval(updateTimer, 1000);
    updateTimer();
</script>
"""

components.html(countdown_html, height=170, scrolling=False)

io_streamlit.markdown("""
    <div class='welcome-container'>
        <h1 class='main-title'>✨ Najah Story</h1>
        <p class='designer-tag'>Designed by Yaakoub Ali Dif</p>
        <p class='sub-title'>صمم وحمل ستوري نجاحك في البكالوريا بأحدث صيحات التصميم العصري وبقوالب لا حصر لها!</p>
    </div>
""", unsafe_allow_html=True)
io_streamlit.write("---")

# تم تنظيف البطاقة الإرشادية تماماً من إشارات الأجواء الموسيقية ومعزوفة التخرج المزعجة والسطور الإضافية
io_streamlit.markdown("""
    <div class='mobile-hide' style='background: linear-gradient(135deg, rgba(124, 58, 237, 0.12), rgba(37, 99, 235, 0.12)); border: 2px solid rgba(124, 58, 237, 0.3); border-radius: 20px; padding: 20px; margin-bottom: 25px; box-shadow: 0 8px 32px rgba(124, 58, 237, 0.15);'>
        <h3 style='background: linear-gradient(135deg, #c084fc, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0 0 8px 0; font-size: 18px; font-weight: 900; display: flex; align-items: center; gap: 8px;'>✨ الدليل الإبداعي والتوجيه البصري الفاخر</h3>
        <p style='color: #cbd5e1; margin: 0; font-size: 13px; line-height: 1.6; text-align: right;'>
            <b>🎨 ميزات تصميمية:</b> تفضل بزيارة <b>القائمة الجانبية (Sidebar)</b> لتفعيل التوهج، واللمعان البلوري المائل، والتدرج الذهبي المعدني للنصوص.
        </p>
    </div>
""", unsafe_allow_html=True)

with io_streamlit.sidebar:
    io_streamlit.markdown("### ✨ ميزات التصميم الفاخرة")
    io_streamlit.info("تحكم بالميزات السينمائية لتشاهد فخامة التصميم المطور مباشرة وبألوان معتمة ثابتة عند التحميل:")

    chk_glow = io_streamlit.checkbox("توهج هالة الصورة الشخصية (Radial Glow)", value=True)
    chk_shine = io_streamlit.checkbox("انعكاس الضوء البلوري المائل (Glass Shine)", value=True)
    chk_gradient = io_streamlit.checkbox("التدرج اللوني الذهبي للنصوص (Gold Text Gradient)", value=True)

    # القيمة الافتراضية "ذهبي ملكي فاخر ✨" في الـ Sidebar كخيار أول (index=0)
    maquam_color_opt = io_streamlit.radio(
        "🎨 لون مجسم مقام الشهيد المطور:",
        ["ذهبي ملكي فاخر ✨", "يتبع لون قالب التصميم 🎨"],
        index=0,
        help="اختر اللون المفضل لمجسم مقام الشهيد في الخلفية ليظهر بأبهى صورة"
    )

    monument_opacity_slider = io_streamlit.slider(
        "🏛️ شفافية خلفية مقام الشهيد:",
        min_value=5,
        max_value=100,
        value=85,
        step=5,
        help="تتحكم بمدى شفافية صرح مقام الشهيد الخلفي عند تحديده كخلفية فنية كبيرة"
    ) / 100.0

col_ctrl, col_view = io_streamlit.columns([1.1, 1])

if 'generated_image_bytes' not in io_streamlit.session_state:
    io_streamlit.session_state['generated_image_bytes'] = None
if 'generated_filename' not in io_streamlit.session_state:
    io_streamlit.session_state['generated_filename'] = ""

with col_ctrl:
    io_streamlit.markdown("### 🔴 أولاً: البيانات الأساسية")

    student_name = io_streamlit.text_input("🎓 الاسم الكامل:", max_chars=32, value="ضيف يعقوب")

    enable_wilaya = io_streamlit.checkbox("📍 عرض الولاية على الكرت", value=True)

    if enable_wilaya:
        selected_wilaya = io_streamlit.selectbox(
            "📍 اختر الولاية الجزائرية:",
            algerian_wilayas_69
        )
    else:
        selected_wilaya = ""

    streams_suggested_ar = [
        "علوم تجريبية", "رياضيات", "تقني رياضي", "تسيير واقتصاد",
        "لغات أجنبية", "آداب وفلسفة"
    ]
    selected_stream_opt = io_streamlit.selectbox("📚 تخصص الشعبة:", streams_suggested_ar + ["شعبة مخصصة أخرى"])

    if selected_stream_opt == "شعبة مخصصة أخرى":
        student_stream = io_streamlit.text_input("اكتب شعبتك بحرية هنا:", value="هندسة البرمجيات")
    else:
        student_stream = selected_stream_opt

    student_gpa = io_streamlit.number_input(
        "📊 معدل البكالوريا:",
        min_value=10.00,
        max_value=20.00,
        value=16.82,
        step=0.01,
        format="%.2f"
    )

    card_ratio_option = io_streamlit.selectbox(
        "📐 مقاس الكارت:",
        ["ستوري عمودي 9:16 (Story Portrait)", "مستطيل أفقي 7:5 (Horizontal Landscape)"]
    )

    is_landscape_selected = (card_ratio_option == "مستطيل أفقي 7:5 (Horizontal Landscape)")

    io_streamlit.write("---")
    io_streamlit.markdown("### 🟢 ثانياً: الخيارات والمظهر")

    template_keys = list(GENERATED_TEMPLATES.keys())
    selected_template = io_streamlit.selectbox(
        "🎨 اختر الثيم (القالب البصري):",
        template_keys
    )

    maquam_label_opt = [
        "إخفاء المعلم بالكامل 🚫",
        "أيقونة مذهبة مصغرة في الزاوية ✨",
        "خلفية فنية ضخمة مدمجة في التصميم 🏛️"
    ]
    selected_maquam_opt = io_streamlit.selectbox(
        "🏛️ مظهر وموضع صرح مقام الشهيد في الكرت:",
        maquam_label_opt,
        index=2
    )

    selected_badge = io_streamlit.selectbox(
        "🎖️ الأوسمة والشارات المضافة:",
        [
            "بدون وسام 🚫",
            "إكليل الغار الملكي 🌿",
            "ميدالية الشرف والتميز 🎖️",
            "تاج النصر الذهبي 👑 (للذكور)",
            "تاج الملكة الأنيق 👑✨ (للإناث)",
            "طوق الياسمين الفاخر 🌸 (للإناث)",
            "إكليل الورد البهيج 💐 (للإناث)",
            "وشاح النجاح والتفوق 🎗️",
            "درع التميز والريادة 🛡️",
            "نجمة المتفوق الساطعة ⭐"
        ]
    )

    uploaded_file = io_streamlit.file_uploader(
        "📸 الصورة الشخصية:",
        type=["png", "jpg", "jpeg"]
    )

    parsed_image = None
    if uploaded_file is not None:
        try:
            parsed_image = Image.open(uploaded_file)
        except Exception:
            io_streamlit.error("فشل قراءة الملف المرفوع.")

    app_mode = "لنفسي"
    custom_footer = ""
    sender_name_val = ""

    if not is_landscape_selected:
        io_streamlit.write("---")
        io_streamlit.markdown("### ✨ تخصيص العبارات والإهداء")

        app_mode = io_streamlit.radio(
            "🎁 نوع الكرت:",
            ["لنفسي", "لصديقي"],
            horizontal=True
        )

        if app_mode == "لنفسي":
            st_footer_toggle = io_streamlit.checkbox("✍️ تفعيل عبارة مخصصة", value=False)
            if st_footer_toggle:
                custom_footer = io_streamlit.text_input(
                    "✍️ اكتب عبارتك المخصصة:",
                    value="حَقَّقْتُ حُلْمِي وَتَوَّتْ مَسِيرَتِي بِالتَّفَوُّقِ"
                )
            else:
                custom_footer = "حَقَّقْتُ حُلْمِي وَتَوَّجْتُ مَسِيرَتِي بِالتَّفَوُّقِ"
        else:
            sender_name_val = io_streamlit.text_input(
                "✍️ اسم الصديق المرسل:",
                placeholder="مثال: صديقك الوفي يعقوب"
            )
            custom_footer = ""

final_story_img = generate_story_v4(
    name=student_name,
    gpa=student_gpa,
    stream=student_stream,
    template_key=selected_template,
    mode=app_mode,
    sender_name=sender_name_val,
    profile_img=parsed_image,
    enable_glow=chk_glow,
    enable_shine=chk_shine,
    enable_gradient=chk_gradient,
    wilaya=selected_wilaya if enable_wilaya else "",
    honor_badge=selected_badge,
    card_ratio=card_ratio_option,
    maquam_option=selected_maquam_opt,
    custom_footer_text=custom_footer,
    monument_opacity=monument_opacity_slider,
    maquam_color_style=maquam_color_opt
)

img_byte_arr = io.BytesIO()
rgb_final_img = final_story_img.convert("RGB")
rgb_final_img.save(img_byte_arr, format='PNG')

io_streamlit.session_state['generated_image_bytes'] = img_byte_arr.getvalue()
io_streamlit.session_state['generated_filename'] = f"NajahStory2026_{student_name.replace(' ', '_')}.png"

if student_name or student_gpa:
    js_confetti_trigger = """
    <script>
        try {
            var parentDoc = window.parent.document;
            if (!window.parent.confetti) {
                var script = parentDoc.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js';
                parentDoc.head.appendChild(script);
                script.onload = function() {
                    fireConfetti();
                };
            } else {
                fireConfetti();
            }

            function fireConfetti() {
                var duration = 4 * 1000;
                var end = Date.now() + duration;

                (function frame() {
                  window.parent.confetti({
                    particleCount: 5,
                    angle: 60,
                    spread: 55,
                    origin: { x: 0, y: 0.8 },
                    colors: ['#006633', '#ffffff', '#d21034', '#ffd700']
                  });
                  window.parent.confetti({
                    particleCount: 5,
                    angle: 120,
                    spread: 55,
                    origin: { x: 1, y: 0.8 },
                    colors: ['#006633', '#ffffff', '#d21034', '#ffd700']
                  });

                  if (Date.now() < end) {
                    requestAnimationFrame(frame);
                  }
                }());
            }
        } catch (e) {
            console.log("Confetti run error: ", e);
        }
    </script>
    """
    io_streamlit.components.v1.html(js_confetti_trigger, height=0, width=0)

with col_view:
    io_streamlit.markdown("### 📱 لوحة المعاينة الحية")

    if io_streamlit.session_state['generated_image_bytes'] is not None:
        io_streamlit.image(
            io_streamlit.session_state['generated_image_bytes'],
            use_container_width=True
        )

        # تم تجميل زر التحميل مظهر التدرج اللوني والتوهج التفاعلي بكسل ببكسل
        io_streamlit.download_button(
            label="📥 تحميل الستوري الخاص بك (PNG بجودة عالية)",
            data=io_streamlit.session_state['generated_image_bytes'],
            file_name=io_streamlit.session_state['generated_filename'],
            mime="image/png",
            use_container_width=True
        )

    dev_avatar_base64 = ""
    local_dev_img_path = "./assets/yaakoub.jpg"
    if os.path.exists(local_dev_img_path):
        try:
            with open(local_dev_img_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                dev_avatar_base64 = f"data:image/jpeg;base64,{encoded_string}"
        except Exception:
            pass

    if not dev_avatar_base64:
        dev_avatar_base64 = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%2310b981'/><text x='50%' y='55%' font-family='sans-serif' font-weight='bold' font-size='24' fill='white' dominant-baseline='middle' text-anchor='middle'>Y</text></svg>"

    io_streamlit.markdown(f"""
        <div class='dev-profile-card-wrapper'>
            <img src='{dev_avatar_base64}' class='dev-avatar' alt='Yaakoub Ali Dif'>
            <div class='dev-name'>
                Yaakoub Ali Dif
                <span class='dev-badge'>💙 Verified</span>
            </div>
            <div class='dev-role'>مطور ومصمم الأداة والموقع الرسمي</div>
            <a href='https://www.instagram.com/akouba.hanma27/' target='_blank' class='instagram-btn'>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" style="vertical-align: middle;">
                    <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334"/>
                </svg>
                صفحة Yaakoub Ali Dif على إنستغرام
            </a>
        </div>
    """, unsafe_allow_html=True)

io_streamlit.write("---")

io_streamlit.markdown("""
    <div class='ad-bottom-wrapper'>
        <div>
            <div class='ad-title-tag'>📢 عرض تمويلي تجريبي • Sponsored Ad</div>
            <div style='font-size: 15px; font-weight:700; color:#ffffff; margin: 6px 0; line-height:1.4;'>🎁 دبلوم هندسة الذكاء الاصطناعي وبايثون للطلبة الجدد 2026</div>
            <div style='font-size: 11px; color:#9ca3af; line-height:1.5;'>باشر رحلتك الجامعية بتعلم مهارات المستقبل. دورات مكثفة وتطبيقية مصممة خصيصاً للناجحين الجدد في البكالوريا مع شهادات دولية معتمدة. سجل الآن مجاناً!</div>
        </div>
        <div style='text-align: center; margin-top: 8px;'>
            <a href='#' style='display:inline-block; background-color:#10b981; color:#ffffff; font-weight:bold; padding:8px 24px; border-radius:30px; text-decoration:none; font-size:12px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);'>سجل واحجز مقعدك فوراً 🔗</a>
        </div>
    </div>
""", unsafe_allow_html=True)

io_streamlit.markdown("---")
io_streamlit.markdown(
    "<p style='text-align: center; color: #4b5563; font-size: 13px;'>Najah Story Template Creator • Website & Tool Developer & Designer | Yaakoub Ali Dif • 2026</p>",
    unsafe_allow_html=True)