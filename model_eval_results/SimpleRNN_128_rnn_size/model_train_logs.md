```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug

2021-05-15 01:25:58 DEBUG    rasa.skill  - Selected skills: 
2021-05-15 01:25:58 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py
2021-05-15 01:25:59 DEBUG    rasa.model  - Extracted model to '/tmp/tmppkn4svd7'.

Training Core model...
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|████████████| 16/16 [00:00<00:00, 5048.82it/s, # trackers=1]

2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|████████████| 16/16 [00:00<00:00, 555.84it/s, # trackers=14]

2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|████████████| 16/16 [00:00<00:00, 223.95it/s, # trackers=34]
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|████████████| 16/16 [00:00<00:00, 217.44it/s, # trackers=31]
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-15 01:25:59 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-15 01:25:59 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-15 01:25:59 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|████████████████| 15/15 [00:00<00:00, 7133.98it/s, # actions=52]

2021-05-15 01:25:59 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 20839.27it/s, # examples=52]
2021-05-15 01:25:59 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-15 01:25:59 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|█████████████| 515/515 [00:00<00:00, 2600.59it/s, # actions=596]
2021-05-15 01:25:59 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
simple_rnn (SimpleRNN)       (None, 128)               22528     
_________________________________________________________________
dense (Dense)                (None, 23)                2967      
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 25,495
Trainable params: 25,495
Non-trainable params: 0
_________________________________________________________________

2021-05-15 01:25:59 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-15 01:25:59 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}

Epoch 1/100
 - 0s - loss: 1.9932 - acc: 0.4597
Epoch 2/100
 - 0s - loss: 1.4089 - acc: 0.5604
Epoch 3/100
 - 0s - loss: 1.2213 - acc: 0.6309
Epoch 4/100
 - 0s - loss: 1.0684 - acc: 0.7047
Epoch 5/100
 - 0s - loss: 0.9548 - acc: 0.7651
Epoch 6/100
 - 0s - loss: 0.8862 - acc: 0.8154
Epoch 7/100
 - 0s - loss: 0.7674 - acc: 0.8507
Epoch 8/100
 - 0s - loss: 0.6871 - acc: 0.8708
Epoch 9/100
 - 0s - loss: 0.5966 - acc: 0.9044
Epoch 10/100
 - 0s - loss: 0.5486 - acc: 0.9144
Epoch 11/100
 - 0s - loss: 0.4872 - acc: 0.9178
Epoch 12/100
 - 0s - loss: 0.4346 - acc: 0.9161
Epoch 13/100
 - 0s - loss: 0.3855 - acc: 0.9279
Epoch 14/100
 - 0s - loss: 0.4141 - acc: 0.8960
Epoch 15/100
 - 0s - loss: 0.3745 - acc: 0.8977
Epoch 16/100
 - 0s - loss: 0.3269 - acc: 0.9128
Epoch 17/100
 - 0s - loss: 0.3201 - acc: 0.9094
Epoch 18/100
 - 0s - loss: 0.3091 - acc: 0.9128
Epoch 19/100
 - 0s - loss: 0.3027 - acc: 0.9094
Epoch 20/100
 - 0s - loss: 0.2572 - acc: 0.9295
Epoch 21/100
 - 0s - loss: 0.2737 - acc: 0.9094
Epoch 22/100
 - 0s - loss: 0.2320 - acc: 0.9329
Epoch 23/100
 - 0s - loss: 0.2370 - acc: 0.9295
Epoch 24/100
 - 0s - loss: 0.2987 - acc: 0.8943
Epoch 25/100
 - 0s - loss: 0.2274 - acc: 0.9279
Epoch 26/100
 - 0s - loss: 0.2425 - acc: 0.9195
Epoch 27/100
 - 0s - loss: 0.2301 - acc: 0.9228
Epoch 28/100
 - 0s - loss: 0.2584 - acc: 0.9094
Epoch 29/100
 - 0s - loss: 0.2251 - acc: 0.9195
Epoch 30/100
 - 0s - loss: 0.2257 - acc: 0.9245
Epoch 31/100
 - 0s - loss: 0.2209 - acc: 0.9228
Epoch 32/100
 - 0s - loss: 0.2249 - acc: 0.9262
Epoch 33/100
 - 0s - loss: 0.2413 - acc: 0.9128
Epoch 34/100
 - 0s - loss: 0.2131 - acc: 0.9346
Epoch 35/100
 - 0s - loss: 0.1996 - acc: 0.9295
Epoch 36/100
 - 0s - loss: 0.2207 - acc: 0.9211
Epoch 37/100
 - 0s - loss: 0.2127 - acc: 0.9245
Epoch 38/100
 - 0s - loss: 0.2055 - acc: 0.9295
Epoch 39/100
 - 0s - loss: 0.2008 - acc: 0.9262
Epoch 40/100
 - 0s - loss: 0.2459 - acc: 0.8993
Epoch 41/100
 - 0s - loss: 0.1827 - acc: 0.9362
Epoch 42/100
 - 0s - loss: 0.2292 - acc: 0.9161
Epoch 43/100
 - 0s - loss: 0.1824 - acc: 0.9362
Epoch 44/100
 - 0s - loss: 0.1964 - acc: 0.9295
Epoch 45/100
 - 0s - loss: 0.1864 - acc: 0.9329
Epoch 46/100
 - 0s - loss: 0.1829 - acc: 0.9262
Epoch 47/100
 - 0s - loss: 0.2051 - acc: 0.9228
Epoch 48/100
 - 0s - loss: 0.1794 - acc: 0.9346
Epoch 49/100
 - 0s - loss: 0.1798 - acc: 0.9295
Epoch 50/100
 - 0s - loss: 0.1741 - acc: 0.9396
Epoch 51/100
 - 0s - loss: 0.1794 - acc: 0.9346
Epoch 52/100
 - 0s - loss: 0.2150 - acc: 0.9195
Epoch 53/100
 - 0s - loss: 0.2241 - acc: 0.9161
Epoch 54/100
 - 0s - loss: 0.2245 - acc: 0.9195
Epoch 55/100
 - 0s - loss: 0.1919 - acc: 0.9362
Epoch 56/100
 - 0s - loss: 0.1942 - acc: 0.9262
Epoch 57/100
 - 0s - loss: 0.1622 - acc: 0.9413
Epoch 58/100
 - 0s - loss: 0.1845 - acc: 0.9329
Epoch 59/100
 - 0s - loss: 0.2039 - acc: 0.9228
Epoch 60/100
 - 0s - loss: 0.1691 - acc: 0.9379
Epoch 61/100
 - 0s - loss: 0.2170 - acc: 0.9178
Epoch 62/100
 - 0s - loss: 0.2069 - acc: 0.9228
Epoch 63/100
 - 0s - loss: 0.2051 - acc: 0.9144
Epoch 64/100
 - 0s - loss: 0.1795 - acc: 0.9362
Epoch 65/100
 - 0s - loss: 0.1884 - acc: 0.9295
Epoch 66/100
 - 0s - loss: 0.1748 - acc: 0.9312
Epoch 67/100
 - 0s - loss: 0.2307 - acc: 0.9144
Epoch 68/100
 - 0s - loss: 0.1814 - acc: 0.9346
Epoch 69/100
 - 0s - loss: 0.2311 - acc: 0.9178
Epoch 70/100
 - 0s - loss: 0.2058 - acc: 0.9195
Epoch 71/100
 - 0s - loss: 0.1837 - acc: 0.9279
Epoch 72/100
 - 0s - loss: 0.2119 - acc: 0.9228
Epoch 73/100
 - 0s - loss: 0.2215 - acc: 0.9144
Epoch 74/100
 - 0s - loss: 0.1768 - acc: 0.9396
Epoch 75/100
 - 0s - loss: 0.2180 - acc: 0.9161
Epoch 76/100
 - 0s - loss: 0.2199 - acc: 0.9211
Epoch 77/100
 - 0s - loss: 0.1631 - acc: 0.9413
Epoch 78/100
 - 0s - loss: 0.1480 - acc: 0.9547
Epoch 79/100
 - 0s - loss: 0.2060 - acc: 0.9228
Epoch 80/100
 - 0s - loss: 0.2245 - acc: 0.9144
Epoch 81/100
 - 0s - loss: 0.1700 - acc: 0.9295
Epoch 82/100
 - 0s - loss: 0.2095 - acc: 0.9228
Epoch 83/100
 - 0s - loss: 0.2196 - acc: 0.9178
Epoch 84/100
 - 0s - loss: 0.1749 - acc: 0.9346
Epoch 85/100
 - 0s - loss: 0.1692 - acc: 0.9329
Epoch 86/100
 - 0s - loss: 0.1985 - acc: 0.9195
Epoch 87/100
 - 0s - loss: 0.2373 - acc: 0.9044
Epoch 88/100
 - 0s - loss: 0.1969 - acc: 0.9195
Epoch 89/100
 - 0s - loss: 0.1714 - acc: 0.9396
Epoch 90/100
 - 0s - loss: 0.1838 - acc: 0.9379
Epoch 91/100
 - 0s - loss: 0.1781 - acc: 0.9362
Epoch 92/100
 - 0s - loss: 0.1934 - acc: 0.9279
Epoch 93/100
 - 0s - loss: 0.1464 - acc: 0.9446
Epoch 94/100
 - 0s - loss: 0.2362 - acc: 0.9161
Epoch 95/100
 - 0s - loss: 0.1711 - acc: 0.9346
Epoch 96/100
 - 0s - loss: 0.1773 - acc: 0.9262
Epoch 97/100
 - 0s - loss: 0.1891 - acc: 0.9312
Epoch 98/100
 - 0s - loss: 0.2216 - acc: 0.9128
Epoch 99/100
 - 0s - loss: 0.1869 - acc: 0.9279
Epoch 100/100
 - 0s - loss: 0.2184 - acc: 0.9211
2021-05-15 01:26:03 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-15 01:26:03 INFO     rasa.core.agent  - Model directory /tmp/tmpko91k_3r/core exists and contains old model files. All files will be overwritten.
2021-05-15 01:26:03 INFO     rasa.core.agent  - Persisted model to '/tmp/tmpko91k_3r/core'
Core model training completed.

Training NLU model...

2021-05-15 01:26:03 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmpfhuarv_b/a650bfa91af249379621bda04d69690b_nlu.md is md
2021-05-15 01:26:03 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'mood_baik', 'menantang_bot', 'mood_tidak_senang', 'intent_prediksi_cuaca', 'intent_jadwal_sholat', 'intent_minta_daftar_nilai', 'terima_kasih', 'intent_minta_jadwal_saja', 'intent_confirm_kota', 'intent_berpisah', 'intent_minta_jadwal', 'intent_menolak', 'intent_menyapa', 'intent_salam', 'intent_setuju', 'intent_confirm_nama_atau_nim'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'NIM', 'nama', 'konsentrasi', 'kota'

2021-05-15 01:26:03 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 01:26:03 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-15 01:26:03 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-15 01:26:04 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|███████████████████| 300/300 [00:10<00:00, 28.08it/s, loss=0.016, acc=0.999]

2021-05-15 01:26:14 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.016, train accuracy=0.999
2021-05-15 01:26:14 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 01:26:15 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmpko91k_3r/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210515-012615.tar.gz'.

```