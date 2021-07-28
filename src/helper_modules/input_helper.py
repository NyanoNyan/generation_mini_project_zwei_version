def input_helper(prompt, condition_list=[], set_int=False, is_cond=False, isLoop=True):
    if isLoop == True:
        while True:
            try:
                user_input = input(prompt)
                if set_int == True:
                    user_input = int(user_input)
            except ValueError:
                print('Please enter a valid input')
                continue
            
            if is_cond == True:
                if user_input in condition_list:
                    break
                else:
                    print('Please enter a valid input')
            else:
                break
    else:
        user_input = input(prompt)
        return user_input

    return user_input