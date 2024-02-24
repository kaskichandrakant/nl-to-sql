def format_res(res):
    query = res.split("SELECT")[1]
    with_singleqoutes = query.replace('"', "'")
    return "SELECT" + with_singleqoutes
