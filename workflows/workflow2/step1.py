import time


def execute(handler):
    print("running workflow2 step1")
    path = "$.workflow2.step1.field1.field2"
    value = "test1"
    handler.flow_data.set(path, value)
    time.sleep(1)
