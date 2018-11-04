def handler(event, context):
    print(event)
    if type(event) == list:
        return event[0]
    return event
