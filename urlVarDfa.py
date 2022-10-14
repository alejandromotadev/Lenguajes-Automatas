from automata.fa.dfa import DFA
import string
num_states = 47
statesaH = []
alphabet = []
symbols = [chr(32),chr(34),chr(39),chr(40),chr(41),chr(42),chr(46),chr(47),chr(44),chr(61),chr(91),chr(93),chr(95)] #space, "", ', ',', =, [, ],_,(,)
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
    
dfaURL = DFA(
    states = set(statesaH),
    input_symbols=alphabet+symbols,
    transitions = {
        'q0': {'M': 'q1', 'S': 'q7'},
        'q1': {'E': 'q2'},
        'q2': {'D': 'q3'},
        'q3': {'I': 'q4'},
        'q4': {'A': 'q5'},
        'q5': {'_': 'q6', ' ': 'q5'},
        'q6': {'U': 'q12', ' ': 'q6', 'R': 'q14'},
        'q7': {'T': 'q8'},
        'q8': {'A': 'q9'},
        'q9': {'T': 'q10'},
        'q10': {'I': 'q11'},
        'q11': {'C': 'q5'},
        'q12': {'R': 'q13'},
        'q13': {'L': 'q43'},
        'q14': {'O': 'q15'},
        'q15': {'O': 'q16'},
        'q16': {'T': 'q17'},
        'q17': {' ': 'q17', '=': 'q18'},
        'q18': {' ': 'q18', 'o': 'q19'},
        'q19': {'s': 'q20'},
        'q20': {'.': 'q21'},
        'q21': {'p': 'q22'},
        'q22': {'a': 'q23'},  
        'q23': {'t': 'q24'},  
        'q24': {'h': 'q25'},  
        'q25': {'.': 'q26'},  
        'q26': {'j': 'q27'},  
        'q27': {'o': 'q28'},  
        'q28': {'i': 'q29'},     
        'q29': {'n': 'q30'},  
        'q30': {'(': 'q31'},  
        'q31': {'B': 'q32'},   
        'q32': {'A': 'q33'},  
        'q33': {'S': 'q34'},  
        'q34': {'E': 'q35'},  
        'q35': {'_': 'q36'},  
        'q36': {'D': 'q37'},  
        'q37': {'I': 'q38'},  
        'q38': {'R': 'q39'},  
        'q39': {',': 'q40'},  
        'q40': {' ': 'q40', '"': 'q41', "'": 'q41'},  
        'q41': dict({'/': 'q41', '"': 'q42', "'": 'q42'},**createDict(alphabet,'q41')),  
        'q42': {')': 'q46'},  
        'q43': {' ': 'q43', '=': 'q44'},  
        'q44': {' ': 'q44', '"': 'q45', "'": 'q45'},  
        'q45': dict({'/': 'q45', '"': 'q46', "'": 'q46'},**createDict(alphabet,'q45')),  
        'q46': {}
    },
    initial_state='q0',
    final_states={'q46'},
    allow_partial=True, 
)