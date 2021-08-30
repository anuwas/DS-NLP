import nltk
# from nltk.tokenize import word_tokenize #this is required for work tokenizer
# from nltk.tokenize import TreebankWordTokenizer
# from nltk.tokenize import TweetTokenizer

# Example of work tokenizer
text="Let me know your mobile#, if that's fine. The call rate is 1.2p/s 😊."
print (nltk.tokenize.word_tokenize(text))

# output - ['Let', 'me', 'know', 'your', 'mobile', '#', ',', 'if', 'that', "'s", 'fine', '.', 'The', 'call', 'rate', 'is', '1.2p/s', '😊', '.']

# Example of sent tokenizer
print (nltk.tokenize.sent_tokenize(text))

#Output - ["Let me know your mobile#, if that's fine.", 'The call rate is 1.2p/s 😊.']

# Punctuation based tokenizer

print(nltk.wordpunct_tokenize(text))

# Output ['Let', 'me', 'know', 'your', 'mobile', '#,', 'if', 'that', "'", 's', 'fine', '.', 'The', 'call', 'rate', 'is', '1', '.', '2p', '/', 's', '😊.']

# Treebankword tokenizer

print(nltk.TreebankWordTokenizer().tokenize(text))

# Output ['Let', 'me', 'know', 'your', 'mobile', '#', ',', 'if', 'that', "'s", 'fine.', 'The', 'call', 'rate', 'is', '1.2p/s', '😊', '.']

# Tweet Tokenizer

print(nltk.TweetTokenizer().tokenize(text))

# Output ['Let', 'me', 'know', 'your', 'mobile', '#', ',', 'if', "that's", 'fine', '.', 'The', 'call', 'rate', 'is', '1.2', 'p', '/', 's', '😊', '.']



