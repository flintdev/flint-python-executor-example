import time


def execute(handler):
    print("running workflow1 step1")
    path = "$.workflow1.step1.field1.field2"
    value = "test1"
    handler.flow_data.set(path, value)
    time.sleep(1)
