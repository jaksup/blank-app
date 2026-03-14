import streamlit as st

st.set_page_config(
    page_title="Betaal jij te veel hypotheekrente?",
    page_icon="🏠",
    layout="centered",
)

# ─── Translations ────────────────────────────────────────────────────────────
T = {
    "nl": {
        "title": "Betaal jij te veel hypotheekrente?",
        "subtitle": "Als jouw woning meer waard is geworden, heb je mogelijk recht op een **lagere rente** — zonder over te sluiten.",
        "intro": "Vul hieronder drie dingen in. We rekenen het voor je uit.",
        "woz_explainer": "🏡 <strong>Eerst: zoek jouw WOZ-waarde op</strong> &nbsp;·&nbsp; <a href='https://www.wozwaardeloket.nl' target='_blank' style='color:#60a5fa;'>wozwaardeloket.nl →</a><br><span style='opacity:0.8;'>De WOZ-waarde is de officiële woningwaarde die de gemeente elk jaar vaststelt. Typ jouw adres in op wozwaardeloket.nl — geen account nodig, gratis, duurt 30 seconden. Noteer het bedrag en vul het hieronder in.</span>",
        "woz_label": "WOZ-waarde (€)",
        "woz_help": "Zoek het op via wozwaardeloket.nl — typ jouw adres in, klaar",
        "bank_label": "Waarde die jouw bank gebruikte (€)",
        "bank_help": "Dit staat in jouw hypotheekofferte of welkomstbrief van de bank. Het is het bedrag waartegen jouw hypotheek oorspronkelijk werd berekend.",
        "mortgage_label": "Wat je nog aan hypotheek hebt openstaan (€)",
        "mortgage_help": "Kijk op de website van jouw bank of in de jaarlijkse opgave. Het gaat om wat je nu nog moet terugbetalen.",
        "rate_label": "Jouw huidige rente (%)",
        "rate_help": "Je vindt dit op jouw bankafschrift of in Mijn Omgeving van jouw hypotheekverstrekker",
        "button": "Bereken of ik in aanmerking kom",
        "old_situation": "Situatie toen",
        "new_situation": "Situatie nu",
        "tier_header": "Hoe werkt het met die klassen?",
        "tier_you": "← jij nu",
        "col_ltv": "Woningwaarde vs. schuld",
        "col_rate": "Wat dat betekent",
        "tier_labels": ["Laagste rente mogelijk", "Zeer lage rente", "Lage rente", "Gemiddelde rente", "Hogere rente", "Hoogste rente"],
        "improved_msg": lambda old, new, val, which: f"Goed nieuws — je valt in een betere categorie! Je schuld is nu {new:.1f}% van de woningwaarde (was {old:.1f}%). Op basis van de {which} van €{val:,.0f} heb je mogelijk recht op een lagere rente.",
        "same_tier_msg": lambda old, new: f"Je verhouding is gedaald van {old:.1f}% naar {new:.1f}% — maar je valt nog net in dezelfde categorie. Controleer volgend jaar opnieuw.",
        "no_change_msg": lambda new: f"Op dit moment valt je nog in dezelfde categorie ({new:.1f}%). Is jouw woning de afgelopen jaren in waarde gestegen? Controleer de actuele WOZ-waarde op wozwaardeloket.nl.",
        "savings_header": "Wat kan je dit opleveren?",
        "savings_rate_reduction": "Geschatte renteverlaging",
        "savings_monthly": "Minder betalen per maand",
        "savings_yearly": "Minder betalen per jaar",
        "savings_note": "Indicatieve berekening op basis van ~0,25% renteverlaging per categorie. Je werkelijke voordeel hangt af van jouw bank en hypotheekvorm.",
        "steps_header": "Wat kun je nu doen?",
        "nhg_warning": "💡 **Heb je een hypotheek met NHG?** Dan geldt dit niet voor jou — bij NHG betaal je al het laagste tarief, ongeacht de woningwaarde. Twijfel je? Check het in jouw hypotheekpapieren of bel jouw bank.",
        "steps_improved": [
            ("Stap 1", "Zoek jouw WOZ-waarde op", "Ga naar <a href='https://www.wozwaardeloket.nl' target='_blank' style='color:#3b82f6;'>wozwaardeloket.nl</a>, typ jouw adres in en noteer de waarde. Geen account nodig, kost 30 seconden."),
            ("Stap 2", "Stuur een berichtje naar jouw bank", "Neem contact op via de app, e-mail of telefoon. Zeg dat je een LTV-herziening wilt aanvragen en stuur een screenshot van WOZ Waardeloket mee als bewijs. Je hoeft geen advocaat in te schakelen — een gewone mail is genoeg."),
            ("Stap 3", "De bank past jouw rente aan", "Banken zijn wettelijk verplicht dit te doen als je in een lagere categorie valt — ook als je nog midden in een rentevaste periode zit. Gemiddeld duurt het 4 tot 8 weken."),
            ("Stap 4", "Geen oversluiting, geen kosten", "Je sluit geen nieuwe hypotheek af. Er zijn geen notariskosten. Het is gewoon een aanpassing van jouw bestaande rente."),
        ],
        "steps_no_improvement": "Woningen zijn de afgelopen jaren flink in waarde gestegen. Controleer jaarlijks jouw WOZ-waarde op <a href='https://www.wozwaardeloket.nl' target='_blank' style='color:#3b82f6;'>wozwaardeloket.nl</a> — het kost 30 seconden en is gratis. Zodra je in een lagere categorie valt, kun je direct actie ondernemen.",
        "woz_link": "WOZ-waarde opzoeken → wozwaardeloket.nl",
        "footer": "Deze tool geeft een indicatie en vervangt geen hypotheekadvies. Het voordeel van een lagere rente geldt alleen voor hypotheken zónder NHG.",
        "which_woz": "WOZ-waarde",
        "which_bank": "bankwaarde",
        "per_month": "per maand",
        "per_year": "per jaar",
    },
    "en": {
        "title": "Are you overpaying on your mortgage?",
        "subtitle": "If your home has gone up in value, you may be entitled to a **lower interest rate** — no refinancing needed.",
        "intro": "Fill in three things below. We'll do the math.",
        "woz_explainer": "🏡 <strong>First: look up your WOZ value</strong> &nbsp;·&nbsp; <a href='https://www.wozwaardeloket.nl' target='_blank' style='color:#60a5fa;'>wozwaardeloket.nl →</a><br><span style='opacity:0.8;'>The WOZ value is the official property value set by your municipality each year. Go to wozwaardeloket.nl, type in your address — no account needed, free, takes 30 seconds. Note the amount and enter it below.</span>",
        "woz_label": "WOZ value (€)",
        "woz_help": "Look it up at wozwaardeloket.nl — type your address, done",
        "bank_label": "Value your bank used (€)",
        "bank_help": "This is in your original mortgage offer or welcome letter from the bank — the figure they used to calculate your mortgage.",
        "mortgage_label": "How much mortgage you still owe (€)",
        "mortgage_help": "Check your bank's app or your annual mortgage statement. It's what you still need to pay back.",
        "rate_label": "Your current interest rate (%)",
        "rate_help": "You'll find this on your bank statement or in your mortgage portal",
        "button": "Check if I qualify",
        "old_situation": "Back then",
        "new_situation": "Right now",
        "tier_header": "How do the brackets work?",
        "tier_you": "← you now",
        "col_ltv": "Home value vs. debt",
        "col_rate": "What that means",
        "tier_labels": ["Lowest rate possible", "Very low rate", "Low rate", "Average rate", "Higher rate", "Highest rate"],
        "improved_msg": lambda old, new, val, which: f"Good news — you've moved to a better bracket! Your debt is now {new:.1f}% of your home's value (was {old:.1f}%). Based on a {which} of €{val:,.0f}, you may be entitled to a lower rate.",
        "same_tier_msg": lambda old, new: f"Your ratio dropped from {old:.1f}% to {new:.1f}% — but you're still just within the same bracket. Check again next year.",
        "no_change_msg": lambda new: f"You're currently in the same bracket ({new:.1f}%). Has your home gone up in value recently? Check the latest WOZ value at wozwaardeloket.nl.",
        "savings_header": "What could this save you?",
        "savings_rate_reduction": "Estimated rate reduction",
        "savings_monthly": "Less to pay each month",
        "savings_yearly": "Less to pay each year",
        "savings_note": "Indicative estimate based on ~0.25% rate reduction per bracket. Your actual saving depends on your lender and mortgage type.",
        "steps_header": "What can you do now?",
        "nhg_warning": "💡 **Do you have an NHG mortgage?** Then this doesn't apply to you — with NHG you already pay the lowest rate regardless of your home's value. Not sure? Check your mortgage paperwork or call your bank.",
        "steps_improved": [
            ("Step 1", "Look up your WOZ value", "Go to <a href='https://www.wozwaardeloket.nl' target='_blank' style='color:#3b82f6;'>wozwaardeloket.nl</a>, type in your address and note the value. No account needed, takes 30 seconds."),
            ("Step 2", "Send a quick message to your bank", "Contact them via their app, email or phone. Tell them you'd like to request an LTV review and attach a screenshot from WOZ Waardeloket as proof. You don't need a lawyer — a simple email is enough."),
            ("Step 3", "Your bank adjusts your rate", "Dutch banks are legally required to do this when you move to a lower bracket — even if you're in the middle of a fixed-rate period. It typically takes 4 to 8 weeks."),
            ("Step 4", "No refinancing, no fees", "You're not taking out a new mortgage. No notary costs. It's simply an adjustment to your existing rate."),
        ],
        "steps_no_improvement": "Home values in the Netherlands have risen significantly in recent years. Check your WOZ value annually at <a href='https://www.wozwaardeloket.nl' target='_blank' style='color:#3b82f6;'>wozwaardeloket.nl</a> — it's free and takes 30 seconds. Once you drop into a lower bracket, you can act right away.",
        "woz_link": "Look up your WOZ value → wozwaardeloket.nl",
        "footer": "This tool gives an indication and is not mortgage advice. The rate benefit only applies to mortgages without NHG.",
        "which_woz": "WOZ value",
        "which_bank": "bank valuation",
        "per_month": "per month",
        "per_year": "per year",
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #e2e8f0;
}

/* Dark background for entire app */
.stApp {
    background-color: #0f1117;
}

/* Hide default streamlit header padding */
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 680px;
}

