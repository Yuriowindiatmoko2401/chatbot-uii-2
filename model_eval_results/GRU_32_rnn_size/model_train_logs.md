```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug


2021-05-16 00:29:13 DEBUG    rasa.skill  - Selected skills: 
2021-05-16 00:29:13 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py

Training Core model...
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 4473.33it/s, # trackers=1]
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 593.93it/s, # trackers=14]
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 219.21it/s, # trackers=34]
2021-05-16 00:29:13 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-16 00:29:14 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|█████████████████████████████████████████| 16/16 [00:00<00:00, 209.78it/s, # trackers=31]
2021-05-16 00:29:14 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-16 00:29:14 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-16 00:29:14 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-16 00:29:14 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-16 00:29:14 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-16 00:29:14 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|█████████████████████████████████████████████| 15/15 [00:00<00:00, 6118.90it/s, # actions=52]
2021-05-16 00:29:14 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 22683.70it/s, # examples=52]
2021-05-16 00:29:14 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-16 00:29:14 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|██████████████████████████████████████████| 515/515 [00:00<00:00, 2116.20it/s, # actions=596]
2021-05-16 00:29:14 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
gru (GRU)                    (None, 32)                7680      
_________________________________________________________________
dense (Dense)                (None, 23)                759       
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 8,439
Trainable params: 8,439
Non-trainable params: 0
_________________________________________________________________

2021-05-16 00:29:14 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-16 00:29:14 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}

Epoch 1/100
 - 0s - loss: 2.9553 - acc: 0.3356
Epoch 2/100
 - 0s - loss: 2.6199 - acc: 0.4815
Epoch 3/100
 - 0s - loss: 2.2507 - acc: 0.4832
Epoch 4/100
 - 0s - loss: 2.0765 - acc: 0.4832
Epoch 5/100
 - 0s - loss: 1.9730 - acc: 0.4832
Epoch 6/100
 - 0s - loss: 1.9135 - acc: 0.4832
Epoch 7/100
 - 0s - loss: 1.8450 - acc: 0.4832
Epoch 8/100
 - 0s - loss: 1.7651 - acc: 0.4832
Epoch 9/100
 - 0s - loss: 1.6658 - acc: 0.4849
Epoch 10/100
 - 0s - loss: 1.5451 - acc: 0.4866
Epoch 11/100
 - 0s - loss: 1.4120 - acc: 0.5268
Epoch 12/100
 - 0s - loss: 1.2765 - acc: 0.5956
Epoch 13/100
 - 0s - loss: 1.1927 - acc: 0.6426
Epoch 14/100
 - 0s - loss: 1.1002 - acc: 0.6879
Epoch 15/100
 - 0s - loss: 1.0199 - acc: 0.7584
Epoch 16/100
 - 0s - loss: 0.9738 - acc: 0.8087
Epoch 17/100
 - 0s - loss: 0.9111 - acc: 0.8523
Epoch 18/100
 - 0s - loss: 0.8334 - acc: 0.8826
Epoch 19/100
 - 0s - loss: 0.8125 - acc: 0.8792
Epoch 20/100
 - 0s - loss: 0.7497 - acc: 0.8876
Epoch 21/100
 - 0s - loss: 0.7005 - acc: 0.8943
Epoch 22/100
 - 0s - loss: 0.6406 - acc: 0.9027
Epoch 23/100
 - 0s - loss: 0.5936 - acc: 0.9144
Epoch 24/100
 - 0s - loss: 0.5796 - acc: 0.8926
Epoch 25/100
 - 0s - loss: 0.5546 - acc: 0.9010
Epoch 26/100
 - 0s - loss: 0.4943 - acc: 0.9044
Epoch 27/100
 - 0s - loss: 0.4875 - acc: 0.8993
Epoch 28/100
 - 0s - loss: 0.4427 - acc: 0.8977
Epoch 29/100
 - 0s - loss: 0.3642 - acc: 0.9262
Epoch 30/100
 - 0s - loss: 0.3782 - acc: 0.9161
Epoch 31/100
 - 0s - loss: 0.3448 - acc: 0.9211
Epoch 32/100
 - 0s - loss: 0.3268 - acc: 0.9161
Epoch 33/100
 - 0s - loss: 0.3520 - acc: 0.9060
Epoch 34/100
 - 0s - loss: 0.2995 - acc: 0.9245
Epoch 35/100
 - 0s - loss: 0.3190 - acc: 0.9161
Epoch 36/100
 - 0s - loss: 0.2761 - acc: 0.9346
Epoch 37/100
 - 0s - loss: 0.3168 - acc: 0.9161
Epoch 38/100
 - 0s - loss: 0.2953 - acc: 0.9279
Epoch 39/100
 - 0s - loss: 0.2473 - acc: 0.9379
Epoch 40/100
 - 0s - loss: 0.2263 - acc: 0.9564
Epoch 41/100
 - 0s - loss: 0.2709 - acc: 0.9413
Epoch 42/100
 - 0s - loss: 0.2667 - acc: 0.9329
Epoch 43/100
 - 0s - loss: 0.2117 - acc: 0.9564
Epoch 44/100
 - 0s - loss: 0.2423 - acc: 0.9446
Epoch 45/100
 - 0s - loss: 0.2248 - acc: 0.9480
Epoch 46/100
 - 0s - loss: 0.2027 - acc: 0.9597
Epoch 47/100
 - 0s - loss: 0.1733 - acc: 0.9614
Epoch 48/100
 - 0s - loss: 0.2397 - acc: 0.9362
Epoch 49/100
 - 0s - loss: 0.2096 - acc: 0.9581
Epoch 50/100
 - 0s - loss: 0.2225 - acc: 0.9513
Epoch 51/100
 - 0s - loss: 0.1826 - acc: 0.9581
Epoch 52/100
 - 0s - loss: 0.1802 - acc: 0.9564
Epoch 53/100
 - 0s - loss: 0.1737 - acc: 0.9732
Epoch 54/100
 - 0s - loss: 0.1793 - acc: 0.9648
Epoch 55/100
 - 0s - loss: 0.1610 - acc: 0.9748
Epoch 56/100
 - 0s - loss: 0.1743 - acc: 0.9698
Epoch 57/100
 - 0s - loss: 0.1493 - acc: 0.9664
Epoch 58/100
 - 0s - loss: 0.1640 - acc: 0.9748
Epoch 59/100
 - 0s - loss: 0.1760 - acc: 0.9547
Epoch 60/100
 - 0s - loss: 0.1570 - acc: 0.9732
Epoch 61/100
 - 0s - loss: 0.1013 - acc: 0.9883
Epoch 62/100
 - 0s - loss: 0.1615 - acc: 0.9614
Epoch 63/100
 - 0s - loss: 0.1445 - acc: 0.9715
Epoch 64/100
 - 0s - loss: 0.1260 - acc: 0.9748
Epoch 65/100
 - 0s - loss: 0.1145 - acc: 0.9732
Epoch 66/100
 - 0s - loss: 0.1257 - acc: 0.9732
Epoch 67/100
 - 0s - loss: 0.1041 - acc: 0.9799
Epoch 68/100
 - 0s - loss: 0.1250 - acc: 0.9815
Epoch 69/100
 - 0s - loss: 0.1482 - acc: 0.9681
Epoch 70/100
 - 0s - loss: 0.1477 - acc: 0.9614
Epoch 71/100
 - 0s - loss: 0.1427 - acc: 0.9698
Epoch 72/100
 - 0s - loss: 0.0825 - acc: 0.9832
Epoch 73/100
 - 0s - loss: 0.1226 - acc: 0.9698
Epoch 74/100
 - 0s - loss: 0.1008 - acc: 0.9832
Epoch 75/100
 - 0s - loss: 0.0963 - acc: 0.9832
Epoch 76/100
 - 0s - loss: 0.1085 - acc: 0.9748
Epoch 77/100
 - 0s - loss: 0.1067 - acc: 0.9732
Epoch 78/100
 - 0s - loss: 0.0998 - acc: 0.9765
Epoch 79/100
 - 0s - loss: 0.1023 - acc: 0.9832
Epoch 80/100
 - 0s - loss: 0.0833 - acc: 0.9815
Epoch 81/100
 - 0s - loss: 0.1172 - acc: 0.9664
Epoch 82/100
 - 0s - loss: 0.0698 - acc: 0.9799
Epoch 83/100
 - 0s - loss: 0.0734 - acc: 0.9866
Epoch 84/100
 - 0s - loss: 0.1028 - acc: 0.9732
Epoch 85/100
 - 0s - loss: 0.0739 - acc: 0.9832
Epoch 86/100
 - 0s - loss: 0.0826 - acc: 0.9799
Epoch 87/100
 - 0s - loss: 0.0853 - acc: 0.9765
Epoch 88/100
 - 0s - loss: 0.0723 - acc: 0.9866
Epoch 89/100
 - 0s - loss: 0.0719 - acc: 0.9849
Epoch 90/100
 - 0s - loss: 0.0710 - acc: 0.9849
Epoch 91/100
 - 0s - loss: 0.0914 - acc: 0.9799
Epoch 92/100
 - 0s - loss: 0.0929 - acc: 0.9732
Epoch 93/100
 - 0s - loss: 0.0812 - acc: 0.9815
Epoch 94/100
 - 0s - loss: 0.0740 - acc: 0.9799
Epoch 95/100
 - 0s - loss: 0.0679 - acc: 0.9799
Epoch 96/100
 - 0s - loss: 0.0648 - acc: 0.9782
Epoch 97/100
 - 0s - loss: 0.0547 - acc: 0.9899
Epoch 98/100
 - 0s - loss: 0.0822 - acc: 0.9799
Epoch 99/100
 - 0s - loss: 0.0640 - acc: 0.9849
Epoch 100/100
 - 0s - loss: 0.0934 - acc: 0.9748

2021-05-16 00:29:21 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-16 00:29:21 INFO     rasa.core.agent  - Persisted model to '/tmp/tmp7qj7v13p/core'
Core model training completed.

Training NLU model...

2021-05-16 00:29:21 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmpzvf0oeou/d15b7cf880af42d2b784af7481b56492_nlu.md is md
2021-05-16 00:29:21 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'intent_minta_jadwal_saja', 'mood_baik', 'intent_jadwal_sholat', 'intent_menyapa', 'intent_berpisah', 'intent_confirm_nama_atau_nim', 'intent_setuju', 'intent_minta_daftar_nilai', 'intent_minta_jadwal', 'intent_confirm_kota', 'intent_prediksi_cuaca', 'mood_tidak_senang', 'menantang_bot', 'intent_salam', 'terima_kasih', 'intent_menolak'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'NIM', 'kota', 'nama', 'konsentrasi'

2021-05-16 00:29:21 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 00:29:21 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-16 00:29:21 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-16 00:29:22 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|████████████████████████████████████████████████| 300/300 [00:10<00:00, 31.03it/s, loss=0.012, acc=0.999]
2021-05-16 00:29:33 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.012, train accuracy=0.999
2021-05-16 00:29:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-16 00:29:33 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmp7qj7v13p/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210516-002933.tar.gz'.

```