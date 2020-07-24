#Clase del Memento

#Estado del Editor
class EditorState:
    def __init__(self, content):
        self.content = content
        return

    def get_content(self):
        return self.content

#---------------------------------------------

#Clase del Caretaker

#Historial de Undos
class History:
    def __init__(self):
        self.states = []

        return

    def push(self, state):
        self.states.append(state)

        return

    def pop(self):
        state = self.states.pop()

        return state

#---------------------------------------------

#Clase del Originator

#Editor de Texto
class Editor:
    def __init__(self):        
        self.content = ""

        return
    
    def save_state(self):
        return EditorState(self.content)

    def undo(self, state):
        self.content = state.content

        return

    def set_content(self, content):
        self.content = content

        return

    def get_content(self):
        return self.content
