```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug

2021-05-16 01:15:10 DEBUG    rasa.skill  - Selected skills: 
2021-05-16 01:15:10 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py
2021-05-16 01:15:10 DEBUG    rasa.model  - Extracted model to '/tmp/tmp_qwvwocn'.

Training Core model...
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 5037.07it/s, # trackers=1]
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 582.27it/s, # trackers=14]
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 219.79it/s, # trackers=34]
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 214.06it/s, # trackers=31]
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-16 01:15:10 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-16 01:15:10 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-16 01:15:10 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|█████████████████████████████████████████████| 15/15 [00:00<00:00, 7064.29it/s, # actions=52]
2021-05-16 01:15:10 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 19824.01it/s, # examples=52]
2021-05-16 01:15:10 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-16 01:15:10 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|██████████████████████████████████████████| 515/515 [00:00<00:00, 2616.75it/s, # actions=596]
2021-05-16 01:15:10 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
gru (GRU)                    (None, 64)                21504     
_________________________________________________________________
dense (Dense)                (None, 23)                1495      
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 22,999
Trainable params: 22,999
Non-trainable params: 0
_________________________________________________________________

2021-05-16 01:15:11 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-16 01:15:11 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}
Epoch 1/100
 - 0s - loss: 2.8244 - acc: 0.4161
Epoch 2/100
 - 0s - loss: 2.2150 - acc: 0.4832
Epoch 3/100
 - 0s - loss: 2.0209 - acc: 0.4832
Epoch 4/100
 - 0s - loss: 1.8646 - acc: 0.4849
Epoch 5/100
 - 0s - loss: 1.6980 - acc: 0.4883
Epoch 6/100
 - 0s - loss: 1.4479 - acc: 0.5134
Epoch 7/100
 - 0s - loss: 1.2564 - acc: 0.6997
Epoch 8/100
 - 0s - loss: 1.1745 - acc: 0.7332
Epoch 9/100
 - 0s - loss: 1.0475 - acc: 0.7601
Epoch 10/100
 - 0s - loss: 0.9946 - acc: 0.8037
Epoch 11/100
 - 0s - loss: 0.8841 - acc: 0.8339
Epoch 12/100
 - 0s - loss: 0.8236 - acc: 0.8423
Epoch 13/100
 - 0s - loss: 0.7114 - acc: 0.8993
Epoch 14/100
 - 0s - loss: 0.6474 - acc: 0.8960
Epoch 15/100
 - 0s - loss: 0.5533 - acc: 0.9195
Epoch 16/100
 - 0s - loss: 0.5023 - acc: 0.9144
Epoch 17/100
 - 0s - loss: 0.4678 - acc: 0.9161
Epoch 18/100
 - 0s - loss: 0.4399 - acc: 0.9211
Epoch 19/100
 - 0s - loss: 0.4333 - acc: 0.8993
Epoch 20/100
 - 0s - loss: 0.3619 - acc: 0.9211
Epoch 21/100
 - 0s - loss: 0.3305 - acc: 0.9295
Epoch 22/100
 - 0s - loss: 0.3427 - acc: 0.9195
Epoch 23/100
 - 0s - loss: 0.2504 - acc: 0.9513
Epoch 24/100
 - 0s - loss: 0.2919 - acc: 0.9295
Epoch 25/100
 - 0s - loss: 0.2682 - acc: 0.9312
Epoch 26/100
 - 0s - loss: 0.2725 - acc: 0.9262
Epoch 27/100
 - 0s - loss: 0.2250 - acc: 0.9463
Epoch 28/100
 - 0s - loss: 0.2359 - acc: 0.9413
Epoch 29/100
 - 0s - loss: 0.2355 - acc: 0.9379
Epoch 30/100
 - 0s - loss: 0.2039 - acc: 0.9480
Epoch 31/100
 - 0s - loss: 0.2077 - acc: 0.9413
Epoch 32/100
 - 0s - loss: 0.1851 - acc: 0.9513
Epoch 33/100
 - 0s - loss: 0.1749 - acc: 0.9513
Epoch 34/100
 - 0s - loss: 0.2005 - acc: 0.9497
Epoch 35/100
 - 0s - loss: 0.1805 - acc: 0.9564
Epoch 36/100
 - 0s - loss: 0.1867 - acc: 0.9530
Epoch 37/100
 - 0s - loss: 0.1737 - acc: 0.9530
Epoch 38/100
 - 0s - loss: 0.1528 - acc: 0.9597
Epoch 39/100
 - 0s - loss: 0.1553 - acc: 0.9614
Epoch 40/100
 - 0s - loss: 0.1556 - acc: 0.9664
Epoch 41/100
 - 0s - loss: 0.1330 - acc: 0.9765
Epoch 42/100
 - 0s - loss: 0.1144 - acc: 0.9681
Epoch 43/100
 - 0s - loss: 0.1338 - acc: 0.9664
Epoch 44/100
 - 0s - loss: 0.1286 - acc: 0.9681
Epoch 45/100
 - 0s - loss: 0.1164 - acc: 0.9765
Epoch 46/100
 - 0s - loss: 0.1566 - acc: 0.9648
Epoch 47/100
 - 0s - loss: 0.1275 - acc: 0.9732
Epoch 48/100
 - 0s - loss: 0.1270 - acc: 0.9765
Epoch 49/100
 - 0s - loss: 0.1041 - acc: 0.9799
Epoch 50/100
 - 0s - loss: 0.0962 - acc: 0.9815
Epoch 51/100
 - 0s - loss: 0.1201 - acc: 0.9748
Epoch 52/100
 - 0s - loss: 0.1125 - acc: 0.9799
Epoch 53/100
 - 0s - loss: 0.1005 - acc: 0.9748
Epoch 54/100
 - 0s - loss: 0.1292 - acc: 0.9715
Epoch 55/100
 - 0s - loss: 0.1112 - acc: 0.9765
Epoch 56/100
 - 0s - loss: 0.1058 - acc: 0.9815
Epoch 57/100
 - 0s - loss: 0.0907 - acc: 0.9832
Epoch 58/100
 - 0s - loss: 0.0874 - acc: 0.9765
Epoch 59/100
 - 0s - loss: 0.0910 - acc: 0.9815
Epoch 60/100
 - 0s - loss: 0.0918 - acc: 0.9765
Epoch 61/100
 - 0s - loss: 0.0928 - acc: 0.9782
Epoch 62/100
 - 0s - loss: 0.0917 - acc: 0.9782
Epoch 63/100
 - 0s - loss: 0.0873 - acc: 0.9849
Epoch 64/100
 - 0s - loss: 0.0770 - acc: 0.9732
Epoch 65/100
 - 0s - loss: 0.0723 - acc: 0.9815
Epoch 66/100
 - 0s - loss: 0.0634 - acc: 0.9866
Epoch 67/100
 - 0s - loss: 0.0853 - acc: 0.9815
Epoch 68/100
 - 0s - loss: 0.0719 - acc: 0.9799
Epoch 69/100
 - 0s - loss: 0.0632 - acc: 0.9883
Epoch 70/100
 - 0s - loss: 0.0667 - acc: 0.9849
Epoch 71/100
 - 0s - loss: 0.0572 - acc: 0.9832
Epoch 72/100
 - 0s - loss: 0.0689 - acc: 0.9815
Epoch 73/100
 - 0s - loss: 0.0538 - acc: 0.9849
Epoch 74/100
 - 0s - loss: 0.0414 - acc: 0.9916
Epoch 75/100
 - 0s - loss: 0.0811 - acc: 0.9782
Epoch 76/100
 - 0s - loss: 0.0515 - acc: 0.9849
Epoch 77/100
 - 0s - loss: 0.0594 - acc: 0.9883
Epoch 78/100
 - 0s - loss: 0.0632 - acc: 0.9765
Epoch 79/100
 - 0s - loss: 0.0558 - acc: 0.9849
Epoch 80/100
 - 0s - loss: 0.0673 - acc: 0.9799
Epoch 81/100
 - 0s - loss: 0.0646 - acc: 0.9765
Epoch 82/100
 - 0s - loss: 0.0728 - acc: 0.9765
Epoch 83/100
 - 0s - loss: 0.0558 - acc: 0.9832
Epoch 84/100
 - 0s - loss: 0.0367 - acc: 0.9916
Epoch 85/100
 - 0s - loss: 0.0722 - acc: 0.9815
Epoch 86/100
 - 0s - loss: 0.0593 - acc: 0.9832
Epoch 87/100
 - 0s - loss: 0.0533 - acc: 0.9832
Epoch 88/100
 - 0s - loss: 0.0456 - acc: 0.9866
Epoch 89/100
 - 0s - loss: 0.0560 - acc: 0.9799
Epoch 90/100
 - 0s - loss: 0.0548 - acc: 0.9832
Epoch 91/100
 - 0s - loss: 0.0523 - acc: 0.9832
Epoch 92/100
 - 0s - loss: 0.0372 - acc: 0.9916
Epoch 93/100
 - 0s - loss: 0.0505 - acc: 0.9899
Epoch 94/100
 - 0s - loss: 0.0538 - acc: 0.9849
Epoch 95/100
 - 0s - loss: 0.0549 - acc: 0.9849
Epoch 96/100
 - 0s - loss: 0.0531 - acc: 0.9815
Epoch 97/100
 - 0s - loss: 0.0795 - acc: 0.9732
Epoch 98/100
 - 0s - loss: 0.0380 - acc: 0.9899
Epoch 99/100
 - 0s - loss: 0.0290 - acc: 0.9933
Epoch 100/100
 - 0s - loss: 0.0458 - acc: 0.9899
2021-05-16 01:15:18 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-16 01:15:18 INFO     rasa.core.agent  - Model directory /tmp/tmp_idyb0z_/core exists and contains old model files. All files will be overwritten.
2021-05-16 01:15:18 INFO     rasa.core.agent  - Persisted model to '/tmp/tmp_idyb0z_/core'
Core model training completed.

Training NLU model...

2021-05-16 01:15:18 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmp5lfzsza9/9e663a4170ae4a51b0a693c96ca47934_nlu.md is md
2021-05-16 01:15:19 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'intent_prediksi_cuaca', 'intent_salam', 'intent_setuju', 'intent_minta_jadwal', 'mood_tidak_senang', 'terima_kasih', 'intent_menolak', 'intent_menyapa', 'menantang_bot', 'intent_confirm_kota', 'intent_jadwal_sholat', 'intent_minta_jadwal_saja', 'mood_baik', 'intent_confirm_nama_atau_nim', 'intent_minta_daftar_nilai', 'intent_berpisah'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'NIM', 'konsentrasi', 'kota', 'nama'

2021-05-16 01:15:19 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 01:15:19 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-16 01:15:19 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-16 01:15:19 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|████████████████████████████████████████████████| 300/300 [00:10<00:00, 28.01it/s, loss=0.017, acc=0.999]
2021-05-16 01:15:30 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.017, train accuracy=0.999
2021-05-16 01:15:30 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 01:15:30 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmp_idyb0z_/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210516-011530.tar.gz'.


```