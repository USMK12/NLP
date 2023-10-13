from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
text="he came.he played.he went to home ,because he want to go school tomorrow "
st=set(stopwords.words('english'))
words=word_tokenize(text)
fil=[word for word in words if word.casefold() not in st]
print(fil)