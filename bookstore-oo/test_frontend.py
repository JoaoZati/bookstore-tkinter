import pytest
from backend_oo import Database
from frontend_oo import Window
from tkinter import *


@pytest.fixture
def database():
    books = Database('books.db')
    return books


@pytest.fixture
def window(database):
    window = Window(database)
    return window


def test_type_database(database):
    assert database.type == 'database'


def test_type_window(window):
    assert window.type == 'window'


def test_window_tkinter(window):
    # assert type(window.window) == type(Tk())
    assert isinstance(window.window, Tk)


def test_window_from_tkinter(database):
    tk = Tk()
    window = Window(database, tk)
    assert isinstance(window.window, Tk)


def test_l1_islabel(window):
    assert isinstance(window.l1, Label)


def test_l1_text(window):
    window.l1.text = 'Title'


