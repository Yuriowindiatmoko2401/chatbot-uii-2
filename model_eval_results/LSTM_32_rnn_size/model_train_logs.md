```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug               

2021-05-15 17:59:25 DEBUG    rasa.skill  - Selected skills: 
2021-05-15 17:59:25 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py

Training Core model...
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 6033.34it/s, # trackers=1]

2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 594.09it/s, # trackers=14]

2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 225.41it/s, # trackers=34]

2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 220.89it/s, # trackers=31]

2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-15 17:59:25 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-15 17:59:25 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-15 17:59:25 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|██████| 15/15 [00:00<00:00, 6029.76it/s, # actions=52]

2021-05-15 17:59:25 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 21485.94it/s, # examples=52]
2021-05-15 17:59:25 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-15 17:59:25 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|███| 515/515 [00:00<00:00, 2813.28it/s, # actions=596]
2021-05-15 17:59:25 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
lstm (LSTM)                  (None, 32)                10240     
_________________________________________________________________
dense (Dense)                (None, 23)                759       
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 10,999
Trainable params: 10,999
Non-trainable params: 0
_________________________________________________________________

2021-05-15 17:59:26 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-15 17:59:26 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}

Epoch 1/100
 - 0s - loss: 3.0383 - acc: 0.2685
Epoch 2/100
 - 0s - loss: 2.7654 - acc: 0.4765
Epoch 3/100
 - 0s - loss: 2.3374 - acc: 0.4832
Epoch 4/100
 - 0s - loss: 2.0790 - acc: 0.4832
Epoch 5/100
 - 0s - loss: 2.0268 - acc: 0.4832
Epoch 6/100
 - 0s - loss: 1.9675 - acc: 0.4849
Epoch 7/100
 - 0s - loss: 1.9332 - acc: 0.4866
Epoch 8/100
 - 0s - loss: 1.8976 - acc: 0.4849
Epoch 9/100
 - 0s - loss: 1.8517 - acc: 0.4832
Epoch 10/100
 - 0s - loss: 1.8122 - acc: 0.4866
Epoch 11/100
 - 0s - loss: 1.7771 - acc: 0.4849
Epoch 12/100
 - 0s - loss: 1.7328 - acc: 0.4849
Epoch 13/100
 - 0s - loss: 1.6912 - acc: 0.4866
Epoch 14/100
 - 0s - loss: 1.6645 - acc: 0.4883
Epoch 15/100
 - 0s - loss: 1.5939 - acc: 0.4883
Epoch 16/100
 - 0s - loss: 1.5693 - acc: 0.4950
Epoch 17/100
 - 0s - loss: 1.5021 - acc: 0.4983
Epoch 18/100
 - 0s - loss: 1.4625 - acc: 0.4950
Epoch 19/100
 - 0s - loss: 1.4180 - acc: 0.5067
Epoch 20/100
 - 0s - loss: 1.3469 - acc: 0.5336
Epoch 21/100
 - 0s - loss: 1.2891 - acc: 0.5721
Epoch 22/100
 - 0s - loss: 1.2165 - acc: 0.6225
Epoch 23/100
 - 0s - loss: 1.1528 - acc: 0.6695
Epoch 24/100
 - 0s - loss: 1.1067 - acc: 0.7013
Epoch 25/100
 - 0s - loss: 1.0487 - acc: 0.7433
Epoch 26/100
 - 0s - loss: 1.0171 - acc: 0.7550
Epoch 27/100
 - 0s - loss: 0.9648 - acc: 0.7970
Epoch 28/100
 - 0s - loss: 0.9387 - acc: 0.8070
Epoch 29/100
 - 0s - loss: 0.9141 - acc: 0.8121
Epoch 30/100
 - 0s - loss: 0.8567 - acc: 0.8456
Epoch 31/100
 - 0s - loss: 0.8205 - acc: 0.8607
Epoch 32/100
 - 0s - loss: 0.7903 - acc: 0.8641
Epoch 33/100
 - 0s - loss: 0.7477 - acc: 0.8943
Epoch 34/100
 - 0s - loss: 0.7444 - acc: 0.8893
Epoch 35/100
 - 0s - loss: 0.7145 - acc: 0.9027
Epoch 36/100
 - 0s - loss: 0.6411 - acc: 0.9295
Epoch 37/100
 - 0s - loss: 0.6453 - acc: 0.9195
Epoch 38/100
 - 0s - loss: 0.6126 - acc: 0.9245
Epoch 39/100
 - 0s - loss: 0.5802 - acc: 0.9295
Epoch 40/100
 - 0s - loss: 0.5665 - acc: 0.9262
Epoch 41/100
 - 0s - loss: 0.5345 - acc: 0.9379
Epoch 42/100
 - 0s - loss: 0.5118 - acc: 0.9430
Epoch 43/100
 - 0s - loss: 0.4972 - acc: 0.9379
Epoch 44/100
 - 0s - loss: 0.4554 - acc: 0.9463
Epoch 45/100
 - 0s - loss: 0.3941 - acc: 0.9681
Epoch 46/100
 - 0s - loss: 0.4083 - acc: 0.9497
Epoch 47/100
 - 0s - loss: 0.4052 - acc: 0.9497
Epoch 48/100
 - 0s - loss: 0.3552 - acc: 0.9648
Epoch 49/100
 - 0s - loss: 0.3381 - acc: 0.9581
Epoch 50/100
 - 0s - loss: 0.3393 - acc: 0.9564
Epoch 51/100
 - 0s - loss: 0.3159 - acc: 0.9631
Epoch 52/100
 - 0s - loss: 0.2897 - acc: 0.9698
Epoch 53/100
 - 0s - loss: 0.2688 - acc: 0.9732
Epoch 54/100
 - 0s - loss: 0.2714 - acc: 0.9715
Epoch 55/100
 - 0s - loss: 0.2661 - acc: 0.9698
Epoch 56/100
 - 0s - loss: 0.2371 - acc: 0.9782
Epoch 57/100
 - 0s - loss: 0.2325 - acc: 0.9698
Epoch 58/100
 - 0s - loss: 0.2203 - acc: 0.9681
Epoch 59/100
 - 0s - loss: 0.2214 - acc: 0.9732
Epoch 60/100
 - 0s - loss: 0.2155 - acc: 0.9765
Epoch 61/100
 - 0s - loss: 0.2014 - acc: 0.9815
Epoch 62/100
 - 0s - loss: 0.2001 - acc: 0.9748
Epoch 63/100
 - 0s - loss: 0.2110 - acc: 0.9782
Epoch 64/100
 - 0s - loss: 0.2047 - acc: 0.9748
Epoch 65/100
 - 0s - loss: 0.2049 - acc: 0.9681
Epoch 66/100
 - 0s - loss: 0.1679 - acc: 0.9832
Epoch 67/100
 - 0s - loss: 0.1611 - acc: 0.9765
Epoch 68/100
 - 0s - loss: 0.1707 - acc: 0.9748
Epoch 69/100
 - 0s - loss: 0.1567 - acc: 0.9765
Epoch 70/100
 - 0s - loss: 0.1652 - acc: 0.9849
Epoch 71/100
 - 0s - loss: 0.1534 - acc: 0.9799
Epoch 72/100
 - 0s - loss: 0.1447 - acc: 0.9799
Epoch 73/100
 - 0s - loss: 0.1484 - acc: 0.9832
Epoch 74/100
 - 0s - loss: 0.1214 - acc: 0.9883
Epoch 75/100
 - 0s - loss: 0.1265 - acc: 0.9832
Epoch 76/100
 - 0s - loss: 0.1368 - acc: 0.9765
Epoch 77/100
 - 0s - loss: 0.0984 - acc: 0.9883
Epoch 78/100
 - 0s - loss: 0.1335 - acc: 0.9748
Epoch 79/100
 - 0s - loss: 0.1000 - acc: 0.9849
Epoch 80/100
 - 0s - loss: 0.1338 - acc: 0.9765
Epoch 81/100
 - 0s - loss: 0.1220 - acc: 0.9765
Epoch 82/100
 - 0s - loss: 0.1101 - acc: 0.9832
Epoch 83/100
 - 0s - loss: 0.0997 - acc: 0.9866
Epoch 84/100
 - 0s - loss: 0.1050 - acc: 0.9815
Epoch 85/100
 - 0s - loss: 0.0974 - acc: 0.9899
Epoch 86/100
 - 0s - loss: 0.0916 - acc: 0.9883
Epoch 87/100
 - 0s - loss: 0.0936 - acc: 0.9849
Epoch 88/100
 - 0s - loss: 0.0985 - acc: 0.9899
Epoch 89/100
 - 0s - loss: 0.1065 - acc: 0.9866
Epoch 90/100
 - 0s - loss: 0.1043 - acc: 0.9916
Epoch 91/100
 - 0s - loss: 0.0932 - acc: 0.9832
Epoch 92/100
 - 0s - loss: 0.0912 - acc: 0.9866
Epoch 93/100
 - 0s - loss: 0.0807 - acc: 0.9933
Epoch 94/100
 - 0s - loss: 0.0838 - acc: 0.9883
Epoch 95/100
 - 0s - loss: 0.0687 - acc: 0.9916
Epoch 96/100
 - 0s - loss: 0.0802 - acc: 0.9916
Epoch 97/100
 - 0s - loss: 0.0759 - acc: 0.9933
Epoch 98/100
 - 0s - loss: 0.0788 - acc: 0.9866
Epoch 99/100
 - 0s - loss: 0.0882 - acc: 0.9883
Epoch 100/100
 - 0s - loss: 0.0659 - acc: 0.9899

2021-05-15 17:59:33 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-15 17:59:33 INFO     rasa.core.agent  - Persisted model to '/tmp/tmpscgz4jlp/core'
Core model training completed.

Training NLU model...

2021-05-15 17:59:33 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmp_snfupvy/749b9f037ba34c5ca7c0a5846f9e971e_nlu.md is md
2021-05-15 17:59:33 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'intent_menyapa', 'intent_berpisah', 'intent_minta_daftar_nilai', 'mood_baik', 'intent_prediksi_cuaca', 'terima_kasih', 'menantang_bot', 'intent_menolak', 'intent_setuju', 'intent_confirm_kota', 'intent_minta_jadwal', 'intent_jadwal_sholat', 'intent_minta_jadwal_saja', 'intent_salam', 'mood_tidak_senang', 'intent_confirm_nama_atau_nim'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'kota', 'NIM', 'konsentrasi', 'nama'

2021-05-15 17:59:33 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 17:59:33 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-15 17:59:33 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-15 17:59:34 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs

Epochs: 100%|█████████| 300/300 [00:10<00:00, 28.32it/s, loss=0.011, acc=0.999]
2021-05-15 17:59:44 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.011, train accuracy=0.999
2021-05-15 17:59:44 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 17:59:44 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmpscgz4jlp/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210515-175944.tar.gz'.

```