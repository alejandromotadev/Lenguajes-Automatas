from automata.fa.dfa import DFA
import string

num_states = 72
statesaH = []
alphabet = []
low_alphabet = []
symbols = [chr(32),chr(33),chr(34),chr(35),chr(36),chr(37),chr(38),chr(39),chr(40),chr(41),chr(42),chr(43),chr(44),chr(45),chr(46),chr(47),chr(48),chr(49),chr(50),chr(51),chr(52),chr(53),chr(54),chr(55),chr(56),chr(57),chr(58),chr(59),chr(60),chr(61),chr(62),chr(63),chr(64),chr(91),chr(92),chr(93),chr(94),chr(95),chr(96),chr(123),chr(124), chr(125), chr(126)] #todos los simbolos

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
    
for c in string.ascii_lowercase:
    low_alphabet.append(c)
    
dfaDb = DFA(
    states = set(statesaH),
    input_symbols=alphabet+symbols,
    transitions = {
        'q0': {'D': 'q1'},
        'q1': {'A': 'q2'},
        'q2': {'T': 'q3'},
        'q3': {'A': 'q4'},
        'q4': {'B': 'q5'},
        'q5': {'A': 'q6'},
        'q6': {'S': 'q12'},
        'q7': {'E': 'q8'},
        'q8': {'S': 'q9'},
        'q9': {' ': 'q9', '=': 'q10'},
        'q10': {' ': 'q10', '{': 'q11'},
        'q11': {'"': 'q12', "'": 'q12'},
        'q12': {'d': 'q13'},
        'q13': {'e': 'q14'},
        'q14': {'f': 'q15'},
        'q15': {'a': 'q16'},
        'q16': {'u': 'q17'},
        'q17': {'l': 'q18'},
        'q18': {'t': 'q19'},
        'q19': {'"': 'q20', "'": 'q20'},
        'q20': {':': 'q21', ' ': 'q20'},
        'q21': {' ': 'q21', '{': 'q22'},
        'q22': {' ': 'q22', '"': 'q23', "'": 'q23'},  
        'q23': {'E': 'q24', 'N': 'q33', 'U': 'q39', 'P': 'q45', 'H': 'q60'},  
        'q24': {'N': 'q25'},  
        'q25': {'G': 'q26'},  
        'q26': {'I': 'q27'},  
        'q27': {'N': 'q28'},  
        'q28': {'E': 'q29'},     
        'q29': {' ': 'q29', ':': 'q30'},  
        'q30': {' ': 'q30', '"': 'q31', "'": 'q31'},  
        'q31': dict({'.': 'q31', '"': 'q32', "'": 'q32'},**createDict(low_alphabet, 'q31')),   
        'q32': {'}': 'q70'},  
        'q33': {'A': 'q34'},  
        'q34': {'M': 'q35'},  
        'q35': {'E': 'q36'},  
        'q36': {':': 'q37', ' ': 'q36'},  
        'q37': {'"': 'q38',"'": 'q38', ' ': 'q37'},  
        'q38': dict({'"': 'q32', "'": 'q32'},**createDict(alphabet, 'q38')),  
        'q39': {'S': 'q40'},  
        'q40': {'E': 'q41'},  
        'q41': {'R': 'q42'}, 
        'q42': {' ': 'q42', ':': 'q43'},  
        'q43': {' ': 'q43', '"': 'q44', "'": 'q44'},  
        'q44': dict({'"': 'q32', "'": 'q32'},**createDict(symbols, 'q44'),**createDict(alphabet, 'q44')), 
        'q45': {'A': 'q46', 'O': 'q55'}, 
        'q46': {'S': 'q47'},
        'q47': {'S': 'q48'},
        'q48': {'W': 'q49'},
        'q49': {'O': 'q50'},
        'q50': {'R': 'q51'},
        'q51': {'D': 'q52'},
        'q52': {':': 'q53', ' ': 'q52'},
        'q53': {' ': 'q53', '"': 'q54', "'": 'q54'},
        'q54': dict({"'": 'q32', '"': 'q32'}, **createDict(symbols, 'q54'),**createDict(alphabet, 'q54')),
        'q55': {'R': 'q56'},
        'q56': {'T': 'q57'},
        'q57': {' ': 'q57', ':': 'q58'},
        'q58': {'"': 'q59', "'": 'q59', ' ': 'q58'},
        'q59': {"'": 'q32', '"': 'q32', '0': 'q59','1': 'q59','2': 'q59','3': 'q59','4': 'q59','5': 'q59','6': 'q59','7': 'q59','8': 'q59','9': 'q59'},
        'q60': {'O': 'q61'},
        'q61': {'S': 'q62'},
        'q62': {'T': 'q63'},
        'q63': {' ': 'q63', ':': 'q64'},
        'q64': {' ': 'q64', "'": 'q65', '"': 'q65'},
        'q65': dict({'0': 'q68','1': 'q68','2': 'q68','3': 'q68','4': 'q68','5': 'q68','6': 'q68','7': 'q68','8': 'q68','9': 'q68'},**createDict(alphabet, 'q66')),
        'q66': {'.': 'q67'},
        'q67': dict({'.': 'q67', '"': 'q32', "'": 'q32'},**createDict(alphabet, 'q67')),
        'q68': {'.': 'q69'},
        'q69': {'"': 'q32',"'": 'q32', '0': 'q69','1': 'q69','2': 'q69','3': 'q69','4': 'q69','5': 'q69','6': 'q69','7': 'q69','8': 'q69','9': 'q69', '.': 'q69'},
        'q70': {'}': 'q71'},
    },
    initial_state='q0',
    final_states={'q71'},
    allow_partial=True, 
)