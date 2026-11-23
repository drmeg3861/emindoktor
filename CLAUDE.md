# emindoktor.com — proje notları (Claude için)

Sahibi: Dr. Öğr. Üyesi Muhammed Emin Göktepe — Trabzon Üniv. Tıp Fak. Aile Hekimliği AD.
Yanıt dili: Türkçe, kısa ve akıcı.

## Altyapı
| Parça | Nerede |
|---|---|
| Domain | emindoktor.com — METUnic'ten alındı (20.11.2026, yenileme 20.11.2027, ~₺1.020/yıl) |
| DNS | Cloudflare (drmeg38@gmail.com hesabı), nameserver: kevin / nadia.ns.cloudflare.com |
| Barındırma | Cloudflare Pages projesi `emindoktor` (ücretsiz), build yok, çıktı klasörü `/` |
| Kod | GitHub `drmeg3861/emindoktor` (public), `main` dalına push → ~10 sn'de yayında |
| Adresler | https://emindoktor.com · https://www.emindoktor.com · https://emindoktor.pages.dev |

Not: Chrome'daki GitHub hesabı `drmeg38` olabilir; Claude'un GitHub bağlantısı `drmeg3861` hesabında.
Cloudflare Pages GitHub uygulaması yalnızca bu depoya yetkili.
Öneri: kayıttan 60 gün sonra domain Cloudflare Registrar'a taşınabilir (yenileme ~10 $).

## Dosyalar
- `index.html` — ana sayfa (Klinik araçlar, Tıbbi hipnoz eğitimi, Sosyal medya)
- `ahurapor/index.html` — AHU Rapor uygulaması (tek dosya HTML + JS)
- `ahurapor/skrs.json` — ticari preparatlar, değişiklik listesi, Medula verisi
- `tools/` — SKRS/enteral veri üretim betikleri (Python)

## AHU Rapor — kurallar
- Kaynak: Uzm. Dr. Ensar Erdoğan, "Aile Hekimliği Uzmanlarının Rapor Çıkarabildiği İlaçlar" (rev. 17.03.2026, TAHUD). Açılış ekranında kaynak + geliştirici künyesi korunur.
- Arama: etken madde / ticari ad / tanı; harf harf daralır, tek sonuçta kart açılır, Enter tüm yazıyı seçer.
- Ticari adlar yalnızca resmi listeden (SKRS e-reçete listesi, TİTCK ruhsat listesi); A→Z sıralı, "ticari kaygı yok". Marka uydurma.
- Statin sınırları (AH uzmanı): Atorva ≤20, Rosuva ≤10, Pitava ≤4, Prava ≤20 mg.
- Medula doğrulaması: kullanıcı kendisi giriş yapar; şifre girilmez. Yalnız İlaç Bilgisi / İlaç Listeleri ekranları; hasta ekranları (KVKK) açılmaz. Yavaş ve parça parça sorgula.
- Medula farkları: Misoprostol yalnız Kadın Doğum; salbutamol / salbutamol+ipratropium / flutikazon NEBÜL formları AH ✕ (inhaler ✓).
- Tıbbi malzeme: strip, glukometre, iğne ucu (raporsuz), hasta bezi (yalnız 2./3. basamak), ostomi; sonda/yara/ortez AH ✕. Marka listeleri resmi değil, örnektir.
- Sağlık kurulu: yetişkin enteral beslenme (SUT 4.2.8.A) branş şartı yok → 3 AH uzmanı kurulu ✓ (malnütrisyon: 3 ay, ≤1200 kcal; kanser/tüple beslenen: 6 ay). Kıvam artırıcı, hepatik formül, çocuk enteral AH ✕.
- Mümessil formu: Google Form (Drive'da "AHU Rapor – Form Betiği"); gelen öneriler doğrudan uygulamaya yazılmaz, önce Medula'da doğrulanır.

## Tema (23.11.2026, v2 "klinik monitör")
- Palet (kullanıcı): beyaz, sarı `#f9ba27`, yeşil `#7abe4a`, açık mavi `#d6f1fb`/`#eef9fd`, turkuaz `#14b8b0` (süs; metin için `#0a7470`). Metin `#0d1b2a`, ikincil `#44566a`.
- Yazı: Unbounded (başlık) + Atkinson Hyperlegible Next (metin) + JetBrains Mono (etiket). Kaçınılacak: krem/serif "editoryal" görünüm, yuvarlak gölgeli kart, hap etiket, emoji ikon (kullanıcı v1'i "Claude yapmış belli" diye reddetti).
- Motifler: EKG kâğıdı ızgarası, animasyonlu EKG çizgisi, monitör çerçeveli portre, köşeli modül satırları; animasyonlar `prefers-reduced-motion`'da kapanır.
- Logo: `img/logo-kalp.webp`; favicon `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`. Portre: `img/portre-sari.webp`.
- Döküntülü rehberde hastalık başına renkler içerik kodudur, korunur.

## Güncelleme akışı
1. Yeni SKRS e-reçete listesi (xlsx) gelince `tools/build.py` ile `ahurapor/skrs.json` yeniden üret.
   - Girdiler (`rows.json`, `names.json`, `etkin.json`) varsayılan olarak `tools/in/` klasöründe aranır; başka klasör için `--girdi YOL`.
   - `python3 tools/build.py` → `tp.json` + `bar.json`; `python3 tools/ent_build.py` → `ent.json` (aynı klasöre yazılır).
   - Yollar betiğin konumuna göre çözülür, hangi klasörden çalıştırıldığı fark etmez.
2. `index.html` / `skrs.json` değiştir → commit → `git push origin main`.
3. https://emindoktor.com/ahurapor/ açıp kontrol et.

## Bekleyenler
- Sosyal medya (23.11.2026): YouTube @emindoktorcom, Instagram @emindoktorcom, Linktree linktr.ee/emindoktor — ana sayfa kartları + JSON-LD sameAs. Hipnoz video ve podcast listeleri sitede, YouTube bağlantılarıyla (20.11.2026 doğrulandı; YouTube Music değil).
- Mümessil formu linki hazır olunca QR + uygulama içi "Eksik preparat mı var?" bağlantısı.
- APK sürümü (aynı dosyalardan).
