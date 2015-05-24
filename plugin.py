def results(fields, original_query):
    suburb = fields.get('~suburb', '')
    return {
        "title": "{0} postcode".format(suburb),
        "run_args": [suburb],
        "html": open("postcode.html").read().decode('utf-8').replace(
            "<!--SUBURB-->", suburb)
    }
