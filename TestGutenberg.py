from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
# text = strip_headers(load_etext(2701)).strip()
# print(text)

# gutenberg.acquire.text 2701 moby-raw.txt
# gutenberg.cleanup.strip_headers moby-raw.txt moby-clean.txt

from gutenberg.query import get_etexts
from gutenberg.query import get_metadata

print(get_metadata('title', 2701))
print(get_metadata('author', 2701))

print(get_etexts('title', 'Moby Dick; Or, The Whale'))
print(get_etexts('author', 'Melville, Hermann'))  

from gutenberg.query import list_supported_metadatas

print(list_supported_metadatas())