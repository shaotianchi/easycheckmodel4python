# coding=utf-8
import re

__author__ = 'tianchishao'


class RBModel:

    def __init__(self):
        pass


def notnull(desc):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            print(func, args, kwargs)
            if args[1] is None or 0 == len(args[1]):
                return False, "{0}不能为空".format(desc)
            else:
                func(*args, **kwargs)
                return True, ''
        return handle_args
    return handle_func


def max_length(arg_of_decorator, desc):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            print(func, args, kwargs)
            if len(args[1]) > arg_of_decorator:
                return False, "{0}的长度不能超过{1}".format(desc, arg_of_decorator)
            else:
                func(*args, **kwargs)
                return True, ''
        return handle_args
    return handle_func


def min_length(arg_of_decorator, desc):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            if len(args[1]) < arg_of_decorator:
                return False, "{0}的长度不能小于{1}".format(desc, arg_of_decorator)
            else:
                func(*args, **kwargs)
                return True, ''
        return handle_args
    return handle_func


def match(arg_of_decorator, desc):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            if re.search(arg_of_decorator, args[1]) is None:
                return False, "{0}的格式不正确".format(desc)
            else:
                func(*args, **kwargs)
                return True, ''
        return handle_args
    return handle_func


class RegisterModel(RBModel):

    def __init__(self):
        RBModel.__init__(self)
        self.__username = None
        self.__tel = None
        self.__psw = None

    @max_length(10, '用户名')
    def set_username(self, username):
        self.__username = username

    def username(self):
        return self.__username

    @match("^(130|131|132|133|134|135|136|137|138|139)\d{8}$", '手机号')
    def set_tel(self, tel):
        self.__tel = tel

    def tel(self):
        return self.__tel

    @max_length(12, '密码')
    def set_psw(self, psw):
        self.__psw = psw

    def psw(self):
        return self.__psw