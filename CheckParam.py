# coding=utf-8
__author__ = 'tianchishao'


class CheckResult:
    def __init__(self, tag, msg, model):
        self.tag = tag
        self.msg = msg
        self.model = model

    def fill(self):
        if True is self.tag:
            print(self)
            for key, value in self.msg.iteritems():
                result = getattr(self.model, "set_{0}".format(key))(value)
                if not result[0]:
                    self.tag = False
                    self.msg = result[1]
                    self.model = None
                    break
        return self


class CheckParam:

    def __init__(self):
        pass

    @classmethod
    def check(cls, model, form):
        check_result = CheckResult(True, '', None)
        model_name = model.__class__.__name__
        request_params = {}
        keys = dir(model)
        for key in keys:
            key_start_str = "_{0}__".format(model_name)
            if not key.startswith(key_start_str):
                continue

            formatted_key = key.replace(key_start_str, '')
            if not (formatted_key in form.keys()):
                check_result = CheckResult(False, '参数缺失:{0}'.format(formatted_key), None)
                break
            else:
                request_params[formatted_key] = form[formatted_key].encode('ascii', 'ignore')
                check_result = CheckResult(True, request_params, model)
        return check_result