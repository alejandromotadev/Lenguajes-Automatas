from automata.fa.dfa import DFA

num_states = 15
statesDb = []
alfabet = ['D','E','B','U','G','T','r','u','e','F','a','l','s']
simbolos = [chr(32),chr(61)] #{' ', =}

for i in range(num_states):
    state = 'q'+str(i)
    statesDb.append(state)
    
dfaDbg = DFA(
    states = set(statesDb),
    input_symbols=alfabet+simbolos,
    transitions = {
        'q0': {'D': 'q1'},
        'q1': {'E': 'q2', 'A': 'q13'},
        'q2': {'B': 'q3'},
        'q3': {'U': 'q4'},
        'q4': {'G': 'q5'},
        'q5': {'=': 'q6', ' ': 'q5'},
        'q6': {'T': 'q7', 'F': 'q10', ' ': 'q6'},
        'q7': {'r': 'q8'},
        'q8': {'u': 'q9'},
        'q9': {'e': 'q0'},
        'q10': {'a': 'q11'},
        'q11': {'l': 'q12'},
        'q12': {'s': 'q9'}, 
        'q13': {'T': 'q14'},
        'q14': {'A': 'q15'},
        'q15': {'B': 'q16'},
        'q16': {'A': 'q17'},
        'q17': {'S': 'q18'},
        'q18': {'E': 'q19'},
        'q19': {'S': 'q20'},
        'q20': {' ': 'q20', '=': 'q21'},
        'q21': {' ': 'q21', '{': 'q22'},
        'q22': {"'": 'q23'},
        'q23': {'d': 'q24'},
        'q197': {'e': 'q198'},
        'q198': {'f': 'q199'},
        'q199': {'a': 'q200'},
        'q200': {'u': 'q24'},
        'q24': {'l': 'q25'},
        'q25': {'t': 'q26'},
        'q26': {"'": 'q27'},
        'q27': {' ': 'q27', ':': 'q28'},
         
    },
    initial_state='q0',
    final_states={'q0'},
    allow_partial = True
) 
