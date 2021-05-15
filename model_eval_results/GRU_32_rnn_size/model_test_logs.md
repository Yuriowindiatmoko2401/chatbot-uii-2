```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa test 


Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 5675.65it/s, # trackers=1]

2021-05-16 01:05:25 INFO     rasa.core.test  - Evaluating 15 stories
Progress:
100%|█████████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 57.78it/s]

2021-05-16 01:05:25 INFO     rasa.core.test  - Finished collecting predictions.
2021-05-16 01:05:25 INFO     rasa.core.test  - Evaluation Results on CONVERSATION level:
2021-05-16 01:05:25 INFO     rasa.core.test  -  Correct:          15 / 15
2021-05-16 01:05:25 INFO     rasa.core.test  -  F1-Score:         1.000
2021-05-16 01:05:25 INFO     rasa.core.test  -  Precision:        1.000
2021-05-16 01:05:25 INFO     rasa.core.test  -  Accuracy:         1.000
2021-05-16 01:05:25 INFO     rasa.core.test  -  In-data fraction: 1
2021-05-16 01:05:25 INFO     rasa.core.test  - Evaluation Results on ACTION level:
2021-05-16 01:05:25 INFO     rasa.core.test  -  Correct:          72 / 72
2021-05-16 01:05:25 INFO     rasa.core.test  -  F1-Score:         1.000
2021-05-16 01:05:25 INFO     rasa.core.test  -  Precision:        1.000
2021-05-16 01:05:25 INFO     rasa.core.test  -  Accuracy:         1.000
2021-05-16 01:05:25 INFO     rasa.core.test  -  In-data fraction: 1
2021-05-16 01:05:25 INFO     rasa.core.test  -  Classification report: 

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

2021-05-16 01:05:25 INFO     rasa.nlu.test  - Confusion matrix, without normalization: 

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

2021-05-16 01:05:27 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmpzgmo6q8n/af712b7c2830473f9d27bc2994c6c089_nlu.md is md
2021-05-16 01:05:27 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

  - intent examples: 693 (16 distinct intents)
  - Found intents: 'terima_kasih', 'intent_minta_jadwal_saja', 'intent_confirm_nama_atau_nim', 'intent_setuju', 'menantang_bot', 'intent_minta_daftar_nilai', 'intent_minta_jadwal', 'intent_prediksi_cuaca', 'mood_baik', 'intent_salam', 'intent_jadwal_sholat', 'intent_confirm_kota', 'intent_berpisah', 'intent_menyapa', 'intent_menolak', 'mood_tidak_senang'

  - entity examples: 645 (4 distinct entities)
  - found entities: 'kota', 'konsentrasi', 'NIM', 'nama'

2021-05-16 01:05:27 INFO     rasa.nlu.test  - Running model for predictions:
100%|██████████████████████████████████████████████████████████████████████████████| 693/693 [00:00<00:00, 723.55it/s]

2021-05-16 01:05:28 INFO     rasa.nlu.test  - Intent evaluation results:
2021-05-16 01:05:28 INFO     rasa.nlu.test  - Intent Evaluation: Only considering those 693 examples that have a defined intent out of 693 examples
2021-05-16 01:05:28 INFO     rasa.nlu.test  - F1-Score:  0.9986045700331414
2021-05-16 01:05:28 INFO     rasa.nlu.test  - Precision: 0.9989177489177489
2021-05-16 01:05:28 INFO     rasa.nlu.test  - Accuracy:  0.9985569985569985
2021-05-16 01:05:28 INFO     rasa.nlu.test  - Classification report: 

                              precision    recall  f1-score   support

             intent_berpisah       1.00      1.00      1.00         3
         intent_confirm_kota       1.00      1.00      1.00       519
intent_confirm_nama_atau_nim       1.00      1.00      1.00         7
        intent_jadwal_sholat       1.00      1.00      1.00        12
              intent_menolak       1.00      1.00      1.00         3
              intent_menyapa       1.00      0.86      0.92         7
   intent_minta_daftar_nilai       1.00      1.00      1.00        11
         intent_minta_jadwal       1.00      1.00      1.00       100
    intent_minta_jadwal_saja       1.00      1.00      1.00         4
       intent_prediksi_cuaca       1.00      1.00      1.00         5
                intent_salam       0.75      1.00      0.86         3
               intent_setuju       1.00      1.00      1.00         6
               menantang_bot       1.00      1.00      1.00         4
                   mood_baik       1.00      1.00      1.00         4
           mood_tidak_senang       1.00      1.00      1.00         3
                terima_kasih       1.00      1.00      1.00         2

                   micro avg       1.00      1.00      1.00       693
                   macro avg       0.98      0.99      0.99       693
                weighted avg       1.00      1.00      1.00       693

2021-05-16 01:05:28 INFO     rasa.nlu.test  - Model prediction errors saved to errors.json.
2021-05-16 01:05:28 INFO     rasa.nlu.test  - Confusion matrix, without normalization: 

[[  3   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0 519   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   7   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0  12   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   3   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   6   0   0   0   0   1   0   0   0   0   0]
 [  0   0   0   0   0   0  11   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0 100   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   4   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   3   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   6   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   4   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   4   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   3   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2]]

2021-05-16 01:05:30 INFO     rasa.nlu.test  - Entity evaluation results:
2021-05-16 01:05:30 INFO     rasa.nlu.test  - Evaluation for entity extractor: CRFEntityExtractor 
2021-05-16 01:05:30 INFO     rasa.nlu.test  - F1-Score:  1.0
2021-05-16 01:05:30 INFO     rasa.nlu.test  - Precision: 1.0
2021-05-16 01:05:30 INFO     rasa.nlu.test  - Accuracy:  1.0
2021-05-16 01:05:30 INFO     rasa.nlu.test  - Classification report: 

              precision    recall  f1-score   support

         NIM       1.00      1.00      1.00         6
 konsentrasi       1.00      1.00      1.00       170
        kota       1.00      1.00      1.00       809
        nama       1.00      1.00      1.00        20
   no_entity       1.00      1.00      1.00       356

   micro avg       1.00      1.00      1.00      1361
   macro avg       1.00      1.00      1.00      1361
weighted avg       1.00      1.00      1.00      1361


```