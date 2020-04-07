import time


def execute(handler):
    print("running workflow1 step1")
    path = "$.workflow1.step1.field1"
    value = "test1"
    handler.flow_data.set(path, value)
    path = "$.workflow1.step1.field2"
    value = "test2"
    handler.flow_data.set(path, value)
    path = "$.workflow1.step1.field3"
    value = "test3"
    handler.flow_data.set(path, value)
    path = "$.workflow1.step1.field4"
    value = 1.2
    handler.flow_data.set(path, value)
    path = "$.workflow1.step1.field5"
    value = "2020-01-01"
    handler.flow_data.set(path, value)
    time.sleep(1)
