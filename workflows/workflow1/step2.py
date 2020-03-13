import time


def execute(handler):
    print("running workflow1 step2")
    path = "$.workflow1.step1.field1.field2"
    value = "hello world"
    handler.flow_data.set(path, value)
    time.sleep(1)
