
## GRU_128_rnn_size

```bash
2021-05-16 03:10:14 INFO     rasa.core.test  - Evaluation Results on CONVERSATION level:
2021-05-16 03:10:14 INFO     rasa.core.test  -  Correct:          15 / 15
2021-05-16 03:10:14 INFO     rasa.core.test  -  F1-Score:         1.000
2021-05-16 03:10:14 INFO     rasa.core.test  -  Precision:        1.000
2021-05-16 03:10:14 INFO     rasa.core.test  -  Accuracy:         1.000
2021-05-16 03:10:14 INFO     rasa.core.test  -  In-data fraction: 1
2021-05-16 03:10:14 INFO     rasa.core.test  - Evaluation Results on ACTION level:
2021-05-16 03:10:14 INFO     rasa.core.test  -  Correct:          72 / 72
2021-05-16 03:10:14 INFO     rasa.core.test  -  F1-Score:         1.000
2021-05-16 03:10:14 INFO     rasa.core.test  -  Precision:        1.000
2021-05-16 03:10:14 INFO     rasa.core.test  -  Accuracy:         1.000
2021-05-16 03:10:14 INFO     rasa.core.test  -  In-data fraction: 1

                           precision    recall  f1-score   support

     action_daftar_jadwal       1.00      1.00      1.00         4
      action_daftar_nilai       1.00      1.00      1.00         1
     action_jadwal_sholat       1.00      1.00      1.00         1
            action_listen       1.00      1.00      1.00        35
        action_pred_cuaca       1.00      1.00      1.00         1
    utter_apakah_membantu       1.00      1.00      1.00         2
           utter_berpisah       1.00      1.00      1.00         2
     utter_membalas_salam       1.00      1.00      1.00         4
            utter_menyapa       1.00      1.00      1.00         6
       utter_menyemangati       1.00      1.00      1.00         2
           utter_saya_bot       1.00      1.00      1.00         1
             utter_senang       1.00      1.00      1.00         2
  utter_tanya_konsentrasi       1.00      1.00      1.00         2
         utter_tanya_kota       1.00      1.00      1.00         2
utter_tanya_nama_atau_nim       1.00      1.00      1.00         1
       utter_terima_kasih       1.00      1.00      1.00         6

                micro avg       1.00      1.00      1.00        72
                macro avg       1.00      1.00      1.00        72
             weighted avg       1.00      1.00      1.00        72

[[ 4  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0 35  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  2  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  2  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  4  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  6  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  2  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  2  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  2  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  2  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  6]]


