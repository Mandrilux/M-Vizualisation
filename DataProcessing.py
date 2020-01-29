def FormatData(data):
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

    return format_data
