```bash
(rasa_16) ➜  chatbot-uii-2 git:(master) 

rasa train -vv --dump-stories --force --debug                 

2021-05-14 22:29:47 DEBUG    rasa.skill  - Selected skills: 

2021-05-14 22:29:47 DEBUG    pykwalify.compat  - Using yaml library: /home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/ruamel/yaml/__init__.py

2021-05-14 22:29:47 DEBUG    rasa.model  - Extracted model to '/tmp/tmpeu6nnsaz'.

Training Core model...

2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Generated trackers will be deduplicated based on their unique last 5 states.

2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Number of augmentation rounds is 3

2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Starting data generation round 0 ... (with 1 trackers)

Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 5530.19it/s, # trackers=1]

2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Finished phase (15 training samples found).
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Data generation rounds finished.
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Found 0 unused checkpoints
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Starting augmentation round 0 ... (with 15 trackers)

Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 592.82it/s, # trackers=14]
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Finished phase (226 training samples found).
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Starting augmentation round 1 ... (with 50 trackers)

Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 219.73it/s, # trackers=34]
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Finished phase (692 training samples found).
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Starting augmentation round 2 ... (with 50 trackers)

Processed Story Blocks: 100%|██| 16/16 [00:00<00:00, 213.52it/s, # trackers=31]
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Finished phase (1130 training samples found).
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Found 1130 training trackers.
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - Subsampled to 500 augmented training trackers.
2021-05-14 22:29:47 DEBUG    rasa.core.training.generator  - There are 15 original trackers.
2021-05-14 22:29:47 DEBUG    rasa.core.agent  - Agent trainer got kwargs: {'dump_stories': True}
2021-05-14 22:29:47 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(SingleStateFeaturizer))...

Processed trackers: 100%|██████| 15/15 [00:00<00:00, 6354.36it/s, # actions=52]
2021-05-14 22:29:47 DEBUG    rasa.core.featurizers  - Created 52 action examples.

Processed actions: 52it [00:00, 19907.25it/s, # examples=52]
2021-05-14 22:29:47 DEBUG    rasa.core.policies.memoization  - Memorized 52 unique examples.
2021-05-14 22:29:47 DEBUG    rasa.core.featurizers  - Creating states and action examples from collected trackers (by MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer))...

Processed trackers: 100%|███| 515/515 [00:00<00:00, 2655.79it/s, # actions=596]
2021-05-14 22:29:48 DEBUG    rasa.core.featurizers  - Created 596 action examples.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 5, 47)             0         
_________________________________________________________________
simple_rnn (SimpleRNN)       (None, 32)                2560      
_________________________________________________________________
dense (Dense)                (None, 23)                759       
_________________________________________________________________
activation (Activation)      (None, 23)                0         
=================================================================
Total params: 3,319
Trainable params: 3,319
Non-trainable params: 0
_________________________________________________________________

2021-05-14 22:29:48 INFO     rasa.core.policies.keras_policy  - Fitting model with 596 total samples and a validation split of 0.1
2021-05-14 22:29:48 DEBUG    rasa.core.policies.policy  - Parameters ignored by `model.fit(...)`: {}

Epoch 1/100
 - 0s - loss: 2.8669 - acc: 0.2567
Epoch 2/100
 - 0s - loss: 2.2020 - acc: 0.5151
Epoch 3/100
 - 0s - loss: 1.7633 - acc: 0.5436
Epoch 4/100
 - 0s - loss: 1.5590 - acc: 0.5587
Epoch 5/100
 - 0s - loss: 1.4302 - acc: 0.5856
Epoch 6/100
 - 0s - loss: 1.3651 - acc: 0.5990
Epoch 7/100
 - 0s - loss: 1.3146 - acc: 0.6225
Epoch 8/100
 - 0s - loss: 1.2527 - acc: 0.6762
Epoch 9/100
 - 0s - loss: 1.1922 - acc: 0.7131
Epoch 10/100
 - 0s - loss: 1.1466 - acc: 0.7517
Epoch 11/100
 - 0s - loss: 1.0939 - acc: 0.7768
Epoch 12/100
 - 0s - loss: 1.0569 - acc: 0.7718
Epoch 13/100
 - 0s - loss: 0.9926 - acc: 0.8104
Epoch 14/100
 - 0s - loss: 0.9397 - acc: 0.8238
Epoch 15/100
 - 0s - loss: 0.8952 - acc: 0.8389
Epoch 16/100
 - 0s - loss: 0.8462 - acc: 0.8289
Epoch 17/100
 - 0s - loss: 0.8199 - acc: 0.8423
Epoch 18/100
 - 0s - loss: 0.7769 - acc: 0.8456
Epoch 19/100
 - 0s - loss: 0.7291 - acc: 0.8708
Epoch 20/100
 - 0s - loss: 0.6970 - acc: 0.8607
Epoch 21/100
 - 0s - loss: 0.6567 - acc: 0.8758
Epoch 22/100
 - 0s - loss: 0.6515 - acc: 0.8658
Epoch 23/100
 - 0s - loss: 0.6100 - acc: 0.8826
Epoch 24/100
 - 0s - loss: 0.5775 - acc: 0.8960
Epoch 25/100
 - 0s - loss: 0.5519 - acc: 0.8909
Epoch 26/100
 - 0s - loss: 0.5181 - acc: 0.8893
Epoch 27/100
 - 0s - loss: 0.4817 - acc: 0.8993
Epoch 28/100
 - 0s - loss: 0.4876 - acc: 0.8876
Epoch 29/100
 - 0s - loss: 0.4387 - acc: 0.9044
Epoch 30/100
 - 0s - loss: 0.4488 - acc: 0.8876
Epoch 31/100
 - 0s - loss: 0.4452 - acc: 0.8842
Epoch 32/100
 - 0s - loss: 0.3789 - acc: 0.9111
Epoch 33/100
 - 0s - loss: 0.4094 - acc: 0.8842
Epoch 34/100
 - 0s - loss: 0.3656 - acc: 0.9128
Epoch 35/100
 - 0s - loss: 0.3641 - acc: 0.9094
Epoch 36/100
 - 0s - loss: 0.3332 - acc: 0.9077
Epoch 37/100
 - 0s - loss: 0.3849 - acc: 0.8859
Epoch 38/100
 - 0s - loss: 0.3259 - acc: 0.9077
Epoch 39/100
 - 0s - loss: 0.2815 - acc: 0.9195
Epoch 40/100
 - 0s - loss: 0.2825 - acc: 0.9111
Epoch 41/100
 - 0s - loss: 0.3067 - acc: 0.9094
Epoch 42/100
 - 0s - loss: 0.2866 - acc: 0.9228
Epoch 43/100
 - 0s - loss: 0.2940 - acc: 0.9060
Epoch 44/100
 - 0s - loss: 0.2176 - acc: 0.9346
Epoch 45/100
 - 0s - loss: 0.2725 - acc: 0.9228
Epoch 46/100
 - 0s - loss: 0.2636 - acc: 0.9228
Epoch 47/100
 - 0s - loss: 0.2135 - acc: 0.9379
Epoch 48/100
 - 0s - loss: 0.2766 - acc: 0.9094
Epoch 49/100
 - 0s - loss: 0.2624 - acc: 0.9178
Epoch 50/100
 - 0s - loss: 0.2636 - acc: 0.9128
Epoch 51/100
 - 0s - loss: 0.2327 - acc: 0.9195
Epoch 52/100
 - 0s - loss: 0.2444 - acc: 0.9111
Epoch 53/100
 - 0s - loss: 0.2395 - acc: 0.9161
Epoch 54/100
 - 0s - loss: 0.2318 - acc: 0.9178
Epoch 55/100
 - 0s - loss: 0.2449 - acc: 0.9111
Epoch 56/100
 - 0s - loss: 0.2400 - acc: 0.9195
Epoch 57/100
 - 0s - loss: 0.2241 - acc: 0.9279
Epoch 58/100
 - 0s - loss: 0.2089 - acc: 0.9279
Epoch 59/100
 - 0s - loss: 0.2036 - acc: 0.9329
Epoch 60/100
 - 0s - loss: 0.2201 - acc: 0.9262
Epoch 61/100
 - 0s - loss: 0.2062 - acc: 0.9279
Epoch 62/100
 - 0s - loss: 0.1992 - acc: 0.9329
Epoch 63/100
 - 0s - loss: 0.2380 - acc: 0.9245
Epoch 64/100
 - 0s - loss: 0.1648 - acc: 0.9446
Epoch 65/100
 - 0s - loss: 0.2257 - acc: 0.9161
Epoch 66/100
 - 0s - loss: 0.1902 - acc: 0.9295
Epoch 67/100
 - 0s - loss: 0.1827 - acc: 0.9396
Epoch 68/100
 - 0s - loss: 0.2290 - acc: 0.9094
Epoch 69/100
 - 0s - loss: 0.2366 - acc: 0.9111
Epoch 70/100
 - 0s - loss: 0.2843 - acc: 0.8909
Epoch 71/100
 - 0s - loss: 0.1823 - acc: 0.9279
Epoch 72/100
 - 0s - loss: 0.2327 - acc: 0.9111
Epoch 73/100
 - 0s - loss: 0.2347 - acc: 0.9128
Epoch 74/100
 - 0s - loss: 0.2162 - acc: 0.9228
Epoch 75/100
 - 0s - loss: 0.2036 - acc: 0.9295
Epoch 76/100
 - 0s - loss: 0.1435 - acc: 0.9480
Epoch 77/100
 - 0s - loss: 0.2128 - acc: 0.9211
Epoch 78/100
 - 0s - loss: 0.1438 - acc: 0.9497
Epoch 79/100
 - 0s - loss: 0.2105 - acc: 0.9211
Epoch 80/100
 - 0s - loss: 0.1999 - acc: 0.9228
Epoch 81/100
 - 0s - loss: 0.1826 - acc: 0.9312
Epoch 82/100
 - 0s - loss: 0.1714 - acc: 0.9379
Epoch 83/100
 - 0s - loss: 0.2164 - acc: 0.9161
Epoch 84/100
 - 0s - loss: 0.1952 - acc: 0.9295
Epoch 85/100
 - 0s - loss: 0.1977 - acc: 0.9195
Epoch 86/100
 - 0s - loss: 0.1906 - acc: 0.9262
Epoch 87/100
 - 0s - loss: 0.2155 - acc: 0.9128
Epoch 88/100
 - 0s - loss: 0.2287 - acc: 0.9111
Epoch 89/100
 - 0s - loss: 0.2107 - acc: 0.9228
Epoch 90/100
 - 0s - loss: 0.1512 - acc: 0.9430
Epoch 91/100
 - 0s - loss: 0.1959 - acc: 0.9295
Epoch 92/100
 - 0s - loss: 0.1840 - acc: 0.9312
Epoch 93/100
 - 0s - loss: 0.2070 - acc: 0.9211
Epoch 94/100
 - 0s - loss: 0.1983 - acc: 0.9279
Epoch 95/100
 - 0s - loss: 0.1872 - acc: 0.9329
Epoch 96/100
 - 0s - loss: 0.1887 - acc: 0.9379
Epoch 97/100
 - 0s - loss: 0.2107 - acc: 0.9295
Epoch 98/100
 - 0s - loss: 0.2194 - acc: 0.9245
Epoch 99/100
 - 0s - loss: 0.2040 - acc: 0.9178
Epoch 100/100
 - 0s - loss: 0.2144 - acc: 0.9228

2021-05-14 22:29:51 INFO     rasa.core.policies.keras_policy  - Done fitting keras policy model
2021-05-14 22:29:51 INFO     rasa.core.agent  - Model directory /tmp/tmph_owqdo9/core exists and contains old model files. All files will be overwritten.
2021-05-14 22:29:51 INFO     rasa.core.agent  - Persisted model to '/tmp/tmph_owqdo9/core'
Core model training completed.

Training NLU model...

/home/yurio/anaconda3/envs/rasa_16/lib/python3.7/site-packages/sklearn/feature_extraction/image.py:167: DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.

Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
  dtype=np.int):

2021-05-14 22:29:51 INFO     rasa.nlu.training_data.loading  - Training data format of /tmp/tmpky3p4h6y/d83cd0509268496f9744107856b9dcf5_nlu.md is md
2021-05-14 22:29:51 INFO     rasa.nlu.training_data.training_data  - Training data stats: 

	- intent examples: 693 (16 distinct intents)
	- Found intents: 'intent_berpisah', 'intent_minta_jadwal', 'intent_prediksi_cuaca', 'intent_confirm_kota', 'mood_baik', 'mood_tidak_senang', 'intent_menolak', 'intent_setuju', 'intent_jadwal_sholat', 'intent_minta_daftar_nilai', 'intent_confirm_nama_atau_nim', 'terima_kasih', 'intent_salam', 'intent_menyapa', 'intent_minta_jadwal_saja', 'menantang_bot'

	- entity examples: 645 (4 distinct entities)
	- found entities: 'kota', 'nama', 'konsentrasi', 'NIM'

2021-05-14 22:29:51 DEBUG    rasa.nlu.training_data.training_data  - Validating training data...
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Starting to train component WhitespaceTokenizer
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Finished training component.
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Starting to train component RegexFeaturizer
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Finished training component.
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Starting to train component CRFEntityExtractor
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Finished training component.
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Starting to train component EntitySynonymMapper
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Finished training component.
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Starting to train component CountVectorsFeaturizer
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Finished training component.
2021-05-14 22:29:51 INFO     rasa.nlu.model  - Starting to train component EmbeddingIntentClassifier
2021-05-14 22:29:51 DEBUG    rasa.nlu.classifiers.embedding_intent_classifier  - Check if num_neg 20 is smaller than number of intents 16, else set num_neg to the number of intents - 1
2021-05-14 22:29:52 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Accuracy is updated every 10 epochs

Epochs: 100%|█████████| 300/300 [00:10<00:00, 27.80it/s, loss=0.018, acc=0.999]

2021-05-14 22:30:02 INFO     rasa.nlu.classifiers.embedding_intent_classifier  - Finished training embedding classifier, loss=0.018, train accuracy=0.999
2021-05-14 22:30:02 INFO     rasa.nlu.model  - Finished training component.
2021-05-14 22:30:03 INFO     rasa.nlu.model  - Successfully saved model into '/tmp/tmph_owqdo9/nlu'

NLU model training completed.
Your Rasa model is trained and saved at '/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210514-223003.tar.gz'.



```