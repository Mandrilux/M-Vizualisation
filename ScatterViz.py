import plotly.express as px


def ScatterViz(data):
    format_data = [{}] * (len(data) - 1)

    for lin in range(1, len(data)):
        line = data[lin]
        format_data[lin - 1] = {
            "place": line[7],
            "age": int(line[2]),
            "size": 50
        }

    for lin in range(1, len(data)):
        line = data[lin]
        format_data[lin - 1]["size"] = len([x for x in format_data if x.get("age") == format_data[lin - 1]["age"]])


    print("Generate graph : please wait")
    fig = px.scatter(format_data, x="age", y="place", color="place", opacity=0.1, size="size")

    fig.write_html('tmp.html', auto_open=True)
