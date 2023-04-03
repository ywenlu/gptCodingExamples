import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding

class NER_SPACYModel:
    def __init__(self):
        self.nlp = spacy.blank("en")
        self.ner = self.nlp.add_pipe("ner")
        self.ner.add_label("NAME")
        self.ner.add_label("DOB")
        self.ner.add_label("ADDRESS")
        self.optimizer = self.nlp.begin_training()
        self.train_data = [
            ("John Smith was born on 01/01/1990 and lives at 123 Main St.", {"entities": [(0, 10, "NAME"), (24, 34, "DOB"), (43, 57, "ADDRESS")]}),
            ("Jane Doe lives at 456 Oak Ave and was born on 02/02/1980.", {"entities": [(0, 8, "NAME"), (38, 48, "DOB"), (16, 28, "ADDRESS")]}),
            ("Mary Johnson was born on 03/03/1970 and lives at 789 Maple Rd.", {"entities": [(0, 13, "NAME"), (27, 37, "DOB"), (43, 56, "ADDRESS")]}),
        ]
        self.n_iter = 10

    def train(self):
        for i in range(self.n_iter):
            losses = {}
            batches = minibatch(self.train_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                examples = []
                for i in range(len(texts)):
                    examples.append(Example.from_dict(self.nlp.make_doc(texts[i]), annotations[i]))
                self.nlp.update(examples, sgd=self.optimizer, losses=losses)
            print(losses)

    def predict(self, text):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

model = NER_SPACYModel()
model.train()
print(model.predict("John Smith was born on 01/01/1990 and lives at 123 Main St."))



import transformers
from transformers import pipeline

class NER_Huggingface_Model:
    def __init__(self):
        self.nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", tokenizer="dbmdz/bert-large-cased-finetuned-conll03-english")      
        self.train_data = [
            ("John Smith was born on 01/01/1990 and lives at 123 Main St.", {"entities": [(0, 10, "PER"), (24, 34, "DATE"), (43, 57, "LOC")]}),
            ("Jane Doe lives at 456 Oak Ave and was born on 02/02/1980.", {"entities": [(0, 8, "PER"), (38, 48, "DATE"), (16, 28, "LOC")]}),
            ("Mary Johnson was born on 03/03/1970 and lives at 789 Maple Rd.", {"entities": [(0, 13, "PER"), (27, 37, "DATE"), (43, 56, "LOC")]}),
        ]
        self.n_iter = 10

    def train(self):
        for i in range(self.n_iter):
            examples = []
            for j in range(len(self.train_data)):
                example = {}
                example['text'] = self.train_data[j][0]
                example['label'] = []
                for k in range(len(self.train_data[j][1]['entities'])):
                    label = {}
                    label['start'] = self.train_data[j][1]['entities'][k][0]
                    label['end'] = self.train_data[j][1]['entities'][k][1]
                    label['entity'] = self.train_data[j][1]['entities'][k][2]
                    example['label'].append(label)
                examples.append(example)
            self.nlp.train(examples)

    def predict(self, text):
        return self.nlp(text)

model = NER_Huggingface_Model()
model.train()
print(model.predict("John Smith was born on 01/01/1990 and lives at 123 Main St."))


train_data = [
    ("Jean Dupont est né le 01/01/1990 et habite au 123 rue principale.", {"entities": [(0, 10, "NAME"), (18, 28, "DOB"), (37, 56, "ADDRESS")]}),
    ("Marie Martin habite au 456 avenue des chênes et est née le 02/02/1980.", {"entities": [(0, 12, "NAME"), (47, 57, "DOB"), (16, 39, "ADDRESS")]}),
    ("Lucie Dubois est née le 03/03/1970 et habite au 789 chemin des érables.", {"entities": [(0, 11, "NAME"), (25, 35, "DOB"), (37, 62, "ADDRESS")]}),
    ("Pierre Durand habite au 12 rue de la paix et est né le 04/04/1960.", {"entities": [(0, 12, "NAME"), (44, 54, "DOB"), (16, 30, "ADDRESS")]}),
    ("Sophie Girard est née le 05/05/1950 et habite au 34 avenue des lilas.", {"entities": [(0, 12, "NAME"), (18, 28, "DOB"), (37, 56, "ADDRESS")]}),
    ("Antoine Moreau habite au 67 rue de la liberté et est né le 06/06/1940.", {"entities": [(0, 14, "NAME"), (44, 54, "DOB"), (16, 35, "ADDRESS")]}),
    ("Céline Lefebvre est née le 07/07/1930 et habite au 89 rue de la gare.", {"entities": [(0, 14, "NAME"), (18, 28, "DOB"), (37, 52, "ADDRESS")]}),
    ("François Dupuis habite au 123 avenue des roses et est né le 08/08/1920.", {"entities": [(0, 14, "NAME"), (44, 54, "DOB"), (16, 39, "ADDRESS")]}),
]
test_data = [
    ("Julie Dupont habite au 123 rue principale.", {"entities": [(0, 11, "NAME"), (18, 33, "ADDRESS")]}),
    ("Lucie Martin est née le 02/02/1980.", {"entities": [(0, 12, "NAME"), (16, 26, "DOB")]}),
    ("Jeanne Dubois habite au 789 chemin des érables.", {"entities": [(0, 12, "NAME"), (18, 43, "ADDRESS")]}),
    ("Pierre Durand est né le 04/04/1960.", {"entities": [(0, 12, "NAME"), (16, 26, "DOB")]}),
    ("Sophie Girard habite au 34 avenue des lilas.", {"entities": [(0, 12, "NAME"), (18, 33, "ADDRESS")]}),
    ("Antoine Moreau est né le 06/06/1940.", {"entities": [(0, 14, "NAME"), (18, 28, "DOB")]}),
    ("Céline Lefebvre habite au 89 rue de la gare.", {"entities": [(0, 14, "NAME"), (18, 33, "ADDRESS")]}),
    ("François Dupuis est né le 08/08/1920.", {"entities": [(0, 14, "NAME"), (16, 26, "DOB")]}),
]



