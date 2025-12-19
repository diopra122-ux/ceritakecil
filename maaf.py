import streamlit as st
import os, base64

st.set_page_config(page_title="Kenangan Kita 💖", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #ff5fa2, #2a001f);
    color: white;
}
.card {
    background: rgba(0,0,0,0.45);
    border: 2px solid #ff6fb5;
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 0 25px rgba(255,111,181,0.6);
    margin: 20px;
    animation: fadein 0.8s;
}
h1, h2, h3 {
    text-align: center;
    color: white;
    text-shadow: 0 0 5px #ff5fa2, 0 0 10px #ff5fa2, 0 0 15px #ff9ac1, 0 0 20px #ff9ac1;
}
.center-btn {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}
.center-btn button, .stButton>button {
    background: linear-gradient(90deg,#c2185b,#ad1457) !important;
    color: #ffffff !important;
    border-radius: 30px;
    height: 3em;
    width: 200px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 0 0 10px rgba(255,255,255,0.4);
}
.stButton>button:hover {
    background: linear-gradient(90deg,#ad1457,#c2185b) !important;
}
.img-box {
    border: 3px solid #ff5fa2;
    border-radius: 20px;
    padding: 6px;
    box-shadow: 0 0 20px rgba(255,95,162,0.8);
    animation: float 3s ease-in-out infinite;
    display: inline-block;
}
.img-box img {
    border-radius: 16px;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}
@keyframes fadein {
    from {opacity: 0;}
    to {opacity: 1;}
}
.song-card {
    background: rgba(0,0,0,0.5);
    border: 2px solid #ff6fb5;
    border-radius: 18px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 0 15px rgba(255,111,181,0.5);
}
</style>
""", unsafe_allow_html=True)

# ================= HELPERS =================
def show_image_outline(path, width=350):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div class="img-box">
            <img src="data:image/jpeg;base64,{data}" width="{width}">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"⚠️ {path} tidak ditemukan")

# ================= STATE =================
if "page" not in st.session_state:
    st.session_state.page = 0
if "song" not in st.session_state:
    st.session_state.song = None

def next_page():
    st.session_state.page += 1
def prev_page():
    st.session_state.page -= 1

# ================= GLOBAL AUDIO =================
if st.session_state.song and os.path.exists(st.session_state.song):
    st.audio(st.session_state.song, autoplay=True)

# ================= PAGES =================

# ---------- PAGE 0 : LOGIN ----------
if st.session_state.page == 0:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>Dariku untukmu 🔐</h1>", unsafe_allow_html=True)
    code = st.text_input("Kode:PW LAPTOP", type="password")
    if st.button("Masuk"):
        if code == "22022022":
            st.session_state.page = 1
            st.rerun()
        else:
            st.error("Kode salah 😢")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- PAGE 1 : PLAYLIST ----------
elif st.session_state.page == 1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>Pilih diantara tiga lagu ini yaa 🎶</h1>", unsafe_allow_html=True)
    st.write("Kenapa aku milih lagu ini? Hm.. mungkin aku ngerasa kamu ada di lagu ini si, makanya aku pilih tiga lagu ini. Lagunya bakal nemenin kamu baca catatan kecilku untukmu.")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='song-card'>", unsafe_allow_html=True)
        show_image_outline("9.jpg", 220)
        st.subheader("Rumah Itu")
        st.caption("Sal Priadi")
        if st.button("▶ Play", key="rumah"):
            st.session_state.song = "rumah_itu.mp3"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='song-card'>", unsafe_allow_html=True)
        show_image_outline("7.jpg", 220)
        st.subheader("Bertaut")
        st.caption("Nadin Amizah")
        if st.button("▶ Play", key="bertaut"):
            st.session_state.song = "Bertaut.mp3"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='song-card'>", unsafe_allow_html=True)
        show_image_outline("8.jpg", 220)
        st.subheader("You're Gonna Live Forever in Me")
        st.caption("John Mayer")
        if st.button("▶ Play", key="john"):
            st.session_state.song = "youre_gonna_live_forever_in_me.mp3"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
    if st.button("➡ Lanjut"):
        next_page(); st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- PAGE 2 : Foto bareng pertama ----------
elif st.session_state.page == 2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Foto bareng pertama</h2>", unsafe_allow_html=True)
        st.write("""
Huh... ini fotbar pertama kita di SMA ga sii?? aku ngrasa gitu si


Aku masih malu ga si sama kamu waktu itu wkwk, tpi happy si di inget-inget momen ini

Habis foto kita pulang bareng gasii? apa engga ya? lupa deh wkwk.

Sejak saat itu aku selalu mikir kamu spesial, meskipun kadang aku suka nakal.

Aduhh.. momen kek gtu ga bisa diulang lagi ya.

Ga kerasa.. momen itu udah hampir 4 tahun yang lalu
Makasih udah milih aku waktu itu ya..
""")
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("⬅ Kembali"):
            prev_page(); st.rerun()
        if st.button("➡ Lanjut"):
            next_page(); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        show_image_outline("1.jpg", 350)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- PAGE 3 : Pantai Pertama Kita ----------
elif st.session_state.page == 3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Pantai Pertama Kita</h2>", unsafe_allow_html=True)
        st.write("""
Kangen ga sii.. ini spesial banget jujur

Kita berdua ✌️ nekat bawa budget pas-pas an buat ke pantai wkwkw.. lucu dah

Ingat juga ga?? kamu kiss pipi aku untuk pertama kalinya dan aku kaget wkwk

Btw tang.. momen lucunya waktu kamu bawa celana pendek kamu hampir ga nyebur wkwk dan akhirnya make celana aku

Terus kita pulang ampe malem, ujan juga ga si ituu.

Iya itu ujan ampe kita kehalang pohon di tengah jalan ditengah hutan juga wkwk.. kangen deh momen itu

Mau ga kepantai bareng lagi? Januari? Kalau kita masih ada chance yaa

Btw itu foto yang di post bundaku pertama kali, bukti bahwa kita di restui kala itu wkwkwk
""")
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("⬅ Kembali"):
            prev_page(); st.rerun()
        if st.button("➡ Lanjut"):
            next_page(); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        show_image_outline("2.jpg", 350)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- PAGE 4 : Jari Lentik Bintang ----------
elif st.session_state.page == 4:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Jari Lentik Bintang</h2>", unsafe_allow_html=True)
        st.write("""
Hii Hiii... Malika STAR maharani

Kamu pasti bingung ini foto apa?

Berkesan dimananya?

Kamu ga cuman cantik tapi cantik banget..

Apalagi cobam? Kamu ga inget pasti

Kamu ini minta foto kalau jari kamu cantik, kamu pamer ke aku.

Muka kamu yang centil itu wkwwkwk di tempat makan favorit kedua kita kalau pulang cekulah
""")
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("⬅ Kembali"):
            prev_page(); st.rerun()
        if st.button("➡ Lanjut"):
            next_page(); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        show_image_outline("3.jpg", 350)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- PAGE 5 : Garage ----------
elif st.session_state.page == 5:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Garage</h2>", unsafe_allow_html=True)
        st.write("""

Banyak banget cerita disini

Garage tempat makan kita.. selalu

Fotonya kenapa berkesan??

Karena kucing favorit kamu

Karena kamu favorit aku

Dan garage favorit kita

Makasih ya... atas semuanya..

I'm happy for that
""")
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("⬅ Kembali"):
            prev_page(); st.rerun()
        if st.button("➡ Lanjut"):
            next_page(); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        show_image_outline("4.jpg", 350)

# ---------- PAGE 6 : Kita Berdua ----------
elif st.session_state.page == 6:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Kita Berdua</h2>", unsafe_allow_html=True)
        st.write("""
Foto baju putih..

Aku minta kamu nemenin aku

Habis kalah basket.. iya ga si aku lupa wee

Kalau ga salah itu deh

Pokoknya disini kita happy..

Kita sama sama jarang ke kota

Kita sama sama motoran.. berdua

Yang ke Madiun nonton film deh

Yang putih kamu minta ramen

Di Solo kamu ga ngajak aku kemana gtu deh...

Balik ini mau ga kemana gtu wkwk??

Aku dah nabung buat ngajak kamu nonton/ cafe

Kamu susah bgt diajak ketemu..

Keknya emg gamau ya.. yaudah gapapa wkwkwk
""")
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("⬅ Kembali"):
            prev_page(); st.rerun()
        if st.button("➡ Lanjut"):
            next_page(); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        show_image_outline("5.jpg", 300)
        show_image_outline("6.jpg", 300)

# ---------- PAGE 7 : Maaf Malika ----------
elif st.session_state.page == 7:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2>Maaf Malika..</h2>", unsafe_allow_html=True)
        st.write("""
Aku mau minta maaf ke kamu dengan tulus. Maaf karena aku udah ninggalin kamu demi cewek lain, dan ngilang selama kurang lebih 4 bulan. Aku sadar banget keputusan aku waktu itu egois dan nyakitin kamu.

Aku tahu aku milih pergi tanpa mikirin perasaan kamu, padahal kamu gak salah apa-apa. Aku bikin kamu ngerasa gak cukup, ngerasa diganti, dan itu pasti sakit banget. Semua itu karena pilihan aku sendiri.

Aku gak punya alasan buat ngebela diri. Apa pun yang aku rasain waktu itu, caraku salah. Harusnya aku jujur dan bertanggung jawab, bukan malah ninggalin kamu dan bikin kamu nanya-nanya sendiri.

Aku nyesel karena udah nyia-nyiain kamu dan kepercayaan yang kamu kasih. Kamu gak pantas diperlakukan kayak gitu. Luka yang aku bikin itu sepenuhnya salah aku.

Aku gak nulis ini buat nyari pembenaran atau maksa kamu buat maafin aku. Aku cuma pengen kamu tahu kalau aku benar-benar minta maaf dari hati atas semua yang aku lakuin ke kamu.
""")
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("⬅ Kembali"):
            prev_page(); st.rerun()
        if st.button("➡ Lanjut"):
            next_page(); st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    with col2:
        show_image_outline("1.jpg", 350)

# ---------- PAGE 8 : Aku Minta Kesempatan ----------
elif st.session_state.page == 8:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2>Aku Minta Kesempatan..</h2>", unsafe_allow_html=True)
    st.write("""
Sekarang aku pengen bilang dengan jujur: aku pengen berubah. Aku pengen jadi orang yang lebih dewasa, lebih jujur, dan lebih bisa jaga perasaan orang yang aku sayang. Aku tahu omongan aja gak cukup, tapi niat aku buat berubah itu serius.

Kalau masih ada sedikit aja ruang di hati kamu, aku minta kesempatan buat benerin semuanya pelan-pelan. Bukan buat balik kayak dulu, tapi buat mulai lagi dari awal dengan versi aku yang lebih baik. Tapi kalau kamu belum bisa, atau bahkan gak mau sama sekali, aku bakal terima, karena itu konsekuensi dari pilihan aku sendiri.

Apa pun jawaban kamu nanti, aku cuma pengen kamu tahu kalau penyesalan aku atas semua luka yang aku bikin ke kamu itu benar-benar tulus.
""")
    st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
    if st.button("⬅ Kembali"):
        prev_page(); st.rerun()
    if st.button("➡ Lanjut"):
        next_page(); st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- PAGE 9 : Penutup ----------
elif st.session_state.page == 9:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>Minta Maaf dan Makasih ya 💖</h1>", unsafe_allow_html=True)
    st.write("""
Aku cuma pengen kamu tau, semua momen bareng kamu itu berharga banget.
Aku minta maaf atas semua salahku dan makasih banget udah jadi bagian hidupku.
Aku harap kita masih bisa saling menghargai dan menyayangi dalam cara baru.
-dion
""")
    st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
    if st.button("⬅ Kembali"):
        prev_page(); st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)
