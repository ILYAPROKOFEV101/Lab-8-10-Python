class State:
    def analyze(self, value_n, value_1):
        raise NotImplementedError("This method should be overridden.")

class StateAnalysis1Wave(State):
    def analyze(self, value_n, value_1):
        print(f"Результат вступительных испытаний: {value_n}")
        print("Конкурс 1 волна")
        if value_n > value_1:
            print("Попадание в 1 волну")
            return StateProcessing()
        else:
            return StateAnalysis2Wave()

class StateProcessing(State):
    def analyze(self, value_n, value_1):
        print("Обработка результатов...")
        # Логика обработки результатов
        return self  # Остаемся в этом состоянии или можем перейти в другое

class StateAnalysis2Wave(State):
    def analyze(self, value_n, value_1):
        print("Переход к состоянию Анализ 2 волна")
        # Логика анализа 2 волны
        return self  # Здесь также можем остаться или перейти в другое состояние

class Context:
    def __init__(self):
        self.state = StateAnalysis1Wave()  # Начальное состояние

    def set_state(self, state):
        self.state = state

    def analyze(self, value_n, value_1):
        new_state = self.state.analyze(value_n, value_1)
        self.set_state(new_state)

# Пример использования
if __name__ == "__main__":
    context = Context()
    value_n = 85  # Пример значения N
    value_1 = 80  # Пример значения 1

    context.analyze(value_n, value_1)  # Анализ 1 волна
    context.analyze(value_n, value_1)  # Обработка (если попадание в 1 волну)
