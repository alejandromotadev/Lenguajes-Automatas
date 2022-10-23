from automata.fa.dfa import DFA
import string
from visual_automata.fa.dfa import VisualDFA

num_states = 201
statesaH = []
alphabet = []
low_alphabet = []
symbols = [chr(34), chr(39), chr(32), chr(33), chr(35), chr(36), chr(37), chr(38), chr(40), chr(41), chr(42), chr(43), chr(44), chr(45), chr(46), chr(47), chr(48), chr(49), chr(50), chr(51), chr(52), chr(53), chr(
    54), chr(55), chr(56), chr(57), chr(58), chr(59), chr(60), chr(61), chr(62), chr(63), chr(64), chr(91), chr(92), chr(93), chr(94), chr(95), chr(96), chr(123), chr(124), chr(125), chr(126)]  # todos los simbolos


def createDict(list, value):
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

def declaracionDFA():
    dfaA = DFA(
        states=set(statesaH),
        input_symbols=alphabet+symbols+low_alphabet,
        transitions={
            'q0': {'D': 'q1', 'I': 'q85', 'L': 'q103', 'M': 'q119', 'S': 'q130', 'A': 'q164'},
            'q1': {'E': 'q2', 'A': 'q13'},
            'q2': {'B': 'q3'},
            'q3': {'U': 'q4'},
            'q4': {'G': 'q5'},
            'q5': {'=': 'q6', ' ': 'q5'},
            'q6': {' ': 'q6', 'T': 'q7', 'F': 'q10'},
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
            'q22': {"'": 'q23', ' ': 'q22'},
            'q23': {'d': 'q197'},
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
            'q39': dict({'.': 'q39', "'": 'q82', '0': 'q39', '1': 'q39', '2': 'q39', '3': 'q39', '4': 'q39', '5': 'q39', '6': 'q39', '7': 'q39', '8': 'q39', '9': 'q39'}, **createDict(low_alphabet, 'q39')),
            'q40': {'A': 'q41'},
            'q41': {'M': 'q42'},
            'q42': {'E': 'q43'},
            'q43': {' ': 'q43', "'": 'q44'},
            'q44': {':': 'q45'},
            'q45': {' ': 'q45', "'": 'q46'},
            'q46': dict({"'": 'q82'}, **createDict(alphabet, 'q46')),
            'q47': {'S': 'q48'},
            'q48': {'E': 'q49'},
            'q49': {'R': 'q50'},
            'q50': {' ': 'q50', "'": 'q51'},
            'q51': {':': 'q52'},
            'q52': {' ': 'q52', "'": 'q53'},
            'q53': dict({"'": 'q82'}, **createDict(symbols[2:len(symbols)+1]+alphabet, 'q53')),
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
            'q70': {"'": 'q82', '0': 'q70', '1': 'q70', '2': 'q70', '3': 'q70', '4': 'q70', '5': 'q70', '6': 'q70', '7': 'q70', '8': 'q70', '9': 'q70'},
            'q71': {'O': 'q72'},
            'q72': {'S': 'q73'},
            'q73': {'T': 'q74'},
            'q74': {' ': 'q74', "'": 'q75'},
            'q75': {':': 'q76'},
            'q76': {' ': 'q76', "'": 'q77'},
            'q77': dict({'0': 'q80', '1': 'q80', '2': 'q80', '3': 'q80', '4': 'q80', '5': 'q80', '6': 'q80', '7': 'q80', '8': 'q80', '9': 'q80'}, **createDict(alphabet, 'q78')),
            'q78': dict({'.': 'q79', "'": 'q82'},**createDict(alphabet, 'q78')),
            'q79': dict({'.': 'q79', "'": 'q82'}, **createDict(alphabet, 'q79')),
            'q80': {'.': 'q81', '0': 'q80', '1': 'q80', '2': 'q80', '3': 'q80', '4': 'q80', '5': 'q80', '6': 'q80', '7': 'q80', '8': 'q80', '9': 'q80'},
            'q81': {'0': 'q81', '1': 'q81', '2': 'q81', '3': 'q81', '4': 'q81', '5': 'q81', '6': 'q81', '7': 'q81', '8': 'q81', '9': 'q81', '.': 'q81', "'": 'q82'},
            'q82': {'}': 'q83', ',': 'q29', ' ': 'q82'},
            'q83': {',': 'q84'},
            'q84': {'}': 'q0'},
            'q85': {'N': 'q86'},
            'q86': {'S': 'q87'},
            'q87': {'T': 'q88'},
            'q88': {'A': 'q89'},
            'q89': {'L': 'q90'},
            'q90': {'L': 'q91'},
            'q91': {'E': 'q92'},
            'q92': {'D': 'q93'},
            'q93': {'_': 'q94'},
            'q94': {'A': 'q95'},
            'q95': {'P': 'q96'},
            'q96': {'P': 'q97'},
            'q97': {'S': 'q98'},
            'q98': {' ': 'q98', '=': 'q99'},
            'q99': {' ': 'q99', '[': 'q100'},
            'q100': {' ': 'q100', "'": 'q101'},
            'q101': dict({'.': 'q101', '_': 'q101', "'": 'q102'}, **createDict(alphabet, 'q101')),
            'q102': {' ': 'q102', ',': 'q100', ']': 'q0'},
            'q103': {'A': 'q104'},
            'q104': {'N': 'q105'},
            'q105': {'G': 'q106'},
            'q106': {'U': 'q107'},
            'q107': {'A': 'q108'},
            'q108': {'G': 'q109'},
            'q109': {'E': 'q110'},
            'q110': {'_': 'q111'},
            'q111': {'C': 'q112'},
            'q112': {'O': 'q113'},
            'q113': {'D': 'q114'},
            'q114': {'E': 'q115'},
            'q115': {' ': 'q115', '=': 'q116'},
            'q116': {' ': 'q116', "'": 'q117'},
            'q117': dict({'-': 'q118'}, **createDict(low_alphabet, 'q117')),
            'q118': dict({"'": 'q0'}, **createDict(low_alphabet, 'q118')),
            'q119': {'E': 'q120'},
            'q120': {'D': 'q121'},
            'q121': {'I': 'q122'},
            'q122': {'A': 'q123'},
            'q123': {' ': 'q123', '_': 'q124'},
            'q124': {' ': 'q124', 'U': 'q125', 'R': 'q135'},
            'q125': {'R': 'q126'},
            'q126': {'L': 'q127'},
            'q127': {' ': 'q127', '=': 'q128'},
            'q128': {' ': 'q128', "'": 'q129'},
            'q129': dict({'/': 'q129', "'": 'q0'}, **createDict(alphabet, 'q129')),
            'q130': {'T': 'q131'},
            'q131': {'A': 'q132'},
            'q132': {'T': 'q133'},
            'q133': {'I': 'q134'},
            'q134': {'C': 'q123'},
            'q135': {'O': 'q136'},
            'q136': {'O': 'q137'},
            'q137': {'T': 'q138'},
            'q138': {' ': 'q138', '=': 'q139'},
            'q139': {' ': 'q139', 'o': 'q140'},
            'q140': {'s': 'q141'},
            'q141': {'.': 'q142'},
            'q142': {'p': 'q143'},
            'q143': {'a': 'q144'},
            'q144': {'t': 'q145'},
            'q145': {'h': 'q146'},
            'q146': {'.': 'q147'},
            'q147': {'j': 'q148'},
            'q148': {'o': 'q149'},
            'q149': {'i': 'q150'},
            'q150': {'n': 'q151'},
            'q151': {'(': 'q152'},
            'q152': {'B': 'q153'},
            'q153': {'A': 'q154'},
            'q154': {'S': 'q155'},
            'q155': {'E': 'q156'},
            'q156': {'_': 'q157'},
            'q157': {'D': 'q158'},
            'q158': {'I': 'q159'},
            'q159': {'R': 'q160'},
            'q160': {"'": 'q161'},
            'q161': {' ': 'q161', "'": 'q162'},
            'q162': dict({'/': 'q162', "'": 'q163'}, **createDict(alphabet, 'q162')),
            'q163': {'}': 'q0'},
            'q164': {'L': 'q165'},
            'q165': {'L': 'q166'},
            'q166': {'O': 'q167'},
            'q167': {'W': 'q168'},
            'q168': {'E': 'q169'},
            'q169': {'D': 'q170'},
            'q170': {'_': 'q171'},
            'q171': {'H': 'q172'},
            'q172': {'O': 'q173'},
            'q173': {'S': 'q174'},
            'q174': {'T': 'q175'},
            'q175': {'S': 'q176'},
            'q176': {' ': 'q176', '=': 'q177'},
            'q177': {' ': 'q177', '[': 'q178'},
            'q178': {' ': 'q178', "'": 'q179', ']': 'q10'},
            'q179': dict({'*': 'q195', '0': 'q193', '1': 'q193', '2': 'q193', '3': 'q193', '4': 'q193', '5': 'q193', '6': 'q193', '7': 'q193', '8': 'q193', '9': 'q193'}, **createDict(alphabet, 'q180')),
            'q180': {'.': 'q191'},
            'q191': dict({'.': 'q191', "'": 'q192'}, **createDict(alphabet, 'q191')),
            'q192': {',': 'q178', ']': 'q0'},
            'q193': {'.': 'q194'},
            'q194': {'0': 'q194', '1': 'q194', '2': 'q194', '3': 'q194', '4': 'q194', '5': 'q194', '6': 'q194', '7': 'q194', '8': 'q194', '9': 'q194', '.': 'q194', "'": 'q192'},
            'q195': {"'": 'q192'}
        },
        initial_state='q0',
        final_states={'q0'},
        allow_partial=True
    )
    return dfaA

def example(data):
    dfa = declaracionDFA()
    return dfa.read_input_stepwise(data)

