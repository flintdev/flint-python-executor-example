import time


def execute(handler):
    print("running workflow1 step1")
    path = "$.workflow1.step1.field1.field2"
    value = handler.flow_data.get(path)
    print(value)
    time.sleep(1)
