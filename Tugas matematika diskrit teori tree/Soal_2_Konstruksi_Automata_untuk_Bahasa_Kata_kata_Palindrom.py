# Definisi state dan transisi
states = {0, 1, 2, 3, 4, 5, 6, 7, 8}
accept_states = {0, 1, 2, 3, 4, 5, 6}
start_state = 0
transitions = {
    0: {'a': 1, 'b': 2},
    1: {'a': 3, 'b': 7},
    2: {'a': 8, 'b': 4},
    7: {'a': 5},
    8: {'b': 6},
}

def dfa_accepts(string):
    current_state = start_state
    for symbol in string:
        if current_state in transitions and symbol in transitions[current_state]:
            current_state = transitions[current_state][symbol]
        else:
            return False
    return current_state in accept_states

# Pengujian DFA dengan beberapa string
test_strings = ["", "a", "b", "aa", "bb", "aba", "bab", "ab", "ba", "abb"]
results = {string: dfa_accepts(string) for string in test_strings}

print("Hasil pengujian DFA:")
for string, result in results.items():
    print(f"String '{string}' diterima? {result}")
