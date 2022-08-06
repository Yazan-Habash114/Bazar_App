from flask_application import app

# Define the Cache claskk
class Cache:
    # Cache Obj:
    # { Tag, Value }
    # { Tag: id (info) or topic (search), Value: SearchEntry obj if search, book as json }
    def __init__(self, max_size: int = 3):   # Default size is three
        self.cache = {}
        self.lru_Q = []
        self.max_size = max_size

    # Insert item
    def insert(self, tag, data):
        # If the item exists, remove it firstly
        if tag in self:
            self.cache.pop(tag)
            self.lru_Q.remove(tag)

        # If cache is full, pop least recently used item
        if len(self.cache) >= self.max_size:
            remove_book_id = self.lru_Q.pop(0)
            self.cache.pop(remove_book_id)

        # Insert the item
        self.cache[tag] = data
        self.lru_Q.append(tag)
        

    # Get item from cache
    def get(self, tag):
        # If item is not in cache, return None
        if tag not in self.cache:
            return None

        # Transferring item to the front of the LRU Q
        self.lru_Q.remove(tag)
        self.lru_Q.append(tag)

        # Return item from cache
        return self.cache[tag]

    # Remove item from cache
    def remove(self, tag):
        if tag in self.cache:
            self.cache.pop(tag)
            self.lru_Q.remove(tag)

    # Clear all entries from cache
    def clear(self):
        self.cache.clear()
        self.lru_Q.clear()

    # Get all keys of cached items
    def all_tags(self):
        return list(self.lru_Q)

    # Check if tag exists in cache
    def __contains__(self, tag):
        return tag in self.cache


# Define class for search entry
class SearchEntry:
    def __init__(self, search_result):
        # Set of topics stored in this entry
        # This is to invalidate the topic when necessary
        self.topics = set([book['topic'] for book in search_result])

        # Assign the parameter to class attribute
        self.search_result = search_result
        
        print('\nSearch entry:\n', self.topics, self.search_result, '\n')

    def __contains__(self, item):
        return item in self.topics


lookup_cache = Cache()
search_cache = Cache(max_size=10)

