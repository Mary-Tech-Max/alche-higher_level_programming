#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_value = None

    for key in a_dictionary:
        if best_value is None or a_dictionary[key] > best_value:
            best_key = key
            best_value = a_dictionary[key]

    return best_key
