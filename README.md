##How to use

	form = request.form
    check_result = CheckParam.check(RegisterModel(), form).fill()
    if not check_result.tag:
        print(check_result.msg)
    else:
        register_model = check_result.model