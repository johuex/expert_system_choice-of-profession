"""
UI + Service logic
"""
from copy import deepcopy

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidgetItem

from UI.mainwindow import Ui_MainWindow  # import generated 'ui to py'
from service.questions import questions_and_variables
from DB.db import (
    create_and_insert,
    get_simptom,
    delete_symptom
)


class Interface(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        # init variables
        self.questions_and_variables = deepcopy(questions_and_variables)
        self.e_0 = 0.01  # threshold rejection of the diagnosis
        self.e_1 = 0.2  # threshold the diagnosis is answer
        self.len_symptoms = 0
        self.answer = None  # receive answer on question from user
        self.df = None
        self.pW = []  # actual probabilities of diagnosis
        self.pW_X_P = None
        self.p_noW_X_P = None
        self.pW_noX_P = None
        self.p_noW_noX_P = None
        self.p_max_W = None
        self.p_min_W = None
        self.questions_done = 0
        self.excluded_diagnosis_count = 0

        # define Qt Signals Handler
        self.yesPushButton.pressed.connect(self.answer_yes_button)
        self.noPushButton.pressed.connect(self.answer_no_button)
        self.startpushButton.pressed.connect(self.start)

        # some preparations for tables
        self.allDiagnosisTableWidget.setColumnCount(2)
        self.allDiagnosisTableWidget.setRowCount(15)
        self.allDiagnosisTableWidget.setHorizontalHeaderLabels(["Название", "Вероятность"])
        self.allDiagnosisTableWidget.horizontalHeaderItem(0).setToolTip("Name")
        self.allDiagnosisTableWidget.horizontalHeaderItem(1).setToolTip("Probability")
        self.allDiagnosisTableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.allDiagnosisTableWidget.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.excludedDiagnosisTableWidget.setColumnCount(1)
        self.excludedDiagnosisTableWidget.setRowCount(15)
        self.excludedDiagnosisTableWidget.setHorizontalHeaderLabels(["Название"])
        self.excludedDiagnosisTableWidget.horizontalHeaderItem(0).setToolTip("Name")
        self.excludedDiagnosisTableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)

    def start(self):
        """Start Loop of questions, main func"""
        self.df = create_and_insert()
        self.len_symptoms = ((len(self.df.columns) - 2)//2)
        self.pW = self.df['Pa'].to_list()
        self.pW_X_P = [0] * self.len_symptoms
        self.p_noW_X_P = [0] * self.len_symptoms
        self.pW_noX_P = [0] * self.len_symptoms
        self.p_noW_noX_P = [0] * self.len_symptoms
        self.p_max_W = [0] * self.len_symptoms
        self.p_min_W = [0] * self.len_symptoms
        self.check_reverse_probability()
        self.conditional_probabilities()

        # loop of questions
        while True or len(self.questions_and_variables) > 0:
            # show most informative question
            self.questionsDoneLabel.setText(str(self.questions_done))
            self.questionsLeft.setText(str(self.len_symptoms))
            inf_quest = self.most_informative_question()
            self.questionTextLabel.setText(self.questions_and_variables[inf_quest])
            self.update()

            # wait answer from user
            while self.answer is None:
                QApplication.processEvents()

            # calculate pW by yes/no Bayes formula
            match self.answer:
                case "yes":
                    self.bayes_yes(inf_quest)
                case "no":
                    self.bayes_no(inf_quest)
            self.answer = None

            # exclude symptom after iteration
            self.df = delete_symptom(self.df, inf_quest)
            self.questions_and_variables.pop(inf_quest)
            self.len_symptoms -= 1
            self.questions_done += 1

            # exclude diagnosis with probability < epselone
            for i in range(len(self.pW)):
                try:
                    if self.pW[i] < self.e_0:
                        self.exclude_diagnosis(i)
                except:
                    break

            # calculate theoretical max and min probabilities
            self.conditional_probabilities()

            # search most likely true diagnosis
            self.W_d, W_d_index = self.max_min_probability()
            self.W_d_max = max(self.pW)
            if self.W_d >= self.W_d_max:
                # Wd diagnosis considered most likely and reported to the user
                # end loop with questions
                self.end_loop(W_d_index)
                break

            if 1 - max(self.pW) < self.e_1:
                # max probability < epselone
                # end loop with questions
                self.end_loop(self.pW.index(max(self.pW)))
                break

    def answer_yes_button(self):
        """Set Bayes yes-answer"""
        self.answer = "yes"

    def answer_no_button(self):
        """Set Bayes no-answer"""
        self.answer = "no"

    def most_informative_question(self):
        """The most informative question is question with minimum of None"""
        _df = deepcopy(self.df)
        res = _df.isna().sum(axis=1).to_list()
        index = res.index(min(res))
        return index

    def check_reverse_probability(self):
        """Set conditional probability flag, if required"""
        _df = deepcopy(self.df)
        _df = _df.drop(["profession", "Pa"], axis=1)
        for i in _df.index:
            for j in range(1, len(_df[i:i+1].columns), 2):
                if _df.iloc[i:i+1, j:j+1].values > _df.iloc[i:i+1, j-1:j].values:  # if p(x/now) > p(x/w)
                    self.df["label"][i] = 1
                else:
                    self.df["label"][i] = 0

    def conditional_probabilities(self):
        """Calculate theoretical max and min probabilities"""
        self.all_yes_answers_probability_true()
        self.all_yes_answers_probability_false()
        self.all_no_answers_probability_true()
        self.all_no_answers_probability_false()
        self.max_theor_prob()
        self.min_theor_prob()

        for i in range(len(self.df)):
            if self.p_max_W[i] < self.pW[i]:
                # exclude j-diagnosis
                self.exclude_diagnosis(i)

    def exclude_diagnosis(self, index):
        """Exlude all information of diagnosis"""
        diagnosis_name = self.df.iloc[index:index+1, 0:1].values[0][0]
        self.df = self.df.drop([index])
        self.pW.pop(index)
        self.pW_X_P.pop(index)
        self.p_noW_X_P.pop(index)
        self.pW_noX_P.pop(index)
        self.p_noW_noX_P.pop(index)
        self.p_max_W.pop(index)
        self.p_min_W.pop(index)
        self.excludedDiagnosisTableWidget.setItem(self.excluded_diagnosis_count, 0, QTableWidgetItem(diagnosis_name))
        self.excluded_diagnosis_count += 1

    def max_min_probability(self):
        """return value and index"""
        res = max(self.p_min_W)
        return res, self.p_min_W.index(res)

    def end_loop(self, answer_index):
        """all activities associated on completion of work"""
        # set alltableWidgets
        for i in range(len(self.pW)):
            self.allDiagnosisTableWidget.setItem(i, 0, QTableWidgetItem(self.df.iloc[i:i+1, 0:1].values[0][0]))
            self.allDiagnosisTableWidget.setItem(i, 1, QTableWidgetItem(str(self.pW[i])))

        # set answer name
        self.answerText.setText(self.df.iloc[answer_index:answer_index+1, 0:1].values[0][0])

    # ---------------- formulas
    def bayes_yes(self, index):
        """Return pW_X on yes answer, Bayes formula"""
        _df = get_simptom(self.df, index)

        for ind in _df.index:
            pX_W = _df.iloc[ind, 0]
            pX_noW = _df.iloc[ind, 1]
            pW = self.pW[ind]
            if pX_W is not None and pX_noW is not None:
                self.pW[ind] = pW * pX_W / (pW*pX_W + (1-pW)*pX_noW)
                # if self.pW[ind] < self.e_0:
                #     self.exclude_diagnosis(ind)

    def bayes_no(self, index):
        """Return pW_X on no answer, Bayes formula"""
        _df = get_simptom(self.df, index)

        for ind in _df.index:
            pX_W = _df.iloc[ind, 0]
            pX_noW = _df.iloc[ind, 1]
            pW = self.pW[ind]
            if pX_W is not None and pX_noW is not None:
                self.pW[ind] = pW * (1 - pX_W) / (pW * (1 - pX_W) + (1 - pW) * (1 - pX_noW))
                # if self.pW[ind] < self.e_0:
                #     self.exclude_diagnosis(ind)

    def all_yes_answers_probability_true(self):
        _df = deepcopy(self.df)
        _df = _df.drop(["profession", "Pa"], axis=1)
        _df = _df[[c for c in _df.columns if (c.endswith("(x/w)") or c.endswith("label"))]]
        cols = [c for c in _df.columns if c.endswith("(x/w)")]
        _df.loc[_df.label == 1, cols] -= 1
        _df.loc[_df.label == 1, cols] *= -1
        _df = _df.drop(["label"], axis=1)

        self.pW_X_P = _df.prod(axis=1).values.tolist()

    def all_yes_answers_probability_false(self):
        _df = deepcopy(self.df)
        _df = _df.drop(["profession", "Pa"], axis=1)
        _df = _df[[c for c in _df.columns if (c.endswith("(x/now)") or c.endswith("label"))]]
        cols = [c for c in _df.columns if c.endswith("(x/now)")]
        _df.loc[_df.label == 1, cols] -= 1
        _df.loc[_df.label == 1, cols] *= -1
        _df = _df.drop(["label"], axis=1)

        self.p_noW_X_P = _df.prod(axis=1).values.tolist()

    def all_no_answers_probability_true(self):
        _df = deepcopy(self.df)
        _df = _df.drop(["profession", "Pa"], axis=1)
        _df = _df[[c for c in _df.columns if (c.endswith("(x/w)") or c.endswith("label"))]]
        cols = [c for c in _df.columns if c.endswith("(x/w)")]
        _df.loc[_df.label == 1, cols] -= 1
        _df.loc[_df.label == 1, cols] *= -1
        _df = _df.drop(["label"], axis=1)
        _df[:][:] -= 1
        _df[:][:] *= -1

        self.p_noW_X_P = _df.prod(axis=1).values.tolist()

    def all_no_answers_probability_false(self):
        _df = deepcopy(self.df)
        _df = _df.drop(["profession", "Pa"], axis=1)
        _df = _df[[c for c in _df.columns if (c.endswith("(x/now)") or c.endswith("label"))]]
        cols = [c for c in _df.columns if c.endswith("(x/now)")]
        _df.loc[_df.label == 1, cols] -= 1
        _df.loc[_df.label == 1, cols] *= -1
        _df = _df.drop(["label"], axis=1)
        _df[:][:] -= 1
        _df[:][:] *= -1

        self.p_noW_X_P = _df.prod(axis=1).values.tolist()

    def max_theor_prob(self):
        for index in range(len(self.df)):
            pW = self.pW[index]
            pW_X_P = self.pW_X_P[index]
            p_noW_noX_P = self.p_noW_noX_P[index]

            self.p_max_W[index] = pW*pW_X_P / (pW*pW_X_P + (1-pW)*p_noW_noX_P)

    def min_theor_prob(self):
        for index in range(len(self.df)):
            pW = self.pW[index]
            pW_noX_P = self.pW_noX_P[index]
            p_noW_noX_P = self.p_noW_noX_P[index]

            try:
                self.p_min_W[index] = pW * pW_noX_P / (pW*pW_noX_P + (1-pW)*p_noW_noX_P)
            except ZeroDivisionError:
                self.p_min_W[index] = pd.NA
