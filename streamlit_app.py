import streamlit as st

st.set_page_config(
    page_title="LTV Check | Beter Tarief?",
    page_icon="🏠",
    layout="centered",
)

# ─── Translations ────────────────────────────────────────────────────────────
T = {
    "nl": {
        "title": "🏠 LTV Checker",
        "subtitle": "Kom jij in aanmerking voor een **beter hypotheektarief**?",
        "intro": "Vul jouw gegevens in om te zien of de woningwaarde is gestegen en je in een lagere LTV-klasse valt.",
        "woz_explainer": "📋 <strong>Stap 1 — Zoek eerst jouw WOZ-waarde op</strong><br>Weet je jouw WOZ-waarde niet? Dat is normaal! Ga naar <a href='https://www.wozwaardeloket.nl' target='_blank'><strong>wozwaardeloket.nl</strong></a>, typ jouw adres in en je ziet direct de officiële waarde van jouw woning. Geen account nodig, volledig gratis. Noteer dit bedrag en vul het hieronder in.",
        "woz_label": "🏡 WOZ-waarde (€)",
        "woz_help": "Gratis opzoeken via wozwaardeloket.nl — typ gewoon jouw adres in",
        "bank_label": "🏦 Taxatiewaarde volgens bank (€)",
        "bank_help": "De waarde die jouw bank hanteerde bij het afsluiten van jouw hypotheek",
        "mortgage_label": "💳 Openstaande hypotheekschuld (€)",
        "mortgage_help": "Het huidige resterende saldo van jouw hypotheek",
        "rate_label": "📈 Huidig rentepercentage (%)",
        "rate_help": "Jouw huidige hypotheekrente (bijv. 4.5)",
        "button": "🔍 Bereken mijn LTV",
        "old_situation": "Oude situatie",
        "new_situation": "Nieuwe situatie",
        "tier_header": "📊 LTV-klassen overzicht",
        "tier_you": "← jij",
        "col_ltv": "LTV",
        "col_rate": "Tariefklasse",
        "tier_labels": ["Beste tarief", "Zeer goed tarief", "Goed tarief", "Gemiddeld tarief", "Hoger tarief", "Maximaal tarief"],
        "improved_msg": lambda old, new, val, which: f"✅ Goed nieuws! Je LTV daalde van **{old:.1f}%** → **{new:.1f}%** op basis van de **{which}** (€{val:,.0f}). Je valt nu in een **lagere tariefklasse**!",
        "same_tier_msg": lambda old, new: f"ℹ️ Je LTV daalde van **{old:.1f}%** naar **{new:.1f}%**, maar je blijft in dezelfde tariefklasse.",
        "no_change_msg": lambda new: f"⚠️ Je LTV is **{new:.1f}%** — geen significante verandering ten opzichte van de huidige waarde.",
        "savings_header": "💰 Potentiële besparing",
        "savings_rate_reduction": "Indicatieve renteverlaging",
        "savings_monthly": "Geschatte maandelijkse besparing",
        "savings_yearly": "Geschatte jaarlijkse besparing",
        "savings_note": "* Gebaseerd op een gemiddelde renteverlaging van ~0,25% per LTV-klasse. De werkelijke besparing hangt af van jouw specifieke hypotheekvorm en bank.",
        "steps_header": "📋 Volgende stappen",
        "nhg_warning": "⚠️ **Belangrijk:** LTV-klassen beïnvloeden jouw rente **alleen als jouw hypotheek zónder NHG (Nationale Hypotheek Garantie) is afgesloten.** Heb je een NHG-hypotheek? Dan betaal je al het laagste, gegarandeerde tarief en heeft jouw LTV geen invloed op je rente.",
        "steps_improved": [
            ("1️⃣", "Zoek jouw WOZ-waarde op via WOZ Waardeloket", "De WOZ-waarde is de officiële waarde die de gemeente jaarlijks aan jouw woning toekent. Je kunt deze gratis en zonder inloggen opzoeken op wozwaardeloket.nl — typ gewoon jouw adres in. Je ziet dan de WOZ-waarde van jouw woning voor het huidige jaar. Houd dit bedrag bij de hand voor stap 2. 👉 wozwaardeloket.nl"),
            ("2️⃣", "Vul de WOZ-waarde in bovenaan deze pagina", "Is de WOZ-waarde hoger dan het bedrag dat jouw bank destijds gebruikte? Dan daalt jouw LTV automatisch. Bereken het resultaat opnieuw als je de waarde hebt opgezocht."),
            ("3️⃣", "Neem contact op met jouw hypotheekverstrekker", "Stuur een schriftelijk verzoek (e-mail of brief) om LTV-herziening. Vermeld jouw hypotheeknummer en voeg de WOZ-beschikking of een screenshot van WOZ Waardeloket bij als bewijs."),
            ("4️⃣", "Vraag om aanpassing van jouw rentetarief", "Banken zijn wettelijk verplicht jouw tarief te herzien als jouw LTV-klasse daalt — ook tijdens een lopende rentevaste periode. Geen oversluiting nodig. Gemiddelde doorlooptijd: 4–8 weken."),
        ],
        "steps_no_improvement": "Controleer jaarlijks jouw WOZ-waarde via **wozwaardeloket.nl** — helemaal gratis, geen account nodig. Naarmate jouw woning in waarde stijgt of jouw hypotheekschuld daalt, kun je alsnog in aanmerking komen voor een lagere LTV-klasse.",
        "woz_link": "🔗 WOZ-waarde opzoeken op WOZ Waardeloket",
        "footer": "ℹ️ Deze tool is puur informatief en vervangt geen professioneel hypotheekadvies. LTV-klassen zijn alleen relevant voor hypotheken zónder NHG. Raadpleeg altijd een erkend hypotheekadviseur.",
        "which_woz": "WOZ-waarde",
        "which_bank": "taxatiewaarde bank",
        "per_month": "/ maand",
        "per_year": "/ jaar",
    },
    "en": {
        "title": "🏠 LTV Checker",
        "subtitle": "Are you entitled to a **better mortgage rate**?",
        "intro": "Enter your details to see whether your property value has risen and you now qualify for a lower LTV bracket — and a better rate.",
        "woz_explainer": "📋 <strong>Step 1 — Look up your WOZ value first</strong><br>Not sure what your WOZ value is? That's totally normal! Go to <a href='https://www.wozwaardeloket.nl' target='_blank'><strong>wozwaardeloket.nl</strong></a>, type in your address, and you'll instantly see the official government-assessed value of your home. No account needed, completely free. Note the amount and enter it below.",
        "woz_label": "🏡 WOZ value / Municipal assessment (€)",
        "woz_help": "Look it up free at wozwaardeloket.nl — just type in your address",
        "bank_label": "🏦 Bank valuation (€)",
        "bank_help": "The value your bank used when you originally took out your mortgage",
        "mortgage_label": "💳 Outstanding mortgage balance (€)",
        "mortgage_help": "The current remaining balance on your mortgage",
        "rate_label": "📈 Current interest rate (%)",
        "rate_help": "Your current mortgage interest rate (e.g. 4.5)",
        "button": "🔍 Calculate my LTV",
        "old_situation": "Old situation",
        "new_situation": "New situation",
        "tier_header": "📊 LTV bracket overview",
        "tier_you": "← you",
        "col_ltv": "LTV",
        "col_rate": "Rate tier",
        "tier_labels": ["Best rate", "Very good rate", "Good rate", "Average rate", "Higher rate", "Maximum rate"],
        "improved_msg": lambda old, new, val, which: f"✅ Great news! Your LTV dropped from **{old:.1f}%** → **{new:.1f}%** based on the **{which}** (€{val:,.0f}). You now qualify for a **lower rate bracket**!",
        "same_tier_msg": lambda old, new: f"ℹ️ Your LTV dropped from **{old:.1f}%** to **{new:.1f}%**, but you remain in the same rate bracket.",
        "no_change_msg": lambda new: f"⚠️ Your LTV is **{new:.1f}%** — no significant change compared to the current bank valuation.",
        "savings_header": "💰 Potential savings",
        "savings_rate_reduction": "Indicative rate reduction",
        "savings_monthly": "Estimated monthly saving",
        "savings_yearly": "Estimated annual saving",
        "savings_note": "* Based on an average rate reduction of ~0.25% per LTV bracket. Actual savings depend on your specific mortgage type and lender.",
        "steps_header": "📋 Next steps",
        "nhg_warning": "⚠️ **Important:** LTV brackets only affect your interest rate if your mortgage was taken out **without NHG (Nationale Hypotheek Garantie)**. If you have an NHG mortgage, you already benefit from the lowest guaranteed rate and your LTV does not influence your interest.",
        "steps_improved": [
            ("1️⃣", "Look up your WOZ value at WOZ Waardeloket", "The WOZ value is the official property value that your municipality assigns to your home every year. You can look it up for free — no login required — at wozwaardeloket.nl. Just type in your address and you'll instantly see the current official value. Keep that number handy for the next step. 👉 wozwaardeloket.nl"),
            ("2️⃣", "Enter the WOZ value at the top of this page", "Is the WOZ value higher than the figure your bank used? Then your LTV automatically drops. Recalculate after looking it up to see your updated result."),
            ("3️⃣", "Contact your mortgage lender", "Send a written request (email or letter) for an LTV review. Include your mortgage number and attach the WOZ letter or a screenshot from WOZ Waardeloket as proof."),
            ("4️⃣", "Request a rate adjustment", "Dutch lenders are legally required to revise your rate when your LTV bracket improves — even during a fixed-rate period. No refinancing needed. Typical processing time: 4–8 weeks."),
        ],
        "steps_no_improvement": "Check your WOZ value annually at **wozwaardeloket.nl** — completely free, no account needed. As your property value rises or your mortgage balance decreases, you may still qualify for a lower LTV bracket in future.",
        "woz_link": "🔗 Look up your WOZ value at WOZ Waardeloket",
        "footer": "ℹ️ This tool is for informational purposes only. LTV brackets are only relevant for mortgages without NHG. Always consult a qualified mortgage advisor.",
        "which_woz": "WOZ value",
        "which_bank": "bank valuation",
        "per_month": "/ month",
        "per_year": "/ year",
    }
}

