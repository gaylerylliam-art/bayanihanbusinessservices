import streamlit as st

st.set_page_config(
    page_title="Bayanihan Emirates Business Services",
    page_icon="🇦🇪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding: 0 !important; max-width: 100% !important; }
        [data-testid="stAppViewContainer"] { padding: 0 !important; }
    </style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Bayanihan Emirates Business Services – Start Your Dubai Business</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
  :root {
    --sky: #e8f4fd;
    --sky2: #c9e8f7;
    --blue: #1a6fad;
    --blue2: #0e4d8a;
    --gold: #f0a500;
    --gold2: #e08c00;
    --white: #ffffff;
    --text: #1a2340;
    --muted: #5a6a8a;
    --card-bg: rgba(255,255,255,0.85);
    --radius: 18px;
    --shadow: 0 8px 32px rgba(14,77,138,0.10);
    --shadow-lg: 0 16px 48px rgba(14,77,138,0.16);
  }
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
  html{scroll-behavior:smooth;}
  body{font-family:'Poppins',sans-serif;background:linear-gradient(160deg,#e8f4fd 0%,#f7fbff 40%,#ffffff 100%);color:var(--text);overflow-x:hidden;}

  /* ── STICKY NAV ── */
  .nav{
    position: sticky; top: 0; z-index: 200;
    background: rgba(255,255,255,0.96);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-bottom: 1px solid rgba(26,111,173,0.09);
    padding: 0 5%;
    transition: box-shadow 0.3s ease, padding 0.3s ease, background 0.3s ease;
  }
  .nav.scrolled{
    box-shadow: 0 4px 28px rgba(14,77,138,0.11);
    background: rgba(255,255,255,0.99);
  }
  .nav-inner{
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 76px;
    max-width: 1200px;
    margin: 0 auto;
    gap: 24px;
    transition: height 0.3s ease;
  }
  .nav.scrolled .nav-inner{ height: 64px; }

  /* Logo */
  .nav-logo-wrap{
    flex-shrink: 0;
    display: flex;
    align-items: center;
  }
  .nav-logo{
    height: 58px;
    width: auto;
    object-fit: contain;
    transition: height 0.3s ease, opacity 0.2s ease;
    display: block;
  }
  .nav.scrolled .nav-logo{ height: 48px; }

  /* Center nav links */
  .nav-links-wrap{
    flex: 1;
    display: flex;
    justify-content: center;
  }
  .nav-links{
    display: flex;
    gap: 6px;
    list-style: none;
    align-items: center;
    margin: 0; padding: 0;
  }
  .nav-links a{
    text-decoration: none;
    color: var(--text);
    font-size: 0.875rem;
    font-weight: 500;
    padding: 8px 14px;
    border-radius: 8px;
    position: relative;
    transition: color 0.22s ease, background 0.22s ease;
    white-space: nowrap;
    letter-spacing: 0.1px;
  }
  .nav-links a::after{
    content: '';
    position: absolute;
    bottom: 4px; left: 14px; right: 14px;
    height: 2px;
    background: var(--blue);
    border-radius: 2px;
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.25s ease;
  }
  .nav-links a:hover{ color: var(--blue); background: rgba(26,111,173,0.06); }
  .nav-links a:hover::after{ transform: scaleX(1); }
  .nav-links a.active{ color: var(--blue); font-weight: 600; }
  .nav-links a.active::after{ transform: scaleX(1); }

  /* Right CTA */
  .nav-right{
    flex-shrink: 0;
    display: flex;
    align-items: center;
  }
  .nav-cta{
    background: linear-gradient(135deg, var(--blue), var(--blue2));
    color: #fff;
    border: none;
    padding: 11px 22px;
    border-radius: 50px;
    font-size: 0.875rem;
    font-weight: 700;
    cursor: pointer;
    transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
    text-decoration: none;
    white-space: nowrap;
    letter-spacing: 0.2px;
    display: inline-flex;
    align-items: center;
    gap: 7px;
  }
  .nav-cta::before{ content: '💬'; font-size: 0.9rem; }
  .nav-cta:hover{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(14,77,138,0.35);
    background: linear-gradient(135deg, #1d7dc5, var(--blue2));
  }

  /* Hamburger */
  .hamburger{ display: none; flex-direction: column; gap: 5px; cursor: pointer; padding: 6px; border-radius: 8px; transition: background 0.2s; }
  .hamburger:hover{ background: rgba(26,111,173,0.07); }
  .hamburger span{ display: block; width: 22px; height: 2px; background: var(--blue); border-radius: 2px; transition: transform 0.3s ease, opacity 0.3s ease; }
  .hamburger.open span:nth-child(1){ transform: translateY(7px) rotate(45deg); }
  .hamburger.open span:nth-child(2){ opacity: 0; }
  .hamburger.open span:nth-child(3){ transform: translateY(-7px) rotate(-45deg); }

  /* Mobile slide-down menu */
  .nav-mobile-menu{
    display: none;
    flex-direction: column;
    gap: 4px;
    background: rgba(255,255,255,0.99);
    border-top: 1px solid rgba(26,111,173,0.08);
    padding: 16px 5% 20px;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.38s ease, padding 0.3s ease;
  }
  .nav-mobile-menu.open{ max-height: 400px; }
  .nav-mobile-menu a{
    text-decoration: none;
    color: var(--text);
    font-size: 0.95rem;
    font-weight: 500;
    padding: 12px 16px;
    border-radius: 10px;
    transition: background 0.2s, color 0.2s;
    display: block;
  }
  .nav-mobile-menu a:hover{ background: rgba(26,111,173,0.06); color: var(--blue); }
  .nav-mobile-cta{
    background: linear-gradient(135deg, var(--blue), var(--blue2));
    color: #fff !important;
    font-weight: 700 !important;
    border-radius: 50px !important;
    text-align: center;
    margin-top: 8px;
  }
  .nav-mobile-cta:hover{ background: linear-gradient(135deg,#1d7dc5,var(--blue2)); opacity: 0.95; }

  /* ── HERO ── */
  .hero{position:relative;overflow:hidden;padding:90px 5% 70px;min-height:92vh;display:flex;align-items:center;}
  .hero-bg{position:absolute;inset:0;background:linear-gradient(145deg,#c8e8f8 0%,#dff2ff 30%,#eef7ff 60%,#f9fbfe 100%);z-index:0;}
  .hero-radial{position:absolute;top:-10%;left:-5%;width:70%;height:80%;background:radial-gradient(ellipse at 30% 40%, rgba(26,111,173,0.10) 0%, rgba(26,111,173,0.04) 45%, transparent 70%);z-index:1;pointer-events:none;}
  .hero-radial2{position:absolute;top:10%;right:-8%;width:50%;height:60%;background:radial-gradient(ellipse at 70% 30%, rgba(240,165,0,0.07) 0%, transparent 65%);z-index:1;pointer-events:none;}
  /* Floating decorative blobs */
  .hero-blob{position:absolute;border-radius:50%;filter:blur(48px);pointer-events:none;z-index:1;}
  .hero-blob-1{width:340px;height:340px;top:-60px;right:10%;background:rgba(26,111,173,0.09);}
  .hero-blob-2{width:220px;height:220px;bottom:15%;left:5%;background:rgba(240,165,0,0.07);}
  .hero-blob-3{width:180px;height:180px;top:30%;right:28%;background:rgba(100,190,255,0.10);}
  /* Floating geometric shapes */
  .hero-shapes{position:absolute;inset:0;z-index:1;pointer-events:none;overflow:hidden;}
  .hshape{position:absolute;border-radius:50%;opacity:0;}
  .hshape-1{width:14px;height:14px;border:2.5px solid rgba(26,111,173,0.3);top:18%;left:8%;}
  .hshape-2{width:22px;height:22px;background:rgba(240,165,0,0.18);top:60%;left:12%;border-radius:4px;transform:rotate(22deg);}
  .hshape-3{width:10px;height:10px;background:rgba(26,111,173,0.2);top:25%;right:22%;border-radius:50%;}
  .hshape-4{width:18px;height:18px;border:2px solid rgba(240,165,0,0.25);top:70%;right:15%;border-radius:4px;transform:rotate(-15deg);}
  .hshape-5{width:8px;height:8px;background:rgba(14,77,138,0.18);top:45%;left:20%;}
  .hshape-6{width:28px;height:28px;border:2px solid rgba(26,111,173,0.12);bottom:25%;right:8%;border-radius:50%;}
  /* Enhanced skyline with fade */
  .hero-skyline{position:absolute;bottom:0;left:0;right:0;height:300px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 300'%3E%3Cdefs%3E%3ClinearGradient id='sg' x1='0' x2='0' y1='0' y2='1'%3E%3Cstop offset='0' stop-color='%2393c8e8' stop-opacity='0.18'/%3E%3Cstop offset='1' stop-color='%2393c8e8' stop-opacity='0.45'/%3E%3C/linearGradient%3E%3ClinearGradient id='sg2' x1='0' x2='0' y1='0' y2='1'%3E%3Cstop offset='0' stop-color='%23aad4ed' stop-opacity='0.25'/%3E%3Cstop offset='1' stop-color='%23aad4ed' stop-opacity='0.55'/%3E%3C/linearGradient%3E%3C/defs%3E%3Cpath fill='url(%23sg)' d='M0,300 L0,210 L60,210 L60,150 L80,150 L80,100 L100,100 L100,75 L110,75 L110,50 L125,50 L125,25 L140,25 L140,50 L155,50 L155,75 L170,75 L170,100 L190,100 L190,150 L210,150 L210,170 L240,170 L240,120 L260,120 L260,85 L275,85 L275,60 L285,60 L285,38 L295,38 L295,15 L305,15 L305,38 L315,38 L315,60 L325,60 L325,85 L340,85 L340,120 L360,120 L360,170 L400,170 L400,130 L430,130 L430,105 L450,105 L450,78 L470,78 L470,52 L490,52 L490,28 L508,28 L508,12 L516,12 L516,6 L524,6 L524,12 L532,12 L532,28 L552,28 L552,52 L572,52 L572,78 L590,78 L590,105 L612,105 L612,130 L645,130 L645,155 L685,155 L685,118 L718,118 L718,85 L738,85 L738,60 L758,60 L758,36 L768,36 L768,18 L778,18 L778,6 L788,6 L788,18 L798,18 L798,36 L810,36 L810,60 L830,60 L830,85 L852,85 L852,118 L882,118 L882,155 L932,155 L932,130 L972,130 L972,98 L1002,98 L1002,72 L1022,72 L1022,48 L1045,48 L1045,25 L1065,25 L1065,48 L1085,48 L1085,72 L1108,72 L1108,98 L1140,98 L1140,130 L1182,130 L1182,158 L1222,158 L1222,138 L1252,138 L1252,115 L1272,115 L1272,92 L1295,92 L1295,70 L1315,70 L1315,92 L1338,92 L1338,115 L1365,115 L1365,145 L1400,145 L1400,185 L1440,185 L1440,300 Z'/%3E%3Cpath fill='url(%23sg2)' d='M0,300 L0,235 L120,235 L120,200 L155,200 L155,178 L175,178 L175,165 L188,165 L188,152 L200,152 L200,138 L212,138 L212,125 L228,125 L228,112 L242,112 L242,125 L265,125 L265,150 L305,150 L305,165 L345,165 L345,148 L378,148 L378,130 L408,130 L408,112 L438,112 L438,92 L462,92 L462,75 L480,75 L480,60 L498,60 L498,75 L516,75 L516,92 L542,92 L542,112 L568,112 L568,130 L598,130 L598,148 L635,148 L635,165 L680,165 L680,148 L720,148 L720,128 L752,128 L752,108 L782,108 L782,128 L815,128 L815,148 L862,148 L862,165 L918,165 L918,155 L962,155 L962,140 L1002,140 L1002,122 L1042,122 L1042,140 L1082,140 L1082,155 L1135,155 L1135,165 L1185,165 L1185,155 L1225,155 L1225,142 L1258,142 L1258,165 L1302,165 L1302,188 L1440,188 L1440,300 Z'/%3E%3C/svg%3E") bottom/cover no-repeat;z-index:1;mask-image:linear-gradient(to top,rgba(0,0,0,1) 0%,rgba(0,0,0,0.7) 55%,transparent 100%);-webkit-mask-image:linear-gradient(to top,rgba(0,0,0,1) 0%,rgba(0,0,0,0.7) 55%,transparent 100%);}
  .hero-inner{position:relative;z-index:2;display:grid;grid-template-columns:1fr 420px;gap:60px;align-items:center;max-width:1200px;margin:0 auto;width:100%;}
  .hero-left{}
  .hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(240,165,0,0.12);border:1px solid rgba(240,165,0,0.35);padding:6px 16px;border-radius:50px;font-size:0.78rem;font-weight:600;color:#c07a00;margin-bottom:22px;letter-spacing:.5px;}
  .hero-badge::before{content:"🇦🇪";font-size:1rem;}
  /* Headline glow highlight on span */
  .hero-h1{font-size:clamp(2rem,4vw,3.1rem);font-weight:800;line-height:1.17;color:var(--text);margin-bottom:16px;position:relative;}
  .hero-h1 span{color:var(--blue);position:relative;display:inline;}
  .hero-h1 span::after{content:'';position:absolute;left:-4px;right:-4px;bottom:-2px;top:-2px;background:linear-gradient(135deg,rgba(26,111,173,0.10),rgba(100,190,255,0.12));border-radius:8px;z-index:-1;filter:blur(4px);}
  .hero-sub{font-size:1.08rem;color:var(--muted);font-weight:400;margin-bottom:22px;line-height:1.65;}
  .hero-tagline{background:linear-gradient(135deg,#fff7e6,#fff3d4);border-left:4px solid var(--gold);padding:16px 22px;border-radius:0 12px 12px 0;margin-top:22px;margin-bottom:30px;font-size:1.05rem;font-style:italic;color:#7a4800;font-weight:600;line-height:1.6;}
  .hero-btns{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:18px;}
  /* ── URGENCY BAR ── */
  .urgency-bar{display:flex;align-items:center;gap:14px;flex-wrap:wrap;background:linear-gradient(135deg,rgba(255,243,205,0.95),rgba(255,236,170,0.95));border:1.5px solid rgba(240,165,0,0.45);border-radius:14px;padding:14px 18px;margin-bottom:22px;position:relative;overflow:hidden;}
  .urgency-bar::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.35),transparent);animation:shimmer-urgency 2.8s infinite;transform:translateX(-100%);}
  @keyframes shimmer-urgency{to{transform:translateX(200%);}}
  .urgency-pulse{width:10px;height:10px;min-width:10px;border-radius:50%;background:#e08c00;box-shadow:0 0 0 0 rgba(224,140,0,0.6);animation:urgency-ping 1.4s infinite;}
  @keyframes urgency-ping{0%{box-shadow:0 0 0 0 rgba(224,140,0,0.6);}70%{box-shadow:0 0 0 8px rgba(224,140,0,0);}100%{box-shadow:0 0 0 0 rgba(224,140,0,0);}}
  .urgency-text{flex:1;min-width:0;}
  .urgency-badge{display:inline-block;font-size:0.72rem;font-weight:800;color:#a05c00;text-transform:uppercase;letter-spacing:1px;margin-bottom:3px;}
  .urgency-body{display:block;font-size:0.84rem;color:#7a4800;line-height:1.5;}
  .urgency-body strong{color:#c07a00;}
  .urgency-countdown{display:flex;flex-direction:column;align-items:center;gap:4px;flex-shrink:0;}
  .cd-label{font-size:0.68rem;font-weight:700;color:#a05c00;text-transform:uppercase;letter-spacing:.8px;white-space:nowrap;}
  .cd-timer{display:flex;align-items:center;gap:4px;}
  .cd-block{display:flex;flex-direction:column;align-items:center;background:rgba(224,140,0,0.18);border:1px solid rgba(224,140,0,0.35);border-radius:8px;padding:5px 9px;min-width:40px;}
  .cd-block span{font-size:1.1rem;font-weight:800;color:#7a4000;line-height:1;}
  .cd-block small{font-size:0.6rem;font-weight:600;color:#a05c00;text-transform:uppercase;letter-spacing:.5px;}
  .cd-sep{font-size:1.1rem;font-weight:800;color:#c07a00;margin-bottom:12px;}
  .btn-primary{background:linear-gradient(135deg,var(--blue),var(--blue2));color:#fff;padding:14px 28px;border-radius:50px;font-weight:700;font-size:0.95rem;text-decoration:none;border:none;cursor:pointer;transition:transform .2s,box-shadow .2s;display:inline-flex;align-items:center;gap:8px;}
  .btn-primary:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(14,77,138,0.4);}
  .btn-secondary{background:transparent;color:var(--blue);padding:14px 28px;border-radius:50px;font-weight:700;font-size:0.95rem;text-decoration:none;border:2px solid var(--blue);cursor:pointer;transition:all .2s;display:inline-flex;align-items:center;gap:8px;}
  .btn-secondary:hover{background:var(--blue);color:#fff;}
  .hero-trust{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:24px;}
  .trust-badge{display:flex;align-items:center;gap:7px;background:var(--card-bg);backdrop-filter:blur(8px);border:1px solid rgba(26,111,173,0.15);padding:9px 16px;border-radius:50px;font-size:0.82rem;font-weight:600;color:var(--text);box-shadow:var(--shadow);white-space:nowrap;}
  .tb-icon{font-size:1rem;line-height:1;}

  /* ── LEAD FORM ── */
  .lead-form-card{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow-lg);padding:36px 32px;border:1px solid rgba(26,111,173,0.10);}
  .lead-form-card h3{font-size:1.25rem;font-weight:700;color:var(--text);margin-bottom:6px;}
  .lead-form-card p{font-size:0.85rem;color:var(--muted);margin-bottom:22px;}
  .form-field{margin-bottom:14px;}
  .form-field label{display:block;font-size:0.8rem;font-weight:600;color:var(--text);margin-bottom:5px;}
  .form-field input,.form-field select{width:100%;padding:11px 14px;border:1.5px solid #d0dce8;border-radius:10px;font-family:inherit;font-size:0.9rem;color:var(--text);background:#f8fbff;transition:border-color .2s,box-shadow .2s;outline:none;}
  .form-field input:focus,.form-field select:focus{border-color:var(--blue);box-shadow:0 0 0 3px rgba(26,111,173,0.12);}
  .form-field select{cursor:pointer;}
  .form-cta{width:100%;background:linear-gradient(135deg,var(--gold),var(--gold2));color:#fff;border:none;padding:14px;border-radius:50px;font-family:inherit;font-size:1rem;font-weight:700;cursor:pointer;transition:transform .2s,box-shadow .2s;margin-top:6px;}
  .form-cta:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(224,140,0,0.4);}
  .form-note{text-align:center;font-size:0.75rem;color:var(--muted);margin-top:10px;}

  /* ── SECTION COMMON ── */
  section{padding:96px 5%;}
  .section-inner{max-width:1200px;margin:0 auto;}
  .section-label{display:inline-block;background:rgba(26,111,173,0.08);color:var(--blue);font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:5px 16px;border-radius:50px;margin-bottom:14px;}
  .section-h2{font-size:clamp(1.7rem,3vw,2.4rem);font-weight:800;color:var(--text);line-height:1.25;margin-bottom:14px;}
  .section-h2 span{color:var(--blue);}
  .section-p{font-size:1rem;color:var(--muted);max-width:600px;line-height:1.7;}
  .section-header{margin-bottom:50px;}
  .section-header.center{text-align:center;}
  .section-header.center .section-p{margin:0 auto;}

  /* ── WHO WE HELP ── */
  .who-we-help{background:#fff;padding:90px 5%;}
  .wwh-inner{display:grid;grid-template-columns:1fr 1.15fr;gap:70px;align-items:center;max-width:1200px;margin:0 auto;}
  .wwh-left .section-label{margin-bottom:14px;}
  .wwh-left .section-h2{margin-bottom:16px;}
  .wwh-list{display:flex;flex-direction:column;gap:20px;}
  .wwh-item{display:flex;align-items:flex-start;gap:18px;background:linear-gradient(135deg,#f4faff,#eef6fd);border:1px solid rgba(26,111,173,0.10);border-radius:16px;padding:22px 22px;transition:transform .25s,box-shadow .25s;}
  .wwh-item:hover{transform:translateX(6px);box-shadow:var(--shadow-lg);}
  .wwh-icon-wrap{width:50px;height:50px;min-width:50px;border-radius:14px;background:linear-gradient(135deg,#d6ecfa,#b8d8ee);display:flex;align-items:center;justify-content:center;font-size:1.5rem;}
  .wwh-content h4{font-size:1rem;font-weight:700;color:var(--text);margin-bottom:5px;}
  .wwh-content p{font-size:0.87rem;color:var(--muted);line-height:1.65;}
  @media(max-width:900px){.wwh-inner{grid-template-columns:1fr;gap:40px;}}

  /* ── WHY FREEZONE ── */
  .freezone{background:linear-gradient(135deg,#f0f8ff 0%,#e8f4fd 100%);}
  .benefits-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;}
  .benefit-card{background:var(--white);border-radius:var(--radius);padding:28px 24px;box-shadow:var(--shadow);border:1px solid rgba(26,111,173,0.07);transition:transform .25s,box-shadow .25s;}
  .benefit-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);}
  .benefit-icon{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#d6ecfa,#b8d8ee);display:flex;align-items:center;justify-content:center;font-size:1.6rem;margin-bottom:16px;}
  .benefit-card h4{font-size:1rem;font-weight:700;color:var(--text);margin-bottom:8px;}
  .benefit-card p{font-size:0.87rem;color:var(--muted);line-height:1.6;}

  /* ── SERVICES ── */
  .services-grid{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 26px;
    align-items: stretch;
  }
  @media(max-width:960px){ .services-grid{ grid-template-columns: repeat(2,1fr); } }
  @media(max-width:580px){ .services-grid{ grid-template-columns: 1fr; } }

  .service-card{
    background: rgba(255,255,255,0.82);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 22px;
    padding: 34px 28px;
    text-align: center;
    box-shadow: 0 4px 24px rgba(14,77,138,0.07), 0 1px 4px rgba(14,77,138,0.05);
    border: 1px solid rgba(26,111,173,0.09);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.32s cubic-bezier(0.34,1.56,0.64,1),
                box-shadow 0.32s ease,
                border-color 0.28s ease,
                background 0.28s ease;
  }
  /* top accent line that grows on hover */
  .service-card::before{
    content:'';
    position:absolute;
    top:0;left:0;right:0;height:3px;
    background:linear-gradient(90deg,var(--blue),#4db6f5,var(--gold));
    transform:scaleX(0);
    transform-origin:left;
    transition:transform 0.35s ease;
    border-radius:22px 22px 0 0;
  }
  /* inner glow on hover */
  .service-card::after{
    content:'';
    position:absolute;
    inset:0;
    background:linear-gradient(145deg,rgba(26,111,173,0.05) 0%,rgba(100,190,255,0.04) 50%,transparent 100%);
    opacity:0;
    transition:opacity 0.3s ease;
    border-radius:22px;
    pointer-events:none;
  }
  .service-card:hover{
    transform: translateY(-10px) scale(1.025);
    box-shadow: 0 24px 48px rgba(14,77,138,0.14), 0 6px 16px rgba(14,77,138,0.08);
    border-color: rgba(26,111,173,0.22);
    background: rgba(255,255,255,0.97);
  }
  .service-card:hover::before{ transform:scaleX(1); }
  .service-card:hover::after{ opacity:1; }

  .service-icon-wrap{
    width: 70px;
    height: 70px;
    border-radius: 20px;
    background: linear-gradient(145deg,#e8f4fd,#d0e9f8);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    margin-bottom: 20px;
    flex-shrink: 0;
    position: relative;
    transition: background 0.3s ease, transform 0.35s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease;
    box-shadow: 0 4px 12px rgba(14,77,138,0.10);
  }
  .service-card:hover .service-icon-wrap{
    background: linear-gradient(145deg,#c5e2f8,#a8d4f0);
    transform: scale(1.15) rotate(4deg);
    box-shadow: 0 8px 24px rgba(14,77,138,0.18);
  }
  .service-card h4{
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 10px;
    transition: color 0.25s ease;
    line-height: 1.3;
  }
  .service-card:hover h4{ color: var(--blue2); }
  .service-card p{
    font-size: 0.86rem;
    color: var(--muted);
    line-height: 1.65;
    margin: 0;
    flex: 1;
    transition: color 0.25s ease;
  }
  .service-card .sc-link{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    margin-top: 18px;
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--blue);
    opacity: 0;
    transform: translateY(6px);
    transition: opacity 0.28s ease, transform 0.28s ease;
    text-decoration: none;
    letter-spacing: 0.3px;
  }
  .service-card:hover .sc-link{ opacity:1; transform:translateY(0); }

  /* ── PROCESS ── */
  .process{background:linear-gradient(135deg,#f0f8ff 0%,#e8f4fd 100%);}
  .steps{display:flex;gap:0;position:relative;flex-wrap:wrap;justify-content:center;}
  .step{flex:1;min-width:220px;max-width:320px;text-align:center;padding:0 20px;position:relative;}
  .step:not(:last-child)::after{content:"";position:absolute;top:34px;right:-2px;width:50%;height:3px;background:linear-gradient(90deg,var(--blue2),var(--blue));z-index:0;}
  .step:not(:first-child)::before{content:"";position:absolute;top:34px;left:-2px;width:50%;height:3px;background:linear-gradient(90deg,var(--blue),var(--blue2));z-index:0;}
  .step-num{width:68px;height:68px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue2));color:#fff;font-size:1.6rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin:0 auto 20px;position:relative;z-index:1;box-shadow:0 6px 20px rgba(14,77,138,0.3);}
  .step-icon{font-size:1.4rem;}
  .step h4{font-size:1rem;font-weight:700;color:var(--text);margin-bottom:8px;}
  .step p{font-size:0.86rem;color:var(--muted);line-height:1.6;}

  /* ── PRICING ── */
  .pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:28px;}
  .price-card{background:var(--white);border-radius:var(--radius);padding:36px 28px;box-shadow:var(--shadow);border:2px solid transparent;transition:transform .25s,box-shadow .25s;position:relative;overflow:hidden;}
  .price-card.featured{border-color:var(--blue);box-shadow:var(--shadow-lg);}
  .price-card.featured::before{content:"Most Popular";position:absolute;top:16px;right:-30px;background:linear-gradient(135deg,var(--blue),var(--blue2));color:#fff;font-size:0.72rem;font-weight:700;padding:5px 46px;transform:rotate(45deg);letter-spacing:.5px;}
  .price-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);}
  .price-tier{font-size:0.78rem;font-weight:700;color:var(--blue);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:10px;}
  .price-name{font-size:1.4rem;font-weight:800;color:var(--text);margin-bottom:6px;}
  .price-amount{font-size:2.4rem;font-weight:800;color:var(--blue);line-height:1;margin-bottom:4px;}
  .price-amount span{font-size:1rem;font-weight:500;color:var(--muted);}
  .price-desc{font-size:0.84rem;color:var(--muted);margin-bottom:24px;padding-bottom:24px;border-bottom:1px solid #e8f0f8;}
  .price-features{list-style:none;margin-bottom:28px;}
  .price-features li{font-size:0.88rem;color:var(--text);padding:7px 0;display:flex;align-items:center;gap:10px;}
  .price-features li::before{content:"✓";width:20px;height:20px;background:linear-gradient(135deg,#d6ecfa,#b8d8ee);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:700;color:var(--blue);flex-shrink:0;}
  .price-btn{width:100%;background:linear-gradient(135deg,var(--blue),var(--blue2));color:#fff;border:none;padding:13px;border-radius:50px;font-family:inherit;font-size:0.95rem;font-weight:700;cursor:pointer;transition:transform .2s,box-shadow .2s;}
  .price-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(14,77,138,0.35);}
  .price-card.featured .price-btn{background:linear-gradient(135deg,var(--gold),var(--gold2));}
  .price-card.featured .price-btn:hover{box-shadow:0 8px 24px rgba(224,140,0,0.4);}

  /* ── WHY US ── */
  .why-us{background:linear-gradient(135deg,var(--blue2),var(--blue));color:#fff;}
  .why-us .section-label{background:rgba(255,255,255,0.15);color:#fff;}
  .why-us .section-h2{color:#fff;}
  .why-us .section-p{color:rgba(255,255,255,0.8);}
  .why-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:22px;}
  .why-card{background:rgba(255,255,255,0.10);backdrop-filter:blur(10px);border-radius:var(--radius);padding:28px 22px;border:1px solid rgba(255,255,255,0.2);text-align:center;transition:background .25s;}
  .why-card:hover{background:rgba(255,255,255,0.18);}
  .why-icon{font-size:2.2rem;margin-bottom:14px;}
  .why-card h4{font-size:1rem;font-weight:700;color:#fff;margin-bottom:8px;}
  .why-card p{font-size:0.84rem;color:rgba(255,255,255,0.78);line-height:1.6;}

  /* ── TESTIMONIALS ── */
  .testi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;}
  .testi-card{background:var(--white);border-radius:var(--radius);padding:28px 24px;box-shadow:var(--shadow);border:1px solid rgba(26,111,173,0.07);}
  .testi-stars{color:var(--gold);font-size:1rem;margin-bottom:12px;letter-spacing:2px;}
  .testi-text{font-size:0.92rem;color:var(--text);line-height:1.7;margin-bottom:20px;font-style:italic;}
  .testi-author{display:flex;align-items:center;gap:12px;}
  .testi-avatar{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue2));display:flex;align-items:center;justify-content:center;font-size:1.2rem;color:#fff;font-weight:700;flex-shrink:0;}
  .testi-name{font-weight:700;font-size:0.9rem;color:var(--text);}
  .testi-role{font-size:0.8rem;color:var(--muted);}

  /* ── FAQ ── */
  .faq{background:linear-gradient(135deg,#f0f8ff 0%,#e8f4fd 100%);}
  .faq-list{max-width:800px;margin:0 auto;display:flex;flex-direction:column;gap:14px;}
  .faq-item{background:var(--white);border-radius:14px;border:1px solid rgba(26,111,173,0.10);overflow:hidden;box-shadow:var(--shadow);}
  .faq-q{width:100%;background:none;border:none;text-align:left;padding:20px 24px;font-family:inherit;font-size:0.97rem;font-weight:600;color:var(--text);cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:12px;}
  .faq-q::after{content:"+";font-size:1.4rem;color:var(--blue);font-weight:300;transition:transform .25s;flex-shrink:0;}
  .faq-item.open .faq-q::after{transform:rotate(45deg);}
  .faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease;}
  .faq-a-inner{padding:0 24px 20px;font-size:0.9rem;color:var(--muted);line-height:1.7;}
  .faq-item.open .faq-a{max-height:300px;}

  /* ── FINAL CTA ── */
  .final-cta{background:linear-gradient(135deg,#0e4d8a 0%,#1a6fad 50%,#0e4d8a 100%);text-align:center;padding:100px 5%;}
  .final-cta h2{font-size:clamp(2rem,4vw,2.8rem);font-weight:800;color:#fff;margin-bottom:16px;}
  .final-cta p{color:rgba(255,255,255,0.8);font-size:1.05rem;margin-bottom:36px;}
  .final-cta-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}
  .btn-white{background:#fff;color:var(--blue2);padding:15px 32px;border-radius:50px;font-weight:700;font-size:1rem;border:none;cursor:pointer;transition:transform .2s,box-shadow .2s;text-decoration:none;display:inline-flex;align-items:center;gap:8px;}
  .btn-white:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(0,0,0,0.25);}
  .btn-gold{background:linear-gradient(135deg,var(--gold),var(--gold2));color:#fff;padding:15px 32px;border-radius:50px;font-weight:700;font-size:1rem;border:none;cursor:pointer;transition:transform .2s,box-shadow .2s;text-decoration:none;display:inline-flex;align-items:center;gap:8px;}
  .btn-gold:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(224,140,0,0.5);}

  /* ── FOOTER ── */
  footer{background:#0a1f3d;color:rgba(255,255,255,0.8);padding:60px 5% 30px;}
  .footer-inner{max-width:1200px;margin:0 auto;}
  .footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:48px;}
  .footer-brand img{height:52px;margin-bottom:18px;filter:brightness(1.1);}
  .footer-brand p{font-size:0.87rem;line-height:1.7;color:rgba(255,255,255,0.65);}
  .footer-socials{display:flex;gap:12px;margin-top:18px;}
  .social-btn{width:38px;height:38px;border-radius:10px;background:rgba(255,255,255,0.10);display:flex;align-items:center;justify-content:center;font-size:1.1rem;text-decoration:none;transition:background .2s;}
  .social-btn:hover{background:var(--blue);}
  footer h5{font-size:0.9rem;font-weight:700;color:#fff;margin-bottom:18px;letter-spacing:.5px;}
  footer ul{list-style:none;}
  footer ul li{margin-bottom:10px;}
  footer ul li a{color:rgba(255,255,255,0.65);text-decoration:none;font-size:0.87rem;transition:color .2s;}
  footer ul li a:hover{color:#fff;}
  .footer-contact p{font-size:0.87rem;color:rgba(255,255,255,0.65);margin-bottom:8px;display:flex;align-items:flex-start;gap:8px;}
  .footer-divider{border:none;border-top:1px solid rgba(255,255,255,0.10);margin-bottom:24px;}
  .footer-bottom{display:flex;align-items:center;justify-content:space-between;flex-wrap:gap;font-size:0.82rem;color:rgba(255,255,255,0.45);}

  /* ── WHATSAPP FLOAT ── */
  .wa-float{position:fixed;bottom:28px;right:28px;z-index:200;display:flex;align-items:center;gap:10px;background:linear-gradient(135deg,#25d366,#1abe54);color:#fff;font-family:'Poppins',sans-serif;font-size:0.88rem;font-weight:700;padding:14px 22px 14px 18px;border-radius:50px;box-shadow:0 6px 28px rgba(37,211,102,0.55);cursor:pointer;transition:transform .25s,box-shadow .25s;text-decoration:none;animation:pulse-wa 2.8s infinite;}
  .wa-float:hover{transform:translateY(-4px) scale(1.04);box-shadow:0 12px 36px rgba(37,211,102,0.7);}
  .wa-float:hover .wa-label{max-width:200px;opacity:1;}
  .wa-icon{width:28px;height:28px;fill:#fff;flex-shrink:0;}
  .wa-label{white-space:nowrap;letter-spacing:0.2px;}
  .wa-dot{width:8px;height:8px;min-width:8px;border-radius:50%;background:#fff;opacity:0.85;animation:wa-blink 1.4s ease-in-out infinite;margin-left:2px;}
  @keyframes wa-blink{0%,100%{opacity:0.85;}50%{opacity:0.3;}}
  @keyframes pulse-wa{0%,100%{box-shadow:0 6px 28px rgba(37,211,102,0.55),0 0 0 0 rgba(37,211,102,0.4);}60%{box-shadow:0 6px 28px rgba(37,211,102,0.55),0 0 0 14px rgba(37,211,102,0);}}
  @keyframes pulse-wa{0%,100%{box-shadow:0 6px 24px rgba(37,211,102,0.5),0 0 0 0 rgba(37,211,102,0.35);}50%{box-shadow:0 6px 24px rgba(37,211,102,0.5),0 0 0 12px rgba(37,211,102,0);}}

  /* ── MOBILE ── */
  @media(max-width:900px){
    .nav-links-wrap,.nav-right{ display:none; }
    .hamburger{ display:flex; }
    .nav-mobile-menu{ display:flex; }
    .hero-inner{grid-template-columns:1fr;}
    .lead-form-card{margin-top:40px;}
    .step:not(:last-child)::after,.step:not(:first-child)::before{display:none;}
    .footer-grid{grid-template-columns:1fr 1fr;}
  }
  @media(max-width:600px){
    .footer-grid{grid-template-columns:1fr;}
    .hero-btns{flex-direction:column;}
    .final-cta-btns{flex-direction:column;align-items:center;}
  }
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav" id="main-nav">
  <div class="nav-inner">
    <div class="nav-logo-wrap">
      <div class="nav-logo-inner">
      <img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAIrBMgDASIAAhEBAxEB/8QAHQABAAEFAQEBAAAAAAAAAAAAAAECBQYHCAQDCf/EAGEQAAEDAwEEBQUGDQ0PBQEAAwEAAgMEBREGBxIhMQgTQVFhFCJxgZEVMlKhsdEWI0JVYnKCkpOUssHSFzM1NkNTVGNzdKKjsyQlJic0N0RFVmRldcLh8BiDhKS08ZXT4v/EABsBAQACAwEBAAAAAAAAAAAAAAAEBQIDBgEH/8QAPREAAgIBAgMDCgUEAQQCAwAAAAECAwQFERIhMRNBUQYUIjJSYXGBkdEzNKGx4RUjwfBCFiRTcmJjNUOS/9oADAMBAAIRAxEAPwDshERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAER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ZX10gL8+Djy9DfYtd686SNupXPpNHW01zxw8sqwY4h4tZ753rwufNaax1DrC5mvv1ylqn5PVx5LYoh3NaOA+XxVh3sHiV3WHoNNKXac34LofOcrU78mblKW78WZRrTXWqdXzF1+u89VHnLacHchb6GDh7clYwcYxgexMjsQkK8hCMFwxWyK9tvqUkA9gXzdDE7nG0+pfRF7shued1FC7k0tPgV8n2/HvJcH7IL3ZUrB1QfVHqk0WjqqqlmbNFvMkYctkjcQ5p7wRxC2boLpBbRNLSRQVVc2/UDOBp7hlzwPsZR54Pp3gO5YSvjNTQzDz4xnvAwVEuwYWLZm2FzidobMNvuh9ZmKjqKg2K6vwPJa14DHn+Ll9670HdPgttNIIBGOK/Mia2lvGJ28D9S7tWwtme27XGg5YqN1Q67WlvA0Na4ndb/Fyc2+jiPBUOTpEoc4E2vK36neyLXuyva9o/aDTtjttb5Lcw3MlvqiGTDvLex48W+vC2DnPJU04Sg9pLZktSUuaJRQFKxPQoKlEBSikqEAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAFJUZUSPaxrnPIa1vEk8ggKicLANpu1Kw6MYaVzvL7q4ebRwuGW9xkdyYPjPYFgW1/bPumax6OmBfxZPcRghneIu8/Zch2ZWgpZJJZXzSyPklkcXPe9xLnOPMknmSq3Kz1D0a+p2OjeS8r0rcrlHw739jJNea81HrKqLrvWbtKDmOjhy2Fvdw+qPifiWM5zzUAYCkclTzm5veXM76iivHgoVJJDn2YQcFKhYm4IikLwAKoY9ahM4BOMnsA7UHTmZBoPSd01jf47RbW7v1VRO4ZZAz4R7z2Adp9eOtNH6XsOh9PGmomRwQxMMlTVSuAc/AyXvd/4ArZsX0hDpHRtPC+MC41TRNWv7S8j3voaOA9Z7VoDpUbVKq73iq0NZqkQ2qif1de9jsGplHNmfgNPDHaQc8Auq0jS3ZJJde9+B8n8pNelk2OEX6C6e/3lW3bb1LeZqiwaRqn09p4smq4+EtV2HdPNsfiOJ8OS0DLVPJIa0N/MvmxnWPDYWukcexjS4k+pXWi0lqqvx5Fpi9VAPIx0Mp+PC7mqNeNDghyOJlvN8TLS6WU/Vn2qN955ud7Vl0Gy7aLKMs0VfD6aUj5VE+zDaLC3efom+bve2lLvkR5EPa/U94H4GJiSQcnu9qqFRMPqyfSvdcdPagtxPuhYbrSY/fqORo9pCthOCQeGO/gvVan0Z5w+49Laxw980H0L7R1MT+3dPivAoPBbY3SR44Jl2GCFKtccskZy0nHcvXDVNcQH+ae/sW+Nyl1MHBo9QRRkEZB4d6ZW0wJXzlijlG69ocPQvohR8weDyWekqY6ugqJYZ4nB8b2PLXscORa4cQVvfZF0mbjap4rNtDjlr6MYY25RM+nxD+MaP1weI87wctLYXmq6SKo9+3Du8c1X5Wn13Lob675QZ+j9hvFsvtqgutnroK6hnbvRTwvDmuHq7RyxzC96/O3Zzr3VuzO6eVWGtLqN7gaijmy6nnx8Jv1Lvshg+nkuytj+2LTG0WlbDSv9z7yxuZrdUOG+O8sP1bfEcR2gLlcrAsx34osqrozNkoiKCbwoIUqEBCIUQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBEHih8AgPlVVENJTy1NTLHFDE0ve95wGgcSSewLmLbHtcqdTSzWXT8slPZQS2SYZa+q/O1nxnt4cFmHSs1HLTWq36appnN8tcZqoNOMxsIw0+Bdx+5XOw4H4lU5+U0+zj8zvPJjRa5QWXct33L/JWCOXYFTy4KR6EKqTuSEUovAQpwoUhD0YUphEDC+lPIIKmCoLd4RSskLfhBrgSPiVACY45Xq6njSaaZ3Fpi+2u/wBnp7ha6uOoglYMFp4tOORHMEdxVrrNC6DfVS1tVpeyOnkcXySSUjMuJOSSSOJXHVBX19vlMtBXVdG883U87oyfTukKK64V9cc1tfW1XhNUPf8AKSriGrOC5J7/ABODs8iuKx7WLh965nXs992caaG75dp23Ob9RGYmO9g4qz1m23Z7Tndjuk1R4w0shHtIAXJ7Wtbxa0D0BbB2PbOK3W9y8pqg+CxU78TzDgZiP3Nn53dnpWK1G66W0UbLfJbAwqndkWPZfBHTuitUW/VtoN2tcVU2kMhjY+eLc6zHMt7xnhnwKvU0gihfK8PIYCSGtLjgdwHEnwXyt9HS0FHDR0cLIKeFgjijYMNY0DgAFgG07a5aNn1eynvdhv74pAOqqoKdhgkPPdDy8cR3HB9XFW9Vc5tRXNnCXyr4m48o9xj+03aHtKEEtJoLZpeJTjHuhXQAAeLIc5Ppdj0LmPWentrl3rzcdT6Z1PUzEn6Y63PLW+A3G4AXQv8A6p9FCTDrBqAN+EI4f01caLpO7NZnATMvdLnmZKMOA+9cVcUu/HW0aiDJQm+cjjKojlp5nQ1ET4JW8DHIwscPSCMqg88LuWTansS1dF5Hc7vZqlrxjq7jSlgAPjI3A9qxnUGwHZZq2mdU6OurbbM4Za6hqhUQethJ4eghS4ajt+LBo1Oj2XucgAqQBhbF2lbGNb6H6ypqaD3TtjckVtEC9oH2bcbzPWMeK1yCDy4qfC2Ni3i9zS4tdT6wzSRHgcjuK98MzJR5p49oVtHEI0lrg5pwR2qRXc4mEopl2ypXnpphIME4d8q+45qYpKS3Rqa2JUKUXp4UuaHDBAI7ivI1lXbq2K42uolp6mncJIpInbr43DkWkcV7VI5LXZXGxbMyjJx6HS2wLpD016fT6a13JFR3M4jp7jgMhqD2Nk7GP8eR8DwPRgIPIhfmjXUMc/nsAbJ8Tluzo/7fKrTU1PpTW08lRZwRHT1ryXSUY5Bru10fxt8RwHL5+lut8VZY0ZKlykdiIvlT1ENTTx1FPLHNDK0Pjexwc17SMggjmCO5fRUZNBUKpQgIRSQoQBERAEREARFOEBCKcJhAQinCYQEIpRAQilMICEU4UIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCkIFKAhQQqlS5AfOqnip6d8872sjY0uc4nkBzVl0teH3mWuqgC2mjeI4W9vAZyfE5WHbTNSGqqHWijk+kRO+nOB4OeOz0D5VkOy+Lc0uZMcXyuPp4ABc7HUnk6iqa36Md9/eya8fgo45dWc47frn7pbUbnh29HSBlKzjy3Rk/G4rAccVfdeSGbXN+kcck3Gbj92R+ZWMkdq03y4rJP3n17TqlXiVxXcl+xIwoeWtbvOIAVvrrmyBwjhHWSE4GOPH868hbWTV3UVQc2QOw9h+oxzBCxUHtuZzyYqXBHmy9Mc17d5hyO9B4owBrQ0dinHDOVgyQua5jCdiiWSOJhdI4NHivlaYrxqG4C3abtNXcak82wxF274k8mjxJAWUISk9kab8iqiPFN7H2OAM7wC801fSxHDpWk+HFbj0b0c77cmsqdY3ttviOCaSixJL6C8+Y0+gO9KznUGz3ZHsz0tUaguNghrnU7MR+XSGd88h96wNcd3JPcOHE9inQwJ7byexzd/lTQp9nSnJ+45no6uCpJbG45HHBC9PJeeOofcrvXXqWlp6V1XKXtggYGRxA8mtA5AL0EjmoM9k9kdLjynOtSmtmwQqHENBJOMc8qYnS1VbFb7fTT11bKd2OngYXPefAD5VvfZRsMe2aG9a7ZFI8YfFa2O3mMPYZTycfsRw8SttONO58uhB1HWMbAjvY934d5iGyDZVcNYyx3S6slorCDkOxuyVXgzub9l7O8dS2m3UVrt0FBb6aOmpYGBkUcbcNaB4L0RMZHG2ONgYxow0NGAB3BVq/ox4UR5dT5hqmrX6jZxWckui8B8i8N8tNtvlsmtl2ooa2jnbuyQzN3mu/7+K9yKQm090VTXiclbY+jdcLaZbvoESV9JxdJbXuzNH/ACbj78eB870rnWpinpqqSlqYJYJ4nFkkUjC17HDmCDyK/T/hlYTtI2W6L19A73etLPLA3djr6f6XUR93ngcQO5wI8FbY2qSjyt5kazGT5xPz2aeHPIX3oqqoophNR1E1LKDkPgkLHD1hbw150ZNW2d0lTpash1BSDJbC4iGpaPQTuu9IIJ7lpe9Wi62StdRXi21dvqGnBjqYXRu+McVdVZFVy3i9yJKEovmZxpnbXtIsJa2LUc1fABgwV7RO1w7snzvjU33UOgdaudPdLK7SF7ecmttrDLRyu75IffN+2Zk+BWusjHJD4hevHhvulszzje2zPTcaXyGsfTGopqkNwRNTyb8bweIIPD2HBHIgFfBUjnwRbNuRiVNJBBBwRyXvppxIN0+/HPxVvBRri1wLeY5LZXY4sxlHcu5QL5QSiVmeR7QvsFNUlJbmnYBFJ4ehZppfZVr7UttjuVp0/M+jlGY5ZpGRCQd7Q8gkeKwsuhUt5vY9UW+hhZXkr6NlSwHk8cj3+Cze+7N9c2KN0tz0xcI4m++kZH1rB6XMysYLADg9nML2M4Wx5PdDnFmy+jhtpqtE1sOldVTvk09I7dimdlzqAk8+8xE8x9TzHaF2dTzxVEDJ4JGSxSNDo3scHNe08QQRzB71+cFbQsqY+PmvHvXLbfRq2zTaQuMGjNVVBNimeGUtRI7/ACF7jwBP70T96ePLK5zVNM4X2kET8bJ39FnZClUteC0OBBB4jHapXOlgSqSqlBQEIiIAiIgJAUoiAIignigJRRlMhASijI7wmUBKKM9yICUUKUBGFGFUiApRSiAhFKYQEIpwmEBCKcKMIAiYTCAIpwmEBCKcJhAQiYRAEREAREQBETCAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiJhAEU4TCAhEwiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIpCAKUUdqAlYxtCvvuPaTHA/FXU5ZFjm0drvV+dZJK9sUbpHuDWtGXE9gWktW3R15vc1Zk9UDuQjuYOXt5+tUWvZ/m1HBF+lIl4dHaz3fRFmDS94bkucTjPetw7O9wab6pp4skc0+nC1Va4t6p3yODAtlbMpR5NWU5PEPD8ekY/MuX8n7OHOW/emWeet6TlXXkBp9cX+F585lxmz63E/nWGXarllnZQULHyzyuDGtjG85zicBoA5nK2L0lYX2baldQxm42sZHVMPeHNDSfvmlXvZHpah0Hoifa1qun6ysez+81HJwOX8Gv4/VO7O5uT28Omjj8V0t+iO0s1VV4FXBzlJJL4mG3axx7OLZBBVGObWlbEJJMEObaIXcg3sM7vhfUjOOwnGbVAGNMhHFx5lTd62uvV3qrpcZnT1lXKZZnntcewdwHIDsAC9QDYohvEANHElaLrFJ7R6Fjp2I6o8dnOT6lbgAc5Xikq5Zq2O32ymlrKyZwZHFEwuc5x7ABzXv0zZL/AK2vjbHpukdM8466Z2RHC34T3dg+M9i6x2TbKtO7O6DykbtZdns/ui4TNAPiGD6hvh7SVtx8R2elLkiv1jX68JcFfORqzZj0eKmubHddoFTJG12HNtlO/jj+MeOXob7V0Pp6x2nT9ujt9lt1NQUrOUcDA0E957z4nirTWamfU1rbfZYhLLIcCV3vR3kDtA71kNJEYIA18jpX4y97uZP5lYYeRRZJwoW6XefPM7Kych8Vz69xTca2lt1DPW1s7IKaCMySyPOGsaBkknuXGO1/XFXtD1V5QHSRWWjcW0NO7hkdsjh8J3xDh35zPpLbS23q4yaTtVUG2mjfiula7hUyg/rY+xb297vRxxHZzst1Xr7cqKRnuRZieNfUMOZB/Fs4F/p4DxWGVbO2XZVnTaLhUYFXnmW9m+i/3vMNmroKYNjyS88GsaMk9wwtiaB2P6z1e+Opr4pNPWl2D1lQz6e9v2LOz0nHrW/9nGyHR2ig2opaI19zx51dWYfJn7EcmfcgHvJWwMDuXtOnKPOfM16j5WW2bwxlsvExHZ3s801oajMVloh18gxNVy+dNL6Xd3gOCy7HqUjkisopRWyOQstnbLjm92PQh5pnih8F6zBci33O8UNBMyGomAkeeDAMlRDeaCWcQCcNlOMNcMc1gWrGO+iOsLjk77cfejCr1K4i8ylpxutZu47PNC4vI8or67J7RW0Zbfv9i1jgQlGPPm1ubLGOaL5UmXUsRceO4CfYvoSBwXYwlxRTKtrZklvHtVvvlktF8ozR3m2Ulwpz+51ETXj41cPQpWxNp7oxfPqaQ1n0bNDXfflsbqqwVJ4jqHdZCT4sdy9RC0hrXo77Q7AHz26lptQUrcnNE/EoH8m7BP3JK7dKEZ5qbVqN9ffv8TVLHhI/MitpamhrH0ddTT0lTGd18M8bo3tPi0jIXwX6Q6w0dpjV1F5JqOy0dxjxhrpWeez7V485vqIXPO0nouvY19boK6l2MuNvuD+fM4ZKB6AA4elytaNVrnynyI08eS6czmXKZVw1JYb1pu6Ptd+tdVbaxn7lOzG94tPJzfEEhW3xHJWSkpLdMj7bH1hlMbw5vrHgrxE4Sxte05B+JWNeqhqTC8NJ81x9ikUz4XszXOO5lOkKGmuWrrLbqv8AyequFPBLxx5j5GtI9hPtX6EQRRwwshhY2ONjQ1rWjAAAwAAvzjgqpKSqhq6dxEsL2yxkdjmkOB9oX6H6cutPe9P0F4pTmGtpo52cc4Dmg49WVSeUClvCXdzJWC1zPfgEYI4LCdc7LNGatY51wtMdPVkebV0o6qUHvJHB3rBWW1VS+GXdAaRjKiOtaeD249HFc1DN7Gfoy2ZZSp41zRyFtO2K6n0kJK23sderU3LjLAz6bE37NnPA7xkehafuVCyui4EdaBgOHb4HwX6StLHty0gjwWqNrWxKwatZLcrNHFaL4fO61jcQznukaO/4QGfSulw9cU0oX9PErbcNx9Ks150S9rkkph2d6oqSamIbtrqZXcXtH7iT3ge98OHYunRxC/OvXumL/pTUIp7jTTW260jxJG9pwHYOWvY7kRkcCF2F0c9p0W0LSQir3tZf7c1sdfFy6zsbK0dzsce4gjuUXUsJQ/vV84s3Y13F6MuptNFA5KVTkspKKSoQBERAVIiIAtSdKnU180ns3guen7lLb6t1yiiMsYaSWlr8jiCOwLba0Z01xnZFT+F2g/JepGJFSvin4mu3lBnPH6te1H/bGt/BRfoKr9W7am3lrGr9cEJ/6FrglZvsK05a9X7U7Tp69RyyUNUJutbFIWO82JzhxHEcQF1FlVMIuTj0K5Sk3tuXMbbtqR56wqvVBD+gvrBty2pQzNkGrJpN3juSU0JB9PmfnXR7OjfsvY3HkFyd4mvk+dYhrnou2qWkkm0deaqmqmgltPXkSxPPdvtAc304coEczCk9nH9Dc6rUYDY+kvtAoZB7oQWq6x9odAYXe1p/Mt4bLNvmkdaVsFpqusst3m82OCpI6uZ3cyTkT3A4JXF19tVxsd4qrRdaR9JW0khjnieOLSPiIPAgjgQQQvBjkRnIIIIOMFb7dPotjvFbGEb5xfM/T0csotNdFXaHV6y0ZNbbxO+ou1oc2OSd5y6eJ2dx7j2u4FpPgCea3KFzdtUqpuEu4sISUluiURFrMgihEBKKFKAIihASiIgCIo4oCUUIgJRQpQBEUICUUBEBKIiAIiIAoIRSgKcFThFKAjCKVCAImUQBFKICMJhEQEYTCqRARhMKUQEYTCKUBGFKIgCIoQEooUoAoUogIwmERAQQiqVJQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBSgUoAqTzVSpccBeN7AwzatezQWpltgd9PrMhxB4tjHP28vatVhxPFXnW9f7q6lqqhrt6OM9VF9q3/vk+tWUgBq+Z6tl+dZMpdy5I6HEp7OpeLLzaI8UvWH6t3xLLdATdTe+qPATRlvrHH51j1PF1dPHH8FoBXvs0/kt0p584DZBk+Hb8qj4NvY5EJ+DNl8OOtxPptV2WU2udd6au1XuihoRILgzODMzIdGz0F29nwytP9KTVXuprGHTFE4C32Ro3ms4NM7mgnl8FpAHcXOXVVXNHTUc1TK7DIoy9xPYAMlcAXCsmudyq7pUEunrZ31MhPwnuLj8q+hZ81CHL/kSvJiqWTdxz6Vrl8WUU27vb5OAOJyr3obSN82hakbaLQwxwMINVVuaTHTM7z3uPHDe30ZKo0PpW6601DDYLS3cdJ59RUObltPED5zz8gHaSuy9H6asGgNKR2y2xiCmgbvTSu4vmf2vee1x+YDhgKHjYynvZPlFF7ruteZw7GrnN/ofHRemNO7O9LNt9thbDBGN6ad4HWTv7XOPaT3dnYsd1Jfqm6ymPzo6UHzYgefie8qnUN3mulWXuLmQN/W488vH0r26Js/l1aK2dmaeB3mgjg5/zBU+Zm26lcsXH5R/f3nGQgq07rnvIyDRtl9z6QVVS3+65hk55sb8H0961xt319eX17dnmgYZqzUNY3+65IOdJEfHk1xB5n3o48yCtzysLo3Ma8sJbgOHHHirNpXStn03DN7nwZqKmQy1VVId6aoeTkue7mT8Q7AF1dGJHHpjTXySIdORCNjusW77l3f6jVuyjYLZrIyC6auEV4uoAc2Bw3qaA+DT78+J9QW62RsYwMY0Na3gABwCrwik11xrW0TVk5VuTPjse4A9ietSqZHbrS7uGVk3st2Ryc8cKDnHNYNUaouJqXSxOY2IHzWFuRjx7VeLPqmlqnthqwKeV3AOLsscfT2FUmPr+HfN18Wz95LnhWwjxbFofebnQXR/lEr3tY/D4zyIz2d3BZrTTx1ELJojvMeA4HwKs2p7MLhD19OAKlg4fZjuXk0VXENdbZgQ5uXRg93a31KLhTuwct0XS3hPnFmdsYW1ccVs11LVrqn3L22QfusQPrBx8y8F9aZLy5oHF3Vj4gsi16xj2Usu+3fY4tIyM4OPmVniENTfaeV0rWs3mF5dwxj/+Lm9VpUc2cF3yT/36k/Gm+yUvBM2BGN2NrR2BYPqm7TzXN8UE8kcUJ3RuPLcntPD/AM4LK7tXMpLVNVMe12G+bg5BJ4BYhpm0OuVX184PUMdl5P1Z7l0Os3WXOvEx3zfN7eBCxIRjxW2dEZdp6SoltEElSS6RzeJPMjPD4lcMrzVlXTUFP1kz2sYBho7T4ALFa3VdW+Q+SRxxR9heMkqxu1LH06qNds92l8yPCid8m4ozRFYtMXmW5CSKoY0SxgHLORBV8U/Eyq8qpWV9GarK3XLhkSoOFKKSYFn1VpmwaptrrdqG00lxpjnDJ4wS0ntaebT4ggrmvap0YqimjluWgK19SxuXG2Vbxv8Aojk7fQ774rqvCEArfTlWUv0Wa51Rl1PzHuVFW2yvmt9yo56OrgduywTsLJGHuIK+HMc1+hG1HZhpTaDQ9XeqLq61jd2Cvp8Nnh7uPJzfsXZHo5rjba7sn1Ps5rC+uh8ts73YguUDD1ZzybIP3N3geB7CV0GLn137J8mQrKXAw+hmL49wnzh8YXZfRI1F7q7NTZ3uJns9Q6LB/e35ew/G4fcriaN5jkDm8wt6dFXVLbLtIgoZZd2kvURpiCeHWjzoz6c5b90pWfV2+LJd65mqmXZ2J+J17cm8WO7MYXjwrnVM6yA944q3Hmvm+ZDhs38S/qe8SgukYCYnbr+xfahusb3dVUDqpOWewr5leG4xcetA58HKJ21lL4ov5GzgjLkz6650hYdZ2V1rvdG2eIj6VK3hJC4/VMd2H4u9charsOrNgW0yhv8ARb1Vby8iGoa3djqoj7+CQcmux2d4Dhy4dfW24vpyI5Tvx8vQvRqixWbVmnqizXikjrKCqZuva7s7nA9jgeII4grpNN1ZTjw9z6ogZGLs9+8r0lf7dqjTdDf7RMJaKthEsRPMZ5tI7CDkEd4KuoXPuxll12TbSqrZffZZJ7HeC6r0/XOGGvePfxnsDyOY7xn6pdBDks7q1CXLp3HkJbrmSoKlQVqMyEREBUiIgC0b01v80EH/ADan+R63ktHdNYf4n4T3Xan+R6lYX48Pia7vUZxf2raHRV/z8af+1qf7B61gtqdFFudutjPdHUn+oeunyvwZfArq/WR3WnM8UHJQSuNLU5B6bVspqXaDaLlE1rZq63kTYHvjG/AJ8cOA9S0FyK270rtVUep9qksNumbNS2mAUQkactdJvF0mPQTu/crUJ7l1+FFqiKl1Ku1pzexv3oSzTjaLdoGl3UPtZc8dm8JGbvyldgLnXoU6Qq7fp656trY3xe6hbBRhzcb0TCSX+guOB9quihy4rn9Rmp3vYm462gSoKlYJt31YNG7M7tdI37tXJH5NSccHrZMgEeji77lQ4Qc5KK7zdJ7Lcxm59IzZxb7jVUMs10lkppnwvdFRlzS5ri04OeIyOauOhNuWhtZaoptOWh9yFbUse6Lyil6tp3RvEZzzxlcJOJxkkk95OSrlpO81GndT2y/Upd11vqmVDQDguDSN5vrGR610E9Kq4OW+5BWTLc/SoLAtpW1nSmz66U1v1F7oxyVMPXRPhpHSMcASCN4do4ZHiFmVmuFLdrTR3OhkElLVwsnhePqmOAI+Iha96SGz8a92fTRUkebvbiaqgIHFzgPOj9Dxw9IaqOiMO1UbOhMm3w7xLIOkxsyJwZ7sP/gOWwtneuNP68ssl309UyS08czoZBLGY3tcADgtPgQcr85i1zXlrg5rgSCDwIwttdFzXg0btCjo66cstN4LaaoyfNZJn6XIfWd0nud4K3ydLgqnKvqRYZEuLmdyqVSDwGPUpyqImll1rqe0aQ09U36+VBgoqfd33NYXOJJAAAHEkkrW3/qS2XjObhch4m3yLVXTH1wLpqOn0bQzZpraeurN08HTuHBp+1b8bvBYt0Y9nH0ba5bcbhCHWS0ObNUBwy2aXOY4vEZGXeAx2hXFWDXGjtbWRJXyc+GJ2vaK6G52yluNOyVkNTE2VglYWPDXAEZaeIPHkV5NV6htOlbDU3y+VXk1BTbvWybpdjecGgYHE5JCugAAC5h6buruFo0VSynJPl1a0Hs4tiaf6bseDVX41Pb2qHcb7J8ENzZP/qE2VZ/bDJ+JTforNdCa007re1y3PTdf5ZTRTGGRxjcwteADghwB5EL85gexb26GerBate1WmKiUinvEO9C0ngJ4wXD2s3vvQrLK02FdTlDqiPXkSckmdiBEClUpMPBqC70FhstZebpN1FDRQumnk3S7cY0ZJwASVrj/ANQmyjf3folPp8jmx+Sr/t4AOxnV/wDyio/IK/PY8+StdPwq8iDlJ9CNfbKDSR+k2kNUWPVtkjvOnq+OuonvcwSNBGHNOCCDxB9PeFeRyXCXR02nTbPdWNp6+Z7tP3F7WVrOYhdybM0eHI97fEBd0080U9PHPBIyWKRofG9jgWuBGQQRzBCi5mK8ee3cbKrONe8+q+c0rIYnyyHdYxpc44zgDiq157mA63VIPIxOyPUVFit2kbG9ka6O3rZVn9tMX4tN+itiWqvpbraqW50EompKuFk8EgBG+xwDmnjx4ghfmW8+aR4FfozsqGNmGlR/wak/sWKxzsOGPCMo95Hptc20z7a11fp/RtuiuGo7gyhppZRCyRzHOBeQTjgD2ArD/wBXvZTnH0VQ/i8v6KxPpsn/ABcWsf8AFWf2b1yAFuw9OrvqU5MxuvlCWyP0W0PrjTOtaapqNM3NlwipXhkzmsc3ccRkDzgOxX+aZkMD55XBscbS9zj2Acyudeg1+17Uo7PLIT/QK6FujQ62VQ74X/klV+RTGq51robq58UOIwL9XHZZgH6MKIgjIIZIf+le/TW1jZ9qS+U9ksmpKasuFRvdVC2N4Lt1pcebQOQJ9S/PiMkRsH2IWyui+7G3rTJ731A/+tKrW3S6oVuab3I8cmTex3qiKFQk0+dVPFTU0tTO8RxRML3uPJrQMk+xYT+rBszwCNaWjiP35ZPqwD6Frt/MpvyHL82ISREzwYPkVlgYUclSbe2xHuudbWx+h1h2kaHv12htVn1Pbq2um3jHBFLvOcAMn4gssHJcL9Fc/wCPaweLKkf/AF5F3StWbjRx7OCJlTY7FuwoUr4VtRFSUs1VUSNjhiY573k8GtAyT7FD6vkbiw6h15o7T9wNvvWpbZb6sNDzDPOGvAPI4XipNqOzyrq4aSn1lZZJ5pGxxxiqbl7nHAA48yVwvtI1NNq3XV21DI5zm1c7jCDzbE04jH3oCx1sj45GyQuLJGODmOacEEciPXhX0NHg4buT3ILynv0P07ClYlsj1PHrDZ3Zr82TflnpmtqM8CJm+bJ/SB9oWWqilFxk0yanutwrJedWaYs1Z5Hd7/bKGp3A/qqipZG7dPI4J8Cr34LivpnAfqxRnAz7lQflPUrDx1kWcDexruscI7o6zt+tdIXGsioqDU1nqqmV27HFFWMc95xyAByVkA5L8x6CpqKCtgraKV1PU08jZYZWcHMcDkEH0rvLYLtLpNomkmTSvjjvNG1sdwgHDzuyRo+C7BPgcjsW/N0/zdKUXujCq/jezNjqERVhILbfL/ZLE2J16u1DbmzEiI1M7Yw8jnjJ4rz2nVumLtWto7XqG1V1S5pcIqerZI8gczgHsWg+nZj3M0nkA/3TU8/tGLWPRG3f1creQ1v+Q1XZ9grKGDGWN22/MjSuanw7HciFFKriSUoiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAqCIiAKxa4ufuXpyqnacSvb1cf2zuHxc1fFrTbDXGSro7a08GNMrxntPAfnVZq+T5viSl3vl9SRi19pakYFyA4quBvWVkEXw3/EOJXzK9FkHWXpvb1URPt4L5odEzIzxUd6nwTCxQNhU+L7pKWnLy01FM+B7u1pLS3P51w5ParhBeDYxRyPuTJzS+TsGXGQHdwPWPYuxdFXRlHUPo53ARTHLSeQd/3GFkXuBp9l5df/cqhbcSzddWdU3rMY+F6O1fQcOyOoY0JOXOPU04GqPSZ2Lh3UunxMZ2LaEptB6SbFN1b7nUgTXCo73496D8FvIes9q+GrLw65VXVQucKaI+YPhO+F8y9uq9QNqgaGhcep5PePqvAeCxclU+s6pGa83o9VdfeR6q522PIu5yfMqp4JKmojp4Rl8jg1vzralro46CghpYhhsbcek9pWJbP7eJaqSvkGREN2P0nn8XyrN1ZeTmGq6ne+sunwIefbxT4F3BFKLpSvCIoQEqCMjComkbFG6R7g1jRlxPYFY2astrpS0tma0HAfu8D+dRcjNx8dpWyS3NkKpz9VHjvml957p7cWjOSYnHHsP5lh9ZBJDKYpo3MeObXDBW0KW52+pGYauJ3hvYPsS4W+iuEPV1UDJW9h7R6CubzdBx8r+5iySfh3E6jOsq9GxbowXT+pqu3ltPUf3RTZx5x85g8D2jwUXu7R1VxNVQRupyMjrBwe/x8F8tTWqltdYyGnmkkDxvYcPejs49varW3A4LncjKyql5ra/Vf+8ywhVVN9rFdT7Ole55e9xc88SSclYdoC5VFZrjWtPLM58NLVwsiaTkM812QPYsivNyprTaqq51r9ynpYzJIfAdnpPJaS2H6yphtGvguEopm313WRGR2AJA9xDc9+HfErDTdOtysHJvUd+FL903+hGyr4V31R3N/ue7dLd5wHdngsiodTx0lpbTw0mKhnAdjT9kVjjgV8nejKpsbNuxW5VvZtbE2yiFi2keyrrJ6yYzVMpe49p5AdwC9lrs1ZcHB0berj7ZH8vV3q7aUttoqIBVlz5pW8HNl4Bp9HasnfVUkDfpk8MQHwnAK9wNFjkbX5Vi2fv5v5kC7McPQqR5rLaqe2QlsWXPd7955lXBWao1LZ4DjykyHuY0n/sq7XqC3XCfqIXvbJ2Ne3GfQupozMGraiuaXgivnXdLecky7ooBRWZoJUEqVCAjtXxrqKkuFFLRV1NDVU0zCyWGVgex7TzBB4EL7Pzund59mVTFIJGbzfQR3HuXnFtLYbbo5M28dHmazNn1FoOCWpt7cvqLYCXSwDtdETxc37HmOzPZonTtfUUVXFNTPMdRSytngeOBa9pyPYQF+j1fVmikbNMM0rjuueP3M9hPgfiWjOkDsNg1C9+r9EU0MN5AL6qiZhsdaOZc3sbJ48ndvHibnTdYXadla+hDyMV7cUTcug9QU+qtH2y/U+N2tp2vc0fUu5Ob6nZC+8rdx7h3FaL6HGpJBS3nRdd1sdRRymqhilBa9gJ3ZGFp4gtdg4+yK31XjFQB8MZHpHNUesY6qm0ui/ZkzEs4oo86okaHNLT2qsKPSqJrcmotMjCx5aexeigrZKWTtcw82/n9K+ldHkB47Oa8WPWq9uVNm8DfynHmXDVunbXq+yMparLHxStqKOpj4S007DlsjD3g+0ZB4FXukbM2libUvbJMGASPa3Ac7HEgdgz2KwW2rdSy4dxjdzH51kUbmvaHNOQeIXTYmZ5xXs+4r7auCRUoUopZrKSikqEBUiIgC0f01P8AM9F/zan+R63gtHdNb/M/D/zan+R6k4f48Pia7vUZxeso2Xavm0JrWj1PBQMr30rZG9Q+Qxh2+wt99g4555LFgVlWybSjNc68oNLvrnUArBIevbFvlu5G5/LhnOMc11lvDwPj6Fat9+RvEdLGs3eOhoST3XI//wCtYPr7pB671TSS2+nkp7DQyAteyh3uue09hkJyPuQ1bCHRPZjhriTPjb2n/rWPao6Luq6GndNYb3b7wW/uEkZp5Hegkubn0kKqrlgJ7o3yV23M0tpzT171LcRbrBbJ7hUhu8Y4QMhucZOSABxXRGybo0bk0F12gTxyAYcLVTvJbnuleMZH2LeHj2LnO60F407eZbfcaartlwp3YkifvRvZ3YI5jtBHA96zDRO2HX+k52eSX2etpmnzqWucZo3DuyfOb6QQpmTC6yP9qSRrrcYv0jvWlggpqaKnp4Y4YYmhkcbGhrWNAwAAOQC+o5LWuxfa9Y9o1K6mZGbfeYGb89HI7Ic34cbvqm/GO3vOyuzxXLWVzrnwzXMsYyUluguROmdrA3HVlHpKmlBp7ZGJ6gNPOZ44A+Ib+Uuq9R3ajsVirrxXyBlNR0755XE/UtGf+3rX5w6muldqLUlddqkPlrbjVOlLRxJc93Bo9oA9Cs9JpUrHZLoiPky5cJeGaNuUuzGbXTGu8ihubaFzd3sLM9ZnuDi1npKxfOCu/LDs4oINh0OzyrY0NltpiqHgf6Q4bzpB4iQ7w9AXBt2t9Ta7pV2yuYWVNLO+GVuOTmuLT8YVriZayHJeD/QjWV8CR190NdXe7Oz+bTVVLvVdkl3YwTxNO/JZ7DvN8AGre3A8fYuB+jnq46Q2rWuplk3KCud5DWZOAGSEBrj3brw0+jK74HJUmo0dldv3PmTMefFHbwOFelPpZ+mtrlwqIaJtPbrqG1lLuDzXEtAlHges3jjucFqvJyADjxC766QOz+PaDoKooYI2e61Hmot7z++AcWHwePN9OD2Lgd8b4pXRSscx7HFrmuGHNIOCCO/PyK507I7apRfVES+HBI7p6NGvPo22ewx1kwfd7XilrMni8AeZJ90BxPeHLLNqOrKXROh7lqGrwTTx4gjzxlldwYwel2PVnuXFOwnXUmgtf0dzkkd7m1BFNcGA8DC4jz/Sw4cPQR2rNOl7tCZqPVkGlrVVMmtdpHWTPjdls1S5vPI4EMaQPS5ygWac3lJL1XzN0b/7fvNOF101HqIYElddLlU8hxdLLI785PqC/QDZNo2l0JoWg0/Thrpo2dZVzNH67O7i93t4DuAA7FoLobbPjU1kuvrnADDBvQWwOHN/J8o9A80eJcuqVr1TJ45KqPRGWPXsuJnwuFVBRUU1ZUyNjggjdJI4nAa1oyT7F+dO0vU9TrDXd11DLkmrnJhYPqY2+axo+5AXWnS61cLBs59xKeUtrb0/qBu82wt4yH1jDfulzl0btJ/RXtetUMsQfR293l9UCMjdjI3Ae/LywejK3abXGqmV0jDIlxTUEYztB0nctF6gFmujSJnUsFQCW7oIkYHEfcu3mnxaVabBdqyx36gvNA7dqqGpZUQn7JpBA9Bxj0Erqvpq6RFw0tbtXU0QM9sk8nqSBxMEmME+DX4+/K5ILcnj61Y4t3nNKk/maLI8Etj9LNMXmk1Dpy3X2gdvU1fTR1EfHOA4A4PiM4PoVzXP3Qt1YLjoyt0nUyg1Fol62nB5mCQk8PQ/e++C6BXMZNXY2uBY1z44pmE7eP8AMzq//lFR+QV+ezuZX6FbdhnY1q8f8IqPyCvz8tHVuvdCyeMSwuqYxJGfqml4BHsyFdaQ9qpP3kXK9ZHyAHLkul+iRtW6mSLZ7qGpJjeSLRPI7keZgJ9pb6x3LUe2vZzX7O9WyUT2OktdUXS26o7Hx594T8JucH1HtWCMkkhmZJFI6KRjg5j2nDmuByCD2EKwurry6du59CPGTrkfp3nK+FzOLdUn+Jf8hWp+jXtVj15p73JuszRqK3RgTgnHlMfISt8eQcOwnuIW2Lnxt1SP4l35JXKzqlVZwy7iyUlKO6PzIf71x8Cv0c2XDGzPSw/4PSf2LF+csjfNcPAr9HNmIxs20wO60Un9i1XGr/hwIuL6zNSdNv8Azc2r/mrf7N65ByuwOm0M7NrYe66s/s3rj9StL/Lr4mvJ/EOq+gyf8H9Sj/fIfyCuh7ocWyqI/eHn4iueOgyP8H9TH/fIfyCuh7r+xdUP4l/5JVLnfmpfElU/ho/Mlg8xn2oWyujEP8e+mD/GVH/5pVreMeY3waFsfo3VNLRbbNPVVbUQU0Ebpy6WaQMY3NPIBknhzIXR5C/sS+BAj6yO9VKsw1VpkjhqK0H/AObH+kp+ijTfP6ILTj+eR/OuQ7OfgWnFHxPpq39qt2/mU39m5fmzGPpbftQv0N1bqnTR0zdGN1BaS91FMGt8sjy47hwOa/POP9bbw+pCvdHTjGe5Dymm1sbP6LPDbvp4+FV/+aRd1Lhbos/59tO+ip//ADSLuhRNX/H+RsxfUZK0z0uNZfQzsyktdNLu119eaRmDgtiAzK773Dfu1uUkrhHpU6v+ira1WwU8m/Q2Ye58GDwL2nMrh6X5bnuYFp06ntb1v0XMzvnwx2MD0/YbnfYrlJbacyNtlC+uqMA+bGwgH18fiKtQK7C6Heiqeh2bVd9r6dskmoHFm69uQaZmWgehxLj7FzBtQ0xJo3aBedOPz1dJUkQE9sLgHRn71zfXnuV/Rlq22VfgQ51uMVLxN8dCXV4E100VVS8HDy2iaT6BK0f0T7V1Kvzg2aalm0hrq0aiiJAo6lrpgPqonebI370lfozS1EVTTRVNPI2SGVgfG9pyHNIyCPUqbVaeC3iXeSsaW8dvA+3auLemgMbX4T32mD8uRdpLi7pocdr8HhaYfy5F5pP5j5MZPqGkR2rJdmWs7noTV1JqG2EuMR3KiAuw2eI43mH04yD2EAq4aK2fXDVuhdQ3uztkmrrLJE91MB+vQua8v3e0vG6DjtGe3CwcHuXQNwt3h18SEt1zP0p0bqO16s01RX+zziajq495p5Fh5Frh2OByCO8K8DkuHujTtTk0HqMWq6zu+h64yATb3KmlOAJR4cMO8MHsXb0UrZY2yRPa+N4Dmuacgg8iD2hcvmYrx57d3cWNVnGvec09PD9j9Ij+PqvyY1rLoin/AB5W7+ZVX5AW0OnY3Ns0mT2VFT+RGtZ9EZn+PC3nuoqr8gK0p/IP5kaX4x3GiIqAmlJRSVCHoREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBSFCkICVClQgI7+K0hq+s8v1FW1IOW9YWN9DeH5luK/1QobNWVZO71ULnA+OOHxrRRJJy7ie0rj/Km/1Kl8S10yHOUz5levSrd6urZexu60f+epeVe3Rg3qWqk+FN8mVyK6MtX4F7wpRQTheIAqt9RUOiETp5XR/BLyR7F8yVBKzUpLkmYtJ9QEKAr12in8qulNT4yHyDPoHE/FlZVxc5qK7xJ7Lc2Jpqk8js1PERh5bvP9J4q4qMhrM8gApX1THrVVca13I5mUnKTk+8lERbjEKFKIC3aijkmstXHECXmI4A5ngtaB2DgnjywttkcV8G0VI2QyNpYQ88S4MGVz+r6JLPsjOMttlsTcXL7CLW25raChrJgDDSzP7i1hXsjt2oIx9Jgq2Dwkx+dbExjgOCYUWryXrgudj39xslqMn/AMUavqaC7SzF89HWSP5FzmFx9q+Rt9c3nRVI/wDad8y2rhMLGXkrW3v2j+hktTkv+KOaOkB5XR7NK3MM0YlngicXMIG6X5PyLlypdjiARjiMcwV3N0rQP1Dr0ccetpv7eNcLTu4HHcu/8mNPjg4Mqk9923+iKPUr3fcptdx3JpyhutRp63TTUNX1r6SJz96M5zuDK9UlpuZ5W+p/BrYOnn9bYbfJ8Olid7WBe9cHb5K0ym3xsuYalNRXI1hFZ7yeDaCobnwwFTJZbtH7+gn9IbvfItoY45Ref9LVbbdoz3+oz39VGopopYXbs0T4j9m3Hyr72YvfeKRsBJf1zThvYMjJPhhbUfFHI3dexrh3EZXygo6SB+/DTQxO72MAKjQ8lZQtUlZyX1NktS4otOJ9m+9GealMKV2SRVBERegheKsk8jqGVBP0mQhkv2JPJ35l7l8auFlRTSQSDLJGlpC0ZEJSg3HquhlF7PmVSxxyxOjkaHMcMEEcCCsNdcKjS9zNLU701re7zDzMQ8PmV/05UvdFJQVDy6opHdW4nm4djvWF8dT0UVXB1crcseMZ+Ce9VOXN348cmnlJf60yTSlGbhPozH7zoejqta2rX+nHxUt1ieGVhb+t11O7zXh32YHEO+xAPYRlt6BbRdeBxhIdjw5H4srCtNXSfT92Fqr3nyOU4jceTCeR9B5H1LYMzBLC+M8nNIPrUunN/qOO0/WXI1zo83s5dGWppDgHNOQeIKLxWqQiN1O730Rx8a9yrq58UdzfJbMokbvNLe9WwjdJB7CrrheCsbuzZ+FxWjJjy3M4PnsfBXSyVhbJ5NIeDveHx7la0bkOBacOByD3Face902KSMrIKUdjLlK81vqBUUrZBz5OHcV6V1sJqcVJd5WtbPYIiLM8CIiALR3TW/zPw/8ANqf5HreK0d01f80MH/NoPyXqTh/jw+Jru9RnF+Fs/oqD/Hvp/wARU/2D1rLC2h0VR/j2sHg2p/sHrqMp/wBmXwK6v1kd3ZQjPagRcaWpozpiaQo7ts8Op4qZguVnewmYDDnU7nbr2HvAJDh3YPeVxz4hd39Jusgo9iOoevOeviZAwd7nSNAXB44ErptIcnS9/ErspJT5F60TqCs0vqm3X+hldFNRzteSPqmZw9p8C0kL9GqGoiq6KGqhcHRTRtkYe8EZHyr8ypATC9o7QQv0k0fE+k0hZ4JRuvhoYWPz2ERtBUfWYr0ZLrzNmI+ppPpm6y9zdM0ejaST+6Lqevq8Hi2nY4YH3T8epjlpfox6TGp9rdukmj6yjtOa6fI4bzP1set5B9RVn236p+jHabd71HIZKTrfJ6PtHUx+a0j7bi77pY9YdR6l086V+n7rc7aagASOpHuZ1gGcZLefM+1S6cd1YvAns2apz4rOI/SPAAwuLumDpdll2oNvFPFu016p+vcQOHXM81/rI3D61hEW07aePe6w1J+GefzK26n1Tq/UsMMepLvdblFTuL4hVAuDCRgkcO5RsLElRapOS2NltvHHbYx0jhjiv0C2D6tOsdl9pus0m/Wxx+S1mTkmaPzXE/bDDvulwCB2rfnQz1j7l6wqtIVUpFNdmGWmBPBs7Bkj7pmfvVI1SjtKeJdUYY8+Gex17jvXH3S92dCw6mbrO1wYtt2kxWNaOENTj33oeAT9sD3hdgjvWu+knEyXYhqgPa127SB4yM4Ie0g+lUeDdKq5Nd/ImXQUonBTuGFc9Fadr9Xawt2nLYxxnrZgwuA4Rs5vefBrcn1K2P5n0rb/AEOYRJtqjef3O21DvjYPzrqMmx11Smu5FdCPFJI7I0xZqHT2n6GyW2IRUlHA2GJo7gOZ8TzPiVciiwrbhqwaM2aXa8skDasx+T0fHiZpPNbj0cXehpXHxTtnt3stG1CJyT0mNYHVu1GubBKH0FqJoabdOWktJ6x49L88e5oW8ehlpRtr0JV6oniIqbzMWxEjlBESG49Lt8+xcgPdk5c7e45cSc5Peszsu2XaFZLVTWu16tfTUdLG2KCIQwEMaBgDiwldLk4zlQqa3sV9dm0+JndutLJT6j0pc7FVAGKup3wnPYSOB9uCvzkuFJNQ19RQ1Ld2emldDKO5zXbp+MLPBt62o/7Zv/F4P0Fg14u9Ve7vVXa4VDJ6yqkMsz2ta3eceZw3AGVjp+PPH3jJ8me32KfNIzbo/wCrDo7anabhJKY6Kpf5HWZ5dXIQMnwDt0+pd9jlwX5iY4cF37sC1e3WWzG13CSXfraePyWt48RLGACT6Rh33Si6xRzViNmLPrE9G3l27sX1eR9aKgf0CuArE0P1DbWntrYR/WNXfu3kZ2L6wH/CKg/0CuALE7Gobae6thP9Y1ZaX+BP/e4ZHro/Q3aZoq0a80nUWK7sDQ/z6edrQX08oHmvb6ORHaCR2rgXXOlrto7VFXp+9wdXVUzuDhnclYfeyMPa0j84PEEL9IQBgLV/SH2YQbQtLmWiYxl+t7S+jl5GQczE49x7O44Peoen5rplwS9V/obLquJbrqcUaVv100zqCjvtmqTT11G/fjd9SR2td3tcOBHcV3rs411a9oOhfdq3kRy9U6Orpi7LqeUN4tPeO0HtGD6Pz9qIZqaokp6iN8M0TyyRjxhzHA4IPiOKy3ZNry4aC1MK+me99BUsMFfTA5EsZ7QPhNzkH0jtVxm4ayEpR6oi1WuD27jDJj+ud+XL9G9moxs50yP+EUv9i1fnJPjMhbxGXEehfo5s24bO9Nf8ppf7Fqh6x+HBG3F9Zmpumx/mzt3/ADaP+zeuPQuw+mx/myt//No/7N648UrS/wAuviYZPrnVnQZP+D2ph/vkP5BXQt2OLXVnuhf+SVz10Gh/g7qU99ZD+QV0NdBvWyqHfC/8kqlzvzUviSqfwj8zIv1tv2oVxsdruV8ukNps9DLXV0+eqgiALn7oLjgHuAJ9StcZ+ls+1C2X0Yj/AI+NM/ylR/8AmlXTW2OupyXcivit5bHk/Uf2nlufoGuf3sf6S+btkO0wcDoa7feM/SX6BYHcmAqL+sWeyib5pHxPz5qdlO0Wlp5J6jRN1jijaXveYm4aAMknB7FhwOQCv0j1a0O0tdh30Uw/oFfm3EPpTPtR8iscDKlkJ7rbYj3VKvbY2d0XDjbtp3/5P/5pF3UuFui43O3XT3gKk/8A15F3SqvV/wAf5EjF9UwzbTq5uidnN1vjXDysRdTRtzxM7/NZ7D5x8GlcAWO1VV91BQWimLpKmvqY4GEnJLnuwSfaSt/9NPVgrdSW7SNPLmG3xmpqWg8OtePNB8QzJ+7Wj9G6kuGkdSUuoLXHSurabe6ryiHrGNJGMgZHEAnCn6dQ66HJdWab57z27kfoppy1U1ksNBaKJgZT0VOyCMAY81oAHyLmnpw6U3Kmy60posB4NurCMcxl8Rx+EGfBqxaPpO7RmjDqbT7/AE0kn5pFY9f7dNW620vVadvdusRpKgtJdFTyNkY5rg4OaTIQDkdxUfGwsim5WM2WWwlDhNVgcPBdwdE7Vg1HsqprfPJvVtkd5FIC7iYwMxO9G4d30sK4h9PetudFDWP0MbUoLfUS7tDfGiilBPAS5zC707xLf/cU/UaO0oe3VczTTPhmdwLjLpoDG12n8bTCf6ci7NC406anDa3R/wDJ4f7SVU+k/mPkSsn1DMugoP7k1aDy6yl+SVYr0qNkX0NXCTWmnaUizVcma6BjeFJKT74DsY4n1HwIWUdBQkw6u+3pPklXSdzoaS5W+ot9fTx1FLUxuimikGWvaRgg+pZ3ZEsfLlJdDCutTq2PzKxjhjC6c6KG13cdTbPdSVGQfMtNVI7+ocT/AET9z3LU23bZtWbOdWvpmtkks1YXSW6oPHLe2Nx+G3hnvGD4DXrXvZIHsc5j2kFrmkgtIOQR3HxVzbCvLp+PQjRlKuR1R06ONn0qf96qBw+0atadEb/PfRfzGq/JCt+0raXNrzZnpuguz9++WmskZUSY/wAojMeGS+nhuu8ePbw93RDOdt9F/Mar8lqiquVWFKEu7c2cSlamjuJERc2WBBUKSoQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERABzVSpHNVIAoUogMT2pVJg0u6NpwZ5mx+kcXH5FqbtWw9sM4xbqXjzfIfYB+da8K+deUNnHmyXhsi/wI7U/EoecNce4K4aJH95XHvld8gVum/Wn/an5FctE/sJ6JT8gVN/xZLfUvPIql5AGXcABlVkZ4rxXqTqrXO4HB3cD1ryPNhnoBBaCORRfKk/yKA/xbfkX0WQ7iVkOgoOtvZlIyIYy71nh86x1Zns3j+lVk2Obms9gJ/OrTRqlbmQT+P0IuZLhpZlNU8NY1na9waPb/wD1fYLxVTwbnSR+D5CPQMfnXtX0SuXFKXu5FC1skSiItpiEREAREQBEUICVCIgNC9MbV9PbdGN0g+imknvDWyx1AcBHGIpWOII5knHxrjqUFzSB2rp3p0txVaTePgVQ+OJcykcV1OmwSxlt3lbe97GdzdHDaUzX+nZ6T3KfQS2aKnp3l0wkEuWEbwwBj3p4La65d6CsmJ9WQ9mKV39qF1CqHOrVV8ox6EyiXFBNkoiKIbgiIgCIiAIiIAoUogMY1A82q/Ul0bkRSfS5sdo/84+pX6tjFRRuDSCcbzT4rwavphU2Oc4y6LEg9XP4sqjR1Z5VZo4y7L4fpbs+HL4lz1LVOfZiv1ZriXx7/uS5LipjZ3rl9iwXy3x3GjdE4ASDjG7uPcr3oavlq7K2Gp3vKaV3Uy73Phy+JfCvj6qtkZyGcj0FVafifFdJZYx9LnZiQdzm8j7MqNhJ0Zmy7+TN1r46v1PNXE0t8mI4AuDvUVdGkFoI5FW7UjcXbeA5xt/OvTbpN+lAOSW8FlF8F84e88fOCZ6CvJXt4Nd6l6ivjWDNOfBZ2reDPI8meBQTjKkry3KXqqOR/bjAVVKXCtySlu9i4aVuPW3KopsgMLd5npB4rKVrbTNR1F7pXZ4OfuHPbkY/OFsgclf6Fe7cdp9zIWZDhs5EoiK7IgREQBaO6an+aGD/AJtT/kvW8VpLpmQ1FTsnp4aanmnf7qwHdijLyAGvycAH/wAKk4b2vi34mu31GcXrZ/RakZHtwsb5HtY0NqMuccAfSXdq12bVdRztVw/FZPmVD7dcg3BtlcPTTP8AmXVXcNkHDfqVsd00z9LGVtG4ZbVwEeEgVrv2rdMWKlfUXi/2yhjaM/TaloJ9AzknwAyvzmFDXY/Y2rH/AMd/zL5vpKlhy6gnZ6YHD8yplpUN/XJXnMvA3L0k9r8Ov6uCx2DrG2Cjk60yvaWuq5OQduniGDjgHic+zTHYrtZ9Lanu8jY7Xp27Vjncuqo3ke3GFtnQPRs1jepYp9RyQ2CjJ85hIkqSPBo4D7o+pWULKMWvh35IjuM7JbmH7BdE1OuNoVBSCBz7dSStqa+THmtjachue9xGMekrqzpLawOkNl1WKWUMr7mfIabB4tDx57h6GZ49+Fluz/Rdg0NYGWfT9IIIQd6WRxzJM/Hvnu7T8Q7Fyv0ur/cNQ7SGWijpayWgssXVAsheWumfgvI4ccea31Ksjas7KW/qokcPZV+9mpNPWqov9+t9loxvVFdUMp48d7iBn1c1+i9htVLZ7JQ2qlYBBR07II+H1LWgD5Fyd0OtH1VdtAqdR11HNFBZ4MRdbEW700oLRjI7Gh54d4XYA5LDVb+Oagu4yxq9luyNxnwR7F8K6jpqykmpKmJskM0ZY9hHAgjBHsXpUYVVu+4k7I/OPaHp2TSWt7vpuXOKGpcyNx5uiPFjvW0grwabvFVp/UNvvlESKigqWTx47d05I9YyPWt/dNjSckF/tOr6OnL46yI0dVuNJPWMy5hOO9pI+4C5zMM4cMwTeH0t3zLrse6N1CbfVFXOLhM/SvT90pb1ZKG70LxJTVkDJ4nD4LgCPlWF9I842IaqP+4n8pqsXRHuzK/Yzb7eTJ19smmppQ8EEAyOkZz7N14HqV76SeTsO1VgHJouwZ+rauZUOzyeHwf+Sw4uKvc4JJyStz9DT/PG7/lVR+XGtK8c+9d7Ct3dC6Nztr1Q/dPmWmbmD2viXSZsl2E/gQKl6aOz8rkjpoax90dVUOj6WUGntbBPVBp5zyDgD9qw5+7K6k1PeKWwaduF7riG09FTvnk48w0Zx6TyX5yagu9Xfr9X3qvJfU11RJUS8Djecc4HozgehVGk0qVjsfcSsmWy4Uba6I+kYtRbRn3atp2TUVngMha9uWulf5rBg88DePqXYXuBYvrLbvxVnzLW/RU0mNN7KqSrni3a28Hy2XI84McPpbT9zg/dLbaj52Q7Lns+SM6YbQ5ls+h+xfWW2/irPmWrOlBoG33fZZWV9rt1NBXWd3lzTBC1pfG0EStJA5bmXelgW5l8aqCKpglp542ywysLHscMhzSMEEdvMqPVdKualv0NkoKS2PzKb2ZW/uhjqz3N1pXaUqJQKa6w9dAD2TxjiB6WZ+8C01tCsb9Ja3vGm6hwaaGrfHGScb0XNjvW0tPrXj03e6iwagt99opA2poKllRHx5lpzj0EZHrXVXxjkUuPiVsW4S3O+duv+ZrV4/4RUfkFcA2BgOorYD21sI/rGrvDafdKXUGwC/3i3SCSlrrBLPC4Hm10RcPmXCFgkYNS2sFzf8ug7f4xqrtM5UzT/wB5EjI5yWx+mI5JhAeARUDJhzN0uNlZlZLtB09SZlYP77wRj3zRynA7xyd4cewlcuE8F+nUsccsbo5WNex4LXNcMgg8wR3LhjpK7NTs+1cay3xFunbk8yUhz5tO/wCqhJ7Mc297fEFdBpebxLsZ/IhZFWz4karlOGO9BX6QbOxjZ/pwd1qpf7Jq/NiSVm44CRvI8M+C/SbZw7e2eabdkHNppTkfyTVjrLXDE9xerNT9NYf4saA911j/ACHrjxdh9NZzW7LqIuIGbrFzOPqHrjgzRfvjPvgpOmPbHXxNeQnxnWXQc/azqP8AnsX5C6Duhxbao/xL/wAkrnroLua/Suo3NII8vjGQf4tdBXh2LTWHl9If+SVS5vPKfxJVPKs/M2L9bZ9qFsrowj/Hzpn7eo//ADSrWkbmCJnnt96O1bM6LzmnbzprdcCQ6oOAf93kXRZL/sS+BBh66O8lKgcgi4/uLUt2p/2tXQf7nL+QV+bMf60z7UfIv0m1Of8ABu6fzSX8gr81I5o+rZ57fejt8Ff6N0kQsrqjavRcONumn/RU/wD55F21e7jS2ez1d0rZBFTUkL55XE8mtaST8S4f6LcjXbddPAOB4VPL+byfOt39NDWYs+iaXS1LMG1V5kzOA7i2nYQXffO3R6itefV2uVGK7xTLhrbOWNX36p1Jqe43+sceurqh0zs/Ugng31DA9S6x2GbG9IO2YWit1Rpqhr7pXRGrkkqI8uYyQ7zGeGGbvDvyuXdk2mnay2i2XTwbvRVNQHVPHlCzz5D96CPSQv0UjYyONscbQ1jQA1oHADuWeqX8CjXB7HmPDibkzCGbINmLeWh7J66YFQ/Y/swfz0NZPVTAfIs7UYVN21ntP6kzgj4HA/SL0dBonahXW+gpm09sqo2VdFGwYaxjhhzR4B7XfEtdQzS09QyeB7o5YnB8bwcFrgcg+nOF17009KG5aKotUU8W9PaJtydwH7hJgEn0ODfaVx6SMrqMK7t6E2+ZXWx4Zs/RzZdqaLWGgbPqKMjfq6ZpnaPqZR5sg9TgfiXLPTW/ztUf/J4f7WVZR0IdYneuuiKqQYH93UQJ9DZGj+i72rEumq/O1ykaOyzQ/wBpKq3Ep7LNcfib7JcVKZmfQROYdXj7Ok+SVdPLl/oHnMer8fCo/klXUGOCg6h+Ykbsf1EY1tI0daddaUqtP3dnmSjfhmaAX08ozuyN8R8YJB5rgPXelrto3U9Xp+9Q9XVU54PbnclYfeyMPa0/FxHML9ISFqfpI7M2a+0n5XbYWe79tBfSO5GZvN0JPjzHcfSVu0/MdMuCXqv9DG+riW66nDZW3eiEM7baM91BVH+i1aila+KV8MrHRyxuLHscMFrgcEEdhC250QXZ220nZ/cFT+S1XuZ+Xl8CHV66O4UUKVyBaEFQpKhAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAHNVKkc1UgCIiA1ftgmJvVHDww2nLva7//AJCwnKzHbBw1DSnvpR8Tz86wxfMtY55tm/idHh/gREgzG4d4K92hnZtUjO1svygLwjjwXp0USxtXCRycHfKFX/8AFm+XUyPsVn1U/dtZHwngK7qwaxd/ccLe+T8y8r9ZCXQu1G3+4afn+tN+QKvHDmMr12OikuFXSUUeRmNpe4fUtwMlZ7dLFRy2V9HTQMY5rcxnHHI8fFWmFpVuXVKyPJL9SLdlRqkovvNb9vFZ9s9Zu2aR/a+Yn2ABYFg5IcMELYWgv2Bb/KO+VSvJ1f8Ae8+5M16g/wCzyPZne1G4fvdN8rv+yuitVNx1HVZ7IGD4yrou0w3xKT97KezlsSiIphrCIiAIiIAoUrxXm5UdotdVdLhUMp6OkidNNK7kxrRklEm3sjxvY+NPeqObUtXYI3Zq6SliqZePANkc9rR6fpZ+JXLPoXKWwraZFdekDebtdpfJoNRxGCnbI4ARmMjqWE8h5gcPFx7yurAQRkEH0KTk48qJJPvSNdVnGtzlzp01ELqnStO2RplY2qe9oPEA9WB8h9i5owtl9Jykjo9t1/iiDgx/Uy4yTxfE0n41rndGeS6jCrUceC9xXXPebN8dDbUtj0/e9Qsvl3oba2pp4OqdVTtiDy1z8gFxGea65o6iCrpIqqlmjngmYHxSxuDmvaRkEEcCCF+aAbyHZ3L9Cdjb+s2TaSf32el/smqn1fHUZ9pv1JWLPf0TLFClUnmqYmE54oFgOiNUVFZtR1vpKrmMgtktNUUm9zbFLC3eb6A4Z+6WfLKcHB7M8T3W5KIixPQiIgChSoQFE8bZYnxu4te0tPrCwzRM7qW8z0Lzwe0j7pp+bKzU8lr98go9aEjgBVflc/lXLa/LsMjHyF3Pb5Mn4a44Th4r9jJ9Qs3Zo5fhAg+pfCzVbYKksk4Mf29y9moW5pondzvzKyY71sypunKc4nlSU69mei+SsnuBLSMNaG5Hb/5lUWx+7N1fwx8YXxLR3Lz1tR5GxlRjg17c+1V87m7HazfGCUeEyBfObjE4eCmKRskTZGEFrhkFRIcRuPgrBtSjuae8tvYrVqGTEUcQ5k7x9Suw4qw3x29WBvwW4VHkvaBMqW8jwQymGaOVvExuDgO/HFbZhdvxNf8ACAK1Nu559y2hZXb1ppXZzmJvyK18m5vinH4EfUFyiz2IiLrCsCIiAKCB2qV4rvcqW10wqKt7mxlwaCG54rCyyNceKT2SPVFyeyPXut7k3WfBCx46ysf7/L+CKpdrWxj92l/BFQ/6rif+RfU2+a2+wzItxnwR7FDoonZBjYfuVjv0b2L99m/BFQdcWIfus34Ip/VcT/yL6jzS1/8ABmSta0DDRgeCnAWLnXVhz+uT/gSr/aq6C5UMdbTFxikzulwweBxy9S205tF8uGuSbPJ02VreS2PSQqerZnO43PoVaKUatikNaM4AGe5SpRAERQgKXsa/G80O49oVJp4DzhjP3IX1ReptdDzZFEcccYwxrWg/BGEkjZIwska17TzDhkFVqMLzme7HnFDRD/RIPwYVcVNTxO3o4I2OxjLWAFfZF65N9WecKPnNDHNEYpmNkY7m14yD6ivKbTayf2Oo/wAA35l7kRSa6MNJ9SljGsYGNAa0DAA5AKpEXh6FGFKIDw1NptVTO6epttHNK7G8+SBrnHHAZJC+ZsNkIwbPb/xZnzK5IslOXiecK8DztpKVtJ5I2nhbT7u71QYAzHdjljwXjOnrCXh5sltLmnIPkrMg9/JXPHHKleKTXRhpMj1KUReHoXkudtt90pxT3Khpq2EODxHURNkaHDkcEYyvWiLdPdAsX0H6THLTFlH/AMCL9FXqGKOGFkMMbI442hrGNGA0AYAAHIKtF65N9WeJJHiutrt11hbBc6CmrYmu32snibI0O78Ec14Bo/SY5aYsv4hF+ir4iKTS2TDimeO2Wu3WuJ8dtoKWiY87zm08LYwTyyQ0BepzGvaWPaC0jBB5EKpF4931PSwHRekO3S1kP/wIvmX3oNLaaoKuOrodP2ulqI87ksNIxj25GDggZHAlXdSsu0n4mPCvAIiLEyKJYo5Y3RyND2PBa5rhkEHmFjP6neg85+g2w5/mEfzLKUWUZyj0Z40n1LDbNHaTtddHXW3TVpoqqPO5NBSMY9uRg4IGeRU6g0hpfUFUyqvmn7bcp42bjJKmnbI5rc5wCRy4lX1QnHLfffmOFdNiwWPRekrFXeX2bTdrt9VuFnXU9KyN+6cZGQPAK/phSvJScnu3uEtgiIvD08l2t1DdrdPbrlSxVVJO3dlhlbvNeO4hYg7ZBsxc7LtEWYn+bhZ0iyjOUeUXsYuKfVGK2DZ1oaw3KO5WbS9soayLIZNDCGuaCMHio1Ts60Rqm5tuWodN0NyrGxiISzMJduDJA5+J9qytQve0nvvvzHAuhYdI6N0vpFtQ3TVkpLWKktMwgbjrN3OM+jJ9qv6hSsW3J7s9S2CpPDsVSLw9MHvmyTZxfLrUXW6aRt9RW1L+smlIc0vd2k4I48F9tK7MNBaWvDLvp/TdJQVzI3RtmjLs7ruY4k9yzJFn2tjW272MeCPXYhSiglYGRBREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERABzVSpUhASoUqEBqbbk8099s0h95NFJG4+gtx+UsQHILOukBTtks9sn5OjqHNB9LSf+kLX1DOJ4Gv+q5OHcV8612vhy5NF/gS3pR6QvVZj1VyGOAkBB9PNeUL6wu6uRkna1wKpSa0ZJ3LGtZv+mUcY7SSsk4EAjl2LHdSx9berezs459qyq9YxfQ2ds1pR1NTWkAk7sTfQACfl+JXH6LLb9Hx0dkiuFD5ZnPDG9jd9OOPoX20NE2PTdOQMdYXPPrJx8S5d1vrKW09Jes1A2QiGhuMdNJx/cmsbHIPyivrPk1pysxFX/8AHf5s5TUchxt4veb21dQ+R3yQtbiOYdY38/x/Ksk2fvzaJGfBmI+IFffVNEy5Wds8OHuY3rGOH1TSOPxLw7PnYZWRdzmu9oI/MuSpx/M9Z4e6W+xZys7XF96LlTPxqqqj+FTsd8ZV5WIahvNtsGpZLpd7hTUFDFQb0s1RIGNHnHHPmeHIcVhP/qT2ZNujaN9fWmFxINWyjkMLOPDOQHexpXR6XCyx2QjFvaT+5AvlGOzb7kblRWnTWorHqW3NuFgu1JcqUnHWU8oeAe49x8DxV1ByFPaaezNaafQlEULw9JRWjV2oLdpfT1bfbtN1VHRx77yOJPc0DtJOAB4rUmxjb3DrbV0+n7vb6a1yVBLraWSl3WAc43k/V44jGAcELdDHsnBziuSMJWRi0mbyXNvTjrqqG2aYooqiVlPUTVDpY2vIbIWhmN4duMn2rpEZXMnTq/W9I/b1XyRqTpi3yYmvI/DZzNvY712J0Maieo2XV3XzzS7l2kazrJC7cb1cRwM8hxPAd644PJde9CV+dm11Z8G7v+OKP5ldaut8ff3kPF9c0r0rRjbneCe2GmP9U1auGOC210t4wzbZXu/fKSncfvMfmWpFLw/wIfBGu312Vjmv0A2Fu39jekT/AMIpx7GBfn5niF310eZOt2J6Td3W9jPvSR+ZV2tfhxfvJGJ6zM9XxqqiCmjdJPNHExoJLnuAAAGT8S+y5b6de6azSI7QyrOPXEqTFo7e1Q323Jds+CPEWjTG021UvSoumpPLomWG6E0L6lzsM6trGhkuT2b0Y49zl1rS1MFVAyopZ454ZGhzJI3BzXA8iCOYX5mF3Z2LffQpu1RFtCuVmNRJ5LU218oiLzu9Yx8fnY78OPFW2fgLs+OL6Ii0XPi28Tr1So8VKoScEREAREQBa21c7qtUVDhwIcx2fHdC2StZ61LXajq8ccbufvQuU8rtvNYf+3+GWOmfiv4GcXk79uDvsgrIr3cv2Ib6GqycFnnvecX4pGNHRhfGrhbPA+Fw4OHsPYvsoKrpbMkJ8zy6crTCDbavzJIzhhP1QV3q5Q2MtB849ncrdJFFIQZGNcRyyOSr4YWddsow4TGUU3uT2LHLi/erZTn6rHsWQkrF5Xb8r3HtcT8agZj5JEmhc9ynPFbK008SWKkcOXVgLWnaFsfSX7XqT7T85Vl5OP8A7iS9xo1Begi7IiLsyoCIiALFNqB/wfj/AJw35CsrWKbTx/g8w91Qz86rtX/J2fAkYv40fia1zkc1XTwVFVMIaaJ80pBIa0cThfILIdnjQdUQnA/W3/IvneLSrro1vvaR0l03XByXcW33AvZ4+5VX+DVLrFex/qqs/BlbqULrf+l6vbZT/wBVsfcjSnuHes8bVWfgT8y2joeCam0zSQzxPikbvZa8YI849ivSeAU7T9Ghg2uyMm+WxHyc2V8eFolF47hcaOgYx1ZOyEOJALivF9E1k+uUHtVlZl0Vy4ZzSfxIyqnJbpF5RW+gvNtr5jDSVkUsgGd1p44717wttdkLFxQe6MZRcXs0SiKCcLM8JRfCtqoKOndUVMrYom4y5xwBngrd9Eti+udNn7dabMmmt7Tkl8WZxrnLmluXhF4rfdKC4Oe2iq4pywAu3DnGV7OxZwsjOPFF7oxcXF7MlFbJL9Z43lj7jTNc04ILxwKRX60SytjjuFO57nBoAeOJWrzujfbjX1Muyn4MuaKF5a64UVDu+V1UUG9nG+4DK2zsjBcUnsjFJt7I9aK1fRFZPrnS/hApF/sxH7J0v4QLR57j+2vqjPsp+DLoitjL9Z3ODRcaYk/Zhe2Gpgn/AFmaN/2rgVshk1Te0ZJ/MxcJR6o+yKOJRbjElEUdqAlFRK9scbpHuDWtBJJOAArZ9EVk+ulL+EC1WX11PackjKMJS6IuyLx0Fyoq7e8jqoZ933244HC9fFZQnGa4ovdHjTT2ZKLzVdbS0m75TURQ73LfcBlfA3q0gfsjS/hQsJZFUHtKSTPVCT5pFwRW4Xu0/XGl/ChSL1aTyuNL+FCx87o9tfU97OfgXBFbzerT9caX8KFBvloHO40o/wDdCedU+2vqOzn4FxReWjr6Osc4UtVFMW8wx4OFFVcqGlk6upq4In4zuvkDTj1rPt6+Hj4lsecMt9tj1orf7tWnAPulSH/3mqDe7QP9ZUv4Vqw87o9tfU97OfgXFFbhfLR9caX8M1VC8WsjIuFKf/db869WVS+k19R2c/A96KiKRksbZI3hzHDILTkEKorcnv0MCUXnq6ympW71RPHE3ve4BWyXVVijIBr2uP2DSVosy6antOaXzM41zl0Re0Vki1TY5DgVzW/bNLflCuVLW0tU3NPURS/aOBSvLose0Jp/MSrnHqj0ooUqQYBERAFCFQgJymVCICcplQiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIOaIOaAqUHxUqCMoDE9qdirb9pxtPQNY6eGdswa443gA4EDx4rRdIZLfXvp6qN8RDtyRjxgtcO8Lp2RzI27z3ta0cy44wsU2gaKo9S0rpot2nuLG4jmA4O+xd3j5PiXPavpDyf7tfXvJ2Jldl6L6GqMdyqAJyrfF5Zaa+S03eJ0EsRwN7u7OPaO4q57vxrhLK5Vy4ZF7GSkt0Xu2P62jbx4t80rw3mIm4Uk2Pehw9CWibq5+rccNf8q9dxZvNYe0HKxi9meG09JcNM2/xp2n4lw3tMcZNo2py7tu9Xn8M5dyaScHaboMccQNHsGFxFtcpzS7UtUQgFv99J34Pc529+dfdPJJpxS/8AijiNUXpfM6r6O2pxqfZlQiaTfq7ePIqjJ4ksA3T62kfGsittK626smhAxBUxF0Z8Qc49XFc1dFTVYsmv3WSpk3KW8s6puTwbO3iz2jeb6SF1jW04mDHsH02Ih8Z8e71jgqryg0zbJjOK5xfEvg+qJODkb1uL+By906oXC76XqOPVugqGY7N4OYfbxK5oPPI4LsrpoWJ9x2aUV6ijJfaq1rpDjlHINwk/dbi46c1dRpLi8ZbdSDk/iM290PLxX0O2KltcNVIyjuNPM2ohB82QsYXNJHeMHB8Su3hyXBfRfd1e3fTZBxvOnb/USLvQclVatFRvW3gScV+iSoOexSo7FVkk5D6W20Q33UQ0ZbJs261SZrC3lNU8t3xDOX2xPcFoqjq6miroa2knfDUQSNlhkYcFj2nIcD2EHism2yN3drWrWj68VP5ZWKO5rs8SqMKIxXTYqLJOU22d8bDtoVJtC0ZFXhzGXOmDYbhTjhuSY98B8F2Mg+kdhWp+nQzNDpKTumqh/Rj+Za86I1ZUU22ihpop5GQ1dNOyaMO82QNjLhkduCMrY3Tp4WrSeP4TU/kNVPChUZ8Yx6Pn+5K7RzpbZy2V1v0IXf4B3tvddc/1TFyOV1n0H3g6M1A34Nyaf6pqn6t+WfyNOP8AiI1d0wBjbPN42+nP5S09lbL6Smp7XqzajU1tpbUCOmhFFL1zA3MkT3gluCcjitaKVhpxogn4Gu17zYXeXRqfvbDtLnup3t9krwuDgOC6R2GbdLHpvSOn9FVtluc1VHKafyiIxmMmSZxB4uB4b4zw7FE1WqdtSUFvszbjSUZczeW2jWs+z/QVVqant7Lg+nliZ1D5erDg94aeIB71zX0uNTW7VNTo242ydktPUWp9S3dcCWb7m+acdoLSD6FuXpgE/qJ12O2spgfwgXE53uALicDAyezuUPSseMkre9NmzJm0+EjOQFsvowXX3J222RznbsdUyemcTy86Nzh8bAta4V/2Z1jLdtJ01XyyNijhucDpHuOAGb+HEnuwTlW+RHirkn4EaD2aZ150ZNot72h2zUdXfJIHPpLlu0zIowwRwuYC1vDngg8TxW31yj0Ha50WptT2hhHUy0sVR45Y8s+RwXV3ILls6tV3uMenL9ixpk5QTBOFGcq1apvlBYLNW3KuqoIG09O+bD3gE7rScAHnnGF+eFfqK+11ZNV1N6uUsszy97nVTzkk5Pas8TBlkpvfbY8tvUGfpJnxUgr8zn3S5NPXNuNYJGec1wndkEcjnK/Sayyuns9FO9xc6SnjeSe0loK8zcJ4yXPfcVXdp3HrzwWq9RSGW/VrueZi0erA/MtpvLWsJJwACStZUcBrb7GQM9bU7/q3iT8S4HytlxdlUurf+/uXWm+i5zfcjOrv5tsY3v3R8Ssvar1qA4gib2bxPxLy223uqMSSZEf5Sm5NMrblXDrsjVVNRhuzxRQTTOxHG53o5KKiCaB27LG5meWeSymONkbQ1jQ1o7AqKynZUU7o3jmOB7it8tHSr3T9IwWU9+nIxRFL2uY8scMOacH0qkqjaaezJm+5RO7die7uaT8SxkclkNxdu0UpzzbhY+fBV+U95JEmnoykrZOlARp+kz8DPxrWruRWz9PN3bJRj+Jb8iuPJxb3yfuIuoP0Ee9ERdiVIREQBYptQ/a43+cM/OsrWLbTRnTrf5dn51Xat+Ts+BIxfxo/E1gFkWzs41RCD2xv+RWABXHTNwjtV4jrpY3yNY1wLWczkY7V89wrI15EJy6Jo6K+LlVJLwNyIsN+j6i/gFT7W/Oo+j+i/gFT7W/Ou+/rWF7f7nPrCv8AZMzULGrNq+ludwio46SeN8mcFxbgYGe9ZKOI4hTcfKqyY8VT3RpsqnW9pLYw3ajwoqP+Vd8i1+52FsDal/kdF/KO+Ra/e3mewc1weu/nZ/L9i+0/8BHrsde623WnrGngx3ngdrTzHsW5YntkjbIw5a4ZB7wtGH2fmWz9nlzFZZhSyHMtN5h4829h/N6lYeTeXwTdEn15r4kfU6d4qa7jJ1BRUTyMhifLI7DWty49wHFdlJpLdlKYHtTuZc+C1RP5fTZf+kH4z7FgzVcb1UvuFznrHZzI8kDuHID5F4McV8y1DJeTkSs7u46jGqVVSiZrsp/yyu4c42fKVsA4AWv9lQxWV32jPlK2AeS7PQvyK+ZSZ/47NL3Mj3RqfCZ/ylTZj/fqi/nDPygl0/ZKqH8c/wDKKWUZvdD/ADiP8oLh1+Y+f+S95dl8jdCwHawQJbfw5iT/AKVnw5LAtrDcyW4+Eg/JXd67+Rl8igwV/fiYN2q92nTl0uVI2qpI4XROJALpN05BwVZMfKtp7Of2rw/bv/KK5HSMKGZfwWdNi6zr5U18UTCq/Td5oojJLSF7BxLozvY9XNWiOSSOQSQvdG4HIcx2CFu7AIwR2LVeuKOOj1DM2JoayRokAHYT/wDxTNX0eODFW1N7EfDzHdJwmkXXSOrakVUVDdH9Yx5DWTEYLSeWe8eK2ACCAQtHYwe7xW5rJM6otFJO45c+FpJ8cK18ns6y6MqrHvt0Iuo0RralHvPYiKO1dMVhjO0W4GksZpo37slUer+5+q+Lh61rDHHgsj15Xiuvz2tdmOnHVN48Cc+cfbw9StFRQTQUdLVPadypDtz1FfO9XyZZOTJx5qPI6LCgqqlv1ZcdD15oNQQgnEU/0p/HvPA+3HxrbHitHjg4EcCORW3tOXAXKzU9Vnzy3df9sOBVx5NZW6lTL4oh6pVs1NFj2g2+trX0nklNJMGh29ujlnCxB1hvRP7F1P3q27hFOy9BqybXa5NNkenPnVFRSNOVtsrqKIPq6SSBpOA547cLx59C2FtQx7kU5/jx+SVrtcjqWHHEvdSe6WxcYtrur45HroqCtrmuNJSyThhw4sHJfU2C9uP7FVP3qyrZc0GKtJ+E35Cs3Vxp+g15VCtc2myFkZ86rHFJGF7OrbXUM9W6rpJIN9rQ0vGM81ZdpjW/RGzgM+Ts4+srZ2AtabSh/hEw/wC7t+UqXq+IsTTlVF77M1YdrtyeJ+Bi2B3fErhFp681EDJ6e3ySRSDea4FvEe1eEc1t/Sg/wdoOH7g35FR6Rp8M62UZtrZE/MyJURTijWH0M34f6qm9o+dS3Tl9H+qaj2D51uH1Ir5+TFHtsr/6pZ3pFv07DNBZKOGaMxyMiaHNPMFWnWmonWljaWl3TVSNzk8ox3n83oWTLUWrZ3VGo655JO7KWDwDRhSNZyZYOLGFb5vkasKqN928uh46momq5jPUyPmkPNzzk+ruV2temLvXxtkZCIYnDLXSndyPRzVtsbYX3mjZUEdUZmh2eXP/AM9q3IwDdAaMDsCodG0yGc5Ttl0LDMyZY+0YI1rU6QvELC5jIpgOxj+J9RwrEY5qerEbmyQytdggghwK3Qrdd7NQ3MN8oiHWN969ow4fOFZ5Pk3BelRLZ+DItepS6WLc90JzE30KtGjAAznCldRBNRW5VvmFBUqkrIBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBSFCkICUREBZtbWz3Z0ld7UB51VRyxNOcEOLTgj0HBWiOjVtyfd5qfRGtKgNujfpNFXSHHlRHDq355Sdx+q9PPo5wyCF+de2yxP0vtb1Da2gxsZWmopt04wyT6Y3B7Mb3tCn4VUb1Kt9e4j3ScGpI701ppW26nouqqWiOpYPpNQ0ecw/nHgtK3KmuWmbsbTembrT+sTji17e8Hu+MKejJtx934qbRmsKrdvLW7lDXSHArAOTHk8pfH6r08966lsNt1DbH0NxgEjHcWOHBzD3tPYVzWtaErW9ltL9yxw81w+BpFry0hwPiCr5HK2ppo5QRxHHwKsupNPXbR1T1VYDU2t7sQ1bRwb3Nd3Hw5dyps1c3rHRB4LX+c3HafBfPcjHsom4zWzR0Fc42LeJuPQEwl07FH2wucw+3P51yt0pLU+2bX62pIAjuNPDVsx9r1bvjjJ9a6T2X1QLKylJwQWyAengfkC1r0yrC6ewWfUkUeTRzupZyBx3JBlpPgHNx90vrXkdlbwqb71t/v0OT1ernL6nMsFRNS1UVRTSuinie2SORvNjgcgj0Hiu7NkmsYNcaFob5GWNqC3qqyMH9bmbwcPQffDwIXBp5rZfR62hnQmrupuEjhZLm5sVXx4QvzhkuPDOD9ifsQF2WsYfnFPFH1kVOLb2c+fRnXus7FT6m0pc7BV8Iq+mfCT8EkcHekHB9S/Oa8UFTarrV2ytYWVNJO+CZvaHtJBHxL9L43Mkja9jg5rhkEHII8Fx/0xdFutGuIdVUkO7Q3lobMWjg2pYMHPdvN3SO8hypNHv4Jup9/wC5NyobpSRo231tZbq+Gut9XPSVcLt6KaF5Y9h7wRyPFdxdGHVt31jsvjr75VeVVtNVyUjpiPOeGBpBd3nDua4XLcldf9CWXGy26sJ/W7xIfbFEfzKbq8E6uLbnuasZ7S2N9ouJ7T0k9otvuz6mrmo7pRulcfJZ6dseGk8Gh7ACCBwGc+tdgaKvkeptI2nUMUDqdlxpI6kROdks3m5xntx3qjycOzHScujJldsZvkcHbaOG17Vo/wCLT/lLEjzWYbcG7m2LVw/4nKfbgrDu0LrMf8GPwKyfrM2j0WHbm3SwfZCpH/15FtTp0/sNpQ91VUfkNWoujNJubctNHvlmb7YJAtvdOYZsulT2eVz/AJDVWX/n637vub6/wZHK/Yureg27Om9TMPIV0R9sf/Zcp9vgup+g2/8AvLqlmOVVTn+g5SNU/Lv5GOP+IjmzV5/wvvXjcaj+0crYrnq0Y1beR2i4VH9o5W0KdX6qNL6k5Vy0w4N1PaHHsr6c/wBY1W0r02l/V3ahkz72pid7HtSeziwup2j0tI+s2JXM/AqKd39aB+dcROHFdx9KvB2HXj7en/tWrh13Mqs0f8B/EkZPrlKpIyMYVRQc1aPoRzevQlk3Nptzj+HaH8PRLGutdRXegsFjrbzc5XRUVFC6ad7WFxaxoyTgcT6lx/0NH7m12Vn75a5x/SjP5l05tzAdse1YP+FT/klc1qME8pJ9+xPx21W2ccbfdVW3WW06vvdnqJ57dJFCyEyxuZgtYA7DTxAzkrAD6VJ4nxULoq641xUV3EFycnuz5zfrbvtSv0p0g/f0laH/AAqGA/1bV+a8gyx3oK/SHQD+s0LYH599bac/1bVTaz0gSsTqz16knNNZKqVvvhGQ30ngFiWiIDLeWyY4Qxl3rPD86uu0CqDKWCkDuMj94jwH/wDV9tC0hhtrqlwwZncPtRwH518vyv8AvdbhX3QW7/f7HQ1/2sSUn1kXWspvKamJrgerYN4+PgvvUzQUVJJPPKyGCFhc97iGtY0DJJPdhfUndGc4AXNXSM2km71b9I2Wf+98D8V8zDwneP3MH4IPPvPDsOenscMdSsfVmOm4FuoXKqHTvfgjJrdtjrtSbVLVYbBDEyzS1Lo3zSMPWVDQxzi4A+9HDh2kexbwHJck9GqhdW7VqOcNy2ippp3HuJG4Pyj7F1tyHBMOydkHKXiTfKHFoxMiNNK5JLf4mP6gg6upbK33sg4+kK2LJL5D1tC4gcWHfWOAeKodSp7O5td/Mg4894HgvTsUmPhOH51ZexXLUL8dTGD3lWwFc5kv+4yxqXok4zwHM8ltaiYI6OFgGA1gGPUtY22I1Fwp4R9VI0fGtpt5LovJuv15kHUZc4olERdUVgREQBYvtL/a6P5dn51lCxbaaf8AB0fy7Pzqu1b8nZ8CRi/jR+JrQL0WuhnuVcyjpt0SvBI3jgcBleZX/Z8P8Kac/YP/ACSvneJUrb4wl0bSOjuk4VuS7kfYaJvZ+ppvwh+ZQdE3z4NN+E/7LaCYC7X/AKbxfFlJ/UrvcYJpjTF1t96p6mobD1bCd7dkyeR8FnYRSrPCwa8ODhX0fMi3XyulxSMK2pH+56EfZu+RY5pigF0fXUXDefTEsPc4OBHxrItqf61QD7J/yBW7ZqP7+S/yBz7QuUzK426twS6Nr9i2pk4YfEv95mKPY5jix4LXNOHA8we0K76PuXuZfIZHnEMp6qT0HkfUfzr2bQLb5FezUMGIqob48HD3w+Q+tY7jnn1+CppKeFk7d8WTYuORT8Ubw5+hYptHuvklsbQxO+m1J447GDn8y9+jLmLjZIy92ZoB1cnq5H1ha/1XcRc73UVLDmJvmRfajt9ZyfWF1+qalHzJOD5z/wBZTYmM3ftLuPvpah8oFZWvGY6Sne7vy7dOPn9ix5vvB6Fs23W73M0HVMe3dllp5JJPSWnh6hgLWQ5YXM5+J5tXUn1a3ZaY93azm+5Gb7K/8rrvtGfKVn5WvtlJPl1b/Js+UrYJXWaD+RXzKjP/AB2aYug/vlVfyz/yiqrGP790P84Z+UFF0/ZKq/ln/lFTY/2cof5wz8oLiI/mPn/kvf8A9PyNyjksF2qjJt/pk/6VnQWD7VOVvPjJ/wBK7vXOeDL5FBhfjxMEA4etbR2djGl4ft3/AJRWsSOCu1r1LdbZRtpaZ0IhaSW78eTknK4/SMyvEvdk+m3cXOZTK6HDE2xI9sbC9zgGjiSexam1RXMuV7nqYjmPgxh7CB2qLnf7pcmdXU1JMfaxnmg+nvXwtFBU3OsFLTbnWOGfPdgYHMqbqmq+f8NVUeX6s0YuJ5tvObPPTwSVFRHTxN3pJHbrR6VuWggFNQwU4AAjYG+wKyaZ0zT2kiomf19Vj32ODfQPzrIVeaHpssSLnZ6zIGbkq5pR6IlW3UdeLbaJ6r6oNwwd7jwCuSwDaZcd+qgtsbsiMdZIB3ngAp2q5Xm2NKfe+S+Zpxau1tUTE6SCWuuEVOzzpJ5A3PieZ+UrZOq7QybTJp4GDfpWh0Xq5/Esd2aW/rrjLcXsyyBu4wkfVHn7B8q2C4bzSDxB4Km0XT1ZizlNevyJmdkONsVH/iaS5jgsx2Z3Dcqp7c93myDrIx4jGfix7FjeoqQ2+9VNNjzWvy37U8Qvjaax1Dc6esH7k8OOO0do9mVzuJbLCy033PZlldBX0v3m6FK+cL2SxMljdlj2gg94K+i+lxaaTRzO2zMQ2o/sPT/zgfkla7HJbF2n/sPT/wAv/wBJWvMLgPKD85L4I6DTvwEZzst/Wq77ZvyFZwsI2XD6VWn7JvyFZuuq0T8lAqc38aQWtdpX7YY/5u35StlLW20r9sEf83b8pUbyj/J/NG3TfxjFwFtTTVxoI7DRRyVlOx7YGhwMgBBx6VqxXKDTd6qoY54aBz4pAHNdvt4j2rltKy7cayUqocW6LXMphbFKctjaJutsH+n0v4ZvzqYrjb5pBHDW073uOA1srST6srWP0J3/AOtzvv2fOrjpvTd3pL9SVNRQlscb8udvtOOB8V0NWsZs5qLpaXwZWzw6YxbVhsgcVqPWVNJS6mrGubgSP61niDx+XIW2xwACsmq7BFe6dpDhFUx/rchGR6D4KdrWBPLo2h1XNGnCyFTZu+jNUt4ce1ZRZtZ3CjY2GqY2riaMAk4eB6e3/wA4qzXOz3K2vLaulka0Hg8DLD6COC8I588rh67cjCn6LcWXsoVZEeezNn23WFoqsNlkfSyHhuyjh7RwV/ikjlYHxua5ruIc05BWlmBXWx3istcwdDI4xZ86InzT6uwq/wAPylmpKN63Xiivv01bb1s2uFK8dpr4bjRMqYT5rhxHa09oXrHJdfXONkVKL5Mp3FxezJVJVSpKzPAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIApChAgKkREAXInTl026m1TY9UxM+lVtO6jnIHJ8Z3m+1rj96uu1rHpN6VdqrZFdYoIy+roAK+mA570fFw9bN4KVhW9lcmaro8UGcFMc5kjXMcWOYQ5rmHBaR2g9hXVvR32+NrvJtKa7q2sqziOjuchw2Y8gyU9ju53I9vHnymMFoLeI7FOBywujyMaF0OGRAhY4PdH6c1lNT1tLJTVUMc0Ejd17HjIcCtPa22dV1pmfcNPCSpo87zqcHekh+1+EPj9K1T0e9vdRp8waY1rUSVNo4Mpq92XyUvc1/a5njzb4jl1vRVVNW0kVXSVEVRTzMD45Y3hzXtPIgjgQuK1bRo2+jYvgy2xcxx5xfyNTbK7211/igm+l1EjTG9p+q7cj1hbC2g6eh1Xou66fmwBWU7mRuP1LxxY71OAPqU3TS1pr7jBc+pNLXQyNkbPAd1xIP1XY4dnEK+ADCh6Ni24CcG+Se6NuVZG977H5x1cFRSVc9HVRmKogkdFMw82vacOHtBVDcHmtpdKjTgse1iathbu094hbVAAcOsHmv9pAP3S1aCvq+Nd21UZ+JzVkOGTR0z0XdqBqYYdDX6ozPG3Fsnef1xg49ST3ge97wMdi2/tQ0hRa60VXaerC1jp2b1NNzMMzeLHj0Hn3gkdq4Npp5qaoiqaaV8M8Tw+ORhw5jgcgg9hBXZ+wfaTTa7082CskjjvtGwNq4hw60chKwdx7R2HPguc1XCdE+3q6fsydjXKS7ORw9e7ZW2e71dpuUBgraOZ0M8Z+pc049nb4ggro3oj6t05YtD32ivV8ttvlkr+shjqalsZeDE0ZAcRniMK99K/ZXLe6V2udP05fcaSLduMDG8aiFo4SDHN7R7W/ahckSuDu4+KkxnHPo2b28TBp0zPjMDvEcwDj413jsK1Rp+DY5paKrvlsp5o7fHG6OWrYxwLcjBBPguEQO9S1rB+5t4+C25eIsmKi3tseV2cD3Rmm22ohqdr2qqinljmhkuL3MkY4Oa4YHEEc1iPblUj1KcqVXHgio+Brk93uZBs81KdH62tmpm0vlZoJTJ1PWbm/lrm4zg459yzDbbtdl2m0NrpZLE22GgmkkDhU9bv7zQMe9GOS1a5x71QXeK1yprlYrGuaPVJpbH1zxW0dhe1sbMobrE6xuuguD4n5bUiLq9wOHa05zvfEtVA8VWDnHErK2uFseGa3TPItxe6PdeaxtwvNdcGxmMVVTJOGE5Ld5xdgn1ryKBzU+hZprbY8KlVC8RVEUh5Mka4+o5/MqAoJXrB0dtq24aQ1rs0uGnrZDdIqyd0RZ18ADDuvDjxBOOAXODuZUE5Te71px6IUR4YdDKUnJ7shAidq3MxZnuwnWdu0Hr+LUF1hqpqVtNLC5tO0OeS4DGASBzHet17Q+kHonUugb5Y6SlvMVXXUUkEXWUzd3fcMDJDjgLljPDgm8VDtwq7bO0l1RsjbKMeFEjnhRjJTPFBzypbNZBGWuHgu19nO2TZtR6HsVvrtXUNPWU9vhimje143HtYARnGOY71xSTxXyneA05+VRMvFjkJJvobK7HB7o7srrvSapu8VVZayKtpKkNZTTRnea5vaR68+xbKpIW01LHAweaxoaB4Bat6M2lK2ybNbPVXmndDXPgLo4ngh0UbnFwyDycQQcdmcd6vO2XaHR6KshZA6Oa8VTSKWHmB3yOHwR8Z4eK+a4GneY3XX2vnJv6bnSx7TNddFK3ey+veYr0h9pbrLSP0tYqgi51DP7pmYeNNGewHse4cu4ce5czkcsHgvTW1NRW1s9bWTvnqZ3mSWR5y57jzJVVpttXd7rSWqgiMtVVyiKNo7z2nwHNR77pZE/2Pp+m6dVpmNt39W/97jf/AESbGY7VdNRSx48qkFPASObGcSR90fiWyNr+qjo/Q9bdIXsFa7ENG1wzmV3AcO3HE+gFXfRtjpdNaZoLLSDEVLC1mccXHtcfEnJ9a536UeqmXfVdNp2klD6e1gunLTwM7scPuW/lFW835tj7d/8Ak4XHh/WdWcmvR33fwX3N47JtUfRjoSiulRu+UuaYqoAYAkbwd6AefrUzRmGZ0TubCQtUdEe9bkt40/I7327VxDPf5rvkb7VuG/N3Lg4jgHNDlXZ7VuPG19SNn4vmmdZSund8zFL2/fr8DjuNAXiAK+1S7rKiR/YXFfNcZZLik2SYrZbF30dCZb/BwyGBzz6h/wB1sQcliegKQBtRWEcSRG35T+ZZau30Gns8VN9/Mpc2fFbt4BERXRECIiALFtpn7XR/Ls/OspWK7TT/AIPNHfUM/Oq7VvydnwJGL+NH4mtFkOz7hqeD7R/yLHx6Fe9E1MFLqKGWomZFGGPy5xwBwXz/AAJKOTBvxX7nQ5Kbqlt4G2UVs937LjIudL+FCG/2Uc7nS/hQvpHnuP7a+qOZVU/BlzRWo6hsY/1pS/hAvTQXKiuAeaKpin3Mb24c4yvYZVM5cMZpv4h1zS3aMV2o8W0A8X/mVu2ccL8/+QPyhXLabx8g+7/6Vbtnoxfn4/eHfK1cjf8A/mV8V+yLev8AI/74mU62t3uhZJNxu9LD9NZ445j2ZWrcLdpGeHYtVattwtt7miaMRP8ApkfoPZ7Vt8pcPZxyF8H/AIMdMu61s8dtudTb46pkBIFREYzx5HsPy+1ezR9t90b1DGW5hi+mSd2ByB+JWYg+tbJ2e2/yWzeUuBElSd7jz3ez5/WqrSceWXkQhL1Y8yVmWKmttdWXXUnDT1fj+DP/ACStMDmVunUPGw14/wB3k/JK0sFZeU34sPgR9L9WRmmyn9kK7+SZ8pWxHLXmykf3wrf5JnylbDPJXGg/kV8yFn/js0xdP2Tqv5Z/5RVdi/Zyh/nDPlCpuv7J1X8s/wDKKqsf7N0P84Z+UFxEfzK/9v8AJev8L5G5AsH2q/6v9Mn/AErOFg21X/V/pk/6V3eufkpFBg874mD8wtl6Bhjl0tEx7GvBfJnI+yK1mCtobPOOmYPt3/lFc15OxUspp+DLPUntVuvEwLU1sdabvLSkHqz50R+xPzcvUvBRzzUtXFUwO3JY3hzSO9bR1lZxdbYTG3+6YcujPf3t9fyrVm6WnBBBHAgqNquHLByN49HzRtw71fXtLr3m4bFcYrpbYquI++Hnt+C7tC9/MLVujLybVcQyRx8mmIEg+Cex3/nYtoNIc0OByDxyF2Ok6gsulN+supTZeO6J7dxRVTMp6aSeR26yNpc49wAWmbnVPrq+oq5CQ6V5djuHYFsLaHcOptrKCNwElRxd9qPnOPjWIaZtouF6ggc3MbTvvzyLR/3VFrt0snIjjQ7v3J+nwVVcrZHht+o7rbIPJ6KrZHFvF2Cxp4nxIXrGt9QcvLIj49S1bOFotef2OpfwTfmU+5dt+t9L+Bb8ykw0bNhHhjdsvma5Z1Enu6zT9xudXdKkT1krHyBu6CGhvDj3L4ArbN8sVDV2mpggpIIpXMO45sYBDhxHLxWpeI4OGHDgQeYVBqmBbiWJ2S4uLvJ+JkRui+FbbGzdnlx8rswpnuzJTHc9LTy+b1LKFqjQdxNDqCJrnYiqPpTvSfen28PWtrZXX6HlecYqTfOPIp86ns7nt0ZiW0/9iKf+X/6Stedi2JtN/YeD+X/6SteLmPKD87L4ItNO/ARnWy79Zrftm/IVmywnZf8ArVb9s35Cs2XVaJ+SgVOb+NILWu0r9sLP5u35StlLWu0r9sDP5u35So3lJ+T+aNum/jGMLcGmgBYKAf7uz5AtPhbg02QbBQcf9HZ8gVR5MP8AvT+H+SXqnqIuBTBRF2vIpRwTCZWOfRRT099qbdW7sTGPAZL2DgDg93pWi/Jroce0e2/JGcK5T34V0Mic1rgQ4AjuIVmuWmbNW5c6lbFIeT4vNPzFXhrg5oc1wIPLHap7l7bRVfHaaTEZyg+T2NZal05PaMTMeZqZxwHYwWnsB+dWLPctl68nii09NG8+dKQxg7c55+rmtZ8+K4HWcWrGyOGvp4eBfYV07a95mbbM6h7vLKcnzGhrgPTkfmWbrC9mdM9tPVVZBAe4Mae/H/8AVma6/Q1JYUNyozdu3lsSoKlQVbEUhERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAVIoClAFRIxsjSx7Wva4YLXDII7lWoIQH53baNKO0RtOvGn2xltIJfKKHPbTyecwAnnu8WE97SsQ7Mrrbps6LNw0tQa1ooC6ptDuorC0cTTSHg4/aPx6nuPYuSBy4Lq8G7tqU31Ky6HDNlWVsTZFtc1Ns7q2w0snuhZ3OzLbp3ncHe6N31DvRwPaFrzsQE96kWVxsjwyW6NcW1zR+gmzPappDXlOwWq4Ngr93MlBUkMmZ34H1Q8RlZzwxzX5kUs81NOyenlkilYd5j43FrmnvBHJbUsG2/aNR0LKWLUkkojGAKiGOR+PtiMn1qps0Zyl/al9SSsvZekjYfTUrYJL/pyhY5pnhp5pH45gOc0D8krn4cF7dSXq6aivE12vFbJWVkxG9I89g5ADsA7gvBniujw8d49Ma2+hBtnxzciveVw03fbnpy+U15s9U6mrKd+9G9vI97XDtaRwIVsyp7FulFSXC1yNa5HcOx7ahaNoNsDPNo7xCweU0bne1zPhN+Mcj46l6QWwGSeoqNU6CpA6R5MlZaWDG8eZfD497PZ3LQdoudfaLjDcbZVy0lXA7eiljOHNP5x3966q2Pbd7XqJsFm1W6G2XY4YycnEFQezj9Q49x4Hs7lzWTg24c+1x+ngWFd0bVw2dTjYwtZK6KV3VSMcWvY5pDmkcwQRwPgV9Gspc+dK8jwb/wB13Hte2K6V2gtkrwz3KvZHm19MwfTD3St5PHLjwdw59i5B2mbNNZ7P6x7b5bJJKHexHcKZpkp3jsy76g+DsFS8bUarls+TNdmPKPwLLA20gjrTUewL1tFi7M5+yBXgsVmvl6/Yey3K49maWkklH9EFZDHs12iyty3Q2ofuqF7flCm+d1xezaIzqk/E8cbbU4gMEBXqZQ254z5NE7xwvu3ZVtJcf2j3v10//dfVmyrafH5zNF3xvoiH5nLJZ9C6tGLx5vo2eb3Ltx/0WP2KHWW3OHGAN+1cQvrV6N2nW9u9LpDUYaO33PfIP6IKtNTX3+2kNuloq6cf7xTSRfKFtjm40uhrdFy6HsfYKI+9dK30Oyvk7T0ePMqHj0hUU+oqZ/B8b2+jivdDdqGTlMGnucC35Vt4qJeBhvai3SaenHvJo3ekYXins9wjGep3x3tOVlcc7H8WODh4Oyq8545WfYQl0HbzXUwOaOWI4kjew+IwvlvcMrPnNYRhzA4eIXiqbdQTcXUrAe8DHyLXLEfczZHJXejD85TmsgnsEDhmGV8Z7ncQrbUWmrhPBokHe0/OtUqZx7jarYy7zxIqpGPjOHtc0+IVK17bGxBMlThUuO6CSPX3LzkCTgDJwujOjFsXfcJ6XXGrKTFE0iS20Urf1482zPHwRzaO3nyxnydG3YlJfZafV+rqUttLSJKKhlbxq+6R4P7n3D6r0c9+7Utolp0Na+qaI6i6SMxS0bCOA5bzse9aPj5BUOqalGuLhB/FljgYNmTYowW7fQ+u1TaDbND2frJQ2puM7SKWkDsF5+E74LR2lcj6gu9xv14qLtdql1RVzuy9x4ADsa0djR2BTqO8XG/Xee7XaodUVc7svceTR2NaOwDuVvJyuCysp3Pl0PsOi6JXp1e75zfV/wCEHYxx4eK6E6MehTTwO1pc4i2WZhZb2uHvYzzk9LuQ8PSsE2H7OJNZXZtzuMRbY6R/ng/6S8fUD7H4R9Xo6B2ia4smgbE1024+qczco6KI4fJjhy+paO09nicBSMOhQXbWckVPlFqcrpeYY3OT67ft9zybZteQaL0451O6N91qgWUkR7D2vI+CPjOAuP55JaiaSeeR0ksjy973nLnOJySfHKu+rL/dNTX2ou91m62eY4AbwbG3sY0dgH/dWh4UbLyXdL3FxomkR06jZ85vr9jOtgNyNr2s2c5xHVGSlf6HMJH9JrV1Fq/6Wxkw7Y3D2Y+dca6KqvJtoml3ZI/vtT5x3F4H512TrrhaoT29YB8SWv8A7CfuOX8popahBrvRhPYoKnsXsslGa66wQYy0uy/7UcT83rXIVwds1BdWQJS4Y7szvTNN5LZaeNww4t33ek8Vc1DQAOClfTKK1VXGC7kc7KTlJthFBQFbTElERAFiu01rnafaGtc49ez3oz3rKlBAIwQo+XR5xTKrfbc2VT7Oal4Gjeqn/eZfvD8ydXL+8y/eFby3W9wUbrfghcx/0t/9n6fyWf8AVX7P6mjurmH7jL94VQWyfvUn3hW9d1vcFG634I9if9K//b+n8j+qv2TRrGv/AHt/3pWebLGuayvBa4ZLOY+2Wbbrfgj2KQ0DkApeB5PvEvjb2m+3u/k1ZGodtW4cOxhW0s/TaBvPg/5WrxbPQfd15xygd8rVsB0bHEFzQccshS1jGnLWNHoC3z0dyzfOuLvXLY1RzNqOy2JIWL7RLf5Ra21kYy+mdk/ann+ZZQhAIwRkK0zMaOVTKqXeRqrHXNSXcadtNE+vudPSNz9Mfhx7m9p9i2/CxsUTY2DDWgAAdykRxg5DGg94CqwoWl6WsBS57tm7Kyne13bHg1DwsNfj+DyfklaWjOQt8FoLS0gEEYIPavk2lpm8oIh9wFo1XSHnTjJS22NmJlrHTW2+5gWysYuFZ/JN+UrYLveqGRxsOWMa0+AwqlO0/DeJQqm9zRkXdtZx7Gmbrj3SquI/Xn/lFVWThfKHt/uhnyrcHk8Gc9TGc/YhBTU4cHCGMOHIhoVCvJqfa8fad+/Qn/1NcHDw/qfQHKwXas4AW/PfJ/0rOlRLDFLjrI2Pxy3hnC6DPxPOqHUntuV9FvZWKe3Q0bvD4Q9q2ns8/axB9u/H3xV88kpf4PF94F9Y2MjbusaGt7gMKs0zRJYV3aOe5Kys7t48O2xOMrXO0Cz+R13uhAzEE587A4Nf/wB1sZUTQxTM3JY2yN54cMhWGpYEc2ns3yfcyNjXuifEjSjcd4PrWa6F1E0AWqtl7PpDyf6PzLMfIKL+CQfgwpFFRhwcKWEEciGDgqjB0O/EtVkLF9CZfnQujwyiax1HcPdK7zVAcHRg7kf2o/8ACsl2c0RbBPXuH64erYfAc/j+RZSaOkP+jQ/eBfWONkbAyNjWNHINGAt2JosqsrziyfF3mu3NUquzitioIiYXQkAYWpNc0QodS1DQAGT/AE2P7rn8eVtxfCoo6WocHz00UrgMAvYCQqvVNO8+qUE9mmScXIdE+I0lFkODmuwQcgjs7QtyWGt8vtNNU/VPYN77bkfjX0Fstw5UNMP/AGm/MvTFFHEzciY1jR2NGAo2laTZgzbct0zbl5ayEuXQxTaaR7jwZwPp45/ala9znmQPWt11FPBUMDJ4mStByA9oK+Pubb/4FT/gwtGpaHPMvdqnsZ42cqYcOxiey/G5XceRYfiKzdfGnpqenz1EMceee60DK+yuMDFeLRGpvfYiX29rNzC1ntLc0ajYC4D+529viVsxeWpt9FUydZUUkMr8Y3nsBK06phSzaOzi9uZli3qmziaNL5b8IK4wagvEELIYbjMyNjQ1rRu4A7uS2n7k2z630v4JvzJ7kWr63Un4FvzKgh5OZFb3hbt9SwlqVcvWhuavOpr5j9lJvY35lQ7Ud8J/Zacegj5ltP3HtX1tpPwLfmUe41p+ttJ+Bb8y2f0LN/8AP+5gs6j/AMf7Fr2f1dTW2Iy1VQ+eTrXDeecnCw/WtFWx32rqZKWUQyPyyQDIIwBzC2bTU0FNH1dPCyJmc7rG4C+jmtcMOaCD2FWeTpLycWFM58495Gqy+ytc4rk+41Far1creMUlY8Rj9zOHN9h5epXg6zu5j3QKUHv3Dn5cLNKqw2epeHzW+Bzh2huPkXm+hOw5yaH+sd86q46PqVK4a7eXxZJll48+coGt7lX1dfN1tZO6V/YOQHoC99h09X3SVrjG6Cm5uleMZHgO1bEpLJaaV2/BQQNcPqt3J9pVwwBwAWeP5OSlPjyZ7/74nlmo7R4a47HnoKSGipI6aBu7HG3AHzr0oi6mEVBKMehWNtvdhQVKLI8KUU4UIAinCYQEIiIAiJhAEU4TCAhFOEwgIRThMICEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAFUqVI5ICUREB4r3bqS8WistVdEJaSrgfBMw/VMcCCPYV+dW0PS1ZonWty0xW7xdRy4hkcP12E8Y3+sc/EFfpDhc+dMnQD7zp2DWltg3620NLKtrRxkpic5+4PH0Eqx03I7KzhfRmjIhxR3OQ+xSOSgYIBHFSF0qK4qblVNcWkEHBHLwVAKnOUB76ep6zzXHDvlX3VpHDkvZS1GcMeePYe9S6rt+UjXKPgewKQqQpW81kqfUMKApXjBtnZXtw1JpFkNuue9erQzzWxTP+nQj7B57PsXcO4hdL6F2j6P1rCGWq4x+VFvn0VQAyZvf5p98PRkLhAFfSKd8UrZI3OY9py1zTgtPeD2KqytJpv9KPJ+4kV5M4cuqO8tUaRmumJLXqC6WdzW7oip5iIPvARj1Fa0vlr2q6dkMlPc7nXwDlLTymb2sdkj2Fah0Vtu13pt0cUtwF3o284a7L3Y8JPfD4wt46N6QmjLwGQ3ptRYqh3Amcb8Oft28vWAuO1HyXtcu0i3v4p/4LWjUo7bP9TH7btd1XQv6q4xU1ZunDhLF1cnxYHxLI7dtnpJnhlZRSUpPbu74Hs4/EtiT2/TGqqJtU+ntt1p3jzJmhsgI8HBYXqHYzYqsOktFVPbpexhPWR+w8R7VzV2DqFXKM2/3LGF2PPrHYvVt1vBXR79LJTVA7mHiPVnKuDdTRSt3JaIOB5jeBB9WFpm8bO9WWJxljpTWxs5TUZLnD7n33syvja9X3O2y9VWtdUMbweyUFr2+vn7VVz1DPx5bSbXxJUcamxbx5m2bjbNDXsH3W0la6kn6qaijc4evGVi122G7Jr0M01BUWuQ/VUVW9n9F2834l67JqS1XNrRFL1ch+ok4E+vkVeHHHEH0FTcfyjyYd+5Hs06p9xp/U/RcqGtdNpPV2TjzYa+HH9ZH+itOay0VtT0JI915sFTPRNP+VU7PKIcd5ezi37oBdjw19XTkdVO9oHYTkK8UGoCcMqo8/ZNXQYfldLdKb2IFulLbdI4FtmpqepG7Us6h3aeY/7K+MeyRofG9rmnkRxyuudabKdnGu2SS1lnp4K5/wDplGBDMD3kjg77oFc87Q+jxrrSj5K/SVSdQW9uSYoxu1DR4x8n/c8fBdvg+UFVqXEymv06UX6JhLzjtXyc7sVnhvckFS+ku9JLR1EZ3XtewtLT3Fp4j1q8RSxzMD45GuaeWOK6OFsLFvFlfKEodUUPjY8YcwOHivLNaqSXk0xnvavaSN9rGgue87rWNG85x7gBxJ8FszQWxPWOpHx1FxiNgtzjkvqmfTnD7GPOR91hR8m+imO9rSM642SfommzYa2Wojp6JjqqaV27HFG0l7yeQAHMrpDYZ0e4be6HUWv4YaipGH09rJDo4u50vY532PIduTwGzLFpjQGyizm4SOggmDd2Suq3B88p+C39Fo9q1JtP2z3S/NltunhJbLa7LXz5xPMPDHvB8fo5LitV12C3VXJfqdZo3k/lZ0unLx7l9zYO1rbBQadbLZdNmGsujRuPkHGGlPjj3zvsR6+5c2XKurLjXzV9fUy1VVO7ellkdlzj83cOS8/EHuHcnJcRfkzue76H1rS9Ix9Or2gt5d77yPALKNm2iqzWl78mjcaa20/nV1WeAib8EH4R+LmVjcRi329a15jz5wYcOI8CeSu101Nc6y1R2WAst9oj95RUuWsd4vPOR3ie3sCwq4E+KX0JWX284cFL2b7/AA+HvN0at2uWLSdoj0xoGmgqTTM6ptTzgix2jHGQ57eWeZWhrvdLheLlNcbrVzVlXKcvlldknwHYAOwDgvN8Xh3KAFndkTt69PAj6fpVGCt4LeT6t9WBk8VBU9vBUVLxFCXHn2KOWb5Lcace6TX1ga3ju3Slx+Fau2tfuxaYB3yj5CuKNnURqNo2nIzzfdafP4QH8y7N2jSYhoYs83OcR6B/3UnIfDgWHzvygfFm1/MxQFZnoSh6qmfXSNw6XzWZ+CP+/wAixO00klfXxU0YPnHzj3DtK2hTxMhhZFGMNYAAoHk/h9pa75LkunxKPPt2XAu8rUqEK7MqSEREBIUqByUoAiKEBKKEBz2ICUUIeXBASihEBKKEQEooRASigIgJRR2ogJRFCAlFGUQEooQoCUUdnFEBKIoQEooBRASigoM4Q83JRQiHpKKEQEooRASiKEBKKEQEooRASihEBKKEQEooyibglFCICUUIDlASijjlMoCUUdqetASoUZKnsQEooQcUBKjCIgClFCAlEUICUUIgJRQpQFKKpQQEBCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAgKIgKkVIKqQBfKphiqIJKeeNksUjCx7HDIc0jBBHaCvqoQHAfSD2ezbOtdy0sEbjZbhvVFtk4kNbnzoie9pOPQQVr0L9DtruhLZtD0ZVafr8RS/rtHU4y6nmHvXjw5gjtBK/P7UdnuWnL/W2G8wOp7hQymKZh5HHJwPa0jBB7iCuk0/LV0eF9UV99XA910PEpCpVQVkRyUREB7KSoyNx5wewr154q0jgvZS1AdiN587sPepVVv/ABka5R70erKnKjCZUg1lWVOVSibAqBVTXEKjKZQF2sGor7p+pFTZLxW26TtNPKWh3pHI+sFbc0l0k9U24xw6itlJeYQMOlj/ALnnPicAsPsHpWjSVCj3YdN69OO5nCycOjO1dI7dNnuoSyKa5Ps9S7lFcWdUCfB+Sz48rNbhZrDqCnZUS09NVBw8yeMjJHeHDmvz2aSOCvWm9Wal03KJLFe6638clkUp3Helh80+sKizfJum6LUeng+ZMqz5wfM7Iumz4CP+90sBDfeslYG/GFjlc3UWn37tRSSdQDjzwXMPocOX/nBa20j0k9S0L44tSWulusA4Omg+kzenHvT7At1aM2waD1YGQRXRlDVScPJa8CJx8AT5rvUVxGf5FOveVacfhzRcUaxvylz+JZqG/wBHU4bKfJ5Dww88D6//AOK8RODsOBBHYQsluek7DcWlxpGROI4SQeb6+HA+xY3XaNuFAC+3TmoiHJnvXj8xXLZGl5mLz4eJe77FlDJps79j0wvLSHMcQ7sOeSu9Fd6hmGyYkaO/msOohdX1Pk0ccz5eRYQeHp7lmlqscjI2vr5i5x+obyHpK26bLIul/ZTXiYZCrivSLRrPQuidoEQZqGxwVFQG4ZUs+lzsHhI3j6jw8Fru2dFzRVJdH1Et5vk9ITllN1jGY8C8NyfVhbd1HqHT2k7eau7V0FHHyaHHznnuA5uPoWkda7e7jU9ZTaWo20cfIVVQN55HHi1nIev2LsqtRtw4bSnz9xpxdEu1GX9qHLxfJG0KOxbNNmVJ5bHR2y1EZAqZnb87vAPcS8+gH1LXmt9vznCSk0lb8dgrKsYHpbHz9pHoWkLtcq+61r625Vc9ZUvOXSzP3j6B3DwC8mVV5GqW3NtfV9TuNO8kcXGSd3pPw6L+S4X69XW/V7q68V89dUHk6R3Bo7mtHBo8BhW48TlSowq5ycnuzqoVwrjwwWyIPE8VPIqTwUZWJmTz5cFBTKYQ9IU4RVY4ZQ9SKTwGVarjP1sm433oXpr6oNaYmHJ7T3K1nnlZRXeRb7f+KM32CUBuO2HTsBjL2xTuqHY7AxjnA+3C6m2izA3Kmi3h9LiJPhk/9lo3oeWkVevbneXNJZQUXVNPZvyOH5mlb+pLab1qaouM4zRwybrB2SFvD2DC3ZVU7caNMOsn+iPnms3x8+bfSK/UuGirWaOgFVOzdnnGcHm1vYFkSjsUq9xceONVGuPccxZY7JcTCgooUgwCIiAqREQBY7r/AFVSaO0++8VtPUTxNkZHuQgbxLjgcyAsiWsekuM7Mpv51B+Wtd0nCDkiXgUwvya659G0ixP6RGnWHDrFdxnvEX6a9tp2/aQq6gRVdHdKFhP67JE17R6dxxPxKw9GqyWO6aduj7rbaGqcysw01ELXkAsbyJHJejpAad0PbdLCqoqWgobt1zBTtpg1jpBnzgQOYxk8eRUPtL+y7TdHRyw9M898z7OW++26Zue0XOiu9BFX22qiqaaUZZLG7LXL2FaW6Kra5mnrt1m/5CaoGn3uWcedj149eVujvUumfaQUtttzndQxViZM6U99maz1htksmm9VT6eqbZcpp4XxsdJE1m554BHNwPaOxbMad5oPeFyVtyx+rLcj/H05/oMXWcBBhZ9qFrx7ZTlNPuZP1XApxceiyvrOO7+iMd2i6upNF2IXetpp6mMzMhDIcb2XZweJA7FRs41pR63s0tzoaSppY453Qlk+7vZABz5pPDisQ6UIB2dxjur4T+UvN0VSPoGrx/xF/wCQxO1l2/B3bHiwav6X5zt6fFt8jb+eKwTXm1TTGkao0VTLLWV7ff01K0Ocz7YkgD0Zys4qCRBIWDLt3gPFcf6NfZpdpok1sd6lfVzeU9cTuiXJxv8A2OeHdy7F5k3Sr4VHvMtF06rL7Sy3dqC32XVm1GdIi0On3X6dr+r7HNljLiPRkfKti6B17YNaMm9x5JxPAAZoZoi1zAeXgeXYVVDpvRF1oGsgtVmqqZw4dXFG4EeoL06T0fYNKyVjrHRClFW5rpWh5I4DhgHkOfBZVq5PnLdGvLs06VTVVcoz7ue6+e5fx2Fa72k7WLPoe9R2qtt9fUyupxOXQBm6GkuGPOcOPmrYozjiuVelaf8AGPHj61s/LkTKsdde8TzRMOrMyuzt6bM6itlXHX2+nrYgQyeJsjQeYBGV4dX32m03p+rvVXFLLBSs33tiA3jxA4ZwO1NG/tTtJ/3KL8gLHduw/wAVV9A/eB+U1bJSahxEKmqM8mNb6N7fqRs82nWHWldUUFHHU0dXC3fEVSGgyN7S3BIOOGfSs57Fw/Z5rvaJ2aktZfEaGpY3r28Qx7gS0OHc4AjuPJdZbMNb0GtdPsradzI6yIBtXT5yY34+Np5g93jlRsXJ7VcMupc67oiwpdpRzh0+DLNrXa7ZNK6mksNZb7jPPGIy6SFrCzz+XNwPxLYzDvMDh2hcldIBx/VervBlN8gXWdN+sM+1C2UWynOafcyLqeDVj49FkOs1uy26svcGndO1t6qopZYaSIyvZHjecB2DJHFaqd0iNPtz/eG7478R/prOdtQzsvv476N/5lpHo22izXbUV3ivNDSVcbKWIsbURtcAd53LPoWF9titUIPqStLwcSeFZk3xb4X3PYzP/wBROns8bFdR64v01sPZrrWi1zZZrpQUtRTxxTmAsm3d7IAPYSMcQqxojRRHm6cs3qpo/mV5tFrttppPJ7XRU1JAXb+5BGGNJ78DtW2uNql6cuRAzLsCde1FbjL3vc9hOBla31ttl0ppq4SW9rqi5VcR3ZY6VoLYyOxziQM+Ays41L5SNPXA0f8AlIppOp+33Tj41yfsUOl3ayjOsOqdC6J3VGqP0vr8j3+eGefPhnxWvIulBxjHlv3krR9Opya7Lrd2oLourNoUvSKtEk2JtO3COPPvmSxvOPRkLZ+htYWXWNukrrNNI8RO3JWSRlrmOxnBz+YlfB+lNEXiia33GtFVARwMcTCPaAvfpPTNm0vQyUNkpfJYJZTKWb5d5x9PHsC2Vq1P0pboj5lmBOr+zXKM/juvuXlYbr7aTprRrm09xnkmrXN320tOzfk3e88QGjxJWZHgOHYFx1eZqSbbJWy6rEhpPdeRtYDnIiDiGjv3d0N5diwyr3Slt1Zt0PTa86yfab7RW+y6v4G1P/UXZ/KN36Ha4xfC66Pe+9z+dZ1s72m6e1tUvore2qgrI4+tdBPFg7uQMgglpGSO1emzWzQN5tjY7bRWSro90ANjjjc3GO7C9WmdEaY03dqm6WO2R0U1TGI5BGSGYBzwbyHHnhe1xu3T4k0MqenOEoxqlCa6c/33MlUqFKklIF57hWU1BRy1lbUR09PC0vkkkcGtaBzJJXoWqOk7JVt2fwsg3xTvro21Jby3MOIB8N4N9eFrtm4QckSsLG86yIU77cT2PFf+kDpmhqnRW+3V9wY3lLgRMd6N7jj1L52TpCacrJmx19quFE085Buytb6cHPxKx9HuPQjqGeK7xW918fMQPK2tJMfZub3D044ra162f6LvdO5lTYqAlzSGzQxhj2+Ic3iolUr7Y8cZL4F/mVaZh2uiymXL/lv+u3QyS2VtNcrdT19HJ1lPURtkifgjea4ZBwfAr6VUwp6aWdwJEbC4gczgZUUNNHR0cNJC3djhYGMHgBgL43r9iKzP7y/5Cp272OZSi7Nl03NQf+ojTpAc2w3gtIB4iMf9af8AqK03j9g7v7Iv01rPYJbLZdNeU1LdqOnqqY0Ujiydgc3IDcHB4LoxuiNBk4GnrJ+Lx/MoFM77Y8SaXyOq1HG0vBtVUq5N7J7pnh2YbSbZr2evit9DW0rqMMc/ygMw7f3sY3XH4JWc+pWmwafsNmdLJZbXRUZmAEjqeJrN/GcZxzxk+1XXsU2Kkl6XU5nJlVKxulNR8Gaq1ZtusOndRV1lntN0nno5Ore+Nse6TgHIy8HHEK1N6RWmy4A2O8D7mP8ATWrNoMccu3SthmYHxSXeBr2niHNJjyCO5dKHZ5oh7TnS1oG8OJFIwH4goldl1kpbNcjpMvF03CqqdkJNyW/Jlv0ZtT0jqmojoqStfTVsnvKeqjMbneAPIn0FZ0MYwFyHt103btG65ZBYXugilgZVRxtcSad+8RwPMDIyO5dUaQq5q/Stqrqj9eqKOKWT7ZzAT8ZWzHvlNuE+qK/VtPooqryMdvhn3PqjG9pW0Wg0NU0kdxt1dUMqmuLJIGsIBaRkHecOPEFX3RWpKHVmnaa927fZDOD5kmN5jgSCDjtBCxvbvpg6m2f1bII96tos1VMccSWg7zfW3I9i1l0U9S9Tcq7S1TMRHUN8qpQT9UODx6xunHgUd0o3KMujPa8Cm/TnfX68Hz+B0WT2nktZag2zWK1avl01HbLlXVUc7Kfep2sLXSOx5oy4HgTg8OazHXt+h01pO4XiYj+54iWD4TzwaPWSFz70ctOy6h15UaiuQdNHb8zue7jv1MhJB9XnH0lqXWyU4wh1Z5puDTZj25OR6sVy97OnmklgJ7VgW0nafatDXOloK+grql9RCZWmnDSAAcYO84LPsYXNPSy/bhaP5i/+0WWVbKutyRq0XEqzMtVWLk9zobTtzivViobvAx8cVZAydjX4yA4AgHHbxXvBKxzZZx2b6c/5ZB/ZtVw1VdorHp64XeUZZSQPlI78DOPWtyl6O7IFlX951w8dl9S3a11vp7SMAfeq5sUjwTFAwb8snoaOOPE4C1jV9I2zRygU+nbg+PPF0krGH2ZK1voqzXHaltElfdauQh4NRWytPFsYOBGzPLngdwBK6PtOzjRNupBT0+m7c5u7hzpYRI53pc7JKhwsuu5weyOgvxNO0zavJTnZtu0nskWLQu2TS+qK+G27tXb66d27DFUR8JDzw1zSR7cLZI581hFBsv0jbdXUupLbbxR1NM1wbFE7ERLhje3ewgZ5d6zcclKq49vT6lJnPFlNPFTS27/EwzabtAt+hY6J9dRVVV5Y57WCDd83dAJzvEd6wZ3SHsLR+wF29sX6S83SyGaWwfy035DV7dhOltKXPZ5RVl1s1tqqoySh0k0THOIEjsZz6lFlZbK51wexd4+Hg16dDKvg5Ntrk9jz/wDqL0+ASbBdQACecX6S3NZ61lytVJcWMcxlTCyZrXcwHAHB8eKx/wCgfQpGBpyyuzwx5NGc/EsngijggjghY2OKNoaxrRgNA5AeCkVxsXrvcqc2zEml5vBxffu9yitqoKOlkqqqVkMETS98jzhrQBkknsC1HqDb/pmhqHQ22hrbm1px1zAI43eguOSPHC9/Sclq4tmrhT74hkq4m1Jb8DJwD4bwasJ6O8WgZ7dNHeIre+/dcd0VmCTHw3erDuHpxx7+xabrp9p2cXsWOn6fj+Zyy74uez22X+TIbN0hNP1MzY6+z3CkaecjSyVrfTg5+Jbcs1xpbva6a50MhkpqmMSRP3S3eaeRweIWNXrZ3om+U721NjoQXtwJYGCN48Q5qyi20cFvt1PQUzS2GnibFGCc+a0YHyLdUrU/Te5X51mDOKeNBxfem918j1IoUrcVpBUKSoQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAQFEQFSKApQEYWl+k3shZryzC+2KJjNTW+M9WOAFZEOJicfhDm09+RyPDdKg4ws67JVSUo9TGUVJbM/MAtkZI+KaJ8UsbiySN7cOY4cCCDyI7lOV1x0mtiDtRmfWOjqYC9NbvVtEwYFa0D3zf40d31Xp58jHIkcxzXNe1xa5jhhzSOYI7CupxcqN8d11K6ytwfMqBUqlFKNRUnJRlAgPZSVJ95IfQV6/QrSvRT1JZ5ruLfjUmu7uZrlDvR7lOVSxzXt3mnIU8lJ33NZOVKpUgcM5QEqcK66cprFVzOgvdxqra13vKmOn65jT3OaCHY8Rn0LYFFsQv14ohXaWv+nr9TEZDoKhzHD7ZrhwPpWmzJrqe03sZKDl0NVhFsmfYbtOhJxp1sniysiP51Q3YjtPcW/wCDJGe+qi4f0lj57j7b8a+p72U/A10B44RxwME/EtsUPR92j1MgbNR26kaebpawHHqaCsw090Yqt72v1BqaONmfOioYST98/wCZarNTxa1zmjKNFku41js92raw0dURNo7lLWUAOHUNW8vjI7m9rD9r7F2RoK/VGptL0l4qrPV2iSdpPk9SMO+2HbunmCQDjsVg0Lsj0PpCZlVb7S2prmcqqsd1sjfFueDfUAsvvt4ttjtM9zutVHS0kDd6SR54Dw8T4Ll9TzKMh71x295ZYtFsXtvvv3Hqf1MLXzO6uMYy5xAHAd5Wktpu3WnopJrVo5kVZUDLXVz+MLD9gPqz48vStfbWtqtz1hNJb6Ay0NjBI6oOxJUeMh7B9jy78rW/hwHoC5TIztvRq+p9H0byVWytzOvs/f7HrvF1ud5uD6+6109bUv5ySuyR4DsA8BwXkBypHgmOKq3JvmztoVxhFRitkSCeWEQIV4Z7BQpTCDYhFOEwg2ARMhfOaaOIec7inUNpc2fQYA4rw11YADHEcntK+FTVukG6PNavKT3LNRItt+/KI58TzVMhAaSeACnOT3K86F0zW601hQ6boGuzO8OqZAOEMAI33nu4cB3kgLZCLk9kQLrY01ucnyR1B0VtNG07LmXCVpjqLxI6pJxxDPes+IZ9a25TQRU9OyGJu6xgwAvlaqOnt9tpqGljEcFPE2KNg+pa0YAXpXQwqjBL3I+U5WRK+6Vj72FKKCtpHIKIiAIiICQpUBSgC1h0mHbuzGYd9XB+WtnrV3SZa92zV4Yx7yayHg1pJ993Bacj8KXwLDSfztX/ALI1Dsn2cz65tFbVQ36S2imqOqcwRFwdloOffDvV11hsPvFltFRdaG7U1xNMwyPjfAY3FoBJwS4gnHYeas+y7aFddB2yso6fTktd5TOJi9++zdO6G4wGnPLPYr9qHa1rPVFtns1s0w+ldUsMcj4Y5JZNw8CB5oAz3lVkY47rXEnv8ztsieqxy3KuS7Pfv4en7mUdHbaFUXxz9L3GmpoZKWAS0slNGI2ujBALS0cAeI5c1ukDsWnej/s7uGnJp7/fIW09XNEIoKbeyYmZyS7xOBw7MLcbeSscXj7JcfU4/W3jvNn5v6v6b9+xyRt4O5tiubn8MSU7j6NxvFdaUpaaeMtIILRx9S09t/2aVmopY9Q2KJstfFH1dRT5wZ2DkWn4Q48O0egLDNObZNU6ToI7Le7C6qdTDq431BfDJujgA7LSHelRoT7C2XH0ZcX0PVsKhYzTlBbNb7Pu+xsDpQvY3Z9C1zgHOr4t0HtwHLzdFX9o9fwPG4v/ACGLWd/ueu9r13poILQ+OlhcepY1jmwRZ4F73u98f/AF0Vs40xBpHSVHZYnCR8QLppcY6yRxy4+34sLOpu292Lpsac6McHTFiTadjlu0u4yLHDC1rtB2Paf1TXSXKmmltdwlOZJIWhzJD3uYeZ8RgrZMmd127zxwXPEm1DaNpG5T0t+sUlZTCZ/VOnhcxxZvHGHtBB4Y7FuyHXttYt0Vuk05U7HLFntJe/bf7lnv2yXXGk2yXSzV4qo4RvOkopXwzBo4k7mePqJWWbBtqN4vF7j0xqB4qpJY3Ppardw87oyWvA4HhyPhxVovW3HUF6t8tBZ9N+TzzNMfWNc6ZzSeHBoaOPpXu6Puzm70F/Zqi9Ur6FkMbmUsEnCRxcMFzh2cOxQoJK1dhvt3nS5blLBsepqPH/x223/Q393LlXpWj/GOz/lbPy3rqkDtXLvSopamXaDHJFTTyNNtY0OZE5wzvv4ZA9Ck5y3q2RSeTMks5N+DOjtG/tTtP8zi/ICx3br/AJrL5n+D/wDUFkWjg5uk7S1zS1wo4gQRgjzAsc27Ne7ZXfWxsc9xgGGtaST5w7At8/wn8Ctxvzsf/Zfuay6NlpoL1ZtU2u407KimqBCyRju0br/j7QVht4pdQbGNo8c9K989JJkwudwbVwZG9G77McPQcHtWwOijHPGy/wDWwzRBzoMF8Zbng/lnmtobR9IW/Wem5rRXNDX+/p5gMuhkHJw+THaMhQ66OOiMlykjo8rUljanbCznXLqvl1OWNq18o9R7QZb1QP36aqjpnN72ndALT3EHIK7Kpf8AJ4/tQuIL1py82S/y2qvoKjr6eUNLo4nOa8ZGHA44g9i7fpf8njyPqQvcLicpuXU1eUqqhXRCp7xSe36GKbZuOzK/D/c3/mXNmy3RM+t7pV0VPcW0DqaFspe6Iv3skjHAjuXSu2BjpNmt+axjnuNG/DWjJK5n2c6yuuhrjV1dJZX1b6qJsZErJGBoBJ7B4/EsMtR7aLn0JPk/O5afcqGuPfl0/wAmyYtg97YeGrWD0QP/AE1u3TtvdarDQ22Sbr30sDInSYxvYaBnt7loNm3/AFGXedpKI+G/KP8ApW0dkOuK3W1trqmttHua6llbGBvOIeC3OfOaFux5UKW1ff8AErtWq1OdSnlbcK8Nv8GckcCDyWptebELJf7jNcrTWSWiqmO/KxsYfC9x7S3hgnwIWzry6obaat1GHGpEL+qDee9g4x61z3b9rm0LTGKLU9gkq3MGC6eJ0T/vmgtPsWzIlXslYuRE0enMk5TxJ7SXdvtv9eTLFf8AZzr3QUUl3t9a40sHnvnoJnMLWjtcw9nfzWztgO0i56plqLFfdyWupYRLHUtbu9azODvDkHDhxHPKwjVO2HUWrbPPZLVpwweWMMMhjD55C08C1oDQBkLMOjvs/uenZanUF6hNLUVMXVQ05PnMZnJLvE4HBRKuVqVTfD3l9qDcsCT1BRVv/Hbbf57G5sLX20bZVp7WVWbjI6WgueA01NPj6YBy32ng7088dq2Afe8Fz3eNfbS9Hamr47jaZqu3SVUr4GzxEgRl53Q2RnLhjgVNvlBLaa3Rzuk0ZFljljTUZL37b/Att72IatspdW2G5w1rovOBiLqeb1cSPjC9uxXapfxqam0vqSWStgqXmGGaUYmhkH1Lj9UDgjjxz2r11e3q7VNIYbfpPq6tww1zpXSAH7UNBKtuxbZ3qGu1jDq7UFLJRU0MrqpgmZuyTyuyc7vYAST7MKBFRVkew39/gdRY7ZYdn9VjHfb0Xy4t/kdIDv71UoGAFKtjggvDebbQ3i21FtuVMyppJ2lskbxwI/8AOOV7lgW2qr1dRadpKrR8FRLVxVgfN1LQ49WGOyC0++BJHBYWSUYttbm/GqlbbGEZbN975bGF6l2B08r3y2G8vp2k5bBVR9Y0eAcMEevK1ve27S9ldwgDrlUwwSuIhLZjNTSkc27ruR9QPcsrotveqLeDDe9LxPlaME/TID6wQVjOsdS6z2s3CloKSwyNp4Xb8UEDHEBxGN58jsDlnHLmeaqrOx23p3Uju8KOoqShncMqu9tp/wC/M6H2Uas+jPRlLeXwiGoJMU8bTwbI3gceB4EelX++/sNWH+If8hWO7I9KO0domls80gkqd50tQ5vvescckDwHAepZDfM+4taOOeofy4/UlWkVLg9LqcTf2Xnb7H1d+XwOPNnGmp9XXuCy01a2ikfTuk64sLgA0DIwCO9bLZ0ertv5OrKceikf+mta7OtQXPRl+hvMFmnq3sp3Q9W9j2Dzscc7p7lsf9X/AFJ26RhH/uS/oKpoVKj/AHFz+Z32pT1SVq80a4dl7P8Ak3Dsy0vNpHSkFlnrhXPjke4zCPdB3nF3Ik9/esnPEFaw2P7Sbtra71tHcLC23x08DZWyBzzvEuxjzmhbPVtXKLinHocDn1XV3yV/rPm+n+DjvahJURbZLrLRM36mO4xugbu53ngM3Rjt44WVX/aDtos1uFZc6D3OpS4M651C3AJ5Di44PpCsut6Kr/V2qJBSVLozeIHBwhcQRvR8c4wupL5aaC92ee2XGnZPS1EZY9jh2fmPaq+imc3NptczrdQzqceGOrK1NcPPfqcxbMtF3Dahf6i9Xy8Mmhimb5aHPzPJ2hoaODGkcAezjgLqumijgp44YmBkcbQ1rQMAAcguTp6XUeyDaZvUbKippmuyzDSW1dO4+9djgHDv7CO7n1Dpq80d/stNdKEv6mdm8A9pa5ve0g8iCt+Ekk016XeVnlHx2ShZF71Nejt3e4uT2h7S0jgea5G2i0FVs32weW0Me5EydtfRgcAY3E7zPR75vox3rroLVHSV0t7s6PZeKWAvrLW/rPNBLnRHg8DHdwd9ys8utyhuuqIugZcaMns5+pPk/wDBhnSO1lDdrZZLXbZ9+mqoW3CUt5uaR9LH5R9QW1tjGmfoX0HRUcjN2rnHlFVkcescM4PoGG+pc+bHtLV2pdeW6OugqfI6BjZZDLG4N3IyNyMZ8SOHdldbNADQByWvF3sk7ZfAma64YdMMCp77c3/gkLmfpaHGsbT/ADF39oV0yuaelfBNLrK1FkMrwKB3FrC4frh7llnLel7EbyaaWoRb8Gbw2VHOzXTZ/wCGU/8AZtXk2zUk1dsxv8EAJf5I54A7Q3Dj8i9uzKN8WzvTkb2lrm2ynBaRgj6W1ZDNGyWN0cjQ5jgWuBGQQVIUeKvh9xVzt7PKdnhLf9Tm/or19NDq26UUjgJaqka+Ik++3HHIH3wPqXSXNcy7RdmepdHai+iLRraiWjjkM0JphmWlPHLC36pnEjt4cCO0+qh6QGo6SmFNc9N08tYBjf33xZPiwtPyqHRaqI9nZy2Oj1PT5apasrEaaklut+aZ0fnipXP2jNV7WtXaxobnBbhTWmF+JoXMMVO6M4yS52XOd3Ecj2c10COSmV2qxbo53Nwp4clCck37nvt7maK6WR/ubT4/jpvyWrFdn2yOs1ZpalvcOoI6Ns5cBC6mc/G64t5hw7srLelbFLLTWAxQSy7ss2dxhdjzW9wWF6J2t33SWmqWxU2mm1EVPvYkeZGlxc4u5bviq65V9u3YuR1+nyy/6TWsRri3e/Tp8zONObEK60363XSTUkc7aOpjmMfkrhvBrgcZ3z3Ld3Fc8R7fNSE/tPi+/l/QW8dHXSa96Wtl3qKbyaWrpmTPiyTuFzc448VLx3VzVZQaxVnvhsy9vBbbf4PXdaCkudBPQV9PHUUszSyWORuWuB71pfU/R/opZHzacvD6Rp4tp6pnWMb4B2Q4evKz3bFV6rotNw1OkIZ5K2Oqa6QRMa49WA7OWnmM45LVlLt61Nb/AKRe9KMdM0YJzJAfWC0rzIlS3w2I26TTqEYdrhzXvW6/VMw+60+0TZZc4A+4T08chJhdHN1tNNjGRuu4D0EArorZJrA610fFdpIGwVLHmCoY3JaJG88eBBBx4rQOsdTav2q1lJRUen5WQRvLoYYWOcN4jG8+QgDGPQFvzZFpN+jdGwWuokbJVPe6eoc3iOsdjIHgAAPUtOLv2j4G+H3k/XeB4kHkKKv37vD3mYgcFKhSrE48gqFKEICEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAFIKhEBUigFSgIwtHbf9hFv1p1+otMMit+pAN6RnvYa7HY/4L+5/wB93jeSgrZVbKqXFF8zGUVJbM/My8W24We51Fsu1DPRV1M/cmgmbuuYfzgjiCOBHJeRd/7XtlWmto1vAuEXkl0iZu01xgaOtjHPdd8NmeO6fURzXGW07ZrqnZ7cDDe6Ivonv3ae4Qgugm7hn6l32Jwe7K6PEz4XLZ8mV9tLh8DDUTkoPgp5pKspkYVOVOUB9IpHxnLXYXshqmO4O80/ErepC2Qm49DxxTLuMFVAK1xTPj96eHcvUyrYffgg96lRtT6mpxaPZkheq03W52etbW2q41VBUt5S08pYfXjmvAyVrh5rgfWpJWTSktmec0bm0h0ita2ncivMdJfKccCZG9VNj7ZowfW0rZ1i6S2jastZdrZdLY88yI2zMHrac/EuSSQqHyNaPOPM4A55KrL9MxrOfDs/cb4ZFkejO67btn2Y14+l6vt8BAyRVb0GPvwAs8p5oqinjqIJWSwytD2Pactc0jIIPaMLlvo87Dp6+rptW62oTFRsIkordM3jMeYfIDyb3NPPt4cD0ze7pb7HaZ7nc6qOlo6ePfkkecNaB/5wC5fNroqnw1PfxLPHdlnVc30PLrHUdq0rYai83moENLA3s4ue48mtHa4nkFxjtT2h3vXt6NTWvfT2+N58koWuy2MdhPwnntPZ2YXs2zbQ63aBqHrWdZBZ6QkUVO7n/KOHwj3dg4d5OBnGSQuay8pzfDHofRdF0ZY0VbavTf6H2hq5oyGk7wHevXFXxHg8EFW1VKA0mdPC2ce8vLJYn+9ePavoAO9WJVNle33riPWseA3LK8UXzd7kwrMKqcfuhVXltR8P4gnAzPzmHgXfHpU4GOKs/ltR8P4lQ6pndzkKcDHnUPAvLiwDi4BfCWrhZ9VvHuCtRc53NxPpKpRQNcsp9yPVNXPeMMG6F5XOLjkkkoQoPBZpJGiU5S6sKDhTwxklXjRWl75rS9ttGnqMzSjBmmdwigb8J7uz0cysoxcnsjTbbCmDnN7I8Nktdyv14prLZaN9Zcal27FEzs73OPY0cyTyXZ2xXZtb9nmnupzHU3apAdXVgbxc7sa3tDB2d/PtVeyHZnZdn1qLKUCruk7R5XXSN8+Q/BA+pYDyHtyVnoAV1i4qqW76nz/WdZlmS7OvlBfqOxETKmFACoREAREQBERAFUqUygJyqXta4YcAR3FSiApEMeMbjfYpEbB9SFV2KU2G7KQOA4KRjkilARgFfGWmp5v12CN+PhNBX3RD1NrofNsTG4DGhoHLAVfBSiHnUgql0Ub/AHzGkeIVahB06HyZTU8fFkMbfQ3C+oAxw4KVC8PW2+owqXMa7iWgqoJhengCjAcMEZHJVIgKWta3k0BCPBVKEBSY2E7xaCe9VJhSgKXAEHIyMcQqepiP7m32KtSh6nsfPqovgN9iqaxrR5owqkQ8bIxkcQqHxRPGHxtcPEKtSgT2PjHTU8f63DGz7VoC+uBjkpUIG2+pAHgodGx3vmg+kKtQgPk2mp2u3mwRg9pDQvphvLCqRA231IwpREAUEZ5hSiA+E1LTy/rsET8cfOaCqmQxMGGxtaPAL6KU2PeJ+JGFBGeanCIeFHVR/AHsUCOP4DfYvoi82QKWsa05DQFVhEXoZT1bc5LQSqgERAUmNjnZcxpI7SFLWgchhSgGEAChwzwVSgjKApaxreLWgepVoiAKhzGOOS0E+IVahARgDACnsUogIIBGDxXxfS0r5A99PE545EsGQvsBhSnU9Ta6FAY1vANAHgquHNEQ8Iexr8bwB9Ko6pmfeD2L6YUoN2fPqox9Q32KsAAAAYA7lKhBzZBA7eS+UlLBIcvhjd6Wgr7KUCbXQ+TIY2DDI2t9Awq8ccqpQnQNtgc8KURAEREBGFCqUICEU4TCAhFUiApRThMICEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAFUqUBQFShSiAheS7W6hutBNb7lSQVdJOzclhmYHseO4gr1oi5c0eNHKm2bo31FIJr1s9a+ogGXSWl7syN5n6S4nzvtTx7ieS5tnjlgnkgmifFLG8skje0hzXDm0gjIOeGCv09wtbbXdjmk9ocL6ipgFtvOMR3KmYBISBwEg5SDlz4jsIVti6nKHo2c14kazHT5xOCMqVtDV+wTaTp+ufDT2R16pcnq6m3kPDh4sPnNPqx3ErGpNm20KM/TNE6gHooXn5ArqOTVJbqSIjhJdxiqqCyX9T3XgGfoL1D//AI6T5kj2f67klEbdFah3jyBt8g+ULPtq/aRjszG8IVnNDsh2nVj9yHRN2b4zNbEPa4hZHaOjntRr8Ont9ttrScf3VWtJ9OIw5YSy6V1kjJVzfcajDscuCOqXxjJk3R3uXT+meilCHsk1LquSRuBvQ2+AM4/bvJ/JW29GbHNnWkpGVFt09TzVjOVVWkzyA94L8hp+1AUSzVqoeq2zZHGlLqci7P8AZTtD1uY5LdaH0VBJg+X1zTFFjvAPnO9Q9a6b2T7BdLaMliudxcb7eWecJ6hgEcR/i2dnpOT6Fnmqtb6U0rCXXu9UdI4DzYd/ekd6GNy4+oLRu0LpFVdTHJR6Nt5pGHI8urGgv7eLYxkDsILs+hUeZrM5JqUtl4IucDQ78h/24b+99DdW0PX2nNEW7ym8VgEzwTBSxYdNMfsW55eJwB3rknaltIv2v7iXVjzS22N+aegjcd1vc55+rd48hxwAsTutdXXSvlr7jVz1lVMcyTTPLnu9Z7PDkF5lzWRmSt5Lkjv9M0OnC9OXpS/3oO3Hb3qSERQy8IwmFKICEKnCYQEYREKAngoKcMKPUh4SmEGML5TVEMLd58gHggbUVuz68l8KmpihGZHertWa6D2W671xuTWy2e59uceNdXAxsI72jG871DHiF0fsv2EaU0fPFcq0G+3dhyKmqYOriPfHHxA9JyR3qXThzs5vkikz9ex8ZOMXxSNIbKNh+o9ZmK538T2GxnDgHt3amob9i0+9B+E4dvAFdX6P0vY9JWaO1WGgio6VnMNGXPPwnHm4+JV6AHcgVvVjwqXI4jN1K/MlvN8vAYGE7OKEqFuK8FERAEREAREQBERAERAgJwilEARQpQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBEUICUUIgJRQiAlFClAERQgJRQiAlFCICUUepEBKKFKAIoUoAihSgCIiAIiIAiKEBKKMqUARFCAlFHqUoAiKEBKKPUpQBEUICUUepPUgJRR6lKAIiIAiIgCIiAIoypQEYTClEBSiqUEICEREAREQBERAEREAREQBERAEREAREQBERAFIUIgKkUZTKAlRgZ5IiAYUYA7FUoQHwrqhtJSy1D2SPbG0uLY2lzjgdgHM+C1tcdumz+31j6Ssrq+nqY+DopLfM1w9RblbQPHmrJqrSemtUUhpL/ZqK4R4wOuiBc37V3Np8QQsJ8b9VkjHlQn/ei2vczXc3SG0Cz9a91Jz9jRkfKQrXXdI+xNz5Dp+5VHDgXljB8pVv1j0ZbNVOdPpO/1lpkJJFPU/wB0Q+gHIePSS70LUmqdkO1DTG8+Wxi8Uzf3e2OM39DAk/o48VAtnlR6HSYNGi2v0m/m9jP7x0itSz7zbbZrfR88Oke6Rw9XALX2otp2ur3ltbqSsjjOfpdMRC3j9rxPtWDVFc+mqHU9dTzU0zSQ6OVhY4Ht4HBVbKunfylA9Kr53XP1mzqsfT9Pr51QX7/ufWQl8jpHuLnuOS5xy4nxPNUuyeYUgtcPNcCmMcCVH3LHh26FHgRhMY5KstVOF6OEpRSmEPNiEUnCgkdyHgROHaQFQ+WJgyXgL085IrVJ4jmvO6ti3wyNrpHnk1oySst0xsx2j6nlYLdpirpYHjPlNa3yeMDvy7ifuQVshVOfREW/NopW85Ixh72MGXOAXyppJ62sZRW2jqK6qecMhgjL3u9DQMrpfQ/RjtUHV1Ws7xNdJsAupKQmGEHtBf79w8Ruehbt0tpLTWmKQUtgstFb4u3qYgHO9LubvWSptWnyfrM53L8p6o8qVucpaH6P+utRGOe+Oj07ROGcTDfnI8GA8PWfUt76D2GaE0s6KpNAbtXs4+U12JMO72s96PYto4TkrCvGrr6I5nK1bKyfWlsvBFMbGsYGta1oAwABjCq5BQUW9FaTlQiIAiIgCIiAIiIAiIgCIiAKRyUKcoCV8pZYozh8rGHGeLscF9Mqy6g0rYr9URVF1ohUSRN3WHrHNwM57CFrsc1H0Fuz2O2/MufllLj/ACmH78fOpFXS4/ymH78LGf1ONG/Wgfh5P0lH6m+jfrQPw8n6SjceX7K+v8G3arxf0/kyfyul/hMP34UGtpP4VB+ECxn9TfRv1pH4eT9JUO2aaLPO0f8A2JP0k48v2V9X9hw1eL+n8mUeXUf8Lg/CBPLqLtq4PwjfnWL/AKmmi+y0f/Yk/SQ7M9F/Wk/jEn6SceX7K+v8HvDT4v6fyZP5fQ/wyn/CN+dPdCg/htP+Fb86xj9TPRf1o/8AsSfpKk7MNEnnaP8A7En6SceX7K+r+w4avF/T+TKDcreOdbTfhW/OoN0tv1wpfwzfnWLnZfog/wCpz+MSfpKl2yvQ5P7Dn8Yk/SXnHl+yvq/sOGrxf0/kyn3Vtn1wpPwzfnVQuduIyK+lP/vN+dYoNlmiBys7vxiT9JDss0R9aHfjEnzpx5fsr6v7Darxf0Moku9qj/XLlRs7t6Zo/Ovmb7ZRxN3oAO/yhnzrGXbKNCuxvWdxx/vMn6SpOybQuf2IePRVS/pJx5fsr6v7Darxf0Mk+iXTw4G+2wf/ACmfOn0Sae+vts/G2fOsZOyLQZ/1O/8AGpf0lQdj2gTztEn41L+kvOPL9lfVnm1XizKDqbTo5361/jcfzqPoo039f7V+Nx/OsXOx7QHbZpPxqX9JQdjez4/6lk/G5f0l7x5fgvqxtV4syn6KdNf7QWr8cj+dPoo01/tBavxyP51i/wCo5s/+sr/xuX9JUnY1s+P+ppPxuX9JOLL8F9WNqvFmVfRTpnt1BavxyP51QdW6XB46itP45H86xn9RrZ7j9hZPxuX9JR+oxs8+ssn43L+knFl+C+rG1XizJ/ot0v8A7RWn8cj+dSNV6YPLUNp/HI/nWMDY1s+HKyyfjcv6SfqN7PvrNJ+Ny/pLziy/BfVjarxZlH0VaZ/2htX45H86fRTpr/aC1fjkfzrGP1G9n/1mk/G5f0lB2NbPvrNJ+Ny/pL1Sy/BfVjarxZlI1Tpr/aC1fjkfzp9FGm+y/wBq/HI/nWLfqN7PvrK/8bl/SUfqNbPc59xX/jcv6ScWX4L6sbVeLMr+ifTf1/tf43H86pOqdNDnqC1fjkfzrF/1G9nw/wBTP/G5f0lH6jWz/P7DS/jcv6ScWX4L6sbVeLMp+inTX+0Fr/G4/nVUepdPSHDL5bHHwqmfOsXGx7QAHCzyfjcv6SqZsh0Ex4cLPISOw1UpH5S84svwX1Y2p8WZUNQWL68278ZZ86n3fsfZeLf+Ms+dYz+pRoP6xj8Yk/SU/qU6D+sg/DyfpL3iy/ZX1f2HDV4syX3esn13t/4yz51H0QWMc7xb/wAZZ86xv9SnQf1kH4eT9JUHZLoInPuJ/wDYk/SXvFl+yvq/sNqvFmT/AEQWL682/wDGWfOpF9sp5XegPoqGfOsZGyjQY5WUfjEn6Sqbss0O0gts+COX0+T9JecWX7K+r+w4afFmVi524gEV1Mc/xrfnT3St/wDDqb8K351YW6B0q0AC2cv413zr6DQ2mG8rd/Wu+deOeZ7K+r+x7w0+L+hevdK3fw+m/Ct+dPdK3/w2m/Ct+dWcaJ012W8fhHfOg0VpwHhQ/wBa7515x5vsr6v7Dhp8X9C8e6NB/Daf8K351PujQfw2n/Ct+dWkaO08P9C/rHfOo+g3T38CP4V3zp2mZ7K+r+w4afF/Qu/ujQfw2m/Cj50FwoTyrKc/+4PnVpGjtPD/AEH+sd86qGkNPjlRf1jvnTjzPZj9X9jzhq8WXXy+i/hcH4QfOp8uo/4VB+EHzq1fQnYf4H/WO+dVDStjHKk/rHfOvePL9lfV/YbVeLLn5bR/wqD8IPnTyyk/hMP34Vt+hiyD/RP6x3zp9DFk5+Sf0z86948v2V9X9jzarxZc/K6X+ERffhT5TTnlPGfugraNNWYf6IPvj86qGnbQOVLj7o/OveLK9lfV/YbV+LLj5RB++s++Cnr4f32P74K3DT9qH+jf0j86kWG1j/R/6R+dZceT7K+r+x5tX4lw6+H99Z98FHXw/vrPvgvF7h2z+DD74qPcG1/wYffn5048n2V9X9htX4nv6+H99Z98FHXw/vrPvgvD7hWv+Df0j86j3AtR/wBFH35+dOPJ9lfV/YbV+JcOvh/fGffBOui/fGffK3nT9p/gg++PzqPoetH8FH35+deceT7K+r+w2r8WXHrov3xntU9bF++N9oVu+h+0/wAF/pu+dQdPWg86Qffu+dOPK9lfV/YbV+L+hcutj/fGffJ1sf74z2hWh2l7G7nQtP3bvnVJ0np887ePwjvnXnHl+yvq/se7VeL+n8l562P4bfaE6yP4bfarL9COnj/q8fhH/OqDo3TZOTbR+Ff86ceX7C+r+w2q8X9P5L71kfw2+1T1jPht9qsP0Gab+to/Cv8AnUfQZpr62t/CP+dOPL9iP1f2HDV4v6fyX/rI/ht9qb7PhD2qw/Qbpv62j8I/50+gzTX1tb+Ff86948v2I/V/YcNXi/p/Jft9vePam834Q9qsP0G6b+to/Cv+dPoM039bR+Ff86ceV7Efq/sNqvF/T+S/bzfhD2qd4d4VgGjdNj/Vw/Cv+dPoN039bR+Ff86ceV7C+r+w2r8X9P5L/vDvTI71Yho/To/1cPwj/nQaQ079bm/hH/OsuPJ9hfV/Y82r8X9P5L7kKN4Ky/Qnp/63N+/d86fQnp/63M+/d86ceR7K+r+w2r8X9P5L3kd49qZHerONL2IcqBv37vnVQ03ZByoW/fu+de8eR7K+v8DaHi/p/Jdt4JkK1fQ7Zv4E3753zqpun7Q3lRN++d8694rvZX1/g82h4/p/Jc8hMjvXgFmtoGBSj74/Oq2WugYQW07cjxKy4rfZX1/g82j4nsTIXnFDSjlCB619G08LeTMesrNOfgecj6ooAAGApWZ4UoiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAkKVSgKAqUKUQEIRkKUQFrven7Je4urvFpoa9u6W4qIGyYB7sha/v+wPZrdWu6uyG3SnlJRTujx6G8W/EtposJVxl1RuryLqvUk0c5Xjot25z3Ps2qa2nGPNZUQtkHtGCsQuXRs1/TN3qC7Wes87G6ZJIzjv4tK68wi0yxKn3FhXrmbD/mcSV+w7axSHDLLDVDvgrIz+UQrRcNlu1Wh3eu0jXyb3LqdyX27rjhd5Jgdy1vAqJcfKTLXXY4A+gLaX/sXe/wAUKqj2fbTXnzdF3vnjjS4+Vd+7re4JgdwXnmFZl/1Nk+COGYNjm1qZgc3S0rQfh1ELT7N5XSj6P21Sp3DLTW6kDuYlrBlvpDQV2lgJgLJYNSNcvKPLl02OVbT0Xr/M7N41XR07McqandIc93nELOrB0adCULo33Oe5XV4HnNkm6tjj6GgH41vDATHgtscauPcQrdWy7OszG9L6G0jploFj0/QUTh9WyEF/3xy741ke6AVOUytySXQr5zlN7ye49KnsUZUZXpiSSoREAREQBERAEREAREQBERAEREAREQBERAFOVCICrKKlMoCpFGUygJRQpQBERAEREAREQBERAQpRQUBKKMplASijKZQEooymUBKKMplASipypygJRRlMoCVCZTKAlERAEREAUKUQBFCICUUEqEBKZTKhATlQiICcqcqlAgKkUZTKAlFGUygJRQiAlERAEREAREQBERAEREAREQBERAEREARQmUBKKEQEoiIAiIgCIiAIiIAiIgCIiAIiIAoKEqEAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBSCoRAVIqUQFSKMplASijKICUUJlASijKZQEooTKAlFGUygIPNERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQE5TKhEBOVCIgCIiAIiIAiIgCIiAIiIAiIgCIiAJlEQDKZREAyiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiICcplQiAnKhEQBERAEREAypyoRATlMqEQE5RQiAqRUogKkVKICpRlQiAnKhEQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREB//2Q==" alt="Bayanihan Emirates Business Services" class="nav-logo"/>
      </div>
    </div>
    <div class="nav-links-wrap">
      <ul class="nav-links">
        <li><a href="#freezone">Why Freezone</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#pricing">Packages</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#lead-form">Contact</a></li>
      </ul>
    </div>
    <div class="nav-right">
      <a href="#lead-form" class="nav-cta">Talk to a Setup Expert</a>
    </div>
    <div class="hamburger" id="hamburger" onclick="toggleMenu()"><span></span><span></span><span></span></div>
  </div>
</nav>
<div class="nav-mobile-menu" id="mobile-menu">
  <a href="#freezone">Why Freezone</a>
  <a href="#services">Services</a>
  <a href="#pricing">Packages</a>
  <a href="#faq">FAQ</a>
  <a href="#lead-form">Contact</a>
  <a href="#lead-form" class="nav-mobile-cta">💬 Talk to a Setup Expert</a>
</div>

<!-- HERO -->
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-radial"></div>
  <div class="hero-radial2"></div>
  <div class="hero-blob hero-blob-1"></div>
  <div class="hero-blob hero-blob-2"></div>
  <div class="hero-blob hero-blob-3"></div>
  <div class="hero-shapes">
    <div class="hshape hshape-1"></div>
    <div class="hshape hshape-2"></div>
    <div class="hshape hshape-3"></div>
    <div class="hshape hshape-4"></div>
    <div class="hshape hshape-5"></div>
    <div class="hshape hshape-6"></div>
  </div>
  <div class="hero-skyline"></div>
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-badge">🇦🇪 UAE Freezone Specialists</div>
      <h1 class="hero-h1">Start Your Dubai Business with <span>100% Ownership</span> — Fast, Simple & Stress-Free</h1>
      <p class="hero-sub">Fast, affordable, and hassle-free company formation in the UAE. Your gateway to the world's most dynamic business hub.</p>
      <div class="hero-btns">
        <a href="#lead-form" class="btn-primary">✨ Get Your Free Business Setup Plan</a>
        <a href="#lead-form" class="btn-secondary">🚀 Start Your Dubai Business Today</a>
      </div>
      <div class="urgency-bar">
        <div class="urgency-pulse"></div>
        <div class="urgency-text">
          <span class="urgency-badge">🎯 Limited-Time Offer</span>
          <span class="urgency-body">Book this week and get a <strong>Free Business Setup Checklist</strong> + <strong>30-min Expert Consultation</strong> — worth AED 500, yours free.</span>
        </div>
        <div class="urgency-countdown">
          <span class="cd-label">Offer ends in</span>
          <div class="cd-timer">
            <div class="cd-block"><span id="cd-h">23</span><small>hrs</small></div>
            <div class="cd-sep">:</div>
            <div class="cd-block"><span id="cd-m">47</span><small>min</small></div>
            <div class="cd-block"><span id="cd-s">12</span><small>sec</small></div>
          </div>
        </div>
      </div>
      <div class="hero-trust">
        <div class="trust-badge"><span class="tb-icon">✅</span><span>1,000+ Businesses Setup</span></div>
        <div class="trust-badge"><span class="tb-icon">⚡</span><span>24–48 Hour Setup</span></div>
        <div class="trust-badge"><span class="tb-icon">🇦🇪</span><span>UAE Experts</span></div>
        <div class="trust-badge"><span class="tb-icon">🤝</span><span>Dedicated Consultant</span></div>
      </div>
      <div class="hero-tagline">
        🇵🇭 "From dreams to success, we're with you — because every Filipino deserves a brighter future."
      </div>
    </div>
    <div class="hero-right" id="lead-form">
      <div class="lead-form-card">
        <h3>Get Your Free Business Setup Quote</h3>
        <p>Fill in the form and our consultant will contact you within 1 hour.</p>
        <div class="form-field">
          <label>Full Name</label>
          <input type="text" placeholder="e.g. Maria Santos"/>
        </div>
        <div class="form-field">
          <label>Email Address</label>
          <input type="email" placeholder="maria@email.com"/>
        </div>
        <div class="form-field">
          <label>WhatsApp / Phone</label>
          <input type="tel" placeholder="+971 50 123 4567"/>
        </div>
        <div class="form-field">
          <label>Business Activity</label>
          <select>
            <option value="" disabled selected>Select your business type</option>
            <option>Trading & General Trading</option>
            <option>Consultancy & Professional Services</option>
            <option>E-commerce & Retail</option>
            <option>Technology & IT Services</option>
            <option>Food & Beverage</option>
            <option>Media & Marketing</option>
            <option>Real Estate</option>
            <option>Healthcare & Beauty</option>
            <option>Other</option>
          </select>
        </div>
        <button class="form-cta" onclick="submitForm()">🎯 Get a Free Quote Now</button>
        <p class="form-note">🔒 Your information is 100% confidential. No spam, ever.</p>
      </div>
    </div>
  </div>
</section>

<!-- WHO WE HELP -->
<section class="who-we-help">
  <div class="section-inner">
    <div class="wwh-inner">
      <div class="wwh-left">
        <div class="section-label">Who We Help</div>
        <h2 class="section-h2">Built for <span>Filipino Entrepreneurs</span> Ready to Take the Leap</h2>
        <p class="section-p">Whether you're an OFW, a freelancer, or an ambitious business owner — we understand your journey better than anyone. Bayanihan Emirates was built for you.</p>
        <a href="#lead-form" class="btn-primary" style="margin-top:28px;display:inline-flex;">✨ Get Your Free Business Setup Plan</a>
      </div>
      <div class="wwh-right">
        <div class="wwh-list">
          <div class="wwh-item">
            <div class="wwh-icon-wrap">🚀</div>
            <div class="wwh-content">
              <h4>Start a Business in Dubai</h4>
              <p>First-time entrepreneurs and OFWs ready to launch their own company with 100% ownership in a world-class freezone.</p>
            </div>
          </div>
          <div class="wwh-item">
            <div class="wwh-icon-wrap">🌍</div>
            <div class="wwh-content">
              <h4>Expand Internationally</h4>
              <p>Filipino business owners looking to access global markets and grow their brand beyond the Philippines using Dubai as their hub.</p>
            </div>
          </div>
          <div class="wwh-item">
            <div class="wwh-icon-wrap">💎</div>
            <div class="wwh-content">
              <h4>Build Long-Term Financial Stability</h4>
              <p>Professionals and investors who want a UAE residency, tax advantages, and a sustainable income outside of traditional employment.</p>
            </div>
          </div>
          <div class="wwh-item">
            <div class="wwh-icon-wrap">💼</div>
            <div class="wwh-content">
              <h4>Freelancers Going Independent</h4>
              <p>Skilled Filipinos in tech, marketing, design, and consulting who want to legalize their work and invoice global clients professionally.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- WHY DUBAI FREEZONE -->
<section class="freezone" id="freezone">
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">Why Freezone?</div>
      <h2 class="section-h2">The Smartest Way to Do <span>Business in Dubai</span></h2>
      <p class="section-p">Dubai Freezones offer unmatched advantages for entrepreneurs and investors from around the world.</p>
    </div>
    <div class="benefits-grid">
      <div class="benefit-card">
        <div class="benefit-icon">👑</div>
        <h4>100% Foreign Ownership</h4>
        <p>Retain full control of your company with no requirement for a local UAE partner or sponsor.</p>
      </div>
      <div class="benefit-card">
        <div class="benefit-icon">💰</div>
        <h4>Tax-Free Income</h4>
        <p>Enjoy 0% personal income tax and 0% corporate tax benefits available in UAE freezones.</p>
      </div>
      <div class="benefit-card">
        <div class="benefit-icon">🌍</div>
        <h4>Full Profit Repatriation</h4>
        <p>Transfer 100% of your profits and capital back home with zero restrictions or currency controls.</p>
      </div>
      <div class="benefit-card">
        <div class="benefit-icon">⚡</div>
        <h4>Quick Business Setup</h4>
        <p>Get your business license issued in as little as 24–48 hours with streamlined digital processes.</p>
      </div>
      <div class="benefit-card">
        <div class="benefit-icon">🤝</div>
        <h4>No Local Sponsor Required</h4>
        <p>Operate independently without the need for a UAE national partner or service agent.</p>
      </div>
      <div class="benefit-card">
        <div class="benefit-icon">🛂</div>
        <h4>Easy Visa Process</h4>
        <p>Apply for UAE residency visas for yourself, your family, and your employees with ease.</p>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section id="services">
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">Our Services</div>
      <h2 class="section-h2">Everything You Need to <span>Launch & Grow</span></h2>
      <p class="section-p">We handle every step of your business journey so you can focus on what matters most.</p>
    </div>
    <div class="services-grid">
      <div class="service-card">
        <div class="service-icon-wrap">🏢</div>
        <h4>Company Formation</h4>
        <p>Freezone, Mainland & Offshore business setup tailored to your goals and industry.</p>
        <a href="#lead-form" class="sc-link">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="service-icon-wrap">📋</div>
        <h4>Business Licensing</h4>
        <p>Commercial, professional, and industrial trade licenses issued fast and correctly.</p>
        <a href="#lead-form" class="sc-link">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="service-icon-wrap">🛂</div>
        <h4>Visa Processing</h4>
        <p>Investor, employee, and dependent visa applications handled end-to-end for you.</p>
        <a href="#lead-form" class="sc-link">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="service-icon-wrap">🏦</div>
        <h4>Bank Account Assistance</h4>
        <p>We guide you through opening your UAE corporate bank account smoothly and quickly.</p>
        <a href="#lead-form" class="sc-link">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="service-icon-wrap">⚙️</div>
        <h4>PRO Services</h4>
        <p>Government liaison, document attestation, renewals, and full compliance support.</p>
        <a href="#lead-form" class="sc-link">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="service-icon-wrap">🏬</div>
        <h4>Office Solutions</h4>
        <p>Flexi-desk, virtual office, and dedicated workspace options to suit your budget.</p>
        <a href="#lead-form" class="sc-link">Learn more →</a>
      </div>
    </div>
  </div>
</section>

<!-- 3-STEP PROCESS -->
<section class="process">
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">How It Works</div>
      <h2 class="section-h2">Your Business in <span>3 Simple Steps</span></h2>
      <p class="section-p">We've made the process effortless. From idea to licensed business in days, not months.</p>
    </div>
    <div class="steps">
      <div class="step">
        <div class="step-num"><span class="step-icon">🎯</span></div>
        <h4>Step 1: Choose Business Activity</h4>
        <p>Tell us what you want to do and we'll recommend the best freezone, license type, and structure for your goals.</p>
      </div>
      <div class="step">
        <div class="step-num"><span class="step-icon">📄</span></div>
        <h4>Step 2: Submit Documents</h4>
        <p>Send us your passport, photos, and any required documents — we prepare all application paperwork for you.</p>
      </div>
      <div class="step">
        <div class="step-num"><span class="step-icon">🎉</span></div>
        <h4>Step 3: Get License & Start Business</h4>
        <p>Receive your trade license, open a bank account, and start operating your Dubai business — officially!</p>
      </div>
    </div>
  </div>
</section>

<!-- PRICING -->
<section id="pricing">
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">Packages & Pricing</div>
      <h2 class="section-h2">Transparent Pricing, <span>No Hidden Fees</span></h2>
      <p class="section-p">Choose the package that fits your business needs and budget. All packages include government fees and our expert guidance.</p>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <div class="price-tier">Starter</div>
        <div class="price-name">Solo Starter</div>
        <div class="price-amount">AED 5,750 <span>/ year</span></div>
        <p class="price-desc">Perfect for freelancers & solo entrepreneurs starting their UAE journey.</p>
        <ul class="price-features">
          <li>1 Trade License Activity</li>
          <li>1 Visa Allocation</li>
          <li>Flexi Desk Included</li>
          <li>Company Stamp & MOA</li>
          <li>E-Channel Registration</li>
          <li>1 Year License</li>
        </ul>
        <button class="price-btn" onclick="scrollToForm()">Get Started</button>
      </div>
      <div class="price-card featured">
        <div class="price-tier">Standard</div>
        <div class="price-name">Business Pro</div>
        <div class="price-amount">AED 12,500 <span>/ year</span></div>
        <p class="price-desc">Ideal for small teams and growing businesses with visa requirements.</p>
        <ul class="price-features">
          <li>3 Trade License Activities</li>
          <li>3 Visa Allocations</li>
          <li>Shared Office Space</li>
          <li>Bank Account Assistance</li>
          <li>Company Stamp & MOA</li>
          <li>PRO Services Included</li>
        </ul>
        <button class="price-btn" onclick="scrollToForm()">Get Started</button>
      </div>
      <div class="price-card">
        <div class="price-tier">Premium</div>
        <div class="price-name">Enterprise Plus</div>
        <div class="price-amount">AED 22,000 <span>/ year</span></div>
        <p class="price-desc">Full-scale setup for businesses with larger teams and operations.</p>
        <ul class="price-features">
          <li>Unlimited License Activities</li>
          <li>6 Visa Allocations</li>
          <li>Dedicated Private Office</li>
          <li>Priority Bank Assistance</li>
          <li>Full PRO Services</li>
          <li>Dedicated Account Manager</li>
        </ul>
        <button class="price-btn" onclick="scrollToForm()">Get Started</button>
      </div>
    </div>
  </div>
</section>

<!-- WHY CHOOSE US -->
<section class="why-us">
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">Why Choose Us</div>
      <h2 class="section-h2">Your Trusted Partner in the UAE</h2>
      <p class="section-p">We're not just a business setup firm — we're your community, your support system, your bridge to success in Dubai.</p>
    </div>
    <div class="why-grid">
      <div class="why-card">
        <div class="why-icon">🇵🇭</div>
        <h4>Filipino-Focused Support</h4>
        <p>We understand the unique journey of Filipino entrepreneurs and speak your language — literally and culturally.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">🏙️</div>
        <h4>Deep UAE Expertise</h4>
        <p>Years of hands-on experience navigating UAE regulations, freezones, and government systems.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">⚡</div>
        <h4>Lightning-Fast Processing</h4>
        <p>We prioritize speed. Get your license issued in 24–48 hours with our streamlined process.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">💎</div>
        <h4>Transparent Pricing</h4>
        <p>What you see is what you pay. No hidden fees, no surprises — ever. Just honest, clear pricing.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">👩‍💼</div>
        <h4>Dedicated Consultants</h4>
        <p>You get a personal consultant who guides you from day one through every step of your business journey.</p>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section>
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">Client Stories</div>
      <h2 class="section-h2">Real People, <span>Real Success Stories</span></h2>
      <p class="section-p">Hear from fellow Filipinos and entrepreneurs who trusted Bayanihan Emirates to build their Dubai dreams.</p>
    </div>
    <div class="testi-grid">
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-text">"Hindi ko inakala na ganito kadali mag-setup ng business sa Dubai! In just 2 days, I had my trade license in hand. Sobrang helpful ng team ng Bayanihan Emirates. Highly recommended!"</p>
        <div class="testi-author">
          <div class="testi-avatar">M</div>
          <div>
            <div class="testi-name">Maria Reyes</div>
            <div class="testi-role">E-commerce Entrepreneur, Cebu → Dubai</div>
          </div>
        </div>
      </div>
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-text">"As an OFW, I was nervous about setting up a business abroad. But Bayanihan Emirates made it feel like home. They walked me through everything patiently. Now I own a consulting firm in DMCC!"</p>
        <div class="testi-author">
          <div class="testi-avatar">J</div>
          <div>
            <div class="testi-name">Jose Dela Cruz</div>
            <div class="testi-role">Management Consultant, Manila → Dubai</div>
          </div>
        </div>
      </div>
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-text">"The team is incredibly professional and responsive. They helped me open my bank account, process my visa, and even advised me on the best freezone for my trading business. Worth every dirham!"</p>
        <div class="testi-author">
          <div class="testi-avatar">A</div>
          <div>
            <div class="testi-name">Ana Villanueva</div>
            <div class="testi-role">General Trading Business Owner, Davao → Dubai</div>
          </div>
        </div>
      </div>
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-text">"I was based in the Philippines when I decided to set up in Dubai. Bayanihan Emirates handled everything remotely. I didn't have to fly to UAE until my license was ready. Game-changer!"</p>
        <div class="testi-author">
          <div class="testi-avatar">R</div>
          <div>
            <div class="testi-name">Ramon Santos</div>
            <div class="testi-role">Digital Marketing Agency, Quezon City → Dubai</div>
          </div>
        </div>
      </div>
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-text">"Transparent pricing, fast service, walang bitin! They delivered exactly what was promised and more. Proud to say I'm now a licensed Dubai business owner thanks to this amazing team!"</p>
        <div class="testi-author">
          <div class="testi-avatar">L</div>
          <div>
            <div class="testi-name">Leilani Buenaventura</div>
            <div class="testi-role">Beauty & Wellness Entrepreneur, Iloilo → Dubai</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="faq" id="faq">
  <div class="section-inner">
    <div class="section-header center">
      <div class="section-label">FAQ</div>
      <h2 class="section-h2">Got Questions? <span>We Have Answers.</span></h2>
      <p class="section-p">Everything you need to know about starting your business in Dubai.</p>
    </div>
    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">How long does it take to set up a business in Dubai?</button>
        <div class="faq-a"><div class="faq-a-inner">Most freezone business setups take between 24 to 72 hours from the time all documents are submitted. Some freezones offer same-day licensing. For mainland businesses, the process typically takes 5–10 working days. We'll give you a specific timeline once we review your business activity.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Do I need to be physically present in the UAE to register?</button>
        <div class="faq-a"><div class="faq-a-inner">No! In most cases, you can complete the entire registration process remotely from the Philippines or anywhere in the world. You will need to travel to the UAE eventually to open a bank account and activate your residency visa, but the business license itself can often be obtained without being physically present.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">How much does it cost to set up a business in Dubai?</button>
        <div class="faq-a"><div class="faq-a-inner">Costs vary depending on the freezone, license type, number of visas, and office requirements. Our packages start from AED 5,750 per year for solo entrepreneurs. We offer transparent, all-inclusive packages with no hidden fees. Contact us for a free, customized quote based on your specific needs.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Can I open a corporate bank account in Dubai?</button>
        <div class="faq-a"><div class="faq-a-inner">Yes, absolutely. Dubai has excellent banking infrastructure with both local and international banks. We assist our clients in preparing all necessary documentation and guide you through the bank account opening process. Note that you typically need to visit UAE in person to complete bank account opening procedures.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">What is the difference between Freezone, Mainland, and Offshore?</button>
        <div class="faq-a"><div class="faq-a-inner">A Freezone company allows 100% foreign ownership but restricts direct trade within the UAE market. A Mainland company lets you trade freely within UAE and across the GCC. An Offshore company is ideal for holding assets, international trading, and tax optimization without requiring a physical UAE office. We'll recommend the right structure for your specific goals.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Can my family members get UAE residency visas too?</button>
        <div class="faq-a"><div class="faq-a-inner">Yes! As a business owner in Dubai, you can sponsor UAE residency visas for your spouse and dependent children. The number of dependents you can sponsor typically depends on your income level and the type of visa you hold. Our team handles all dependent visa applications as part of our comprehensive services.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- FINAL CTA -->
<section class="final-cta">
  <div>
    <h2>Ready to Start Your Business in Dubai?</h2>
    <p>Join over 1,000 entrepreneurs who've built their future in the UAE with Bayanihan Emirates. <br/>Your dream is closer than you think — let's make it happen together.</p>
    <div class="final-cta-btns">
      <a href="#lead-form" class="btn-white">📞 Get Your Free Business Setup Plan</a>
      <a href="https://wa.me/971501234567" class="btn-gold" target="_blank">💬 Chat on WhatsApp</a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAIrBMgDASIAAhEBAxEB/8QAHQABAAEFAQEBAAAAAAAAAAAAAAECBQYHCAQDCf/EAGEQAAEDAwEEBQUGDQ0PBQEAAwEAAgMEBREGBxIhMQgTQVFhFCJxgZEVMlKhsdEWI0JVYnKCkpOUssHSFzM1NkNTVGNzdKKjsyQlJic0N0RFVmRldcLh8BiDhKS08ZXT4v/EABsBAQACAwEBAAAAAAAAAAAAAAAEBQIDBgEH/8QAPREAAgIBAgMDCgUEAQQCAwAAAAECAwQFERIhMRNBUQYUIjJSYXGBkdEzNKGx4RUjwfBCFiRTcmJjNUOS/9oADAMBAAIRAxEAPwDshERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAER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ZX10gL8+Djy9DfYtd686SNupXPpNHW01zxw8sqwY4h4tZ753rwufNaax1DrC5mvv1ylqn5PVx5LYoh3NaOA+XxVh3sHiV3WHoNNKXac34LofOcrU78mblKW78WZRrTXWqdXzF1+u89VHnLacHchb6GDh7clYwcYxgexMjsQkK8hCMFwxWyK9tvqUkA9gXzdDE7nG0+pfRF7shued1FC7k0tPgV8n2/HvJcH7IL3ZUrB1QfVHqk0WjqqqlmbNFvMkYctkjcQ5p7wRxC2boLpBbRNLSRQVVc2/UDOBp7hlzwPsZR54Pp3gO5YSvjNTQzDz4xnvAwVEuwYWLZm2FzidobMNvuh9ZmKjqKg2K6vwPJa14DHn+Ll9670HdPgttNIIBGOK/Mia2lvGJ28D9S7tWwtme27XGg5YqN1Q67WlvA0Na4ndb/Fyc2+jiPBUOTpEoc4E2vK36neyLXuyva9o/aDTtjttb5Lcw3MlvqiGTDvLex48W+vC2DnPJU04Sg9pLZktSUuaJRQFKxPQoKlEBSikqEAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAFJUZUSPaxrnPIa1vEk8ggKicLANpu1Kw6MYaVzvL7q4ebRwuGW9xkdyYPjPYFgW1/bPumax6OmBfxZPcRghneIu8/Zch2ZWgpZJJZXzSyPklkcXPe9xLnOPMknmSq3Kz1D0a+p2OjeS8r0rcrlHw739jJNea81HrKqLrvWbtKDmOjhy2Fvdw+qPifiWM5zzUAYCkclTzm5veXM76iivHgoVJJDn2YQcFKhYm4IikLwAKoY9ahM4BOMnsA7UHTmZBoPSd01jf47RbW7v1VRO4ZZAz4R7z2Adp9eOtNH6XsOh9PGmomRwQxMMlTVSuAc/AyXvd/4ArZsX0hDpHRtPC+MC41TRNWv7S8j3voaOA9Z7VoDpUbVKq73iq0NZqkQ2qif1de9jsGplHNmfgNPDHaQc8Auq0jS3ZJJde9+B8n8pNelk2OEX6C6e/3lW3bb1LeZqiwaRqn09p4smq4+EtV2HdPNsfiOJ8OS0DLVPJIa0N/MvmxnWPDYWukcexjS4k+pXWi0lqqvx5Fpi9VAPIx0Mp+PC7mqNeNDghyOJlvN8TLS6WU/Vn2qN955ud7Vl0Gy7aLKMs0VfD6aUj5VE+zDaLC3efom+bve2lLvkR5EPa/U94H4GJiSQcnu9qqFRMPqyfSvdcdPagtxPuhYbrSY/fqORo9pCthOCQeGO/gvVan0Z5w+49Laxw980H0L7R1MT+3dPivAoPBbY3SR44Jl2GCFKtccskZy0nHcvXDVNcQH+ae/sW+Nyl1MHBo9QRRkEZB4d6ZW0wJXzlijlG69ocPQvohR8weDyWekqY6ugqJYZ4nB8b2PLXscORa4cQVvfZF0mbjap4rNtDjlr6MYY25RM+nxD+MaP1weI87wctLYXmq6SKo9+3Du8c1X5Wn13Lob675QZ+j9hvFsvtqgutnroK6hnbvRTwvDmuHq7RyxzC96/O3Zzr3VuzO6eVWGtLqN7gaijmy6nnx8Jv1Lvshg+nkuytj+2LTG0WlbDSv9z7yxuZrdUOG+O8sP1bfEcR2gLlcrAsx34osqrozNkoiKCbwoIUqEBCIUQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBEHih8AgPlVVENJTy1NTLHFDE0ve95wGgcSSewLmLbHtcqdTSzWXT8slPZQS2SYZa+q/O1nxnt4cFmHSs1HLTWq36appnN8tcZqoNOMxsIw0+Bdx+5XOw4H4lU5+U0+zj8zvPJjRa5QWXct33L/JWCOXYFTy4KR6EKqTuSEUovAQpwoUhD0YUphEDC+lPIIKmCoLd4RSskLfhBrgSPiVACY45Xq6njSaaZ3Fpi+2u/wBnp7ha6uOoglYMFp4tOORHMEdxVrrNC6DfVS1tVpeyOnkcXySSUjMuJOSSSOJXHVBX19vlMtBXVdG883U87oyfTukKK64V9cc1tfW1XhNUPf8AKSriGrOC5J7/ABODs8iuKx7WLh96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QUBKKMplASijKZQEooymUBKKMplASipypygJRRlMoCVCZTKAlERAEREAUKUQBFCICUUEqEBKZTKhATlQiICcqcqlAgKkUZTKAlFGUygJRQiAlERAEREAREQBERAEREAREQBERAEREARQmUBKKEQEoiIAiIgCIiAIiIAiIgCIiAIiIAoKEqEAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBSCoRAVIqUQFSKMplASijKICUUJlASijKZQEooTKAlFGUygIPNERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQE5TKhEBOVCIgCIiAIiIAiIgCIiAIiIAiIgCIiAJlEQDKZREAyiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiICcplQiAnKhEQBERAEREAypyoRATlMqEQE5RQiAqRUogKkVKICpRlQiAnKhEQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREB//2Q==" alt="Bayanihan Emirates Business Services"/>
        <p>Your trusted Filipino-run business setup consultancy in the UAE. Helping entrepreneurs from the Philippines and beyond build their future in Dubai since 2015.</p>
        <div class="footer-socials">
          <a class="social-btn" href="#" title="Facebook">📘</a>
          <a class="social-btn" href="#" title="Instagram">📷</a>
          <a class="social-btn" href="#" title="LinkedIn">💼</a>
          <a class="social-btn" href="#" title="TikTok">🎵</a>
        </div>
      </div>
      <div>
        <h5>Quick Links</h5>
        <ul>
          <li><a href="#freezone">Why Dubai Freezone</a></li>
          <li><a href="#services">Our Services</a></li>
          <li><a href="#pricing">Packages</a></li>
          <li><a href="#faq">FAQ</a></li>
          <li><a href="#lead-form">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h5>Our Services</h5>
        <ul>
          <li><a href="#">Company Formation</a></li>
          <li><a href="#">Business Licensing</a></li>
          <li><a href="#">Visa Processing</a></li>
          <li><a href="#">Bank Account Setup</a></li>
          <li><a href="#">PRO Services</a></li>
          <li><a href="#">Office Solutions</a></li>
        </ul>
      </div>
      <div class="footer-contact">
        <h5>Contact Us</h5>
        <p>📍 Office 2104, Single Business Tower, Business Bay, Dubai, UAE</p>
        <p>📞 <a href="tel:+971501234567" style="color:rgba(255,255,255,0.65)">+971 50 123 4567</a></p>
        <p>✉️ <a href="/cdn-cgi/l/email-protection#5930373f36193b38203837303138373c34302b382d3c2a3b3023773a3634" style="color:rgba(255,255,255,0.65)"><span class="__cf_email__" data-cfemail="3f565159507f5d5e465e5156575e515a52564d5e4b5a4c5d5645115c5052">[email&#160;protected]</span></a></p>
        <p>🕐 Mon–Sat: 9:00 AM – 7:00 PM</p>
      </div>
    </div>
    <hr class="footer-divider"/>
    <div class="footer-bottom">
      <span>© 2025 Bayanihan Emirates Business Services. All rights reserved.</span>
      <span>Designed with ❤️ for the Filipino community</span>
    </div>
  </div>
</footer>

<!-- WHATSAPP FLOAT -->
<a href="https://wa.me/971501234567" class="wa-float" target="_blank" title="Chat with a Consultant on WhatsApp">
  <svg class="wa-icon" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  <span class="wa-label">Chat with a Consultant</span>
  <span class="wa-dot"></span>
</a>

<!-- GSAP + ScrollTrigger -->
<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/TextPlugin.min.js"></script>

<script>
  /* ── UTILITY ── */
  function toggleFaq(btn){
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  }
  /* ── COUNTDOWN TIMER ── */
  (function(){
    // Persist end time in sessionStorage so it doesn't reset on scroll
    let end = sessionStorage.getItem('urgency_end');
    if (!end) {
      end = Date.now() + (23 * 3600 + 47 * 60 + 12) * 1000;
      sessionStorage.setItem('urgency_end', end);
    }
    function tick(){
      const diff = Math.max(0, end - Date.now());
      const h = Math.floor(diff / 3600000);
      const m = Math.floor((diff % 3600000) / 60000);
      const s = Math.floor((diff % 60000) / 1000);
      const hEl = document.getElementById('cd-h');
      const mEl = document.getElementById('cd-m');
      const sEl = document.getElementById('cd-s');
      if (hEl) hEl.textContent = String(h).padStart(2,'0');
      if (mEl) mEl.textContent = String(m).padStart(2,'0');
      if (sEl) sEl.textContent = String(s).padStart(2,'0');
    }
    tick();
    setInterval(tick, 1000);
  })();

  function scrollToForm(){ document.getElementById('lead-form').scrollIntoView({behavior:'smooth'}); }
  function toggleMenu(){
    const menu = document.getElementById('mobile-menu');
    const ham = document.getElementById('hamburger');
    const isOpen = menu.classList.contains('open');
    menu.classList.toggle('open', !isOpen);
    ham.classList.toggle('open', !isOpen);
  }
  // Close mobile menu on link click
  document.querySelectorAll('.nav-mobile-menu a').forEach(a => {
    a.addEventListener('click', () => {
      document.getElementById('mobile-menu').classList.remove('open');
      document.getElementById('hamburger').classList.remove('open');
    });
  });
  // Scroll shrink + shadow
  const mainNav = document.getElementById('main-nav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) { mainNav.classList.add('scrolled'); }
    else { mainNav.classList.remove('scrolled'); }
  }, { passive: true });
  function submitForm(){
    const btn = document.querySelector('.form-cta');
    btn.textContent = '✅ Submitting...';
    gsap.to(btn, { scale: 0.96, duration: 0.1, yoyo: true, repeat: 1 });
    setTimeout(() => {
      btn.textContent = "🎉 Thank You! We'll contact you soon.";
      btn.style.background = 'linear-gradient(135deg,#25d366,#1ebe5c)';
      gsap.fromTo(btn, { scale: 0.9 }, { scale: 1, duration: 0.5, ease: 'back.out(2)' });
    }, 1200);
  }

  /* ── WAIT FOR GSAP ── */
  window.addEventListener('load', () => {
    gsap.registerPlugin(ScrollTrigger, TextPlugin);

    /* ── 1. NAV: slide down on load ── */
    gsap.from('.nav', {
      yPercent: -100, opacity: 0, duration: 0.7, ease: 'power3.out', delay: 0.1
    });
    gsap.from('.nav-logo', { opacity: 0, scale: 0.85, duration: 0.6, delay: 0.4, ease: 'back.out(2)' });
    gsap.from('.nav-links li', { opacity: 0, y: -10, stagger: 0.07, duration: 0.45, delay: 0.5, ease: 'power2.out' });
    gsap.from('.nav-cta', { opacity: 0, scale: 0.85, duration: 0.5, delay: 0.75, ease: 'back.out(2)' });

    /* ── FLOATING SHAPES: stagger in then loop float ── */
    gsap.to('.hshape', { opacity: 1, stagger: 0.18, duration: 0.6, delay: 1.2, ease: 'power2.out' });
    gsap.utils.toArray('.hshape').forEach((s, i) => {
      gsap.to(s, {
        y: `${(i % 2 === 0 ? -1 : 1) * (8 + i * 2)}px`,
        x: `${(i % 3 === 0 ? 1 : -1) * (4 + i)}px`,
        rotation: `+=${(i % 2 === 0 ? 12 : -12)}`,
        duration: 3.5 + i * 0.5, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: i * 0.4
      });
    });

    /* ── BLOBS: slow drift ── */
    gsap.to('.hero-blob-1', { x: 30, y: 20, duration: 8, ease: 'sine.inOut', yoyo: true, repeat: -1 });
    gsap.to('.hero-blob-2', { x: -20, y: -15, duration: 10, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: 2 });
    gsap.to('.hero-blob-3', { x: 15, y: 25, duration: 7, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: 1 });

    /* ── SKYLINE: fade up on load ── */
    gsap.from('.hero-skyline', { opacity: 0, y: 40, duration: 1.4, delay: 0.8, ease: 'power2.out' });

    /* ── 2. HERO: staggered cinematic entrance ── */
    const heroTl = gsap.timeline({ delay: 0.5 });
    heroTl
      .from('.hero-badge',  { opacity: 0, y: 30, duration: 0.6, ease: 'power3.out' })
      .from('.hero-h1',     { opacity: 0, y: 40, duration: 0.7, ease: 'power3.out' }, '-=0.3')
      .from('.hero-sub',    { opacity: 0, y: 30, duration: 0.6, ease: 'power3.out' }, '-=0.4')
      .from('.hero-tagline',{ opacity: 0, x: -40, duration: 0.6, ease: 'power3.out' }, '-=0.3')
      .from('.hero-btns .btn-primary',   { opacity: 0, scale: 0.8, duration: 0.5, ease: 'back.out(2)' }, '-=0.2')
      .from('.hero-btns .btn-secondary', { opacity: 0, scale: 0.8, duration: 0.5, ease: 'back.out(2)' }, '-=0.35')
      .from('.urgency-bar',  { opacity: 0, y: 16, duration: 0.55, ease: 'power3.out' }, '-=0.2')
      .from('.hero-tagline', { opacity: 0, x: -40, duration: 0.6, ease: 'power3.out' }, '-=0.2')
      .from('.trust-badge', { opacity: 0, y: 20, stagger: 0.15, duration: 0.5, ease: 'power2.out' }, '-=0.2')
      .from('.lead-form-card', { opacity: 0, x: 60, duration: 0.8, ease: 'power3.out' }, '-=0.9');

    /* ── 3. HERO SKYLINE: slow parallax drift ── */
    gsap.to('.hero-skyline', {
      yPercent: 20,
      ease: 'none',
      scrollTrigger: { trigger: '.hero', scrub: 1.5 }
    });

    /* ── 4. SECTION LABELS: fade + slide up ── */
    gsap.utils.toArray('.section-label').forEach(el => {
      gsap.from(el, {
        opacity: 0, y: 20, duration: 0.5,
        scrollTrigger: { trigger: el, start: 'top 88%', toggleActions: 'play none none none' }
      });
    });

    /* ── 5. SECTION HEADINGS: word-by-word reveal ── */
    gsap.utils.toArray('.section-h2').forEach(el => {
      gsap.from(el, {
        opacity: 0, y: 35, duration: 0.7, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });

    /* ── WHO WE HELP: left slides in, items stagger from right ── */
    gsap.from('.wwh-left > *', {
      opacity: 0, x: -50, stagger: 0.12, duration: 0.7, ease: 'power3.out',
      scrollTrigger: { trigger: '.who-we-help', start: 'top 78%', toggleActions: 'play none none none' }
    });
    gsap.from('.wwh-item', {
      opacity: 0, x: 50, stagger: 0.13, duration: 0.65, ease: 'power3.out',
      scrollTrigger: { trigger: '.wwh-list', start: 'top 82%', toggleActions: 'play none none none' }
    });
    gsap.utils.toArray('.wwh-icon-wrap').forEach((icon, i) => {
      gsap.to(icon, {
        y: -5, duration: 1.6 + i * 0.2, ease: 'sine.inOut',
        yoyo: true, repeat: -1, delay: i * 0.3
      });
    });

    /* ── 6. BENEFIT CARDS: staggered fan-up ── */
    gsap.from('.benefit-card', {
      opacity: 0, y: 50, scale: 0.94, stagger: 0.1, duration: 0.65, ease: 'power3.out',
      scrollTrigger: { trigger: '.benefits-grid', start: 'top 80%', toggleActions: 'play none none none' }
    });

    /* ── 7. SERVICE CARDS: cascade with slight rotation ── */
    gsap.from('.service-card', {
      opacity: 0, y: 50, scale: 0.93, stagger: { amount: 0.55, from: 'start' },
      duration: 0.65, ease: 'back.out(1.5)',
      scrollTrigger: { trigger: '.services-grid', start: 'top 80%', toggleActions: 'play none none none' }
    });
    gsap.from('.service-icon-wrap', {
      scale: 0, rotation: -20, stagger: { amount: 0.55, from: 'start' }, duration: 0.5, ease: 'back.out(2)', delay: 0.15,
      scrollTrigger: { trigger: '.services-grid', start: 'top 80%', toggleActions: 'play none none none' }
    });

    /* ── 8. PROCESS STEPS: slide in from sides alternating ── */
    gsap.utils.toArray('.step').forEach((step, i) => {
      gsap.from(step, {
        opacity: 0, x: i % 2 === 0 ? -50 : 50, duration: 0.7, ease: 'power3.out',
        scrollTrigger: { trigger: step, start: 'top 82%', toggleActions: 'play none none none' }
      });
    });

    /* ── 9. STEP NUMBERS: pop bounce ── */
    gsap.utils.toArray('.step-num').forEach((num, i) => {
      gsap.from(num, {
        scale: 0, rotation: -180, duration: 0.7, ease: 'back.out(2)', delay: i * 0.15,
        scrollTrigger: { trigger: num, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });

    /* ── 10. PRICING CARDS: rise up with depth ── */
    gsap.from('.price-card', {
      opacity: 0, y: 60, scale: 0.92, stagger: 0.15, duration: 0.75, ease: 'power3.out',
      scrollTrigger: { trigger: '.pricing-grid', start: 'top 78%', toggleActions: 'play none none none' }
    });

    /* Featured card gets an extra glow pulse after entrance */
    ScrollTrigger.create({
      trigger: '.price-card.featured', start: 'top 78%',
      onEnter: () => {
        gsap.to('.price-card.featured', {
          boxShadow: '0 0 0 6px rgba(26,111,173,0.25)', duration: 0.4,
          yoyo: true, repeat: 3, ease: 'power1.inOut'
        });
      }
    });

    /* ── 11. WHY-US CARDS: stagger left to right ── */
    gsap.from('.why-card', {
      opacity: 0, y: 40, scale: 0.9, stagger: 0.1, duration: 0.6, ease: 'back.out(1.5)',
      scrollTrigger: { trigger: '.why-grid', start: 'top 80%', toggleActions: 'play none none none' }
    });

    /* ── 12. TESTIMONIALS: slide up with depth ── */
    gsap.from('.testi-card', {
      opacity: 0, y: 50, stagger: 0.12, duration: 0.65, ease: 'power3.out',
      scrollTrigger: { trigger: '.testi-grid', start: 'top 80%', toggleActions: 'play none none none' }
    });

    /* ── 13. FAQ ITEMS: slide from left ── */
    gsap.from('.faq-item', {
      opacity: 0, x: -40, stagger: 0.08, duration: 0.55, ease: 'power3.out',
      scrollTrigger: { trigger: '.faq-list', start: 'top 82%', toggleActions: 'play none none none' }
    });

    /* ── 14. FINAL CTA: zoom in from below ── */
    gsap.from('.final-cta h2', {
      opacity: 0, y: 40, duration: 0.7, ease: 'power3.out',
      scrollTrigger: { trigger: '.final-cta', start: 'top 80%', toggleActions: 'play none none none' }
    });
    gsap.from('.final-cta p', {
      opacity: 0, y: 30, duration: 0.6, delay: 0.15, ease: 'power3.out',
      scrollTrigger: { trigger: '.final-cta', start: 'top 80%', toggleActions: 'play none none none' }
    });
    gsap.from('.final-cta-btns a', {
      opacity: 0, scale: 0.8, stagger: 0.15, duration: 0.55, ease: 'back.out(2)', delay: 0.3,
      scrollTrigger: { trigger: '.final-cta', start: 'top 80%', toggleActions: 'play none none none' }
    });

    /* ── 15. FOOTER: fade up in blocks ── */
    gsap.from('.footer-grid > *', {
      opacity: 0, y: 30, stagger: 0.12, duration: 0.6, ease: 'power3.out',
      scrollTrigger: { trigger: '.footer-grid', start: 'top 90%', toggleActions: 'play none none none' }
    });

    /* ── 16. WHATSAPP BUTTON: bounce in after hero loads ── */
    gsap.from('.wa-float', {
      scale: 0, rotation: 360, duration: 0.8, delay: 2.5, ease: 'back.out(2)'
    });

    /* ── 17. BENEFIT ICONS: continuous gentle float ── */
    gsap.utils.toArray('.benefit-icon').forEach((icon, i) => {
      gsap.to(icon, {
        y: -6, duration: 1.8 + i * 0.15, ease: 'sine.inOut',
        yoyo: true, repeat: -1, delay: i * 0.2
      });
    });

    /* ── 18. TRUST BADGES: subtle shimmer loop ── */
    gsap.utils.toArray('.trust-badge').forEach((badge, i) => {
      gsap.to(badge, {
        boxShadow: '0 4px 20px rgba(26,111,173,0.22)',
        duration: 1.5, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: i * 0.5
      });
    });

    /* ── 19. SECTION PARALLAX BACKGROUNDS ── */
    gsap.utils.toArray('.freezone, .process, .faq').forEach(section => {
      gsap.fromTo(section,
        { backgroundPositionY: '0%' },
        { backgroundPositionY: '30%', ease: 'none',
          scrollTrigger: { trigger: section, scrub: 2 }
        }
      );
    });

    /* ── 20. COUNTER ANIMATION on trust badges text ── */
    const counters = [
      { el: document.querySelector('.trust-badge:nth-child(1)'), from: 0, to: 1000, suffix: '+ Businesses Setup' },
    ];
    ScrollTrigger.create({
      trigger: '.hero-trust', start: 'top 85%',
      onEnter: () => {
        counters.forEach(c => {
          if (!c.el) return;
          const obj = { val: c.from };
          gsap.to(obj, {
            val: c.to, duration: 1.8, ease: 'power2.out',
            onUpdate: () => { c.el.childNodes[c.el.childNodes.length - 1].textContent = ' ' + Math.round(obj.val) + c.suffix; }
          });
        });
      }
    });

    /* ── 22. MAGNETIC HOVER on primary buttons ── */
    document.querySelectorAll('.btn-primary, .btn-gold, .nav-cta').forEach(btn => {
      btn.addEventListener('mousemove', e => {
        const rect = btn.getBoundingClientRect();
        const dx = (e.clientX - rect.left - rect.width / 2) * 0.25;
        const dy = (e.clientY - rect.top - rect.height / 2) * 0.25;
        gsap.to(btn, { x: dx, y: dy, duration: 0.3, ease: 'power2.out' });
      });
      btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.4)' });
      });
    });

    /* ── 23. CARD TILT on benefit & service cards ── */
    document.querySelectorAll('.benefit-card, .price-card').forEach(card => {
      card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const rx = ((e.clientY - rect.top)  / rect.height - 0.5) * -10;
        const ry = ((e.clientX - rect.left) / rect.width  - 0.5) *  10;
        gsap.to(card, { rotationX: rx, rotationY: ry, transformPerspective: 800, duration: 0.3, ease: 'power2.out' });
      });
      card.addEventListener('mouseleave', () => {
        gsap.to(card, { rotationX: 0, rotationY: 0, duration: 0.5, ease: 'elastic.out(1, 0.5)' });
      });
    });

    /* ── 24. SCROLL PROGRESS INDICATOR ── */
    const bar = document.createElement('div');
    bar.style.cssText = 'position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#1a6fad,#f0a500);"""

st.components.v1.html(HTML, height=9000, scrolling=True)
