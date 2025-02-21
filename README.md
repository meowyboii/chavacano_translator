---
metrics:
- bleu
base_model:
- facebook/mbart-large-50-many-to-many-mmt
pipeline_tag: translation
library_name: transformers
license: apache-2.0
---
# English-Chavacano Translator
This model is `mbart-large-50-many-to-many-mmt` model fine-tuned on English to Zamboanga Chavacano sentences from our own corpus.
Chavacano is a Spanish creole, and Zamboanga Chavacano is the most widely spoken Chavacano variety in the Philippines.
This translation model aims to leverage the relatedness of Chavacano to Spanish, Tagalog, and other Romance languages through transfer learning to create an English-Zamboanga Chavacano translation model.

The training set contains 5203 sentence, validation set contains 650 sentences, while test set contains 651 sentences. Each sentence is composed of 2-20 words.

The BLEU score of this model on the validation set is 36.37 and 37.74 on the test set.
```
batch_size = 16
num_train_epochs = 4
learning_rate=2e-4
gradient_accumulation_steps=4
weight_decay=0.01
warmup_steps=500
adam_epsilon=1e-8
max_grad_norm=1.0
fp16=True
```

### Additional Info
* Source Language: English 
* Target Language: Zamboanga Chavacano
* BLEU Score: 37.74
* Brevity Penalty: 0.976
* Reference Length: 5323
* Hypothesis Length: 5198
