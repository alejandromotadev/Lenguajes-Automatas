from dfa  import DFA

num_states = 15
statesDb = []
alfabet = ['D','E','B','U','G','T','r','u','e','F','a','l','s']
simbolos = [chr(32),chr(61)] #{' ', =}

for i in range(num_states):
    state = 'q'+str(i)
    statesDb.append(state)
    
dfa = DFA(
    states = set(statesDb),
    transitions = {
        'q0': {'D': 'q1'},
        'q1': {'E': 'q2'},
        'q2': {'B': 'q3'},
        'q3': {'U': 'q4'},
        'q4': {'G': 'q5'},
        'q5': {'=': 'q6', ' ': 'q5'},
        'q6': {'T': 'q7', 'F': 'q10', ' ': 'q6'},
        'q7': {'r': 'q8'},
        'q8': {'u': 'q9'},
        'q9': {'e': 'q14'},
        'q10': {'a': 'q11'},
        'q11': {'l': 'q12'},
        'q12': {'s': 'q13'},
        'q13': {'e': 'q14'}   
    },
    start  = 'q0',
    end  = 'q14',
    allow_partial = True
)  

