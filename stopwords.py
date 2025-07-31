# import the nltk library
import nltk

# desde nltk descargar el paquete de stopwords
nltk.download('stopwords')

# importar las stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('spanish')

#imprimir las stopwords
print(lista_stopwords)