LTV_THRESHOLDS  = [60,    70,              80,           90,               100,           106]
LTV_RANGE_LABELS = ["≤ 60%","≤ 70%","≤ 80%","≤ 90%","≤ 100%","≤ 106%"]

def get_tier_index(ltv: float) -> int:
    for i, t in enumerate(LTV_THRESHOLDS):
        if ltv <= t:
            return i
    return len(LTV_THRESHOLDS) - 1

def get_color(ltv: float) -> str:
    if ltv <= 70: return "good"
    if ltv <= 90: return "neutral"
    return "bad"

# ─── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1,h2,h3 { font-family: 'Playfair Display', serif; }
.stApp { background: linear-gradient(145deg, #f0f4f8 0%, #e3ecf7 100%); }

.result-box {
    background: white;
    border-radius: 20px;
    padding: 2rem 2.25rem;
    box-shadow: 0 6px 32px rgba(0,0,0,0.09);
    margin-top: 1.5rem;
}
.ltv-badge {
    font-size: 2.8rem;
    font-weight: 900;
    font-family: 'Playfair Display', serif;
    line-height: 1.1;
}
.good    { color: #16a34a; }
.neutral { color: #d97706; }
.bad     { color: #dc2626; }

.tier-table { width:100%; border-collapse:collapse; margin-top:0.75rem; border-radius:10px; overflow:hidden; }
.tier-table th { background:#1e3a5f; color:white; padding:10px 14px; text-align:left; font-weight:500; font-size:0.9rem; }
.tier-table td { padding:9px 14px; border-bottom:1px solid #f0f0f0; font-size:0.92rem; }
.tier-table tr.highlight { background:#dcfce7 !important; font-weight:600; }
.tier-table tr:nth-child(even) { background:#f9fafb; }

.savings-box {
    background: linear-gradient(135deg,#ecfdf5,#d1fae5);
    border: 1.5px solid #6ee7b7;
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    margin-top: 1.25rem;
}
.savings-row { display:flex; justify-content:space-between; align-items:center; padding:0.4rem 0; border-bottom:1px solid #a7f3d0; }
.savings-row:last-child { border-bottom:none; font-weight:600; font-size:1.05rem; }
.savings-label { color:#065f46; }
.savings-value { color:#047857; font-weight:600; }

.step-card { background:#eff6ff; border-left:4px solid #3b82f6; border-radius:10px; padding:1rem 1.25rem; margin-bottom:0.75rem; }
.step-title { font-weight:600; font-size:0.97rem; color:#1e3a5f; margin-bottom:0.25rem; }
.step-body  { font-size:0.9rem; color:#374151; line-height:1.5; }

.tip-box { background:#fefce8; border-left:4px solid #eab308; border-radius:10px; padding:1rem 1.25rem; margin-top:1.25rem; font-size:0.92rem; color:#713f12; }
</style>
""", unsafe_allow_html=True)

# ─── Language toggle ──────────────────────────────────────────────────────────
col_hdr, col_lang = st.columns([6, 1])
with col_lang:
    lang = st.selectbox("🌐", ["NL", "EN"], label_visibility="collapsed")

t = T[lang.lower()]

# ─── Header ──────────────────────────────────────────────────────────────────
st.markdown(f"## {t['title']}")
st.markdown(t["subtitle"])
st.markdown(t["intro"])
st.divider()

# ─── WOZ explainer box ───────────────────────────────────────────────────────
st.markdown(f"""
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;border-radius:10px;padding:1rem 1.25rem;margin-bottom:1.25rem;font-size:0.92rem;color:#0c4a6e;">
{t['woz_explainer']}
</div>
""", unsafe_allow_html=True)

# ─── Inputs ──────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    woz_value = st.number_input(t["woz_label"], min_value=50_000, max_value=5_000_000,
                                value=350_000, step=5_000, help=t["woz_help"])
with col2:
    bank_value = st.number_input(t["bank_label"], min_value=50_000, max_value=5_000_000,
                                 value=300_000, step=5_000, help=t["bank_help"])

col3, col4 = st.columns(2)
with col3:
    mortgage_balance = st.number_input(t["mortgage_label"], min_value=0, max_value=5_000_000,
                                       value=220_000, step=1_000, help=t["mortgage_help"])
with col4:
    current_rate = st.number_input(t["rate_label"], min_value=0.1, max_value=15.0,
                                   value=4.5, step=0.05, format="%.2f", help=t["rate_help"])

st.markdown("")

if st.button(t["button"], use_container_width=True, type="primary"):

    best_value  = max(woz_value, bank_value)
    which_value = t["which_woz"] if woz_value >= bank_value else t["which_bank"]

    ltv_old = (mortgage_balance / bank_value) * 100
    ltv_new = (mortgage_balance / best_value) * 100

    old_idx  = get_tier_index(ltv_old)
    new_idx  = get_tier_index(ltv_new)
    improved = new_idx < old_idx

    color_old = get_color(ltv_old)
    color_new = get_color(ltv_new)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    # NHG warning
    st.markdown(t["nhg_warning"])
    st.markdown("")

    # Banner
    if improved:
        st.success(t["improved_msg"](ltv_old, ltv_new, best_value, which_value))
    elif ltv_new < ltv_old:
        st.info(t["same_tier_msg"](ltv_old, ltv_new))
    else:
        st.warning(t["no_change_msg"](ltv_new))

    # Side-by-side LTV
    ca, cb = st.columns(2)
    with ca:
        st.markdown(f"""
        **{t['old_situation']}**<br>
        <span class="ltv-badge {color_old}">{ltv_old:.1f}%</span><br>
        <small>{LTV_RANGE_LABELS[old_idx]} — {t['tier_labels'][old_idx]}</small>
        """, unsafe_allow_html=True)
    with cb:
        st.markdown(f"""
        **{t['new_situation']}**<br>
        <span class="ltv-badge {color_new}">{ltv_new:.1f}%</span><br>
        <small>{LTV_RANGE_LABELS[new_idx]} — {t['tier_labels'][new_idx]}</small>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tier table
    st.markdown(f"**{t['tier_header']}**")
    rows = ""
    for i, (threshold, range_label, tier_label) in enumerate(
            zip(LTV_THRESHOLDS, LTV_RANGE_LABELS, t["tier_labels"])):
        hl     = "highlight" if i == new_idx else ""
        marker = t["tier_you"] if i == new_idx else ""
        rows  += f'<tr class="{hl}"><td>{range_label}</td><td>{tier_label}</td><td>{marker}</td></tr>'

    st.markdown(f"""
    <table class="tier-table">
        <tr><th>{t['col_ltv']}</th><th>{t['col_rate']}</th><th></th></tr>
        {rows}
    </table>
    """, unsafe_allow_html=True)

    # ── Savings estimator ────────────────────────────────────────────────────
    if improved and mortgage_balance > 0:
        brackets_gained  = old_idx - new_idx
        rate_reduction   = brackets_gained * 0.25          # ~0.25% per bracket
        monthly_saving   = (mortgage_balance * (rate_reduction / 100)) / 12
        yearly_saving    = monthly_saving * 12

        st.markdown(f"<br><strong>{t['savings_header']}</strong>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="savings-box">
            <div class="savings-row">
                <span class="savings-label">{t['savings_rate_reduction']}</span>
                <span class="savings-value">~{rate_reduction:.2f}%</span>
            </div>
            <div class="savings-row">
                <span class="savings-label">{t['savings_monthly']}</span>
                <span class="savings-value">€ {monthly_saving:,.0f} {t['per_month']}</span>
            </div>
            <div class="savings-row">
                <span class="savings-label">{t['savings_yearly']}</span>
                <span class="savings-value">€ {yearly_saving:,.0f} {t['per_year']}</span>
            </div>
        </div>
        <p style="font-size:0.78rem;color:#6b7280;margin-top:0.5rem;">{t['savings_note']}</p>
        """, unsafe_allow_html=True)

    # ── Next steps ───────────────────────────────────────────────────────────
    st.markdown(f"<br><strong>{t['steps_header']}</strong>", unsafe_allow_html=True)
    if improved:
        for icon, title, body in t["steps_improved"]:
            st.markdown(f"""
            <div class="step-card">
                <div class="step-title">{icon} {title}</div>
                <div class="step-body">{body}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="tip-box">💡 {t['steps_no_improvement']}</div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─── WOZ link & footer ───────────────────────────────────────────────────────
st.markdown("")
st.markdown(f"[{t['woz_link']}](https://www.wozwaardeloket.nl)")
st.divider()
st.caption(t["footer"])
