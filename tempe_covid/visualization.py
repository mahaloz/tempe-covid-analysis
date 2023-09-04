#
# Markdown Table
#

def tablify_data(date_tuples):
    table_summary = list()
    for date, data in date_tuples:

        row = {"Week": date}
        for metric_name, metric_data in data.items():
            row[metric_name] = metric_data

        table_summary.append(row)

    return table_summary


def format_as_markdown_table(data_tuples, max_rows=10):
    def format_table(myDict, colList=None):
        """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
        If column names (colList) aren't specified, they will show in random order.
        Author: Thierry Husson - Use it as you want but don't blame me.
        """
        if not colList: colList = list(myDict[0].keys() if myDict else [])
        myList = [colList]  # 1st row = header
        for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
        colSize = [max(map(len, col)) for col in zip(*myList)]
        formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
        myList.insert(1, ['-' * i for i in colSize])  # Seperating line
        for item in myList: yield formatStr.format(*item)

    table_summary = tablify_data(data_tuples)
    formatted_data = format_table(table_summary)
    markdown_summary = ""
    for i, row in enumerate(formatted_data):
        if i > max_rows:
            break
        markdown_summary += row + "\n"

    return markdown_summary
