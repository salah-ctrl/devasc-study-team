from test_data import *

def json_search(key, input_object):
    """Return a list of {key: value} matches found anywhere in a nested JSON-like object."""
    results = []

    def walk(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    results.append({k: v})
                # Recurse into the value (dict/list wordt verder afgevangen)
                walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)
        # scalars (str, int, float, bool, None) worden genegeerd

    walk(input_object)
    return results

