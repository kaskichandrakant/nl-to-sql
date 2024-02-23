def format_res(res):
    query = res.split("SELECT")[1]
    return "SELECT" + query