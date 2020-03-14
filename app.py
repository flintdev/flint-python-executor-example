from flint import create_app
from workflows import workflow1, workflow2

workflows = {
    "workflow1": {
        "step1": workflow1.step1.execute,
        "step2": workflow1.step2.execute,
        "step3": workflow1.step3.execute,
        "step4": workflow1.step4.execute
    },
    "workflow2": {
        "step1": workflow2.step1.execute,
        "step2": workflow2.step2.execute,
        "step3": workflow2.step3.execute,
        "step4": workflow2.step4.execute
    }
}

app = create_app()
app.register_workflows(workflows)

if __name__ == "__main__":
    app.start()
