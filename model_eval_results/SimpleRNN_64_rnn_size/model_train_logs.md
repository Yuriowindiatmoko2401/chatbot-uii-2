```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug

2021-05-15 00:49:29 DEBUG    rasa.skill  - Selected skills: 
2021-05-15 00:49:29 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py
2021-05-15 00:49:29 DEBUG    rasa.model  - Extracted model to '/tmp/tmpasy1renu'.

Training Core model...
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|█████████████████████████| 16/16 [00:00<00:00, 6378.56it/s, # trackers=1]
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|█████████████████████████| 16/16 [00:00<00:00, 542.24it/s, # trackers=14]
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████| 16/16 [00:00<00:00, 202.42it/s, # trackers=34]
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████| 16/16 [00:00<00:00, 195.45it/s, # trackers=31]
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-15 00:49:29 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-15 00:49:29 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-15 00:49:29 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|█████████████████████████████| 15/15 [00:00<00:00, 6580.33it/s, # actions=52]
2021-05-15 00:49:29 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 18231.53it/s, # examples=52]
2021-05-15 00:49:29 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-15 00:49:29 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|██████████████████████████| 515/515 [00:00<00:00, 2530.39it/s, # actions=596]
2021-05-15 00:49:30 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
simple_rnn (SimpleRNN)       (None, 64)                7168      
_________________________________________________________________
dense (Dense)                (None, 23)                1495      
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 8,663
Trainable params: 8,663
Non-trainable params: 0
_________________________________________________________________

2021-05-15 00:49:30 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-15 00:49:30 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}

Epoch 1/100
 - 0s - loss: 2.4241 - acc: 0.3977
Epoch 2/100
 - 0s - loss: 1.6885 - acc: 0.5503
Epoch 3/100
 - 0s - loss: 1.4350 - acc: 0.5822
Epoch 4/100
 - 0s - loss: 1.3131 - acc: 0.6258
Epoch 5/100
 - 0s - loss: 1.2044 - acc: 0.6829
Epoch 6/100
 - 0s - loss: 1.1266 - acc: 0.7131
Epoch 7/100
 - 0s - loss: 1.0173 - acc: 0.7685
Epoch 8/100
 - 0s - loss: 0.9472 - acc: 0.8138
Epoch 9/100
 - 0s - loss: 0.8736 - acc: 0.8272
Epoch 10/100
 - 0s - loss: 0.8105 - acc: 0.8423
Epoch 11/100
 - 0s - loss: 0.7485 - acc: 0.8691
Epoch 12/100
 - 0s - loss: 0.7298 - acc: 0.8674
Epoch 13/100
 - 0s - loss: 0.6386 - acc: 0.8977
Epoch 14/100
 - 0s - loss: 0.6134 - acc: 0.8926
Epoch 15/100
 - 0s - loss: 0.5762 - acc: 0.8893
Epoch 16/100
 - 0s - loss: 0.5084 - acc: 0.9010
Epoch 17/100
 - 0s - loss: 0.4956 - acc: 0.9044
Epoch 18/100
 - 0s - loss: 0.4452 - acc: 0.9144
Epoch 19/100
 - 0s - loss: 0.3935 - acc: 0.9262
Epoch 20/100
 - 0s - loss: 0.4204 - acc: 0.9044
Epoch 21/100
 - 0s - loss: 0.3787 - acc: 0.9195
Epoch 22/100
 - 0s - loss: 0.3617 - acc: 0.9044
Epoch 23/100
 - 0s - loss: 0.3482 - acc: 0.9195
Epoch 24/100
 - 0s - loss: 0.2957 - acc: 0.9295
Epoch 25/100
 - 0s - loss: 0.3380 - acc: 0.9077
Epoch 26/100
 - 0s - loss: 0.2493 - acc: 0.9430
Epoch 27/100
 - 0s - loss: 0.2515 - acc: 0.9312
Epoch 28/100
 - 0s - loss: 0.3018 - acc: 0.9195
Epoch 29/100
 - 0s - loss: 0.2403 - acc: 0.9262
Epoch 30/100
 - 0s - loss: 0.2643 - acc: 0.9128
Epoch 31/100
 - 0s - loss: 0.2434 - acc: 0.9195
Epoch 32/100
 - 0s - loss: 0.2544 - acc: 0.9111
Epoch 33/100
 - 0s - loss: 0.2628 - acc: 0.9060
Epoch 34/100
 - 0s - loss: 0.2714 - acc: 0.9060
Epoch 35/100
 - 0s - loss: 0.2126 - acc: 0.9279
Epoch 36/100
 - 0s - loss: 0.2574 - acc: 0.9077
Epoch 37/100
 - 0s - loss: 0.1998 - acc: 0.9262
Epoch 38/100
 - 0s - loss: 0.2096 - acc: 0.9362
Epoch 39/100
 - 0s - loss: 0.2210 - acc: 0.9228
Epoch 40/100
 - 0s - loss: 0.2334 - acc: 0.9178
Epoch 41/100
 - 0s - loss: 0.2007 - acc: 0.9362
Epoch 42/100
 - 0s - loss: 0.2032 - acc: 0.9228
Epoch 43/100
 - 0s - loss: 0.2078 - acc: 0.9329
Epoch 44/100
 - 0s - loss: 0.2044 - acc: 0.9228
Epoch 45/100
 - 0s - loss: 0.2015 - acc: 0.9262
Epoch 46/100
 - 0s - loss: 0.2384 - acc: 0.9211
Epoch 47/100
 - 0s - loss: 0.1892 - acc: 0.9312
Epoch 48/100
 - 0s - loss: 0.2083 - acc: 0.9245
Epoch 49/100
 - 0s - loss: 0.2216 - acc: 0.9211
Epoch 50/100
 - 0s - loss: 0.1550 - acc: 0.9396
Epoch 51/100
 - 0s - loss: 0.1752 - acc: 0.9396
Epoch 52/100
 - 0s - loss: 0.2044 - acc: 0.9195
Epoch 53/100
 - 0s - loss: 0.1999 - acc: 0.9245
Epoch 54/100
 - 0s - loss: 0.1902 - acc: 0.9295
Epoch 55/100
 - 0s - loss: 0.1965 - acc: 0.9295
Epoch 56/100
 - 0s - loss: 0.2217 - acc: 0.9161
Epoch 57/100
 - 0s - loss: 0.1985 - acc: 0.9262
Epoch 58/100
 - 0s - loss: 0.1766 - acc: 0.9312
Epoch 59/100
 - 0s - loss: 0.2468 - acc: 0.8993
Epoch 60/100
 - 0s - loss: 0.1795 - acc: 0.9295
Epoch 61/100
 - 0s - loss: 0.1994 - acc: 0.9195
Epoch 62/100
 - 0s - loss: 0.1776 - acc: 0.9312
Epoch 63/100
 - 0s - loss: 0.1578 - acc: 0.9379
Epoch 64/100
 - 0s - loss: 0.1856 - acc: 0.9312
Epoch 65/100
 - 0s - loss: 0.2113 - acc: 0.9195
Epoch 66/100
 - 0s - loss: 0.2097 - acc: 0.9279
Epoch 67/100
 - 0s - loss: 0.1886 - acc: 0.9279
Epoch 68/100
 - 0s - loss: 0.2356 - acc: 0.9094
Epoch 69/100
 - 0s - loss: 0.2274 - acc: 0.9094
Epoch 70/100
 - 0s - loss: 0.2145 - acc: 0.9262
Epoch 71/100
 - 0s - loss: 0.2024 - acc: 0.9178
Epoch 72/100
 - 0s - loss: 0.1667 - acc: 0.9329
Epoch 73/100
 - 0s - loss: 0.1966 - acc: 0.9195
Epoch 74/100
 - 0s - loss: 0.2031 - acc: 0.9195
Epoch 75/100
 - 0s - loss: 0.1882 - acc: 0.9262
Epoch 76/100
 - 0s - loss: 0.1805 - acc: 0.9295
Epoch 77/100
 - 0s - loss: 0.1454 - acc: 0.9413
Epoch 78/100
 - 0s - loss: 0.1727 - acc: 0.9362
Epoch 79/100
 - 0s - loss: 0.2066 - acc: 0.9178
Epoch 80/100
 - 0s - loss: 0.1746 - acc: 0.9379
Epoch 81/100
 - 0s - loss: 0.1649 - acc: 0.9413
Epoch 82/100
 - 0s - loss: 0.1567 - acc: 0.9396
Epoch 83/100
 - 0s - loss: 0.2004 - acc: 0.9195
Epoch 84/100
 - 0s - loss: 0.2471 - acc: 0.8977
Epoch 85/100
 - 0s - loss: 0.2175 - acc: 0.9211
Epoch 86/100
 - 0s - loss: 0.1621 - acc: 0.9379
Epoch 87/100
 - 0s - loss: 0.2137 - acc: 0.9144
Epoch 88/100
 - 0s - loss: 0.2131 - acc: 0.9144
Epoch 89/100
 - 0s - loss: 0.1709 - acc: 0.9329
Epoch 90/100
 - 0s - loss: 0.1728 - acc: 0.9279
Epoch 91/100
 - 0s - loss: 0.1801 - acc: 0.9279
Epoch 92/100
 - 0s - loss: 0.1862 - acc: 0.9312
Epoch 93/100
 - 0s - loss: 0.1850 - acc: 0.9245
Epoch 94/100
 - 0s - loss: 0.2093 - acc: 0.9195
Epoch 95/100
 - 0s - loss: 0.1875 - acc: 0.9228
Epoch 96/100
 - 0s - loss: 0.1975 - acc: 0.9312
Epoch 97/100
 - 0s - loss: 0.2380 - acc: 0.9111
Epoch 98/100
 - 0s - loss: 0.2027 - acc: 0.9279
Epoch 99/100
 - 0s - loss: 0.2100 - acc: 0.9128
Epoch 100/100
 - 0s - loss: 0.2270 - acc: 0.9178

2021-05-15 00:49:33 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-15 00:49:33 INFO     rasa.core.agent  - Model directory /tmp/tmpcn_ntf0m/core exists and contains old model files. All files will be overwritten.
2021-05-15 00:49:33 INFO     rasa.core.agent  - Persisted model to '/tmp/tmpcn_ntf0m/core'

Core model training completed.

Training NLU model...
/home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/sklearn/feature_extraction/image.py:167: DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
  dtype=np.int):
2021-05-15 00:49:33 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmp70flgtxb/0f091382d0d54faa8e430bc7039368b2_nlu.md is md
2021-05-15 00:49:33 INFO     rasa.nlu.training_data.training_data  - Training data stats: 
	- intent examples: 693 (16 distinct intents)
	- Found intents: 'intent_minta_jadwal_saja', 'mood_baik', 'mood_tidak_senang', 'intent_minta_daftar_nilai', 'intent_setuju', 'intent_confirm_kota', 'intent_confirm_nama_atau_nim', 'intent_berpisah', 'intent_menyapa', 'terima_kasih', 'intent_prediksi_cuaca', 'intent_salam', 'menantang_bot', 'intent_menolak', 'intent_jadwal_sholat', 'intent_minta_jadwal'
	- entity examples: 645 (4 distinct entities)
	- found entities: 'NIM', 'nama', 'kota', 'konsentrasi'

2021-05-15 00:49:33 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 00:49:33 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-15 00:49:34 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 00:49:34 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-15 00:49:34 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-15 00:49:34 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs

Epochs: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 300/300 [00:10<00:00, 31.20it/s, loss=0.014, acc=0.999]
2021-05-15 00:49:45 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.014, train accuracy=0.999
2021-05-15 00:49:45 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 00:49:45 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmpcn_ntf0m/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210515-004945.tar.gz'.




```