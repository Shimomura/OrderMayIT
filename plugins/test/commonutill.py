# -*- coding: utf-8 -*-

def split_options(arg):
    """
    コマンドのオプションを分割します。
    return:dict key:オプション種別(例：「-p」) value:指定値
    """

    # 引数の文字列を空白で分割
    options = arg.split()

    # 返却値となるdict
    optionDic = {}

    tmp_key = ""
    tmp_value = []

    # 前回読み込んだ値がvalueだったか？keyの場合はfalse
    lasttime_is_value = True
    for opt in options:
        if lasttime_is_value:
            #value⇨keyときた場合
            if opt.startswith("-") and len(opt) == 2:
                # １番最初以外はdictに追加
                if tmp_key:
                    optionDic[tmp_key] = tmp_value

                # 値初期化
                tmp_value = []
                tmp_key = opt
                lasttime_is_value = False
            # value⇨valueときた場合
            else:
                if not tmp_key:
                    # key未指定でvalueが指定された場合はエラー
                    raise Exception("コマンドが不正")
                tmp_value.append(opt)
                lasttime_is_value = True
        else:
            # key⇨keyときた場合
            if opt.startswith("-") and len(opt) == 2:
                # 連続でkeyを受け取ったらエラー
                raise Exception("コマンドが不正")
            # key⇨valueときた場合
            else:
                tmp_value.append(opt)
                lasttime_is_value = True

    # 最後に残った値をdictに格納
    if tmp_key and len(tmp_value) > 0:
        optionDic[tmp_key] = tmp_value
    else:
        raise Exception("コマンドが不正")

    return optionDic
