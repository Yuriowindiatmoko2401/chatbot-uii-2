```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug

2021-05-16 03:03:41 DEBUG    rasa.skill  - Selected skills: 
2021-05-16 03:03:41 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py

Training Core model...
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 5334.57it/s, # trackers=1]
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 538.12it/s, # trackers=14]
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 210.84it/s, # trackers=34]
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 204.13it/s, # trackers=31]
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-16 03:03:41 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-16 03:03:41 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-16 03:03:41 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|█████████████████████████████████████████████| 15/15 [00:00<00:00, 4298.91it/s, # actions=52]
2021-05-16 03:03:41 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 15127.19it/s, # examples=52]
2021-05-16 03:03:41 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-16 03:03:41 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|██████████████████████████████████████████| 515/515 [00:00<00:00, 2027.97it/s, # actions=596]
2021-05-16 03:03:41 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
gru (GRU)                    (None, 128)               67584     
_________________________________________________________________
dense (Dense)                (None, 23)                2967      
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 70,551
Trainable params: 70,551
Non-trainable params: 0
_________________________________________________________________

2021-05-16 03:03:41 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-16 03:03:41 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}
Epoch 1/100
 - 0s - loss: 2.5289 - acc: 0.4446
Epoch 2/100
 - 0s - loss: 1.9795 - acc: 0.4832
Epoch 3/100
 - 0s - loss: 1.6548 - acc: 0.4933
Epoch 4/100
 - 0s - loss: 1.2960 - acc: 0.6309
Epoch 5/100
 - 0s - loss: 1.1541 - acc: 0.7148
Epoch 6/100
 - 0s - loss: 0.9928 - acc: 0.7970
Epoch 7/100
 - 0s - loss: 0.8658 - acc: 0.8507
Epoch 8/100
 - 0s - loss: 0.7437 - acc: 0.8826
Epoch 9/100
 - 0s - loss: 0.6206 - acc: 0.9077
Epoch 10/100
 - 0s - loss: 0.5605 - acc: 0.8926
Epoch 11/100
 - 0s - loss: 0.4722 - acc: 0.9060
Epoch 12/100
 - 0s - loss: 0.4316 - acc: 0.9077
Epoch 13/100
 - 0s - loss: 0.3678 - acc: 0.9195
Epoch 14/100
 - 0s - loss: 0.3357 - acc: 0.9195
Epoch 15/100
 - 0s - loss: 0.3248 - acc: 0.9128
Epoch 16/100
 - 0s - loss: 0.2801 - acc: 0.9245
Epoch 17/100
 - 0s - loss: 0.2537 - acc: 0.9329
Epoch 18/100
 - 0s - loss: 0.2640 - acc: 0.9211
Epoch 19/100
 - 0s - loss: 0.2380 - acc: 0.9279
Epoch 20/100
 - 0s - loss: 0.2174 - acc: 0.9379
Epoch 21/100
 - 0s - loss: 0.1927 - acc: 0.9430
Epoch 22/100
 - 0s - loss: 0.2118 - acc: 0.9329
Epoch 23/100
 - 0s - loss: 0.1963 - acc: 0.9379
Epoch 24/100
 - 0s - loss: 0.1772 - acc: 0.9430
Epoch 25/100
 - 0s - loss: 0.1877 - acc: 0.9430
Epoch 26/100
 - 0s - loss: 0.1778 - acc: 0.9446
Epoch 27/100
 - 0s - loss: 0.1921 - acc: 0.9480
Epoch 28/100
 - 0s - loss: 0.1689 - acc: 0.9581
Epoch 29/100
 - 0s - loss: 0.1618 - acc: 0.9530
Epoch 30/100
 - 0s - loss: 0.1680 - acc: 0.9480
Epoch 31/100
 - 0s - loss: 0.1175 - acc: 0.9698
Epoch 32/100
 - 0s - loss: 0.1293 - acc: 0.9664
Epoch 33/100
 - 0s - loss: 0.1363 - acc: 0.9530
Epoch 34/100
 - 0s - loss: 0.1322 - acc: 0.9648
Epoch 35/100
 - 0s - loss: 0.1375 - acc: 0.9631
Epoch 36/100
 - 0s - loss: 0.1111 - acc: 0.9732
Epoch 37/100
 - 0s - loss: 0.1270 - acc: 0.9648
Epoch 38/100
 - 0s - loss: 0.1286 - acc: 0.9681
Epoch 39/100
 - 0s - loss: 0.1030 - acc: 0.9748
Epoch 40/100
 - 0s - loss: 0.1111 - acc: 0.9715
Epoch 41/100
 - 0s - loss: 0.0914 - acc: 0.9799
Epoch 42/100
 - 0s - loss: 0.0960 - acc: 0.9765
Epoch 43/100
 - 0s - loss: 0.1139 - acc: 0.9732
Epoch 44/100
 - 0s - loss: 0.1020 - acc: 0.9715
Epoch 45/100
 - 0s - loss: 0.0735 - acc: 0.9849
Epoch 46/100
 - 0s - loss: 0.1018 - acc: 0.9732
Epoch 47/100
 - 0s - loss: 0.0880 - acc: 0.9732
Epoch 48/100
 - 0s - loss: 0.1061 - acc: 0.9681
Epoch 49/100
 - 0s - loss: 0.0674 - acc: 0.9849
Epoch 50/100
 - 0s - loss: 0.0882 - acc: 0.9732
Epoch 51/100
 - 0s - loss: 0.0822 - acc: 0.9732
Epoch 52/100
 - 0s - loss: 0.0739 - acc: 0.9883
Epoch 53/100
 - 0s - loss: 0.0869 - acc: 0.9698
Epoch 54/100
 - 0s - loss: 0.0607 - acc: 0.9815
Epoch 55/100
 - 0s - loss: 0.0879 - acc: 0.9765
Epoch 56/100
 - 0s - loss: 0.0741 - acc: 0.9732
Epoch 57/100
 - 0s - loss: 0.0786 - acc: 0.9832
Epoch 58/100
 - 0s - loss: 0.0516 - acc: 0.9832
Epoch 59/100
 - 0s - loss: 0.0571 - acc: 0.9849
Epoch 60/100
 - 0s - loss: 0.0825 - acc: 0.9698
Epoch 61/100
 - 0s - loss: 0.0397 - acc: 0.9899
Epoch 62/100
 - 0s - loss: 0.0560 - acc: 0.9849
Epoch 63/100
 - 0s - loss: 0.0725 - acc: 0.9732
Epoch 64/100
 - 0s - loss: 0.0647 - acc: 0.9815
Epoch 65/100
 - 0s - loss: 0.0713 - acc: 0.9765
Epoch 66/100
 - 0s - loss: 0.0438 - acc: 0.9899
Epoch 67/100
 - 0s - loss: 0.0551 - acc: 0.9866
Epoch 68/100
 - 0s - loss: 0.0773 - acc: 0.9765
Epoch 69/100
 - 0s - loss: 0.0395 - acc: 0.9866
Epoch 70/100
 - 0s - loss: 0.0663 - acc: 0.9765
Epoch 71/100
 - 0s - loss: 0.0518 - acc: 0.9799
Epoch 72/100
 - 0s - loss: 0.0414 - acc: 0.9916
Epoch 73/100
 - 0s - loss: 0.0773 - acc: 0.9748
Epoch 74/100
 - 0s - loss: 0.0564 - acc: 0.9832
Epoch 75/100
 - 0s - loss: 0.0646 - acc: 0.9782
Epoch 76/100
 - 0s - loss: 0.0683 - acc: 0.9748
Epoch 77/100
 - 0s - loss: 0.0480 - acc: 0.9866
Epoch 78/100
 - 0s - loss: 0.0783 - acc: 0.9732
Epoch 79/100
 - 0s - loss: 0.0514 - acc: 0.9815
Epoch 80/100
 - 0s - loss: 0.0455 - acc: 0.9849
Epoch 81/100
 - 0s - loss: 0.0584 - acc: 0.9799
Epoch 82/100
 - 0s - loss: 0.0559 - acc: 0.9815
Epoch 83/100
 - 0s - loss: 0.0351 - acc: 0.9866
Epoch 84/100
 - 0s - loss: 0.0522 - acc: 0.9849
Epoch 85/100
 - 0s - loss: 0.0500 - acc: 0.9849
Epoch 86/100
 - 0s - loss: 0.0656 - acc: 0.9732
Epoch 87/100
 - 0s - loss: 0.0615 - acc: 0.9815
Epoch 88/100
 - 0s - loss: 0.0415 - acc: 0.9849
Epoch 89/100
 - 0s - loss: 0.0659 - acc: 0.9782
Epoch 90/100
 - 0s - loss: 0.0583 - acc: 0.9832
Epoch 91/100
 - 0s - loss: 0.0657 - acc: 0.9799
Epoch 92/100
 - 0s - loss: 0.0339 - acc: 0.9916
Epoch 93/100
 - 0s - loss: 0.0726 - acc: 0.9732
Epoch 94/100
 - 0s - loss: 0.0455 - acc: 0.9849
Epoch 95/100
 - 0s - loss: 0.0459 - acc: 0.9832
Epoch 96/100
 - 0s - loss: 0.0586 - acc: 0.9815
Epoch 97/100
 - 0s - loss: 0.0248 - acc: 0.9883
Epoch 98/100
 - 0s - loss: 0.0681 - acc: 0.9799
Epoch 99/100
 - 0s - loss: 0.0526 - acc: 0.9849
Epoch 100/100
 - 0s - loss: 0.0449 - acc: 0.9832

2021-05-16 03:03:52 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-16 03:03:52 INFO     rasa.core.agent  - Persisted model to '/tmp/tmptyczmb5c/core'
Core model training completed.

Training NLU model...

2021-05-16 03:03:52 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmpx1uborj_/c4ad5b981a144b59b43b300db332b53a_nlu.md is md
2021-05-16 03:03:52 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'mood_tidak_senang', 'intent_minta_daftar_nilai', 'menantang_bot', 'intent_prediksi_cuaca', 'intent_minta_jadwal', 'intent_salam', 'intent_confirm_kota', 'intent_berpisah', 'intent_minta_jadwal_saja', 'intent_menyapa', 'terima_kasih', 'intent_confirm_nama_atau_nim', 'mood_baik', 'intent_menolak', 'intent_jadwal_sholat', 'intent_setuju'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'NIM', 'kota', 'nama', 'konsentrasi'

2021-05-16 03:03:52 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 03:03:52 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-16 03:03:52 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-16 03:03:52 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|████████████████████████████████████████████████| 300/300 [00:10<00:00, 28.38it/s, loss=0.015, acc=0.999]
2021-05-16 03:04:03 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.015, train accuracy=0.999
2021-05-16 03:04:03 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 03:04:03 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmptyczmb5c/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210516-030403.tar.gz'.


```