/* Main title */
h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

/* All text defaults */
p, label, span, div {
    color: #cbd5e1;
}

/* Input fields */
.stNumberInput input {
    background-color: #1e2130 !important;
    border: 1px solid #2d3548 !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
    font-size: 1rem !important;
    padding: 0.6rem 0.75rem !important;
}
.stNumberInput input:focus {
    border-color: #4f8ef7 !important;
    box-shadow: 0 0 0 2px rgba(79,142,247,0.2) !important;
}

/* Input labels */
.stNumberInput label {
    color: #94a3b8 !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}

/* Selectbox (language toggle) */
.stSelectbox > div > div {
    background-color: #1e2130 !important;
    border: 1px solid #2d3548 !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: #4f8ef7 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: 0.75rem 1.5rem !important;
    letter-spacing: -0.01em;
    transition: background 0.15s;
}
.stButton > button[kind="primary"]:hover {
    background: #3b7de8 !important;
}

/* Divider */
hr { border-color: #1e2130 !important; }

/* Caption / footer */
.stCaption { color: #475569 !important; font-size: 0.78rem !important; }

/* Result card */
.result-card {
    background: #1a1f2e;
    border: 1px solid #2d3548;
    border-radius: 16px;
    padding: 2rem 2.25rem;
    margin-top: 1.5rem;
}

/* LTV big number */
.ltv-number {
    font-size: 3.2rem;
    font-weight: 700;
    letter-spacing: -0.04em;
    line-height: 1;
}
.good    { color: #34d399; }
.neutral { color: #fbbf24; }
.bad     { color: #f87171; }

.ltv-label {
    font-size: 0.82rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
    font-weight: 500;
}
.ltv-sublabel {
    font-size: 0.88rem;
    color: #64748b;
    margin-top: 4px;
}

/* Result banner */
.banner-good    { background:#052e16; border:1px solid #166534; border-radius:10px; padding:1rem 1.25rem; color:#86efac; font-size:0.95rem; margin-bottom:1.25rem; }
.banner-info    { background:#0c1a2e; border:1px solid #1e40af; border-radius:10px; padding:1rem 1.25rem; color:#93c5fd; font-size:0.95rem; margin-bottom:1.25rem; }
.banner-warn    { background:#1c1400; border:1px solid #854d0e; border-radius:10px; padding:1rem 1.25rem; color:#fde68a; font-size:0.95rem; margin-bottom:1.25rem; }
.banner-nhg     { background:#1a1a2e; border:1px solid #4338ca; border-radius:10px; padding:0.9rem 1.25rem; color:#a5b4fc; font-size:0.88rem; margin-bottom:1.25rem; }

/* Section label inside card */
.section-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #475569;
    font-weight: 600;
    margin: 1.5rem 0 0.75rem;
}

/* Tier table */
.tier-table { width:100%; border-collapse:collapse; margin-top:0.5rem; }
.tier-table th {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #475569;
    font-weight: 600;
    padding: 0 0.75rem 0.5rem;
    text-align: left;
    border-bottom: 1px solid #2d3548;
}
.tier-table td { padding:0.6rem 0.75rem; border-bottom:1px solid #1e2535; font-size:0.9rem; color:#94a3b8; }
.tier-table tr.hl td { background:#0d2818; color:#86efac; font-weight:600; }
.tier-table tr.hl td:first-child { border-left: 3px solid #34d399; }

/* Savings */
.savings-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    margin-top: 0.5rem;
}
.savings-cell {
    background: #0d2818;
    border: 1px solid #166534;
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
}
.savings-cell .val { font-size:1.4rem; font-weight:700; color:#34d399; letter-spacing:-0.02em; }
.savings-cell .lbl { font-size:0.72rem; color:#4ade80; margin-top:4px; text-transform:uppercase; letter-spacing:0.05em; }

/* Step cards */
.step-card {
    background: #1a1f2e;
    border: 1px solid #2d3548;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.6rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
}
.step-num {
    background: #2d3548;
    color: #94a3b8;
    border-radius: 6px;
    padding: 2px 8px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    white-space: nowrap;
    margin-top: 2px;
    text-transform: uppercase;
}
.step-title { font-weight: 600; font-size: 0.92rem; color: #e2e8f0; margin-bottom: 3px; }
.step-body  { font-size: 0.86rem; color: #64748b; line-height: 1.55; }
.step-body a { color: #4f8ef7; text-decoration: none; }

/* WOZ explainer */
.woz-box {
    background: #131926;
    border: 1px solid #2d3548;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
    line-height: 1.6;
    color: #94a3b8;
}
.woz-box a { color: #60a5fa; text-decoration: none; }
.woz-box strong { color: #e2e8f0; }

/* Savings note */
.savings-note { font-size:0.75rem; color:#334155; margin-top:0.6rem; }

/* Bottom WOZ link */
.woz-footer-link a { color: #4f8ef7 !important; font-size:0.88rem; text-decoration:none; }
</style>
""", unsafe_allow_html=True)

# ─── Language toggle ──────────────────────────────────────────────────────────
col_hdr, col_lang = st.columns([6, 1])
with col_lang:
    lang = st.selectbox("🌐", ["NL", "EN"], label_visibility="collapsed")

t = T[lang.lower()]

# ─── Header ──────────────────────────────────────────────────────────────────
st.markdown(f"## {t['title']}")
st.markdown(f"<p style='color:#64748b;font-size:1.05rem;margin-top:-0.5rem;'>{t['subtitle'].replace('**','<strong>').replace('**','</strong>')}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:#475569;font-size:0.9rem;'>{t['intro']}</p>", unsafe_allow_html=True)
st.divider()

# ─── WOZ explainer box ───────────────────────────────────────────────────────
st.markdown(f'<div class="woz-box">{t["woz_explainer"]}</div>', unsafe_allow_html=True)

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

    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    # NHG warning
    st.markdown(f'<div class="banner-nhg">{t["nhg_warning"]}</div>', unsafe_allow_html=True)

    # Banner
    if improved:
        st.markdown(f'<div class="banner-good">{t["improved_msg"](ltv_old, ltv_new, best_value, which_value)}</div>', unsafe_allow_html=True)
    elif ltv_new < ltv_old:
        st.markdown(f'<div class="banner-info">{t["same_tier_msg"](ltv_old, ltv_new)}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="banner-warn">{t["no_change_msg"](ltv_new)}</div>', unsafe_allow_html=True)

    # Side-by-side LTV numbers
    ca, cb = st.columns(2)
    with ca:
        st.markdown(f"""
        <div class="ltv-label">{t['old_situation']}</div>
        <div class="ltv-number {color_old}">{ltv_old:.1f}%</div>
        <div class="ltv-sublabel">{LTV_RANGE_LABELS[old_idx]} · {t['tier_labels'][old_idx]}</div>
        """, unsafe_allow_html=True)
    with cb:
        st.markdown(f"""
        <div class="ltv-label">{t['new_situation']}</div>
        <div class="ltv-number {color_new}">{ltv_new:.1f}%</div>
        <div class="ltv-sublabel">{LTV_RANGE_LABELS[new_idx]} · {t['tier_labels'][new_idx]}</div>
        """, unsafe_allow_html=True)

    # Tier table
    st.markdown(f'<div class="section-label">{t["tier_header"]}</div>', unsafe_allow_html=True)
    rows = ""
    for i, (threshold, range_label, tier_label) in enumerate(
            zip(LTV_THRESHOLDS, LTV_RANGE_LABELS, t["tier_labels"])):
        hl     = "hl" if i == new_idx else ""
        marker = t["tier_you"] if i == new_idx else ""
        rows  += f'<tr class="{hl}"><td>{range_label}</td><td>{tier_label}</td><td style="color:#34d399;font-size:0.8rem;">{marker}</td></tr>'

    st.markdown(f"""
    <table class="tier-table">
        <tr><th>{t['col_ltv']}</th><th>{t['col_rate']}</th><th></th></tr>
        {rows}
    </table>
    """, unsafe_allow_html=True)

    # ── Savings estimator ────────────────────────────────────────────────────
    if improved and mortgage_balance > 0:
        brackets_gained  = old_idx - new_idx
        rate_reduction   = brackets_gained * 0.25
        monthly_saving   = (mortgage_balance * (rate_reduction / 100)) / 12
        yearly_saving    = monthly_saving * 12

        st.markdown(f'<div class="section-label">{t["savings_header"]}</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="savings-grid">
            <div class="savings-cell">
                <div class="val">~{rate_reduction:.2f}%</div>
                <div class="lbl">{t['savings_rate_reduction']}</div>
            </div>
            <div class="savings-cell">
                <div class="val">€{monthly_saving:,.0f}</div>
                <div class="lbl">{t['savings_monthly']}</div>
            </div>
            <div class="savings-cell">
                <div class="val">€{yearly_saving:,.0f}</div>
                <div class="lbl">{t['savings_yearly']}</div>
            </div>
        </div>
        <div class="savings-note">{t['savings_note']}</div>
        """, unsafe_allow_html=True)

    # ── Next steps ───────────────────────────────────────────────────────────
    st.markdown(f'<div class="section-label">{t["steps_header"]}</div>', unsafe_allow_html=True)
    if improved:
        for step_num, title, body in t["steps_improved"]:
            st.markdown(f"""
            <div class="step-card">
                <div><span class="step-num">{step_num}</span></div>
                <div>
                    <div class="step-title">{title}</div>
                    <div class="step-body">{body}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="step-card">
            <div class="step-body">{t['steps_no_improvement']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─── WOZ link & footer ───────────────────────────────────────────────────────
st.markdown("")
st.markdown(f'<div class="woz-footer-link"><a href="https://www.wozwaardeloket.nl" target="_blank">{t["woz_link"]}</a></div>', unsafe_allow_html=True)
st.divider()
st.caption(t["footer"])
