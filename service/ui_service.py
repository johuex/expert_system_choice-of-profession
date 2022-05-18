"""
UI + Service logic
"""
from copy import deepcopy
import sqlite3

from UI.mainwindow import Ui_MainWindow  # import generated ui to py
from .questions import questions_and_variables


class Interface(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        # init variables
        self.questions_and_variables = deepcopy(questions_and_variables)
        self.e_0 = 0.01  # threshold rejection of the diagnosis
        self.e_1 = 0.2  # # threshold the diagnosis is answer
        self.answer = None  # receive answer on question from user
        self.questionTextLabel = ""
        self.pW_X = []

        # define Qt Signals Handler
        self.yesPushButton.pressed.connect(self.answer_yes_button())
        self.noPushButton.pressed.connect(self.answer_no_button())
        # self.exitPushButton.pressed.connect(self.)

        # start loop of questions
        self.start()

    def start(self):
        """
        Start Loop of questions, main func
        :return:
        """
        # информативный симптом - тот, который присутсвует в большем кол-ве диагнозов
        while True or len() > 0:
            # show most informative question
            self.questionTextLabel = "вопрос"

            # wait answer from user
            while self.answer is None:
                pass

            # calculate pW_X by yes/no Bayes formula
            match self.answer:
                case "yes":
                    self.pW_X = self.bayes_yes()
                case "no":
                    self.pW_X = self.bayes_no()
            self.answer = None

            # calculate theoretical max and min probabilities
            # TODO стоит учесть тут про условные вероятности p` = 1 - p
            pW_X_P = self.all_yes_answers_probability_true()
            p_noW_X_P = self.all_yes_answers_probability_false()
            pW_noX_P = self.all_no_answers_probability_true()
            p_noW_noX_P = self.all_no_answers_probability_false()
            p_max_W = self.max_theor_prob()
            p_min_W = self.min_theor_prob()
            if p_max_W < self.p_W:
                # j-й диагноз можно исключить из дальнейшего рассмотрения
                pass

            # search most likely true diagnosis
            self.W_d = self.min_theor_prob()
            self.W_d_max = self.max_theor_prob()
            if self.W_d >= self.W_d_max:
                # диагноз Wd считается наиболее вероятным и сообщается пользователю
                # завершаем работу системы
                self.end_loop()
                break

            """if self.pW_X < self.e_0:
                # j-й диагноз можно исключить из дальнейшего рассмотрения
                pass
            if 1 - self.pW_X < self.e_1:
                # j-й диагноз можно считать истинным и закончить
                # работу системы
                pass"""


        # если вероятность, посчитанная по Байесу билзка к 0, то дигноз исключается
        # если вероятность, псчитанная по Байесу близка к 1, то диагноз истинный и можно закончить алгоритм
        # если максимальна возможная вероятность меньне нынешней, то исключаем диагноз

    def answer_yes_button(self):
        """
        Calculate Bayes yes-answer
        :return:
        """
        # не забыть тут про условные вероятности вида p` = 1 - р
        self.answer = "yes"

    def answer_no_button(self):
        """
        Calculate Bayes no-answer
        :return:
        """
        # не забыть тут про условные вероятности вида p` = 1 - р
        self.answer = "no"

    def pop_question(self):
        pass

    def most_informative_question(self):
        """
        для каждого еще не заданного вопроса определяется
        количество еще не исключенных диагнозов, в которых он учитывается. Вопрос с
        максимальным значением считается самым информативным в текущем цикле
        :return:
        """
        pass

    # ---------------- formulas
    def bayes_yes(self, pW, pX_W, pX_noW):
        """
        Return pW_X on yes answer, Bayes formula
        """
        result = pW * pX_W / (pW*pX_W + (1-pW)*pX_noW)

        return result

    def bayes_no(self, pW, pX_W, pX_noW):
        """
        Return pW_X on no answer, Bayes formula
        """
        result = pW * (1 - pX_W) / (pW * (1 - pX_W) + (1 - pW) * (1 - pX_noW))

        return result
