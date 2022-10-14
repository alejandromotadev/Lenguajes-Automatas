import string
from automata.fa.dfa import DFA

num_states = 23
statesaH = []
alphabet = []
symbols = [chr(48),chr(49),chr(50),chr(51),chr(52),chr(53),chr(54),chr(55),chr(56),chr(57),chr(32),chr(34),chr(39),chr(42),chr(46),chr(44),chr(61),chr(91),chr(93),chr(95)] #0,1,2,3,4,5,6,7,8,9 space, "", ', ',', =, [, ],_,* 
def createDict(list,value): 
    myDict = dict()
    for c in list:
        myDict[c] = value
    return myDict 
    
for i in range(num_states):
    state = 'q'+str(i)
    statesaH.append(state)
    
for c in string.ascii_letters:  
    alphabet.append(c)
    
dfaAh = DFA(
    states = set(statesaH),
    input_symbols=alphabet+symbols,
    transitions = {
        'q0': {'A': 'q1'},
        'q1': {'L': 'q2'},
        'q2': {'L': 'q3'},
        'q3': {'O': 'q4'},
        'q4': {'W': 'q5'},
        'q5': {'E': 'q6'},
        'q6': {'D': 'q7'},
        'q7': {'_': 'q8'},
        'q8': {'H': 'q9'},
        'q9': {'O': 'q10'},
        'q10': {'S': 'q11'},
        'q11': {'T': 'q12'},
        'q12': {'S': 'q13'},
        'q13': {'=': 'q14', ' ': 'q13'},
        'q14': {'[': 'q15', ' ': 'q14'},
        'q15': {'"': 'q16', "'": 'q16', ' ': 'q15', '*': 'q19', ']': 'q22'},
        'q16': dict({'0': 'q20','1': 'q20','2': 'q20','3': 'q20','4': 'q20','5': 'q20','6': 'q20','7': 'q20','8': 'q20','9': 'q20'},**createDict(alphabet,'q17')),
        'q17': {'.': 'q18'},
        'q18': dict({'.': 'q18', '"': 'q19', "'": 'q19'},**createDict(alphabet,'q18')),
        'q19': {']': 'q22'},
        'q20': {'.': 'q21'},
        'q21': {'"': 'q19',"'": 'q19', '.': 'q21','0': 'q21','1': 'q21','2': 'q21','3': 'q21','4': 'q21','5': 'q21','6': 'q21','7': 'q21','8': 'q21','9': 'q21'}
    },
    initial_state='q0',
    final_states={'q22'},
    allow_partial=True, 
)