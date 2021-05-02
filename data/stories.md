## story Hai
* intent_menyapa
  - utter_menyapa

## story salam
* intent_salam
  - utter_membalas_salam

## story perpisahan
* intent_berpisah
  - utter_berpisah

## story terima kasih
* terima_kasih
  - utter_terima_kasih

## alur senang
* intent_menyapa
  - utter_menyapa
* mood_baik
  - utter_senang

## alur sedih
* intent_menyapa
  - utter_menyapa
* mood_tidak_senang
  - utter_menyemangati
  - utter_apakah_membantu
* intent_setuju
  - utter_senang

## alur sedih  2
* intent_menyapa
  - utter_menyapa
* mood_tidak_senang
  - utter_menyemangati
  - utter_apakah_membantu
* intent_menolak
  - utter_berpisah

## mengucapkan perpisahan
* intent_berpisah
  - utter_berpisah

## menantang bot
* menantang_bot
  - utter_saya_bot

## story minta jadwal
* intent_menyapa
  - utter_menyapa
* intent_minta_jadwal
  - action_daftar_jadwal
* terima_kasih
  - utter_terima_kasih

## story minta jadwal 1
* intent_salam
  - utter_membalas_salam
* intent_minta_jadwal
  - action_daftar_jadwal
* terima_kasih
  - utter_terima_kasih

## story minta jadwal 2
* intent_menyapa
  - utter_menyapa
* intent_minta_jadwal_saja
  - utter_tanya_konsentrasi
* intent_minta_jadwal
  - action_daftar_jadwal
* terima_kasih
  - utter_terima_kasih

## story minta jadwal 3
* intent_salam
  - utter_membalas_salam
* intent_minta_jadwal_saja
  - utter_tanya_konsentrasi
* intent_minta_jadwal
  - action_daftar_jadwal
* terima_kasih
  - utter_terima_kasih

## story minta nilai
* intent_salam
  - utter_membalas_salam
* intent_minta_daftar_nilai
  - utter_tanya_nama_atau_nim
* intent_confirm_nama_atau_nim
  - action_daftar_nilai
* terima_kasih
  - utter_terima_kasih

## story minta jadwal sholat
* intent_jadwal_sholat
  - utter_tanya_kota
* intent_confirm_kota
  - action_jadwal_sholat

## story minta prediksi cuaca
* intent_prediksi_cuaca
  - utter_tanya_kota
* intent_confirm_kota
  - action_pred_cuaca

  