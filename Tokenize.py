from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# Prepare a tokenizer on training data
x_tokenizer = Tokenizer()
x_tokenizer.fit_on_texts(list(x_train))
threshold = 2
cnt_infrequent = 0
total_cnt = 0
for key, value in x_tokenizer.word_counts.items():
    total_cnt = total_cnt + 1
    if value < threshold:
       cnt_infrequent = cnt_infrequent + 1
print("% of not frequent words in vocabulary: ", (cnt_infrequent / total_cnt) * 100)
# Remove the infrequent words
x_tokenizer = Tokenizer(num_words = total_cnt - cnt_infrequent)
x_tokenizer.fit_on_texts(list(x_train))
# Convert the code sequences to integer sequences (integer numbers ranging from 1 to the maximum vocab sizes)
x_train_seqs = x_tokenizer.texts_to_sequences(x_train)
x_validation_seqs = x_tokenizer.texts_to_sequences(x_validation)
# printing the integer sequences
print (x_train_seqs)

# Pad zero upto maximum length
x_train = pad_sequences(x_train_seqs,  maxlen=max_code_len, padding='post')
x_validation = pad_sequences(x_validation_seqs, maxlen=max_code_len, padding='post')
# Size of vocabulary (+1 for padding token)
x_voc = x_tokenizer.num_words + 1
print("Size of vocabulary in X = {}".format(x_voc))

y_tokenizer = Tokenizer()
y_tokenizer.fit_on_texts(list(y_train))
threshold = 2
cnt_infrequent = 0
total_cnt = 0
for key, value in y_tokenizer.word_counts.items():
    total_cnt = total_cnt + 1
    if value < threshold:
        cnt_infrequent = cnt_infrequent + 1
y_tokenizer = Tokenizer(num_words = total_cnt - cnt_infrequent)
y_tokenizer.fit_on_texts(list(y_train))
y_train_seqs = y_tokenizer.texts_to_sequences(y_train)
y_validation_seqs = y_tokenizer.texts_to_sequences(y_validation)
y_train = pad_sequences(y_train_seqs,  maxlen=max_summary_len, padding='post')
y_validation = pad_sequences(y_validation_seqs, maxlen=max_summary_len, padding='post')
y_voc = y_tokenizer.num_words + 1
print("Size of vocabulary in Y = {}".format(y_voc))


print(len(x_train))
print(len(y_train))
print(len(x_validation))
print(len(y_validation))

# vocab sizes for x and y are 356 ans 105, hence highest integer value would be less than that. Also the maximum lengths of x and y are different
print((x_train[0]))
print((y_train[0]))
