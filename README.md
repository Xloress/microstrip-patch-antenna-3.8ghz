# Realization, Fabrication, and Measurement of Inset-Fed Microstrip Single Patch Antenna on FR-4 PCB

Dokumentasi lengkap perancangan, simulasi gelombang mikro menggunakan **CST Studio Suite**, proses fabrikasi kimiawi (*etching* PCB), serta pengukuran karakteristik parameter frekuensi radio (*RF*) antena mikrostrip single patch menggunakan **Keysight FieldFox Microwave Analyzer**.

Proyek praktikum ini dikerjakan pada mata kuliah *Antena dan Propagasi*, Program Studi D4 Teknik Telekomunikasi, Jurusan Teknik Elektro, **Politeknik Negeri Bandung (POLBAN)**.

---

## 📌 Ringkasan Proyek

* **Mata Kuliah:** Antena dan Propagasi
* **Dosen Pengampu:** Asep Barnas Simanjuntak, BSEE., M.T., Hanny Madiawati, S.ST., M.T., & Ir. Enceng Sulaeman, MT
* **Tim Praktikan (Kelompok 2):**
  1. Arya Haikal Yusuf (241344005)
  2. **Azlan Abdurahman (241344006)**
  3. Azzahra Reiva Alqudsy (241344007)
* **Periode Pengerjaan:** 12 Mei 2026 – 9 Juni 2026
* **Alat Ukur RF:** Keysight FieldFox Microwave Analyzer & Anritsu Site Master

---

## ⚙️ Spesifikasi & Hasil Pengukuran RF

* **Material Substrat:** Epoxy FR-4 Double Layer ($\varepsilon_r = 4.4$, ketebalan $h = 1.6\text{ mm}$, $\tan\delta = 0.02$)
* **Metode Pencatuan:** *Inset Feed* (pencocokan impedansi $50\ \Omega$)
* **Karakteristik Hasil Pengukuran VNA:**
  * **Frekuensi Resonansi Aktual ($f_0$):** $3,692\text{ GHz}$
  * **Nilai Return Loss ($S_{11}$):** **$-16,98\text{ dB}$** *(memenuhi standar industri telekomunikasi $\le -10\text{ dB}$)*
  * **Frekuensi Batas Bawah ($M_1$):** $3,614\text{ GHz}$
  * **Frekuensi Batas Atas ($M_3$):** $3,774\text{ GHz}$
  * **Bandwidth Kerja ($BW$):** **$160\text{ MHz}$**

---

## 🔬 Alur Fabrikasi Mandiri

1. **Transfer Pola:** Desain hasil optimasi CST dicetak ke stiker transfer dan ditempel pada PCB tembaga.
2. **Penyetrikaan:** Penyetrikaan panas untuk melekatkan pola pelindung tembaga.
3. **Etching:** Perendaman kimia dalam larutan *Ferric Chloride* ($FeCl_3$) untuk melarutkan tembaga berlebih.
4. **Pembersihan & Pemasangan Konektor:** Pelarutan sisa toner dengan thinner, pengikiran tepi, serta penyolderan konektor SMA $50\ \Omega$.
5. **Analisis VNA:** Pengukuran nilai $S_{11}$, pergeseran frekuensi resonansi, dan analisis faktor toleransi dimensi fisik.

---

## 📂 Struktur Repositori

```text
├── docs/
│   └── Laporan_Praktikum_Realisasi_Antena_Mikrostrip.docx  # Naskah laporan resmi praktikum
├── calculations/
│   └── antenna_design_calc.py                             # Skrip rumus analitis dimensi patch
└── README.md
```
