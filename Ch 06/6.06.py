# Однопоточная подель MapReduce

import functools
from typing import Dict


def map_frequency(text: str) -> Dict[str, int]:
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merge = first
    for key in second:
        merge[key] = merge[key] + second[key] if key in merge else second[key]
    return merge


lines = ["I know what I know",
         "I know that I know",
         "I don't know much",
         "They don't know much"]

mapped_results = [map_frequency(line) for line in lines]

for result in mapped_results:
    print(result)

print(functools.reduce(merge_dictionaries, mapped_results))
