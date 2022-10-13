from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
import string
def debugDfa():
    num_states = 15
    statesDb = []
    alfabet = ['D','E','B','U','G','T','r','u','e','F','a','l','s']
    simbolos = [chr(32),chr(61)] #{' ', =}

    for i in range(num_states):
        state = 'q'+str(i)
        statesDb.append(state)
        
    dfa = DFA(
        states = set(statesDb),
        input_symbols=alfabet+simbolos,
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
        initial_state='q0',
        final_states={'q14'},
        allow_partial = True
    )  
    dfa2 = VisualDFA(dfa)
    print(dfa2.table)
def installedAppsDfa():
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
        
    dfa = DFA(
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
            'q15': {'[': 'q16'},
            'q16': {' ': 'q16', "'": 'q17','"': 'q17'},
            'q17': dict({'.': 'q17', '_': 'q17', "'": 'q18', '"': 'q18'},**createDict(alphabet,'q17')),
            'q18': {' ': 'q18', ',': 'q16', ']': 'q19'}
        },
        initial_state='q0',
        final_states={'q19'},
        allow_partial=True, 
    )
    dfa2 = VisualDFA(dfa)
    print(dfa2.table) 
def allowedHost():
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
        
    dfa = DFA(
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
            'q14': {'[': 'q15'},
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
    dfa2 = VisualDFA(dfa)
    print(dfa2.table) 
def urlVar():
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
        
    dfa = DFA(
        states = set(statesaH),
        input_symbols=alphabet+symbols,
        transitions = {
            'q0': {'M': 'q1', 'S': 'q7'},
            'q1': {'E': 'q2'},
            'q2': {'D': 'q3'},
            'q3': {'I': 'q4'},
            'q4': {'A': 'q5'},
            'q5': {'=': 'q6', ' ': 'q5'},
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
    dfa2 = VisualDFA(dfa)
    print(dfa2.table) 
def languageCod():
    num_states = 18
    statesLg = []
    alphabet = ['L','A','N','G','U','E','C','O','D']
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
        alphabet.append(c)

    for i in range(num_states):
        state = 'q'+str(i)
        statesLg.append(state)
        
    dfa = DFA(
        states = set(statesLg),
        input_symbols=alphabet+simbolos,
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
            'q15': dict({'-': 'q16'},**createDict(alphabet,'q15')),   
            'q16': dict({'"': 'q17', "'": 'q17'},**createDict(alphabet,'q16')), 
            'q17': {}
        },
        initial_state='q0',
        final_states={'q17'},
        allow_partial = True
    )  
    dfa2 = VisualDFA(dfa)
    print(dfa2.table)
def main():
    debugDfa()
    installedAppsDfa()  
    allowedHost() 
    urlVar()
    languageCod()
if __name__ == "__main__":
    main()