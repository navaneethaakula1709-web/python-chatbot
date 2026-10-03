class ConversationManager:

    def __init__(self):
        self.history = []
        self.last_question = None
        self.last_category = None
        self.last_answer = None

    def add_conversation(
        self,
        question,
        category,
        answer
    ):
        conversation = {
            "question": question,
            "category": category,
            "answer": answer
        }

        self.history.append(conversation)

        self.last_question = question
        self.last_category = category
        self.last_answer = answer

    def get_last_question(self):
        return self.last_question

    def get_last_category(self):
        return self.last_category

    def get_last_answer(self):
        return self.last_answer

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        self.last_question = None
        self.last_category = None
        self.last_answer = None