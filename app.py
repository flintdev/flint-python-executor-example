from flint import create_app
from workflows.workflow1 import step1, step2, step3, step4

workflows = {
    "workflow1": {
        "step1": step1.execute,
        "step2": step2.execute,
        "step3": step3.execute,
        "step4": step4.execute
    }
}

app = create_app()
app.register_workflows(workflows)

if __name__ == "__main__":
    app.start()
