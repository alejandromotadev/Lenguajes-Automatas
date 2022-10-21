from automata.fa.dfa import DFA
import string

num_states = 201
statesaH = []
alphabet = []
low_alphabet = []
symbols = [chr(34),chr(39),chr(32),chr(33),chr(35),chr(36),chr(37),chr(38),chr(40),chr(41),chr(42),chr(43),chr(44),chr(45),chr(46),chr(47),chr(48),chr(49),chr(50),chr(51),chr(52),chr(53),chr(54),chr(55),chr(56),chr(57),chr(58),chr(59),chr(60),chr(61),chr(62),chr(63),chr(64),chr(91),chr(92),chr(93),chr(94),chr(95),chr(96),chr(123),chr(124), chr(125), chr(126)] #todos los simbolos

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
    
dfaDbg = DFA(
    states = set(statesaH),
        input_symbols=alphabet+symbols+low_alphabet,
    transitions = {
        'q0': {'D': 'q1', 'I': 'q85'},
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
        'q28': {' ': 'q28', '{': 'q29'},
        'q29': {' ': 'q29', "'": 'q30'},
        'q30': {'E': 'q31', 'N': 'q40', 'U': 'q47', 'P': 'q54', 'H': 'q71'},
        'q31': {'N': 'q32'},
        'q32': {'G': 'q33'},
        'q33': {'I': 'q34'},
        'q34': {'N': 'q35'},
        'q35': {'E': 'q36'},
        'q36': {' ': 'q36', "'": 'q37'},
        'q37': {':': 'q38'},
        'q38': {' ': 'q38', "'": 'q39'},
        'q39': dict({'.': 'q39', "'": 'q82','0': 'q39','1': 'q39','2': 'q39','3': 'q39','4': 'q39','5': 'q39','6': 'q39','7': 'q39','8': 'q39','9': 'q39'},**createDict(low_alphabet, 'q39')),   
        'q40': {'A': 'q41'},
        'q41': {'M': 'q42'},
        'q42': {'E': 'q43'},
        'q43': {' ': 'q43', "'": 'q44'},      
        'q44': {':': 'q45'},
        'q45': {' ': 'q45', "'": 'q46'},
        'q46': dict({"'": 'q82'},**createDict(alphabet, 'q46')),  
        'q47': {'S': 'q48'},
        'q48': {'E': 'q49'},
        'q49': {'R': 'q50'},
        'q50': {' ': 'q50', ':': 'q51'},
        'q51': {':': 'q52'},
        'q52': {' ': 'q52', "'": 'q53'},
        'q53': dict({"'": 'q82'},**createDict(symbols[2:len(symbols)+1]+alphabet, 'q53')), 
        'q54': {'A': 'q55', 'O': 'q65'},
        'q55': {'S': 'q56'},
        'q56': {'S': 'q57'},
        'q57': {'W': 'q58'},
        'q58': {'O': 'q59'},
        'q59': {'R': 'q60'},
        'q60': {'D': 'q61'},
        'q61': {' ': 'q61', "'": 'q62'},
        'q62': {':': 'q63'},
        'q63': {' ': 'q63', "'": 'q64'},
        'q64': dict({"'": 'q82'}, **createDict(symbols[2:len(symbols)+1]+alphabet, 'q64')),
        'q65': {'R': 'q66'},
        'q66': {'T': 'q67'},
        'q67': {' ': 'q67', "'": 'q68'},
        'q68': {':': 'q69'},
        'q69': {' ': 'q69', "'": 'q70'},
        'q70': {"'": 'q82', '0': 'q70','1': 'q70','2': 'q70','3': 'q70','4': 'q70','5': 'q70','6': 'q70','7': 'q70','8': 'q70','9': 'q70'},
        'q71': {'O': 'q72'},
        'q72': {'S': 'q73'},
        'q73': {'T': 'q74'},
        'q74': {' ': 'q74', "'": 'q75'},
        'q75': {':': 'q76'},
        'q76': {' ': 'q76', "'": 'q77'},
        'q77': dict({'0': 'q80','1': 'q80','2': 'q80','3': 'q80','4': 'q80','5': 'q80','6': 'q80','7': 'q80','8': 'q80','9': 'q80'},**createDict(alphabet,'q78')),
        'q78': {'.': 'q79'},
        'q79': dict({'.': 'q79', "'": 'q82'},**createDict(alphabet,'q79')),
        'q80': {'.': 'q81'},
        'q81':{'0': 'q81','1': 'q81','2': 'q81','3': 'q81','4': 'q81','5': 'q81','6': 'q81','7': 'q81','8': 'q81','9': 'q81', '.': 'q81', "'": 'q82'},
        'q82': {'}': 'q83'},
        'q83': {',': 'q84'},
        'q84': {'}': 'q0'},
        'q85': {'N': 'q86'},
        'q86': {'S': 'q87'},
        
    },
    initial_state='q0',
    final_states={'q0'},
    allow_partial = True
) 
