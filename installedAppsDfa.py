from automata.fa.dfa import DFA
import string
num_states = 20
states_iA = []
alphabet = []
symbols = [chr(32),chr(34),chr(39),chr(46),chr(44),chr(61),chr(91),chr(93),chr(95)] #space, "", ', ',', =, [, ],_ 

def createDict(list,value): 
    myDict = dict()
    for c in list:
        myDict[c] = value
    return myDict 
    
for i in range(num_states):
    state = 'q'+str(i)
    states_iA.append(state)
    
for c in string.ascii_letters:  
    alphabet.append(c)

def declaracionDFA():  
    dfaIA = DFA(
        states = set(states_iA),
        input_symbols=alphabet+symbols,
        transitions = {
            'q0': {'I': 'q1'},
            'q1': {'N': 'q2'},
            'q2': {'S': 'q3'},
            'q3': {'T': 'q4'},
            'q4': {'A': 'q5'},
            'q5': {'L': 'q6'},
            'q6': {'L': 'q7'},
            'q7': {'E': 'q8'},
            'q8': {'D': 'q9'},
            'q9': {'_': 'q10'},
            'q10': {'A': 'q11'},
            'q11': {'P': 'q12'},
            'q12': {'P': 'q13'},
            'q13': {'S': 'q14'},
            'q14': {'=': 'q15', ' ': 'q14'},
            'q15': {'[': 'q16', ' ': 'q15'},
            'q16': {' ': 'q16', "'": 'q17','"': 'q17'},
            'q17': dict({'.': 'q17', '_': 'q17', "'": 'q18', '"': 'q18'},**createDict(alphabet,'q17')),
            'q18': {' ': 'q18', ',': 'q16', ']': 'q19'}
            
        },
        initial_state='q0',
        final_states={'q19'},
        allow_partial=True, 
    )
    return dfaIA