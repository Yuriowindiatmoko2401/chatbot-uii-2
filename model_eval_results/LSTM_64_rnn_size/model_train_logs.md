```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 
rasa train -vv --dump-stories --force --debug               

2021-05-15 19:18:09 DEBUG    rasa.skill  - Selected skills: 
2021-05-15 19:18:09 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py

Training Core model...
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 4905.26it/s, # trackers=1]

2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 575.58it/s, # trackers=14]

2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 210.09it/s, # trackers=34]

2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)
Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 205.53it/s, # trackers=31]

2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-15 19:18:09 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-15 19:18:09 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-15 19:18:09 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...
Processed trackers: 100%|██████| 15/15 [00:00<00:00, 6446.82it/s, # actions=52]
2021-05-15 19:18:09 DEBUG    rasa.core.featurizers  - Created 52 action examples.
Processed actions: 52it [00:00, 17576.26it/s, # examples=52]

2021-05-15 19:18:09 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-15 19:18:09 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...
Processed trackers: 100%|███| 515/515 [00:00<00:00, 2493.47it/s, # actions=596]
2021-05-15 19:18:09 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
lstm (LSTM)                  (None, 64)                28672     
_________________________________________________________________
dense (Dense)                (None, 23)                1495      
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 30,167
Trainable params: 30,167
Non-trainable params: 0
_________________________________________________________________

2021-05-15 19:18:10 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-15 19:18:10 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}
Epoch 1/100
 - 0s - loss: 2.9242 - acc: 0.4044
Epoch 2/100
 - 0s - loss: 2.2776 - acc: 0.4832
Epoch 3/100
 - 0s - loss: 2.0770 - acc: 0.4832
Epoch 4/100
 - 0s - loss: 1.9730 - acc: 0.4832
Epoch 5/100
 - 0s - loss: 1.9021 - acc: 0.4832
Epoch 6/100
 - 0s - loss: 1.8390 - acc: 0.4832
Epoch 7/100
 - 0s - loss: 1.7648 - acc: 0.4849
Epoch 8/100
 - 0s - loss: 1.6939 - acc: 0.4849
Epoch 9/100
 - 0s - loss: 1.5939 - acc: 0.4899
Epoch 10/100
 - 0s - loss: 1.5047 - acc: 0.4916
Epoch 11/100
 - 0s - loss: 1.3940 - acc: 0.5034
Epoch 12/100
 - 0s - loss: 1.2904 - acc: 0.5738
Epoch 13/100
 - 0s - loss: 1.1755 - acc: 0.6661
Epoch 14/100
 - 0s - loss: 1.0858 - acc: 0.7030
Epoch 15/100
 - 0s - loss: 0.9956 - acc: 0.7584
Epoch 16/100
 - 0s - loss: 0.9190 - acc: 0.8020
Epoch 17/100
 - 0s - loss: 0.8836 - acc: 0.8238
Epoch 18/100
 - 0s - loss: 0.8362 - acc: 0.8507
Epoch 19/100
 - 0s - loss: 0.7633 - acc: 0.8977
Epoch 20/100
 - 0s - loss: 0.7294 - acc: 0.8993
Epoch 21/100
 - 0s - loss: 0.6878 - acc: 0.9027
Epoch 22/100
 - 0s - loss: 0.6189 - acc: 0.9430
Epoch 23/100
 - 0s - loss: 0.5897 - acc: 0.9346
Epoch 24/100
 - 0s - loss: 0.5497 - acc: 0.9346
Epoch 25/100
 - 0s - loss: 0.4944 - acc: 0.9547
Epoch 26/100
 - 0s - loss: 0.4696 - acc: 0.9379
Epoch 27/100
 - 0s - loss: 0.4335 - acc: 0.9480
Epoch 28/100
 - 0s - loss: 0.4205 - acc: 0.9463
Epoch 29/100
 - 0s - loss: 0.3967 - acc: 0.9396
Epoch 30/100
 - 0s - loss: 0.3740 - acc: 0.9547
Epoch 31/100
 - 0s - loss: 0.3422 - acc: 0.9480
Epoch 32/100
 - 0s - loss: 0.3088 - acc: 0.9547
Epoch 33/100
 - 0s - loss: 0.2946 - acc: 0.9547
Epoch 34/100
 - 0s - loss: 0.2673 - acc: 0.9597
Epoch 35/100
 - 0s - loss: 0.2587 - acc: 0.9664
Epoch 36/100
 - 0s - loss: 0.2302 - acc: 0.9748
Epoch 37/100
 - 0s - loss: 0.2428 - acc: 0.9631
Epoch 38/100
 - 0s - loss: 0.2231 - acc: 0.9631
Epoch 39/100
 - 0s - loss: 0.2113 - acc: 0.9681
Epoch 40/100
 - 0s - loss: 0.2290 - acc: 0.9530
Epoch 41/100
 - 0s - loss: 0.1832 - acc: 0.9732
Epoch 42/100
 - 0s - loss: 0.1824 - acc: 0.9698
Epoch 43/100
 - 0s - loss: 0.1634 - acc: 0.9765
Epoch 44/100
 - 0s - loss: 0.1471 - acc: 0.9765
Epoch 45/100
 - 0s - loss: 0.1536 - acc: 0.9765
Epoch 46/100
 - 0s - loss: 0.1396 - acc: 0.9698
Epoch 47/100
 - 0s - loss: 0.1336 - acc: 0.9715
Epoch 48/100
 - 0s - loss: 0.1666 - acc: 0.9648
Epoch 49/100
 - 0s - loss: 0.1365 - acc: 0.9765
Epoch 50/100
 - 0s - loss: 0.1646 - acc: 0.9698
Epoch 51/100
 - 0s - loss: 0.1422 - acc: 0.9698
Epoch 52/100
 - 0s - loss: 0.1378 - acc: 0.9765
Epoch 53/100
 - 0s - loss: 0.1305 - acc: 0.9815
Epoch 54/100
 - 0s - loss: 0.1291 - acc: 0.9883
Epoch 55/100
 - 0s - loss: 0.1002 - acc: 0.9866
Epoch 56/100
 - 0s - loss: 0.1107 - acc: 0.9765
Epoch 57/100
 - 0s - loss: 0.1070 - acc: 0.9849
Epoch 58/100
 - 0s - loss: 0.1220 - acc: 0.9832
Epoch 59/100
 - 0s - loss: 0.1111 - acc: 0.9849
Epoch 60/100
 - 0s - loss: 0.0943 - acc: 0.9849
Epoch 61/100
 - 0s - loss: 0.0757 - acc: 0.9883
Epoch 62/100
 - 0s - loss: 0.0941 - acc: 0.9815
Epoch 63/100
 - 0s - loss: 0.0874 - acc: 0.9866
Epoch 64/100
 - 0s - loss: 0.0865 - acc: 0.9883
Epoch 65/100
 - 0s - loss: 0.0917 - acc: 0.9883
Epoch 66/100
 - 0s - loss: 0.0910 - acc: 0.9883
Epoch 67/100
 - 0s - loss: 0.1119 - acc: 0.9832
Epoch 68/100
 - 0s - loss: 0.0842 - acc: 0.9866
Epoch 69/100
 - 0s - loss: 0.0894 - acc: 0.9899
Epoch 70/100
 - 0s - loss: 0.0590 - acc: 0.9916
Epoch 71/100
 - 0s - loss: 0.0923 - acc: 0.9849
Epoch 72/100
 - 0s - loss: 0.0728 - acc: 0.9950
Epoch 73/100
 - 0s - loss: 0.0689 - acc: 0.9950
Epoch 74/100
 - 0s - loss: 0.0727 - acc: 0.9916
Epoch 75/100
 - 0s - loss: 0.0608 - acc: 0.9933
Epoch 76/100
 - 0s - loss: 0.0640 - acc: 0.9950
Epoch 77/100
 - 0s - loss: 0.0778 - acc: 0.9832
Epoch 78/100
 - 0s - loss: 0.0666 - acc: 0.9899
Epoch 79/100
 - 0s - loss: 0.0522 - acc: 0.9966
Epoch 80/100
 - 0s - loss: 0.0747 - acc: 0.9866
Epoch 81/100
 - 0s - loss: 0.0630 - acc: 0.9899
Epoch 82/100
 - 0s - loss: 0.0436 - acc: 0.9950
Epoch 83/100
 - 0s - loss: 0.0539 - acc: 0.9899
Epoch 84/100
 - 0s - loss: 0.0580 - acc: 0.9933
Epoch 85/100
 - 0s - loss: 0.0538 - acc: 0.9933
Epoch 86/100
 - 0s - loss: 0.0511 - acc: 0.9899
Epoch 87/100
 - 0s - loss: 0.0472 - acc: 0.9950
Epoch 88/100
 - 0s - loss: 0.0554 - acc: 0.9866
Epoch 89/100
 - 0s - loss: 0.0399 - acc: 0.9983
Epoch 90/100
 - 0s - loss: 0.0504 - acc: 0.9966
Epoch 91/100
 - 0s - loss: 0.0370 - acc: 0.9950
Epoch 92/100
 - 0s - loss: 0.0566 - acc: 0.9883
Epoch 93/100
 - 0s - loss: 0.0506 - acc: 0.9899
Epoch 94/100
 - 0s - loss: 0.0453 - acc: 0.9883
Epoch 95/100
 - 0s - loss: 0.0445 - acc: 0.9933
Epoch 96/100
 - 0s - loss: 0.0528 - acc: 0.9883
Epoch 97/100
 - 0s - loss: 0.0456 - acc: 0.9916
Epoch 98/100
 - 0s - loss: 0.0399 - acc: 0.9933
Epoch 99/100
 - 0s - loss: 0.0383 - acc: 0.9966
Epoch 100/100
 - 0s - loss: 0.0410 - acc: 0.9916
2021-05-15 19:18:18 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-15 19:18:18 INFO     rasa.core.agent  - Persisted model to '/tmp/tmp0tw24y25/core'

Core model training completed.

Training NLU model...
/home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/sklearn/feature_extraction/image.py:167: DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
  dtype=np.int):
2021-05-15 19:18:18 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmp7h9tr1ur/c885b935995a491ab9e8cc0efd65bd34_nlu.md is md
2021-05-15 19:18:18 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'mood_tidak_senang', 'intent_minta_jadwal_saja', 'intent_salam', 'intent_setuju', 'intent_menolak', 'terima_kasih', 'intent_minta_jadwal', 'intent_confirm_kota', 'intent_confirm_nama_atau_nim', 'mood_baik', 'intent_menyapa', 'intent_prediksi_cuaca', 'intent_minta_daftar_nilai', 'menantang_bot', 'intent_jadwal_sholat', 'intent_berpisah'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'kota', 'nama', 'konsentrasi', 'NIM'

2021-05-15 19:18:18 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 19:18:18 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-15 19:18:18 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-15 19:18:19 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs
Epochs: 100%|█████████| 300/300 [00:11<00:00, 30.49it/s, loss=0.011, acc=0.999]
2021-05-15 19:18:30 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.011, train accuracy=0.999
2021-05-15 19:18:30 INFO     rasa.nlu.model  - Finished training component.
2021-05-15 19:18:30 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmp0tw24y25/nlu'
NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210515-191830.tar.gz'.


```