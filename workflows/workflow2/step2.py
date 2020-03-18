import time


def execute(handler):
    print("running workflow2 step2")
    path = "$.workflow2.step1.field1.field2"
    value = handler.flow_data.get(path)
    print(path, value)
    time.sleep(1)
