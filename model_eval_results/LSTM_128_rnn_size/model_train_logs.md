```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug               


2021-05-15 23:48:05 DEBUG    rasa.skill  - Selected skills: 
2021-05-15 23:48:05 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py

Training Core model...
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 5764.38it/s, # trackers=1]
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 545.39it/s, # trackers=14]

2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 227.16it/s, # trackers=34]

2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 221.72it/s, # trackers=31]

2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-15 23:48:05 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-15 23:48:05 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-15 23:48:05 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|██████| 15/15 [00:00<00:00, 6390.51it/s, # actions=52]

2021-05-15 23:48:05 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 23652.95it/s, # examples=52]
2021-05-15 23:48:05 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-15 23:48:05 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|███| 515/515 [00:00<00:00, 2778.20it/s, # actions=596]
2021-05-15 23:48:05 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
lstm (LSTM)                  (None, 128)               90112     
_________________________________________________________________
dense (Dense)                (None, 23)                2967      
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 93,079
Trainable params: 93,079
Non-trainable params: 0
_________________________________________________________________

2021-05-15 23:48:06 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-15 23:48:06 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}

Epoch 1/100
 - 0s - loss: 2.5846 - acc: 0.4480
Epoch 2/100
 - 0s - loss: 2.0766 - acc: 0.4832
Epoch 3/100
 - 0s - loss: 1.9438 - acc: 0.4832
Epoch 4/100
 - 0s - loss: 1.8407 - acc: 0.4832
Epoch 5/100
 - 0s - loss: 1.7325 - acc: 0.4866
Epoch 6/100
 - 0s - loss: 1.5997 - acc: 0.4899
Epoch 7/100
 - 0s - loss: 1.4206 - acc: 0.5201
Epoch 8/100
 - 0s - loss: 1.2715 - acc: 0.6275
Epoch 9/100
 - 0s - loss: 1.1281 - acc: 0.7030
Epoch 10/100
 - 0s - loss: 1.0395 - acc: 0.7366
Epoch 11/100
 - 0s - loss: 0.9188 - acc: 0.8054
Epoch 12/100
 - 0s - loss: 0.8291 - acc: 0.8523
Epoch 13/100
 - 0s - loss: 0.7550 - acc: 0.8775
Epoch 14/100
 - 0s - loss: 0.7050 - acc: 0.9077
Epoch 15/100
 - 0s - loss: 0.6366 - acc: 0.9094
Epoch 16/100
 - 0s - loss: 0.5869 - acc: 0.8993
Epoch 17/100
 - 0s - loss: 0.5352 - acc: 0.9195
Epoch 18/100
 - 0s - loss: 0.4619 - acc: 0.9413
Epoch 19/100
 - 0s - loss: 0.4328 - acc: 0.9312
Epoch 20/100
 - 0s - loss: 0.3738 - acc: 0.9497
Epoch 21/100
 - 0s - loss: 0.3782 - acc: 0.9279
Epoch 22/100
 - 0s - loss: 0.3087 - acc: 0.9581
Epoch 23/100
 - 0s - loss: 0.3016 - acc: 0.9430
Epoch 24/100
 - 0s - loss: 0.2825 - acc: 0.9480
Epoch 25/100
 - 0s - loss: 0.2254 - acc: 0.9631
Epoch 26/100
 - 0s - loss: 0.2529 - acc: 0.9463
Epoch 27/100
 - 0s - loss: 0.2444 - acc: 0.9547
Epoch 28/100
 - 0s - loss: 0.1976 - acc: 0.9614
Epoch 29/100
 - 0s - loss: 0.2086 - acc: 0.9530
Epoch 30/100
 - 0s - loss: 0.1795 - acc: 0.9631
Epoch 31/100
 - 0s - loss: 0.1816 - acc: 0.9581
Epoch 32/100
 - 0s - loss: 0.1609 - acc: 0.9614
Epoch 33/100
 - 0s - loss: 0.1605 - acc: 0.9648
Epoch 34/100
 - 0s - loss: 0.1712 - acc: 0.9631
Epoch 35/100
 - 0s - loss: 0.1448 - acc: 0.9799
Epoch 36/100
 - 0s - loss: 0.1521 - acc: 0.9664
Epoch 37/100
 - 0s - loss: 0.1392 - acc: 0.9698
Epoch 38/100
 - 0s - loss: 0.1216 - acc: 0.9849
Epoch 39/100
 - 0s - loss: 0.1406 - acc: 0.9748
Epoch 40/100
 - 0s - loss: 0.1227 - acc: 0.9782
Epoch 41/100
 - 0s - loss: 0.1152 - acc: 0.9815
Epoch 42/100
 - 0s - loss: 0.1173 - acc: 0.9799
Epoch 43/100
 - 0s - loss: 0.1008 - acc: 0.9799
Epoch 44/100
 - 0s - loss: 0.1013 - acc: 0.9832
Epoch 45/100
 - 0s - loss: 0.1148 - acc: 0.9799
Epoch 46/100
 - 0s - loss: 0.1017 - acc: 0.9815
Epoch 47/100
 - 0s - loss: 0.0966 - acc: 0.9832
Epoch 48/100
 - 0s - loss: 0.0863 - acc: 0.9832
Epoch 49/100
 - 0s - loss: 0.0998 - acc: 0.9832
Epoch 50/100
 - 0s - loss: 0.1010 - acc: 0.9799
Epoch 51/100
 - 0s - loss: 0.0863 - acc: 0.9866
Epoch 52/100
 - 0s - loss: 0.0820 - acc: 0.9799
Epoch 53/100
 - 0s - loss: 0.0720 - acc: 0.9883
Epoch 54/100
 - 0s - loss: 0.0683 - acc: 0.9849
Epoch 55/100
 - 0s - loss: 0.0646 - acc: 0.9899
Epoch 56/100
 - 0s - loss: 0.0584 - acc: 0.9916
Epoch 57/100
 - 0s - loss: 0.0707 - acc: 0.9899
Epoch 58/100
 - 0s - loss: 0.0703 - acc: 0.9866
Epoch 59/100
 - 0s - loss: 0.0588 - acc: 0.9916
Epoch 60/100
 - 0s - loss: 0.0502 - acc: 0.9933
Epoch 61/100
 - 0s - loss: 0.0565 - acc: 0.9899
Epoch 62/100
 - 0s - loss: 0.0398 - acc: 0.9950
Epoch 63/100
 - 0s - loss: 0.0473 - acc: 0.9933
Epoch 64/100
 - 0s - loss: 0.0366 - acc: 0.9916
Epoch 65/100
 - 0s - loss: 0.0437 - acc: 0.9916
Epoch 66/100
 - 0s - loss: 0.0631 - acc: 0.9849
Epoch 67/100
 - 0s - loss: 0.0495 - acc: 0.9966
Epoch 68/100
 - 0s - loss: 0.0557 - acc: 0.9899
Epoch 69/100
 - 0s - loss: 0.0432 - acc: 0.9933
Epoch 70/100
 - 0s - loss: 0.0616 - acc: 0.9899
Epoch 71/100
 - 0s - loss: 0.0460 - acc: 0.9933
Epoch 72/100
 - 0s - loss: 0.0420 - acc: 0.9916
Epoch 73/100
 - 0s - loss: 0.0508 - acc: 0.9933
Epoch 74/100
 - 0s - loss: 0.0497 - acc: 0.9899
Epoch 75/100
 - 0s - loss: 0.0391 - acc: 0.9966
Epoch 76/100
 - 0s - loss: 0.0576 - acc: 0.9883
Epoch 77/100
 - 0s - loss: 0.0393 - acc: 0.9933
Epoch 78/100
 - 0s - loss: 0.0322 - acc: 0.9950
Epoch 79/100
 - 0s - loss: 0.0379 - acc: 0.9916
Epoch 80/100
 - 0s - loss: 0.0281 - acc: 0.9950
Epoch 81/100
 - 0s - loss: 0.0302 - acc: 0.9933
Epoch 82/100
 - 0s - loss: 0.0359 - acc: 0.9933
Epoch 83/100
 - 0s - loss: 0.0301 - acc: 0.9950
Epoch 84/100
 - 0s - loss: 0.0219 - acc: 0.9966
Epoch 85/100
 - 0s - loss: 0.0360 - acc: 0.9950
Epoch 86/100
 - 0s - loss: 0.0265 - acc: 0.9966
Epoch 87/100
 - 0s - loss: 0.0300 - acc: 0.9916
Epoch 88/100
 - 0s - loss: 0.0285 - acc: 0.9950
Epoch 89/100
 - 0s - loss: 0.0271 - acc: 0.9916
Epoch 90/100
 - 0s - loss: 0.0388 - acc: 0.9899
Epoch 91/100
 - 0s - loss: 0.0276 - acc: 0.9966
Epoch 92/100
 - 0s - loss: 0.0287 - acc: 0.9950
Epoch 93/100
 - 0s - loss: 0.0337 - acc: 0.9933
Epoch 94/100
 - 0s - loss: 0.0407 - acc: 0.9883
Epoch 95/100
 - 0s - loss: 0.0283 - acc: 0.9966
Epoch 96/100
 - 0s - loss: 0.0191 - acc: 0.9966
Epoch 97/100
 - 0s - loss: 0.0293 - acc: 0.9933
Epoch 98/100
 - 0s - loss: 0.0375 - acc: 0.9899
Epoch 99/100
 - 0s - loss: 0.0214 - acc: 0.9966
Epoch 100/100
 - 0s - loss: 0.0303 - acc: 0.9933

2021-05-15 23:48:15 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-15 23:48:15 INFO     rasa.core.agent  - Persisted model to '/tmp/tmpdl_9uy00/core'
Core model training completed.

Training NLU model...

2021-05-15 23:48:15 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmpg33d_fs9/87138cb813414e4db249b153ed2a9c45_nlu.md is md
2021-05-15 23:48:15 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'intent_menolak', 'intent_berpisah', 'intent_confirm_kota', 'intent_confirm_nama_atau_nim', 'terima_kasih', 'intent_minta_jadwal_saja', 'intent_salam', 'mood_baik', 'intent_minta_daftar_nilai', 'intent_minta_jadwal', 'mood_tidak_senang', 'menantang_bot', 'intent_jadwal_sholat', 'intent_menyapa', 'intent_prediksi_cuaca', 'intent_setuju'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'kota', 'NIM', 'nama', 'konsentrasi'

2021-05-15 23:48:15 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 23:48:15 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-15 23:48:15 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-15 23:48:16 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|███████████████████████████████████| 300/300 [00:10<00:00, 28.40it/s, loss=0.013, acc=0.999]
2021-05-15 23:48:26 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.013, train accuracy=0.999
2021-05-15 23:48:26 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 23:48:26 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmpdl_9uy00/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210515-234826.tar.gz'.


```