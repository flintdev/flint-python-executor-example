import time


def execute(handler):
    print("running workflow1 step2")
    path = "$.workflow1.step1.field4"
    value = handler.flow_data.get(path)
    print(path, value)
    time.sleep(1)
