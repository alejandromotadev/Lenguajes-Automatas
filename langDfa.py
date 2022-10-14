from automata.fa.dfa import DFA
import string
num_states = 18
statesLg = []
alphabet = ['L','A','N','G','U','E','C','O','D']
low_alphabet = []
simbolos = [chr(95),chr(32),chr(45),chr(61),chr(39),chr(34)] 

def createDict(list,value): 
    myDict = dict()
    for c in list:
        myDict[c] = value
    return myDict 
    
for i in range(num_states):
    state = 'q'+str(i)
    statesLg.append(state)
    
for c in string.ascii_lowercase:  
    low_alphabet.append(c)


for i in range(num_states):
    state = 'q'+str(i)
    statesLg.append(state)
    
dfaLg = DFA(
    states = set(statesLg),
    input_symbols=alphabet+simbolos+low_alphabet,
    transitions = {
        'q0': {'L': 'q1'},
        'q1': {'A': 'q2'},
        'q2': {'N': 'q3'},
        'q3': {'G': 'q4'},
        'q4': {'U': 'q5'},
        'q5': {'A': 'q6'},
        'q6': {'G': 'q7'},
        'q7': {'E': 'q8'},
        'q8': {'_': 'q9'},
        'q9': {'C': 'q10'},
        'q10': {'O': 'q11'},
        'q11': {'D': 'q12'},
        'q12': {'E': 'q13'},
        'q13': {' ': 'q13', '=': 'q14'},
        'q14': {' ': 'q14', '"': 'q15', "'": 'q15'},  
        'q15': dict({'-': 'q16'},**createDict(low_alphabet,'q15')),   
        'q16': dict({'"': 'q17', "'": 'q17'},**createDict(low_alphabet,'q16')), 
    },
    initial_state='q0',
    final_states={'q17'},
    allow_partial = True
)  