from hopex.utils.print_mix_object import TypeCheck


def fill_obj(dict_data, class_name=object):
    obj = class_name()
    for ks, vs in dict_data.items():
        # print("===== fill_obj =====", ks, obj_key, str(vs))
        if hasattr(obj, ks):
            setattr(obj, ks, vs)
            continue
    return obj


def fill_obj_list(list_data, class_name):
    if TypeCheck.is_list(list_data):
        inner_obj_list = list()
        for idx, row in enumerate(list_data):
            inner_obj = fill_obj(row, class_name)
            inner_obj_list.append(inner_obj)
        return inner_obj_list

    return list()


def default_parse(dict_data, outer_class_name=object, inner_class_name=object):
    rsp_obj = outer_class_name()

    for outer_key, outer_value in dict_data.items():
        if hasattr(rsp_obj, outer_key):
            new_value = outer_value
            # print("==========", type(outer_value), outer_value)
            if TypeCheck.is_list(outer_value):
                new_value = fill_obj_list(outer_value, inner_class_name)
            elif TypeCheck.is_dict(outer_value):
                new_value = fill_obj(outer_value, inner_class_name)

            setattr(rsp_obj, outer_key, new_value)
            continue

    return rsp_obj


def default_parse_list_dict(inner_data, inner_class_name=object, default_value=None):
    new_value = default_value
    if inner_data and len(inner_data):
        if TypeCheck.is_list(inner_data):
            new_value = fill_obj_list(inner_data, inner_class_name)
        elif TypeCheck.is_dict(inner_data):
            new_value = fill_obj(inner_data, inner_class_name)
        else:
            new_value = default_value

    return new_value


def default_parse_fill_directly(dict_data, outer_class_name=object):
    rsp_obj = outer_class_name()

    for outer_key, outer_value in dict_data.items():
        # obj_key = key_trans(outer_key)
        if hasattr(rsp_obj, outer_key):
            new_value = outer_value
            setattr(rsp_obj, outer_key, new_value)
            continue

    return rsp_obj
