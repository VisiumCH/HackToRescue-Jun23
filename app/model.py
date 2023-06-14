class ChatGPTModel:
    def __init__(self) -> None:
        pass
    
    def predict(self, inputs_: str):
        return [f"Outputs: {inputs_[::-1]}"]